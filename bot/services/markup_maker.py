from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.Constants import Constants
from traider.responses.user_info_responses import AssetsShow


def assets_markup_maker(my_assets: list[AssetsShow]) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    for item in my_assets:
        short_name = item.name.split()[0]
        callback_data = f'{Constants.ACCETS_CALBACK}{item.figi}'
        markup.add(InlineKeyboardButton(text=short_name, callback_data=callback_data))
    return markup
