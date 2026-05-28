# WhatsApp AI Website Generator 🚀

An automated AI-powered website generation system that accepts requests via WhatsApp and delivers fully deployed websites within minutes. Built for the ElevateBox Internship Screening Task.

## 📖 Problem Statement
The goal is to build a zero-friction website builder. A user sends a simple message on WhatsApp (e.g., "Build me a restaurant website"), and the system automatically extracts requirements, generates a professional React + Tailwind CSS website, and deploys it to a live URL.

## 🛠️ Tech Stack
- **Backend:** FastAPI (Python)
- **AI Brain:** Google Gemini 1.5 Flash (Requirement extraction & content generation)
- **WhatsApp Integration:** Twilio WhatsApp Sandbox
- **Site Engine:** React + Tailwind CSS (via Jinja2 Templating)
- **Deployment:** Netlify API
- **Tooling:** Uvicorn, Pydantic, Requests
- ## 🏗️ System Architecture

The system follows a modular event-driven architecture to ensure high performance and scalability.

### **Data Flow Overview**
1. **Inbound Trigger:** User sends a natural language prompt via WhatsApp.
2. **Webhook Tunneling:** **Twilio** receives the message and forwards it via a **Localtunnel** webhook to the local **FastAPI** server.
3. **AI Orchestration:** The backend sends the prompt to **Google Gemini 2.0**. It performs:
   - **Requirement Extraction:** Converts text to a structured JSON blueprint.
   - **Content Generation:** Writes marketing copy, headers, and descriptions.
4. **Site Engine:** A custom **Jinja2** engine injects the AI-generated JSON into modern **Tailwind CSS/HTML** templates.
5. **Automated Deployment:** The system zips the generated site and pushes it to **Netlify** via its REST API.
6. **Outbound Notification:** The backend receives a live URL from Netlify and sends it back to the user via **Twilio WhatsApp API**.

### **Module Breakdown**
- `main.py`: The central FastAPI controller and endpoint manager.
- `src/ai/`: Handles communication with Google Gemini and prompt engineering.
- `src/generator/`: The "Engine" that builds the physical files from AI data.
- `src/deployment/`: Manages automated cloud uploads to Netlify.
- `src/whatsapp/`: Manages the Twilio messaging lifecycle.
- `templates/`: Professional-grade Jinja2 templates for various business niches.

---

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.10+
- Node.js & npm (to run generated sites locally)
- [ngrok](https://ngrok.com/) (to expose local server to WhatsApp)

### 2. Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd whatsapp-ai

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory and add the following:
```env
GEMINI_API_KEY=your_gemini_api_key
NETLIFY_AUTH_TOKEN=your_netlify_personal_access_token
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
PORT=8000
```

### 4. Running the Application
```bash
python main.py
```

### 5. Connecting to WhatsApp
1. Start ngrok: `ngrok http 8000`
2. Copy the `https` URL provided by ngrok.
3. Go to Twilio Console > Messaging > Try it Out > WhatsApp Sandbox.
4. Paste the URL in the "When a message comes in" field: `https://<your-ngrok-url>/whatsapp`
5. Save settings.

## 🧪 How to Test
1. Send a message to your Twilio Sandbox number: `"Create a modern dark-themed portfolio for a creative developer named Alex."`
2. Wait for the bot to acknowledge.
3. In ~2 minutes, receive a live Netlify URL.

## ⚠️ Limitations
- **React Build:** Currently deploys source files for preview. A full production build step can be added in `src/deployment`.
- **Media:** Uses Unsplash placeholders; direct image upload from WhatsApp is a future feature.

## 🔮 Future Improvements
- **Voice Message Support:** Integration with OpenAI Whisper for voice-to-website.
- **Interactive Editing:** "Change the hero color to red" via follow-up WhatsApp messages.
- **Custom Domains:** Automated mapping via Netlify/Cloudflare API.

---
**Demo Video:** [https://drive.google.com/file/d/1FQQx6DAm9UtlnnfCKEs8sQSzkFjp4Fll/view?usp=drive_link]
]
**Developer:** [keerthivardhan]
