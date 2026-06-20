import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("اهلاً بك في بوت فَـدُؤْكَـة 🛡")

async def main():
    print("Bot Started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
