import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from weather import get_weather


logger = logging.getLogger(__name__)
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        "Привет! Отправь мне название города, и я покажу текущую погоду."
    )


@router.message()
async def weather_handler(msg: Message):
    city = msg.text.strip()

    if not city:
        await msg.reply("Введите название города")
        
        return

    try:
        data = await get_weather(city)

    except Exception as e:
        logger.error("Ошибка при запросе погоды: %s", e)
        await msg.reply("Не удалось получить данные о погоде. Попробуйте позже.")

        return

    if data is None:
        await msg.reply("Город не найден. Проверьте название и попробуйте снова.")

        return

    await msg.reply(data.format_message())