from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup
)

from bot.keyboards.main_menu_buttons import main_menu_buttons


def get_main_buttons() -> ReplyKeyboardMarkup:
    return main_menu_buttons


async def start_leaving_message(bot_type: Message | CallbackQuery) -> None:
    message_or_query = isinstance(bot_type, Message)
    replyer = bot_type.answer if message_or_query else bot_type.message.answer
    await replyer(
        'Оставьте сообщение и как мы ответим вам можно скорее!'
    )
