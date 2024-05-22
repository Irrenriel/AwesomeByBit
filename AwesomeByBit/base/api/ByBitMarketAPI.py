from typing import Union, List

from AwesomeByBit.base.ByBitBase import ByBitBase
from AwesomeByBit.enums.ProductType import ProductType
from AwesomeByBit.models.PyBitServerTimeResponse import PyBitServerTimeResponse
from AwesomeByBit.models.PyBitTickerResponse import PyBitTickerResponse


class ByBitMarketAPI(ByBitBase):
    @property
    async def server_time(
            self
    ) -> PyBitServerTimeResponse:
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/time

        :return: PyBitServerTimeResponse model
        """
        response = await self.send_signed_request(
            method='GET',
            endpoint='/v5/market/time'
        )
        return PyBitServerTimeResponse(**response['result'], client=self)

    async def get_kline(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/kline

        :return:
        """
        ...

    async def get_mark_price_kline(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/mark-kline

        :return:
        """
        ...

    async def get_index_price_kline(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/index-kline

        :return:
        """
        ...

    async def get_premium_index_price_kline(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/preimum-index-kline

        :return:
        """
        ...

    async def get_instruments_info(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/instrument

        :return:
        """
        ...

    async def get_orderbook(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/orderbook

        :return:
        """
        ...

    async def get_tickers(
            self,
            category: Union[ProductType, str],
            symbol: str
    ) -> List[PyBitTickerResponse]:
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/tickers

        :param category: Product type
            'spot', 'linear', 'inverse', 'option'
        :param symbol: Symbol name
        :return: List of PyBitTickerResponse models
        """
        # TODO: Add 'baseCoin', 'expDate' params, ses -> https://bybit-exchange.github.io/docs/v5/market/tickers
        if isinstance(category, str):
            category = ProductType(category)

        response = await self.send_signed_request(
            method='GET',
            endpoint='/v5/market/tickers',
            params={'category': category.value, 'symbol': symbol}
        )
        return [PyBitTickerResponse(**self._insert_client(r)) for r in response['result']['list']]

    async def get_funding_rate_history(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/history-fund-rate

        :return:
        """
        ...

    async def get_public_recent_trading_history(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/recent-trade

        :return:
        """
        ...

    async def get_open_interest(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/open-interest

        :return:
        """
        ...

    async def get_historical_volatility(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/iv

        :return:
        """
        ...

    async def get_insurance(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/insurance

        :return:
        """
        ...

    async def get_risk_limit(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/risk-limit

        :return:
        """
        ...

    async def get_delivery_price(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/delivery-price

        :return:
        """
        ...

    async def get_long_short_ratio(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/market/long-short-ratio

        :return:
        """
        ...
