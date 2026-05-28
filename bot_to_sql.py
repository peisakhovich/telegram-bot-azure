import asyncio
import os
import psycopg2
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def get_conn():
    return psycopg2.connect(DATABASE_URL)

@dp.message(Command("start"))
async def start(message: types.Message):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO users (telegram_id, username)
        VALUES (%s, %s)
        ON CONFLICT (telegram_id) DO NOTHING;
    """, (message.from_user.id, message.from_user.username))

    conn.commit()
    cur.close()
    conn.close()

    await message.answer("Бот подключен к Neon ✔")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())