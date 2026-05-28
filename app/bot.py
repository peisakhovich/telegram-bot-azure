import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN missing")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def remove_webhook():
    webhook_info = await bot.get_webhook_info()

    print("Current webhook:", webhook_info.url)

    await bot.delete_webhook(drop_pending_updates=True)

    print("Webhook deleted")


@dp.message()
async def all_messages(message: Message):
    print("MESSAGE:", message.text)

    await message.answer(
        f"Получил сообщение: {message.text}"
    )

@dp.channel_post()
async def channel_post_handler(message: Message):
    print("CHANNEL MESSAGE:", message.text)




async def start_bot():
    await remove_webhook()

    print("Bot is running...")

    await dp.start_polling(bot)


def main():
    asyncio.run(start_bot())