from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886" # Default Sandbox Number

client = None
if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to_number, message_body):
    if not client:
        print(f"Twilio not configured. Message to {to_number}: {message_body}")
        return

    client.messages.create(
        body=message_body,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=to_number
    )
