# Telegram Bot for Render

## Установка зависимостей
```
pip install -r requirements.txt
```

## Настройка переменных
Создайте файл `.env` и укажите в нём:
```
TOKEN=your_bot_token
CHANNEL_ID=123456789
```

## Запуск
```
python bot.py
```

## Деплой на Render
1. Загрузите этот репозиторий в GitHub
2. Подключите его к Render
3. Укажите:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
   - Environment: Python 3.10+
