import json
import os

SESSION_DIR = "sessions"

def save_session(phone_number, data):
    """Saves the latest site data for a user."""
    os.makedirs(SESSION_DIR, exist_ok=True)
    file_path = os.path.join(SESSION_DIR, f"{phone_number.replace(':', '_')}.json")
    with open(file_path, "w") as f:
        json.dump(data, f)

def get_session(phone_number):
    """Retrieves the latest site data for a user."""
    file_path = os.path.join(SESSION_DIR, f"{phone_number.replace(':', '_')}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return None
