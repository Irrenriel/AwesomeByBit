from AwesomeByBit.base.ByBitBase import ByBitBase


class ByBitTradeAPI(ByBitBase):
    async def place_order(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/create-order

        :return:
        """
        ...

    async def amend_order(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/amend-order

        :return:
        """
        ...

    async def cancel_order(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/cancel-order

        :return:
        """
        ...

    async def get_open_and_closed_orders(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/open-order

        :return:
        """
        ...

    async def cancel_all_orders(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/cancel-all

        :return:
        """
        ...

    async def get_order_history(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/order-list

        :return:
        """
        ...

    async def get_trade_history(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/execution

        :return:
        """
        ...

    async def batch_place_order(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/batch-place

        :return:
        """
        ...

    async def batch_amend_order(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/batch-amend

        :return:
        """
        ...

    async def batch_cancel_order(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/batch-cancel

        :return:
        """
        ...

    async def get_borrow_quota(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/spot-borrow-quota

        :return:
        """
        ...

    async def set_dcp(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/order/dcp

        :return:
        """
        ...
