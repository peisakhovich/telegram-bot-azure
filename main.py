import os
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher
from aiogram.types import Update

app = FastAPI()
dp = Dispatcher()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)


@app.get("/")
async def root():
    return {"status": "running"}


@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.model_validate(data)

    await dp.feed_update(bot, update)

    return {"ok": True}


@dp.message()
async def echo(message):
    await message.answer(f"Echo: {message.text}")
