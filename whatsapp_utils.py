import os
import requests
import json

# --------------------------------------------------------------
# Load environment variables
# --------------------------------------------------------------

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
RECIPIENT_WAID = os.environ["RECIPIENT_WAID"]
PHONE_NUMBER_ID = os.environ["PHONE_NUMBER_ID"]
VERSION = os.environ["VERSION"]
APP_ID = os.environ["APP_ID"]
APP_SECRET = os.environ["APP_SECRET"]

VIR = os.environ["VIR"]

# SOMETIMES MUST SEND A MESSAGE TO THE TEST NUMBER BEFORE
def get_text_message_input(recipient, text):
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        }
    )

def send_message(data):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"

    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        print("Status:", response.status_code)
        print("Content-type:", response.headers["content-type"])
        print("Body:", response.text)
        return response
    else:
        print(response.status_code)
        print(response.text)
        return response

def send_dolar_notif(dol_type, operation, value):
    message = f'El {dol_type} está {value} para la {operation}'
    data = get_text_message_input(
        recipient=RECIPIENT_WAID, text=message
    )
    send_message(data)

def send_dolar_notif_vir(dol_type, operation, value):
    message = f'El {dol_type} está {value} para la {operation}'
    data = get_text_message_input(
        recipient=VIR, text=message
    )
    send_message(data)