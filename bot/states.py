from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Dispatcher
from bot.config import dp


class MyState(State):
    """"Переопределяем метод set для возможности set state по user_id"""
    async def set(self, user_id=None):
        """Option to set state for concrete user"""
        state = Dispatcher.get_current().current_state(user=user_id, chat=user_id)
        await state.set_state(self.state)


class DialogState(StatesGroup):
    waiting = MyState()
    dialog = MyState()
