from rich.panel import Panel


def render_widget(data):

    if "error" in data:

        return Panel(
            f"❌ Error:\n{data['error']}",
            title="Weather Error"
        )

    return Panel.fit(
        f"""
🌍 City: {data['city']}

🌡️ Temp: {data['temp']}°C

💧 Humidity: {data['humidity']}%

🌧️ Rain Chance: {data['rain']}%

☁️ Weather: {data['weather']}
""",
        title="BD Live Weather"
    )
