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
**Demo Video:** [Link to your video here]
**Developer:** [Your Name]
