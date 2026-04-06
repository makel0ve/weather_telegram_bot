from dataclasses import dataclass
from datetime import datetime

import aiohttp

from config import OPENWEATHER_TOKEN, API_URL


@dataclass
class WeatherData:
    """Данные о погоде для отображения пользователю."""

    city: str
    temp: float
    description: str
    humidity: int
    pressure_mmhg: int
    wind_speed: float
    sunrise: datetime
    sunset: datetime

    @property
    def day_length(self) -> str:
        delta = self.sunset - self.sunrise
        hours, remainder = divmod(delta.seconds, 3600)
        minutes = remainder // 60

        return f"{hours}ч {minutes}мин"

    def format_message(self) -> str:
        return (
            f"{datetime.now().strftime('%H:%M %d/%m/%Y')}\n"
            f"Погода в городе: {self.city}\n"
            f"Температура: {self.temp}°C, {self.description}\n"
            f"Влажность: {self.humidity}%\n"
            f"Давление: {self.pressure_mmhg} мм.рт.ст\n"
            f"Ветер: {self.wind_speed} м/с\n"
            f"Восход: {self.sunrise.strftime('%H:%M')}\n"
            f"Закат: {self.sunset.strftime('%H:%M')}\n"
            f"Продолжительность дня: {self.day_length}"
        )


async def get_weather(city: str) -> WeatherData | None:
    """
    Запрашивает текущую погоду для указанного города.

    Args:
        city: название города.

    Returns:
        WeatherData или None, если город не найден.
    """

    params = {
        "q": city,
        "lang": "ru",
        "units": "metric",
        "appid": OPENWEATHER_TOKEN,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params=params) as response:
            if response.status != 200:
                return None

            data = await response.json()

    if not data.get("name"):
        return None

    return WeatherData(
        city=data["name"],
        temp=data["main"]["temp"],
        description=data["weather"][0]["description"],
        humidity=data["main"]["humidity"],
        pressure_mmhg=round(data["main"]["pressure"] / 1.333),
        wind_speed=data["wind"]["speed"],
        sunrise=datetime.fromtimestamp(data["sys"]["sunrise"]),
        sunset=datetime.fromtimestamp(data["sys"]["sunset"]),
    )