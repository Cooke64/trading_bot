from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

current_asset = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='График свеч', callback_data='Item_candle'
            ),
            InlineKeyboardButton(
                text='Доходность', callback_data='Item_benefits'
            ),
            InlineKeyboardButton(
                text='Купить', callback_data='Item_buy'
            ),
            InlineKeyboardButton(
                text='Продать', callback_data='Item_sell'
            ),
        ],
    ],
    row_width=2
)