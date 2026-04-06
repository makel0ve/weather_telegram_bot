import os

from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OPENWEATHER_TOKEN = os.getenv("OPENWEATHER_TOKEN", "")
API_URL = "http://api.openweathermap.org/data/2.5/weather"
