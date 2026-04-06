# Weather Telegram Bot

Телеграм-бот для получения текущей погоды. Отправляешь название города — получаешь температуру, влажность, давление, ветер, время восхода и заката.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Aiogram](https://img.shields.io/badge/Aiogram-3-green)
![OpenWeather](https://img.shields.io/badge/OpenWeather-API-orange)

## Пример ответа

```
14:30 06/04/2026
Погода в городе: Москва
Температура: -2.5°C, пасмурно
Влажность: 78%
Давление: 748 мм.рт.ст
Ветер: 3.2 м/с
Восход: 06:15
Закат: 19:42
Продолжительность дня: 13ч 27мин
```

## Стек

- **Aiogram 3** — асинхронный фреймворк для Telegram Bot API
- **aiohttp** — асинхронные HTTP-запросы к OpenWeather API
- **python-dotenv** — загрузка токенов из `.env`

## Структура проекта

```
weather_telegram_bot/
├── main.py            # Точка входа, запуск бота
├── handlers.py        # Обработчики сообщений
├── weather.py         # Логика запросов к OpenWeather API
├── config.py          # Загрузка конфигурации из .env
├── requirements.txt   # Зависимости
├── .env.example       # Шаблон переменных окружения
└── README.md
```

## Установка и запуск

1. Клонировать репозиторий:

```bash
git clone https://github.com/makel0ve/weather_telegram_bot.git
cd weather_telegram_bot
```

2. Установить зависимости:

```bash
pip install -r requirements.txt
```

3. Создать `.env` файл и указать токены:

```bash
cp .env.example .env
```

```
BOT_TOKEN=ваш_токен_от_BotFather
OPENWEATHER_TOKEN=ваш_ключ_от_OpenWeather
```

4. Запустить:

```bash
python main.py
```

## Получение токенов

- **Telegram Bot Token** — создайте бота через [BotFather](https://t.me/BotFather)
- **OpenWeather API Key** — зарегистрируйтесь на [openweathermap.org](https://openweathermap.org/api) и получите бесплатный ключ