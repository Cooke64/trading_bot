from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from tinkoff.invest.grpc.operations_pb2 import Operation

from bot.Constants import Constants
from bot.loader import dp
from bot.services.markup_maker import assets_markup_maker, \
    current_asset_markup_maker
from traider.user_info_service.get_user_info import user_info, user_operations


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


def get_mes(opers: list[Operation]):
    res = [i for i in opers]
    return 'new_mes'


@dp.message_handler(Text(equals=Constants.LAST_OPERATIONS))
async def get_list_of_operations(messages: Message):
    mes = user_operations.get_last_operations()
    mew = get_mes(mes)
    await messages.answer(text=mew)


@dp.callback_query_handler(
    lambda call: call.data.startswith(Constants.ACCETS_CALBACK))
async def current_asset_item_handler(call: CallbackQuery):
    await call.message.answer(
        user_info.get_current_asset(call.data),
        reply_markup=current_asset_markup_maker(call.data)
    )
