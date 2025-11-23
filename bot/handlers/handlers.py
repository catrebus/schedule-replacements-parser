from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.crud import create_user

botRouter = Router()

@botRouter.message(CommandStart())
async def cmdStart(message: Message):
    await create_user(message.chat.id)
    await message.answer("Бот готов к работе")
