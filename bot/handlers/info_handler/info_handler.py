from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from bot.Constants import Constants
from bot.loader import dp
from bot.services.markup_maker import assets_markup_maker
from traider.get_user_info import user_info


def get_balance_message(my_balance):
    return f'{my_balance.units} {my_balance.currency}, доходность {my_balance.yield_} %'


def price_after_selling_assets():
    return f'Цена после продажи {user_info.get_price_after_selling()}'


@dp.message_handler(Text(equals=Constants.INFO_ASSETS))
async def run_start_command(messages: Message):
    mes = f'Привет, {messages.from_user.full_name}.' \
          f'\n баланс {get_balance_message(user_info.get_total_balance())}' \
          f'\n цена продажи всех активов {price_after_selling_assets()}'
    await messages.answer(mes, reply_markup=assets_markup_maker(
        user_info.get_list_of_assets()))


@dp.callback_query_handler(
    lambda call: call.data.startswith(Constants.ACCETS_CALBACK))
async def download_audio_handler(call: CallbackQuery):
    await call.message.answer(user_info.get_current_asset(call.data))
