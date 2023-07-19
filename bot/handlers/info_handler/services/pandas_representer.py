from pandas import DataFrame

from traider.responses.candles_response import CandleBase
from ta.trend import ema_indicator
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def create_candle_df(candles: list[CandleBase]):
    df = DataFrame(
        [{**candle.dict()} for candle in candles]
    )
    return df


def create_candle_image(candles) -> str:
    df = DataFrame(
        [{**candle.dict()} for candle in candles]
    )
    df['ema'] = ema_indicator(close=df['close'], window=9)
    ax = df.plot(x='time', y='close')
    df.plot(ax=ax, x='time', y='ema')
    png_name = 'saved_figure.png'
    plt.savefig(png_name)
    return png_name
