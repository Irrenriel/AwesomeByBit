from models.PyBitBaseModel import PyBitBaseModel
from models.PyBitTickerResponse import PyBitTickerResponse


class PyBitCoin(PyBitBaseModel):
    coin: str
    equity: str
    usdValue: str
    walletBalance: float
    free: str
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

    def get_usdt(self, ticker: PyBitTickerResponse):
        return float(self.walletBalance) * float(ticker.lastPrice)
