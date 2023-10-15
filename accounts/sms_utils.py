import requests
from django.conf import settings

def send_sms_via_infobip(phone_number, message):
    url = f"{settings.INFOBIP_BASE_URL}/sms/2/text/single"
    headers = {
        "Authorization": f"App {settings.INFOBIP_API_KEY}"
    }
    payload = {
        "from": settings.INFOBIP_DEFAULT_FROM,
        "to": phone_number,
        "text": message
    }

    response = requests.post(url, headers=headers, json=payload)
    return response
