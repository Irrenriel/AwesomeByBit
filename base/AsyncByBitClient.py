from typing import List, Union

from base.AsyncByBitBase import AsyncByBitBase
from enums import AccountType, ProductType
from models import PyBitServerTimeResponse, PyBitWalletBalanceResponse, PyBitTickerResponse


class AsyncByBitClient(AsyncByBitBase):
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

    async def get_wallet_balance(
            self,
            account_type: Union[AccountType, str] = AccountType.SPOT
    ) -> List[PyBitWalletBalanceResponse]:
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/wallet-balance

        :param account_type: AccountType
            Unified account: UNIFIED (trade spot/linear/options), CONTRACT(trade inverse)
            Classic account: CONTRACT, SPOT
        :return: List of PyBitWalletBalanceResponse models
        """
        # TODO: Add 'coin' param, see -> https://bybit-exchange.github.io/docs/v5/account/wallet-balance
        if isinstance(account_type, str):
            account_type = AccountType(account_type)

        response = await self.send_signed_request(
            method='GET',
            endpoint='/v5/account/wallet-balance',
            params={'accountType': account_type.value}
        )
        return [PyBitWalletBalanceResponse(**self._insert_client(r)) for r in response['result']['list']]

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
