import time

from rich.live import Live

from modules.gps import detect_location
from modules.weather import get_weather
from modules.widgets import render_widget
from modules.cyclone import cyclone_check
from modules.voice import speak
from modules.telegram_alert import send_alert

from config import REFRESH_TIME


city = detect_location()

with Live(refresh_per_second=1) as live:

    while True:

        weather_data = get_weather(city)

        live.update(
            render_widget(weather_data)
        )

        if "error" not in weather_data:

            if cyclone_check(
                weather_data["weather"]
            ):

                alert = (
                    f"⚠️ Cyclone Alert in {city}"
                )

                speak(alert)

                send_alert(alert)

        time.sleep(REFRESH_TIME)
