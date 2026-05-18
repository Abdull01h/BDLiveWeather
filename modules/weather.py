import requests

from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(city):

    try:

        params = {
            "q": f"{city},BD",
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=5
        )

        response.raise_for_status()

        data = response.json()

        current = data["list"][0]

        return {
            "city": city,
            "temp": current["main"]["temp"],
            "humidity": current["main"]["humidity"],
            "weather": current["weather"][0]["description"],
            "rain": current.get("pop", 0) * 100
        }

    except Exception as e:

        return {
            "error": str(e)
        }
