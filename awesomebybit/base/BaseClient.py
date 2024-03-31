import asyncio
import time

from aiohttp import ClientSession


class BybitBaseClient:
    """
    Testnet:
        https://api-testnet.bybit.com

    Mainnet (both endpoints are available):
        https://api.bybit.com
        https://api.bytick.com
    """
    API_URL = 'https://api.bybit.com/'

    def __init__(self, api_key: str, api_secret: str, **kwargs):
        self.api_key = api_key
        self.api_secret = api_secret

    def generate_headers(self):
        timestamp = self.generate_timestamp()

        return {
            "Content-Type": "application/json",
            "X-BAPI-API-KEY": self.api_key,

            "X-BAPI-TIMESTAMP": str(timestamp),
        }

    @staticmethod
    def generate_timestamp():
        """
        Return a millisecond integer timestamp.
        """
        return int(time.time() * 10**3)


async def main():
    async with BybitBaseClient() as client:
        async with client.get(client.API_URL + '')


asyncio.run(main())
