from aiogram.types import Message
from bot.database import add_user


async def start(message: Message):
    add_user(message.from_user.id, message.from_user.full_name)
    await message.answer(
        "Здравствуйте. Это бот для анонимного чата.\nВозможно, мы будем хранить в базе данных ваши сообщения, "
        "но так как бот анонимный, у вас не будет никаких данных о разработчике.\nДля нового диалога пропишите "
        "/new_dialog\n "
        "Для остановки - /end_dialog\n Желаю хорошо провести время.")
