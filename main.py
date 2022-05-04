import logging

from aiogram import executor
from bot.config import dp
from bot.database import init_main_information
from bot.regiter_handlers import register_handlers
from bot.set_commands import set_commands

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    init_main_information()
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=set_commands)
