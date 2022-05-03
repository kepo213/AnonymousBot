from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from bot.handlers.common import start
from bot.handlers.dialog import send_message_to_dialog, start_dialog, end_dialog
from bot.states import DialogState


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start", "help"])
    dp.register_message_handler(start_dialog, commands=["new_dialog"])
    dp.register_message_handler(end_dialog, commands=["end_dialog"], state=DialogState.dialog)
    dp.register_message_handler(send_message_to_dialog, state=DialogState.dialog)
    set_commands(dp)


def set_commands(dp: Dispatcher):
    dp.bot.set_my_commands(
        [
            types.BotCommand("help", "Инфа о боте"),
            types.BotCommand("new_dialog", "Начать новый диалог"),
            types.BotCommand("end_dialog", "Закончить действующий диалог"),

        ]
    )
