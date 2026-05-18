import geocoder


def detect_location():

    try:

        g = geocoder.ip("me")

        if g.ok and g.city:
            return g.city.strip()

    except Exception:
        pass

    return "Dhaka"
