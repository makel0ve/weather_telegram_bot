import requests
import math
from datetime import datetime
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import config


router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer("Приветствую в боте для узнавания погоды.")
    
    
@router.message()
async def get_weather(msg: Message):
    text = msg.text[0].upper() + msg.text[1:]
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={text}&lang=ru&units=metric&appid={config.OPENWEATHER_TOKEN}")
    data = response.json()

    if data.get('name'):
        city = data["name"]
        current_temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(data["sys"]["sunset"])
        len_of_the_day = sunset - sunrise
        sunrise = sunrise.strftime('%H:%M %d/%m/%Y')
        sunset = sunset.strftime('%H:%M %d/%m/%Y')
        weather_description_eng_to_rus = {
            "Clear": "Ясно",
            "Clouds": "Облачно",
            "Rain": "Дождь",
            "Drizzle": "Дождь",
            "Thunderstorm": "Гроза",
            "Snow": "Снег",
            "Mist": "Туман"
        }
        weather_description = data["weather"][0]["main"]
        if weather_description in weather_description_eng_to_rus:
            wd = weather_description_eng_to_rus[weather_description]
        else:
            wd = "Я не знаю какого типа погода"
        await msg.reply(f"{datetime.now().strftime('%H:%M %d/%m/%Y')}\n"\
                            f"Погода в городе: {city}\n"\
                            f"Температура: {current_temp} {wd}\n"\
                            f"Влажность: {humidity}\n"\
                            f"Давление: {math.ceil(pressure/1.333)} мм.рт.ст\n"\
                            f"Ветер: {wind} м/с\n"\
                            f"Восход солнца: {sunrise}\n"\
                            f"Закат солнца: {sunset}\n"\
                            f"Продолжительность дня: {len_of_the_day}")
    else:
        await msg.reply("Проверьте название города")