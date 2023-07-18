from aiogram.types import CallbackQuery, InputFile
from tinkoff.invest import CandleInterval

from bot.Constants import Constants
from bot.handlers.info_handler.services.pandas_representer import \
    create_candle_df, create_candle_image
from bot.loader import dp, bot
from traider.candles_service.get_my_candles import candles, TimeDelta


async def get_candles(figi: str, chat_id: int = None):
    all_candles = candles.get_candles_by_figi(
        figi, TimeDelta.days, 5, CandleInterval.CANDLE_INTERVAL_DAY
    )
    file_name = create_candle_image(all_candles)
    photo = InputFile(file_name)

    await bot.send_photo(chat_id=chat_id, photo=photo)
    return create_candle_df(all_candles)


async def get_benefits(figi, *args):
    print(figi)


async def buy_item(figi, *args):
    print(figi)


async def sell_item(figi, *args):
    print(figi)


func = {
    'candle': get_candles,
    'benefits': get_benefits,
    'buy': buy_item,
    'sell': sell_item,
}


@dp.callback_query_handler(
    lambda call: call.data.startswith(Constants.CURRENT_ITEM))
async def download_audio_handler(call: CallbackQuery):
    _, fun_name, figi = call.data.split('_')
    message = await func.get(fun_name)(figi, call.message.chat.id)
    await call.message.answer(text=message)
