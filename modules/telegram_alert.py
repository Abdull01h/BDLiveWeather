import requests

from config import BOT_TOKEN
from config import CHAT_ID


def send_alert(message):

    try:

        url = (
            f"https://api.telegram.org/"
            f"bot{BOT_TOKEN}/sendMessage"
        )

        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        requests.post(
            url,
            data=payload,
            timeout=5
        )

    except Exception:
        pass
