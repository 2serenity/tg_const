# bot.py
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# Функция для запуска бота с динамическим токеном
async def start_bot(token):
    bot = Bot(token=token)
    dp = Dispatcher()

    # Обработчик команды /start
    @dp.message(Command("start"))
    async def send_welcome(message: Message):
        await message.reply("Привет! Я Telegram бот, запущенный из Kivy!")

    # Обработчик текстовых сообщений
    @dp.message()
    async def echo(message: Message):
        await message.answer(message.text)

    print("Бот запущен...")
    await dp.start_polling(bot)
