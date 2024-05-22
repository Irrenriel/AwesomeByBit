from AwesomeByBit.base.api import ByBitMarketAPI, ByBitAccountAPI, ByBitTradeAPI, ByBitPositionAPI


class ByBitClient(
    ByBitMarketAPI, ByBitAccountAPI, ByBitTradeAPI, ByBitPositionAPI
):
    ...

    # async def get_(self):
    #     """
    #     Documentation Link:
    #
    #     :return:
    #     """
    #     ...
