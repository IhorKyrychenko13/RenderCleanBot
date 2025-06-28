import asyncio
import os
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

keywords = ["запрещённое слово1", "запрещённое слово2", "запрещённое слово3"]

def normalize_text(text):
    return ' '.join(text.split()).lower().strip() if text else ""

async def delete_bot_message(message):
    await asyncio.sleep(60)
    try:
        await message.delete()
        print(f"✅ Сообщение от бота удалено через минуту: {message.message_id}")
    except Exception as e:
        print(f"Ошибка при удалении сообщения от бота: {e}")

@router.message()
async def check_and_delete(message: Message):
    if message.chat.id != CHANNEL_ID:
        print(f"Сообщение из другой группы: {message.chat.id}, игнорируем")
        return

    if message.from_user.username == "GroupHelp":
        raw_text = message.text or message.caption or ""
        print(f"Сообщение от GroupHelp: {raw_text}")
        if any(keyword.lower() in raw_text.lower() for keyword in keywords):
            print("Обнаружено запрещённое сообщение от GroupHelp. Удаляем.")
            await message.delete()
        else:
            print("Запрещённые слова в сообщении от GroupHelp не обнаружены.")
        return

    photos = message.photo or []
    photo_count = len(photos)
    raw_text = message.text or message.caption or ""
    text = normalize_text(raw_text)
    thread_id = message.message_thread_id if message.is_topic_message else 0
    username = message.from_user.username or message.from_user.full_name

    print(f"Получено сообщение от @{username}: {text if text else '[Без текста]'}. Изображения: {photo_count}")

    # Здесь должна быть логика базы, если она нужна (удалена по твоему запросу)
    print("✅ Симуляция сохранения сообщения в базу")

async def main():
    dp.include_router(router)
    print("Бот запущен и готов к работе")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
