from models.PyBitBaseModel import PyBitBaseModel


class PyBitTickerResponse(PyBitBaseModel):
    symbol: str
    lastPrice: str
    indexPrice: str
    markPrice: str
    prevPrice24h: str
    price24hPcnt: str
    highPrice24h: str
    lowPrice24h: str
    prevPrice1h: str
    openInterest: str
    openInterestValue: str
    turnover24h: str
    volume24h: str
    fundingRate: str
    nextFundingTime: str
    predictedDeliveryPrice: str
    basisRate: str
    deliveryFeeRate: str
    deliveryTime: str
    ask1Size: str
    bid1Price: str
    ask1Price: str
    bid1Size: str
    basis: str
