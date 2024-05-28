from typing import List

from pydantic import field_validator

from AwesomeByBit.enums.AccountType import AccountType
from AwesomeByBit.models.PyBitBaseModel import PyBitBaseModel
from AwesomeByBit.models.PyBitCoin import PyBitCoin


class PyBitWalletBalanceResponse(PyBitBaseModel):
    accountType: AccountType
    accountIMRate: float
    accountMMRate: float
    accountLTV: float
    totalEquity: float
    totalWalletBalance: float
    totalMarginBalance: float
    totalAvailableBalance: float
    totalPerpUPL: float
    totalInitialMargin: float
    totalMaintenanceMargin: float
    coin: List[PyBitCoin]

    @field_validator(
        "accountIMRate", "accountMMRate", "accountLTV", "totalEquity", "totalWalletBalance",
        "totalMarginBalance", "totalAvailableBalance", "totalPerpUPL", "totalInitialMargin", "totalMaintenanceMargin",
        mode="before"
    )
    def validating(cls, value):  # noqa
        if not value:
            return 0

        return value

    def __repr__(self):
        return str(self.__dict__)
