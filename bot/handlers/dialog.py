from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher

from bot.config import bot
from bot.database import search_opponent, end_waiting, delete_opponent, set_opponent, get_opponent_id
from bot.states import DialogState


async def send_message_to_dialog(message: Message):
    opponent_id = get_opponent_id(message.from_user.id)
    match message.content_type:
        case ContentType.TEXT:
            text = message.text
            await bot.send_message(opponent_id, text)
        case ContentType.AUDIO:
            audio = message.audio.file_id
            await bot.send_audio(opponent_id, audio)
        case ContentType.VOICE:
            voice = message.voice.file_id
            await bot.send_voice(opponent_id, voice)
        case ContentType.VIDEO:
            video = message.video.file_id
            await bot.send_video(opponent_id, video)
        case ContentType.DOCUMENT:
            document = message.document.file_id
            await bot.send_document(opponent_id, document)
        case ContentType.VIDEO_NOTE:
            video_note = message.video_note.file_id
            await bot.send_video_note(opponent_id, video_note)
        case ContentType.PHOTO:
            photo = message.photo[2].file_id
            await bot.send_photo(opponent_id, photo)


async def start_dialog(message: Message):
    opponent_id = search_opponent(message.from_user.id)
    if opponent_id is None:
        await bot.send_message(message.from_user.id, "Вы добавлены в очередь")
        await DialogState.waiting.set(message.from_user.id)
        return
    text = "Собеседник найден. Для завершения диалога введите /end_dialog"
    end_waiting(message.from_user.id)
    end_waiting(opponent_id)
    set_opponent(message.from_user.id, opponent_id)
    await DialogState.dialog.set(opponent_id)
    await DialogState.dialog.set(message.from_user.id)
    await bot.send_message(message.from_user.id, text)
    await bot.send_message(opponent_id, text)


async def end_dialog(message: Message, state: FSMContext):
    opponent_id = get_opponent_id(message.from_user.id)
    delete_opponent(message.from_user.id, opponent_id)
    opponent_state = Dispatcher.get_current().current_state(user=opponent_id, chat=opponent_id)
    text = "Беседа окончена. Для новой напишите /new_dialog"
    await state.finish()
    await opponent_state.finish()
    await bot.send_message(message.from_user.id, text)
    await bot.send_message(opponent_id, text)


async def cancel_waiting(message: Message, state: FSMContext):
    end_waiting(message.from_user.id)
    await state.finish()
    await message.answer("Вы отменили поиск собеседника.")
