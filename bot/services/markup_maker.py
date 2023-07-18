from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.Constants import Constants
from traider.responses.user_info_responses import AssetsShow


def assets_markup_maker(my_assets: list[AssetsShow]) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    for item in my_assets:
        short_name = item.name.split()[0]
        callback_data = f'{Constants.ACCETS_CALBACK}{item.figi}'
        markup.add(
            InlineKeyboardButton(text=short_name, callback_data=callback_data))
    return markup


def current_asset_markup_maker(figi: str):
    figi = figi.split('_')[1]
    current_asset = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='График свеч', callback_data=f'Item_candle_{figi}'
                ),
                InlineKeyboardButton(
                    text='Доходность', callback_data=f'Item_benefits_{figi}'
                ),
                InlineKeyboardButton(
                    text='Купить', callback_data=f'Item_buy_{figi}'
                ),
                InlineKeyboardButton(
                    text='Продать', callback_data=f'Item_sell_{figi}'
                ),
            ],
        ],
        row_width=2
    )
    return current_asset

