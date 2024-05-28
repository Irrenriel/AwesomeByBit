from typing import Optional

from pydantic import field_validator

from AwesomeByBit.models.PyBitBaseModel import PyBitBaseModel


class PyBitCoin(PyBitBaseModel):
    coin: str
    equity: float
    usdValue: float
    walletBalance: float
    locked: str
    availableToWithdraw: str
    availableToBorrow: str
    borrowAmount: str
    accruedInterest: str
    totalOrderIM: str
    totalPositionIM: str
    totalPositionMM: str
    unrealisedPnl: str
    cumRealisedPnl: str
    free: Optional[str] = ''

    @field_validator(
        "equity", "usdValue",
        mode="before"
    )
    def validating(cls, value):  # noqa
        if not value:
            return 0

        return value

    def __repr__(self):
        return str(self.__dict__)
