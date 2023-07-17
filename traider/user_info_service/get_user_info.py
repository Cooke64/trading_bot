# assset - актив. Подразумевается, что это конкретный элемент из активов в портфеле на счете у брокера
from tinkoff.invest import (
    PortfolioPosition
)

from traider.responses.user_info_responses import (
    AssetsShow,
    ShowMyMoney,
    CurrentAsset
)
from traider.traider_client import TraiderClient


class PortfolioUserInfo(TraiderClient):
    def __init__(self):
        super().__init__()
        self._portfolio = self._operations.get_portfolio(account_id=self.id_)

    def __create_asset_item(self, item: PortfolioPosition) -> AssetsShow:
        """Создает объект AssetsShow, который исспользуется для отображения
        усеченной информации об Активе, отображенного в списке всех активов.
        """
        item_name = self._get_asset_item(
            item.instrument_type, item.figi).name
        return AssetsShow(
            name=item_name,
            figi=item.figi,
            amount=self.resp_to_float(item.quantity),
            average_price=self.resp_to_float(
                item.average_position_price),
            item_type=item.instrument_type
        )

    def get_total_balance(self) -> ShowMyMoney:
        portfolio = self._portfolio.total_amount_portfolio
        return ShowMyMoney(
            units=portfolio.units,
            currency=portfolio.currency,
            yield_=self.resp_to_float(self._portfolio.expected_yield))

    def get_list_of_assets(self) -> list[AssetsShow]:
        my_assets = []
        for pos in self._portfolio.positions:
            my_assets.append(self.__create_asset_item(pos))
        return my_assets

    def __sum_price(self, item: PortfolioPosition) -> float:
        """Рассчет сумы всех активов после продажи"""
        amount = self.resp_to_float(item.quantity)
        avg_price = self.resp_to_float(item.average_position_price)
        exp_yield = self.resp_to_float(item.expected_yield)
        nkd = self.resp_to_float(item.current_nkd)
        tax = exp_yield * 0.013 if exp_yield else 0
        return (amount * avg_price) + exp_yield + (nkd * amount) - tax

    def get_price_after_selling(self) -> float:
        positions = self._portfolio.positions
        sell_sum = [self.__sum_price(item) for item in positions]
        sum_without_comission = sum(sell_sum)
        return sum_without_comission - (sum_without_comission * 0.003)

    def __get_current_asset_item(
            self, item: PortfolioPosition) -> CurrentAsset:
        return CurrentAsset(
            name=self._get_asset_item(
                item.instrument_type, item.figi).name,
            amount=self.resp_to_float(item.quantity),
            current_price=self.resp_to_float(item.current_price),
            average_price=self.resp_to_float(item.average_position_price),
            figi=item.figi,
            nkd=self.resp_to_float(item.current_nkd)
        )

    def get_current_asset(self, figi_callback: str) -> CurrentAsset | str:
        """Передается в переменную figi_callback строка вида
        ,например, Figi_HND123LKJ.
        """
        figi = figi_callback.split('_')[1]
        item = [i for i in self._portfolio.positions if i.figi == figi]
        if item:
            return self.__get_current_asset_item(item[0])
        return 'ничего не нафдено'


user_info = PortfolioUserInfo()
