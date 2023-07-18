import datetime
import logging
from enum import Enum
from xmlrpc.client import ResponseError

from tinkoff.invest import CandleInterval

from traider.responses.candles_response import CandleBase
from traider.traider_client import TraiderClient


class TimeDelta(Enum):
    days = 'days'
    hours = 'hours'
    weeks = 'weeks'


class MyCandles(TraiderClient):
    def __init__(self):
        super().__init__()

    def __create_candle_response(self, candles_list) -> list[CandleBase]:
        candles_list = [
            CandleBase(
                time=item.time.strftime("%Y-%m-%d"),
                volume=item.volume,
                open=self.resp_to_float(item.open),
                close=self.resp_to_float(item.close),
                hight=self.resp_to_float(item.high),
                low=self.resp_to_float(item.low)

            ) for item in candles_list
        ]
        return candles_list

    def get_candles_by_figi(
            self, figi: str, time_delta: TimeDelta,
            time_delta_amount: int, interval: CandleInterval
    ) -> list[CandleBase]:
        delta = datetime.timedelta(**{time_delta.value: time_delta_amount})
        try:
            candle = self.client.market_data.get_candles(
                figi=figi,
                from_=datetime.datetime.utcnow() - delta,
                to=datetime.datetime.utcnow(),
                interval=interval
            )
            return self.__create_candle_response(candle.candles)
        except ResponseError as e:
            logging.error(e)
            print(e)


candles = MyCandles()
