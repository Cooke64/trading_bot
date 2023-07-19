from pydantic import BaseModel, Field


class AssetBase(BaseModel):
    name: str = Field(...)
    item_type: str = None
    figi: str = None
    amount: float = Field(...)
    average_price: float = Field(...)


class AssetsShow(AssetBase):
    pass


class ShowMyMoney(BaseModel):
    units: int
    currency: str
    yield_: str


class CurrentAsset(BaseModel):
    current_price: float = Field(...)
    nkd: float | None


class OperationsBase(BaseModel):
    ...
