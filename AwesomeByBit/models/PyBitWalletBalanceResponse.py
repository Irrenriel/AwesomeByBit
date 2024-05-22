from typing import List

from AwesomeByBit.enums.AccountType import AccountType
from AwesomeByBit.models.PyBitBaseModel import PyBitBaseModel
from AwesomeByBit.models.PyBitCoin import PyBitCoin


class PyBitWalletBalanceResponse(PyBitBaseModel):
    accountType: AccountType
    accountIMRate: str
    accountMMRate: str
    accountLTV: str
    totalEquity: str
    totalWalletBalance: str
    totalMarginBalance: str
    totalAvailableBalance: str
    totalPerpUPL: str
    totalInitialMargin: str
    totalMaintenanceMargin: str
    coin: List[PyBitCoin]
