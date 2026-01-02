import logging
from aiogram import Bot, Dispatcher, executor, types

# Вставь сюда токен, который ты взял у @BotFather
API_TOKEN = '8509244045:AAHF5UjdLnUyYbEW-SGLiSX44W55LMj6dVs'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Этот обработчик отвечает на команду /start.
    Помогает узнать твой ID, если ты его забыл.
    """
    user_id = message.from_user.id
    await message.reply(f"Привет! Я бот для CityGDPS.\nТвой ID: {user_id}\nУбедись, что этот ID прописан в коде сайта в TG_CHAT_ID.")

if __name__ == '__main__':
    print("Бот запущен и готов к работе...")
    executor.start_polling(dp, skip_updates=True)
