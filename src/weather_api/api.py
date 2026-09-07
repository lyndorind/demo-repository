import requests

WEATHER_API_KEY = "f574b5a2ae174c37946140519260709"


def get_weather(city: str) -> dict[str, any]:
    params = {
        "q": city,
        "key": WEATHER_API_KEY
    }

    response = requests.get("https://api.weatherapi.com/v1/current.json", params=params)
    return response.json()["current"]

def get_timezone(city: str) -> dict[str, any]:
    params = {
        "q": city,
        "key": WEATHER_API_KEY
    }

    response = requests.get("https://api.weatherapi.com/v1/timezone.json", params=params)
    return response.json()["location"]["tz_id"]
