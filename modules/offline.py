import json
import os


def save_cache(data, filename):

    try:

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    except Exception:
        pass


def load_cache(filename):

    try:

        if not os.path.exists(filename):
            return None

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:
        return None
