import asyncio
import logging
import tracemalloc

import uvicorn
from aiogram import Bot, Dispatcher
from fastapi import FastAPI

from bot.config import BOT_TOKEN, API_HOST, API_PORT
from bot.handlers import botRouter
from bot.middlewares import LoggingMiddleware
from bot.routers import centralApiRouter

# FastAPI
app = FastAPI(title="Bot API")

app.include_router(centralApiRouter)

app.add_middleware(LoggingMiddleware)

# Bot
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

async def start_bot():
    dp.include_router(botRouter)
    await dp.start_polling(bot)

async def start_api():
    config = uvicorn.Config(app, host=API_HOST, port=API_PORT)
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    await asyncio.gather(
        start_bot(),
        start_api()
    )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    tracemalloc.start()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')