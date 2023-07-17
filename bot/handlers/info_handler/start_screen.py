from aiogram.types import Message

from bot.loader import dp
from bot.services.start_bot_maker import get_main_buttons


@dp.message_handler(text='/start')
async def run_start_command(messages: Message):
    mes = 'Бот работает'
    await messages.answer(mes, reply_markup=get_main_buttons())
