import logging

from tinkoff.invest import Client
from tinkoff.invest import (
    MoneyValue,
    Quotation,
    Share,
    Bond,
    Currency
)
from tinkoff.invest.grpc.instruments_pb2 import (
    INSTRUMENT_ID_TYPE_FIGI,
)
from tinkoff.invest.services import Services

from config import settings

AssetResponse = Share | Bond | Currency


class TraiderClient:
    COMSISSION = 0.003

    def __init__(self, account: int = 0):
        self.__account = account
        self.__client = self.__make_client()
        self._operations = self.__client.operations
        self._instruments = self.__client.instruments
        self._users = self.__client.users

    @classmethod
    def __make_client(cls) -> Services:
        client_manager = Client(settings.TRAIDER_TOKEN)
        client = client_manager.__enter__()
        return client

    @property
    def id_(self) -> int:
        """Получает аккаунт ID, количество получает необходимый аккаунт брокерского счета."""
        if self.client:
            return self._users.get_accounts().accounts[self.__account].id

    @staticmethod
    def resp_to_float(value: MoneyValue | Quotation) -> float:
        return value.units + value.nano / 1e9

    @property
    def client(self):
        return self.__client

    def _get_asset_item(
            self, instrument_type: str,
            figi: str) -> AssetResponse:
        """Возвращает в зависимости от типа актива объект AssetResponse по его Figi.
        Только для активовв акиции(share), облигации (bond), денежные средства (currency)
        В остальных случаех генерируется ошибка типа данных.
        """
        match instrument_type:
            case 'bond':
                res = self._instruments.bond_by(
                    id_type=INSTRUMENT_ID_TYPE_FIGI, id=figi)
            case 'share':
                res = self._instruments.share_by(
                    id_type=INSTRUMENT_ID_TYPE_FIGI, id=figi)
            case 'currency':
                res = self._instruments.currency_by(
                    id_type=INSTRUMENT_ID_TYPE_FIGI, id=figi)
            case _:
                message = 'Тип активов должен быть bond, share, currency'
                logging.error(message)
                raise ValueError(message)
        return res.instrument
