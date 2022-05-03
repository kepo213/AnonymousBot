from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import Dispatcher


def register_middleware(dp: Dispatcher):
    dp.middleware.setup()
