# Weather telegram bot

Этот бот для Telegram предоставляет информацию о текущей погоде, используя API OpenWeather.

## Возможности
- Получение актуальных данных о погоде на основе введенного города или местоположения.
- Отображение температуры, погодных условий и других подробностей.
- Простое управление через команды в Telegram.

## Требования
- Python 3.7+
- Токен Telegram-бота (получается через [BotFather](https://core.telegram.org/bots#botfather))
- Ключ API OpenWeather ([openweathermap.org](https://openweathermap.org/))

## Установка
- Клонировать репозиторий
```
git clone https://github.com/makel0ve/weather_telegram_bot.git
```
- Перейти в папку с проектом
```
cd weather_telegram_bot
```
- Установить зависимости
```
pip install -r requirements.txt
```
- Поместить токены в файл config.py
  - BOT_TOKEN: Токен ваше бота Telegram
  - OPENWEATHER_TOKEN: Ключ API OpenWeather

Пример файла config.py
```
BOT_TOKEN = "your_telegram_token"
OPENWEATHER_TOKEN = "your_weather_api_key"
```

## Использование
```
python main.py
```

## Файлы
- main.py: Основной файл для запуска бота
- handlers.py: Обработка входящих сообщений и ответов бота
- config.py: Настройки для токенов и API-ключей
