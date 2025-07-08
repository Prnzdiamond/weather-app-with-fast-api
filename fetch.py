import os
import requests

from dotenv import load_dotenv

load_dotenv()


def get_weather(city):
    apikey = os.getenv("OPENWEATHER_API_KEY")
    print(apikey)
    response = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={apikey}&q={city}&aqi=no")
    data = response.json()
    return data
