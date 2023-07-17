from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.Constants import Constants

main_menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=Constants.INFO_ASSETS),
            KeyboardButton(text='❕ Пройду ли я к вам?'),
        ],
        [
            KeyboardButton(text='📞 Связаться с нами'),
            KeyboardButton(text='✉ Оставить сообщение'),
        ],
        [
            KeyboardButton(text='Новости'),
        ],
    ],
    resize_keyboard=True
)
admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛂 Получить информацию'),
            KeyboardButton(text='❕ Пройду ли я к вам?'),
        ],
        [
            KeyboardButton(text='Новости'),
            KeyboardButton(text='Админ панель'),
        ],
    ],
    resize_keyboard=True
)
info_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Про расположение'),
            KeyboardButton(text='Чем предстоит заниматься?'),
        ],
        [
            KeyboardButton(text='Льготы и зарплата'),
            KeyboardButton(text='Видеопрезентация'),
        ],
        [
            KeyboardButton(text='Вернуться в главное меню.'),
        ],
    ],
    resize_keyboard=True
)


async def contact_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    first_button = KeyboardButton(text="📱 Отправить", request_contact=True)
    markup.add(first_button)
    return markup