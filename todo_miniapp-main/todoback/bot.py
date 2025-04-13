import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters.command import Command
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Получаем токен бота и URL фронтенда из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN", "7713242801:AAH0Jw7LJiKP6P-e0eXW1PD_gChsNRP0yTk")
FRONTEND_URL = os.getenv("FRONTEND_URL", "https://your-netlify-app.netlify.app")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Кнопка для запуска веб-приложения
    webapp_button = InlineKeyboardButton(
        text="Открыть Todo приложение", 
        web_app=WebAppInfo(url=FRONTEND_URL)
    )
    
    # Создаем клавиатуру с кнопкой
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[webapp_button]])
    
    # Отправляем приветственное сообщение с кнопкой
    await message.answer(
        "Привет! Я помогу вам управлять вашими задачами. Нажмите на кнопку ниже, чтобы открыть Todo приложение:",
        reply_markup=keyboard
    )

# Запуск бота
async def main():
    logging.info("Starting bot")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 