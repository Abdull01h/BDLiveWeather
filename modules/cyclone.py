DANGER_KEYWORDS = [
    "storm",
    "cyclone",
    "hurricane",
    "thunderstorm",
    "heavy rain"
]


def cyclone_check(weather):

    weather = weather.lower()

    return any(
        word in weather
        for word in DANGER_KEYWORDS
    )
