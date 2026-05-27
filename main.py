import uvicorn
from fastapi import FastAPI, Form, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

from src.utils.schemas import SiteGenerationRequest, SiteGenerationResponse
from src.ai.gemini_client import get_gemini_model
from src.ai.prompts import EXTRACTION_SYSTEM_PROMPT
from src.generator.engine import SiteGenerator
from src.deployment.netlify import deploy_to_netlify
from src.whatsapp.handler import send_whatsapp_message
from src.utils.session_manager import save_session, get_session
from src.ai.prompts import EXTRACTION_SYSTEM_PROMPT, EDIT_SYSTEM_PROMPT

app = FastAPI(title="WhatsApp AI Website Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "WhatsApp AI Website Generator is active"}

# --- WhatsApp Webhook ---
@app.post("/whatsapp")
async def whatsapp_webhook(
    background_tasks: BackgroundTasks,
    Body: str = Form(None),
    From: str = Form(...),
    MediaUrl0: str = Form(None),
    MediaContentType0: str = Form(None)
):
    """Twilio WhatsApp Webhook handling Text and Voice"""
    print(f"Received message from {From}")

    # 1. Acknowledge immediately
    if MediaUrl0 and "audio" in MediaContentType0:
        acknowledge_msg = "🎙️ I've received your voice message! Give me a moment to listen and build your site..."
    else:
        acknowledge_msg = f"🚀 I've received your request. I'm building your website now..."

    # Send quick reply so user knows it's working
    send_whatsapp_message(From, acknowledge_msg)

    # 2. Process in background
    background_tasks.add_task(process_whatsapp_request, Body, From, MediaUrl0)

    return {"status": "processing"}

async def process_whatsapp_request(prompt: str, phone_number: str, media_url: str = None):
    try:
        model = get_gemini_model()

        # Check for existing session (for Website Editing bonus)
        existing_data = get_session(phone_number)

        if existing_data and any(word in (prompt or "").lower() for word in ["change", "update", "make", "add", "fix", "blue", "red", "green", "color"]):
            # This is likely an edit request
            ai_prompt = EDIT_SYSTEM_PROMPT.format(
                current_json=json.dumps(existing_data),
                user_prompt=prompt
            )
        else:
            # This is a new site request
            if media_url:
                prompt = f"[User sent a voice message at {media_url}] - please interpret the requirements for a website."
            ai_prompt = EXTRACTION_SYSTEM_PROMPT.format(user_prompt=prompt)

        response = model.generate_content(ai_prompt)
        data = json.loads(response.text)

        # Save session for future edits
        save_session(phone_number, data)

        # Generation
        generator = SiteGenerator()
        site_path = generator.generate_files(data)

        # Deployment
        print(f"Deploying {data.get('business_name')} to Netlify...")
        url = deploy_to_netlify(site_path, data.get("business_name", "site"))

        # Print the URL to terminal immediately so you can see it!
        print(f"\n🚀 SUCCESS! YOUR WEBSITE IS LIVE AT: {url}\n")

        # Send Reply (Truncated to avoid Twilio 1600 char limit)
        reply = f"✅ Website Generated!\n\n🔗 Live URL: {url}\n\nBusiness: {data.get('business_name')}"
        if len(reply) > 1500:
            reply = reply[:1500] + "..."

        send_whatsapp_message(phone_number, reply)

    except Exception as e:
        # Keep error messages short for WhatsApp
        error_msg = f"❌ Error: {str(e)[:200]}"
        print(f"ERROR: {str(e)}")
        send_whatsapp_message(phone_number, error_msg)

# --- Standard API Endpoint ---
@app.post("/api/v1/generate-site")
async def generate_site(request: SiteGenerationRequest):
    try:
        model = get_gemini_model()
        response = model.generate_content(EXTRACTION_SYSTEM_PROMPT.format(user_prompt=request.prompt))
        data = json.loads(response.text)
        generator = SiteGenerator()
        site_path = generator.generate_files(data)

        return {
            "status": "success",
            "data": {
                "requirements": data,
                "path": site_path
            }
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"\n🚀 WhatsApp AI Generator starting at http://localhost:{port}")
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
