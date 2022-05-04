from aiogram import types, Dispatcher
# from bot.config import dp


async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("help", "Инфа о боте"),
            types.BotCommand("new_dialog", "Начать новый диалог"),
            types.BotCommand("end_dialog", "Закончить действующий диалог"),
            types.BotCommand("cancel", "Отменить поиск диалога"),

        ]
    )
