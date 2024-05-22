import asyncio

from AwesomeByBit.base import ByBitClient


API_KEY = "*****"
API_SECRET = "*****"


async def main():
    client = ByBitClient(
        api_key=API_KEY,
        api_secret=API_SECRET
    )

    wallet = await client.get_wallet_balance()
    print(wallet)

asyncio.run(main())
