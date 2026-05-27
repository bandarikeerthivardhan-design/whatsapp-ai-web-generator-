# System Architecture Document

## 🏗️ System Design Diagram

```text
[ User (WhatsApp) ] 
       │
       ▼
[ Twilio Webhook ] ──▶ [ FastAPI (main.py) ]
                               │
                               ▼
                    [ Background Task (process_whatsapp_request) ]
                               │
       ┌───────────────────────┴───────────────────────┐
       │                                               │
       ▼                                               ▼
[ Gemini 1.5 Flash ]                          [ Generator Engine ]
(Requirement Extraction)                      (Jinja2 + React Templates)
       │                                               │
       └───────────────────────┬───────────────────────┘
                               │
                               ▼
                     [ Netlify Deployment API ]
                               │
                               ▼
                    [ Twilio Messaging API ] ──▶ [ User (Live URL) ]
```

## 🔄 Data Flow Explanation

1. **Ingress:** The user sends a text prompt to the WhatsApp bot. Twilio forwards this as a POST request to our `/whatsapp` webhook.
2. **Acknowledgement:** The system immediately sends a "Processing" message back to the user to manage expectations.
3. **Intelligence (AI):** The prompt is sent to Google Gemini 1.5 Flash. The AI uses a specialized system prompt to output a structured JSON object containing business type, theme, colors, and marketing copy.
4. **Creation (Engine):** The `SiteGenerator` engine takes the JSON data and populates Jinja2 templates for `App.jsx`, `index.css`, `tailwind.config.js`, etc., creating a standalone React project directory.
5. **Fulfillment (Deployment):** The generated folder is zipped and sent to the Netlify API. Netlify hosts the static assets and returns a unique live URL.
6. **Egress:** The system sends a final WhatsApp message to the user containing the live URL and a summary of the generated features.

## ⚖️ Tech Stack Justification

### 1. Gemini 1.5 Flash
- **Why:** Chosen over GPT-4 or Gemini Pro for its superior speed and low latency. In a 3-minute turnaround requirement, every second counts. It is highly capable of JSON extraction.

### 2. FastAPI
- **Why:** Asynchronous by nature, making it perfect for handling webhooks and background tasks without blocking the main thread.

### 3. Netlify API
- **Why:** Offers the simplest "zip-and-deploy" API for static sites, allowing for instant hosting without complex CLI configurations.

### 4. Tailwind CSS
- **Why:** Allows the AI to generate modern designs by simply changing class strings. It ensures the generated sites look professional with zero custom CSS writing.

### 5. Jinja2
- **Why:** Provides a powerful way to inject AI-generated content into React code while maintaining clean, readable templates.
