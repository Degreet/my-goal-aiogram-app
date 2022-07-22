from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if __name__ == "__main__":
    from handlers import setup_handlers
    from db import database

    setup_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
    database.db.close()
