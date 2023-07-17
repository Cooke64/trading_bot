import datetime
import logging
from enum import Enum
from xmlrpc.client import ResponseError

from tinkoff.invest import CandleInterval

from traider.traider_client import TraiderClient


class TimeDelta(Enum):
    days = 'days'
    hours = 'hours'
    weeks = 'weeks'


class MyCandles(TraiderClient):
    def __init__(self):
        super().__init__()

    def get_candles_by_figi(
            self, figi: str, time_delta: TimeDelta,
            time_delta_amount: int, interval: CandleInterval
    ):
        delta = datetime.timedelta(**{time_delta.value: time_delta_amount})
        try:
            candle = self.client.market_data.get_candles(
                figi=figi.split('_')[1],
                from_=datetime.datetime.utcnow() - delta,
                to=datetime.datetime.utcnow(),
                interval=interval
            )
            print(candle)
            return candle
        except ResponseError as e:
            logging.error(e)
            print(e)


candles = MyCandles()
