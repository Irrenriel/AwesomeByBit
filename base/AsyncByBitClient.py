from typing import List

from base.AsyncByBitBase import AsyncByBitBase
from enums import AccountType
from models import PyBitServerTimeResponse, PyBitWalletBalanceResponse, PyBitTickerResponse


class AsyncByBitClient(AsyncByBitBase):
    @property
    async def server_time(
            self
    ) -> PyBitServerTimeResponse:
        response = await self.send_signed_request(
            method='GET',
            endpoint='/v5/market/time'
        )
        return PyBitServerTimeResponse(**response['result'], client=self)

    async def get_wallet_balance(
            self,
            account_type: AccountType = AccountType.SPOT
    ) -> List[PyBitWalletBalanceResponse]:
        response = await self.send_signed_request(
            method='GET',
            endpoint='/v5/account/wallet-balance',
            params={'accountType': account_type.value}
        )
        return [PyBitWalletBalanceResponse(**self._insert_client(r)) for r in response['result']['list']]

    async def get_tickers(
            self,
            symbol: str
    ) -> List[PyBitTickerResponse]:
        response = await self.send_signed_request(
            method='GET',
            endpoint='/v5/market/tickers',
            params={'category': 'inverse', 'symbol': symbol}
        )
        return [PyBitTickerResponse(**self._insert_client(r)) for r in response['result']['list']]

    def _insert_client(
            self,
            data: dict
    ) -> dict:
        """
        I forgot why I decided to insert the client into each response model, but so be it.
        """
        data.update({'client': self})

        for k, v in data.items():
            if isinstance(v, dict):
                self._insert_client(v)

            elif isinstance(v, list) or isinstance(v, tuple):
                [self._insert_client(vv) for vv in v]

        return data
