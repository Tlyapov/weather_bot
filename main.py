import asyncio
import requests
from aiogram import Bot, Dispatcher
from app.handlers import router
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    bot_token = os.getenv("bot_token")
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('bot off')