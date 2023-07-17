from datetime import datetime

from pydantic import BaseModel, Field


class CandleBase(BaseModel):
    """Модель для отображения данных свечи за определенный интервал
        - time: временной промежуток
        - volume: объем торгов
        - open: цена открытия
        - close: цена закрытия
        - hight: максимальная цена
        - low: минимальная цена
    """
    time: datetime = Field(...)
    volume: int | float = Field(...)
    open: float = Field(...)
    close: float = Field(...)
    hight: float = Field(...)
    low: float = Field(...)
