from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from bot.handlers.common import start
from bot.handlers.dialog import send_message_to_dialog, start_dialog, end_dialog, cancel_waiting
from bot.states import DialogState


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start", "help"])
    dp.register_message_handler(start_dialog, commands=["new_dialog"])
    dp.register_message_handler(end_dialog, commands=["end_dialog"], state=DialogState.dialog)
    dp.register_message_handler(send_message_to_dialog, state=DialogState.dialog, content_types=types.ContentTypes.all())
    dp.register_message_handler(cancel_waiting, commands=["cancel"], state=DialogState.waiting)
