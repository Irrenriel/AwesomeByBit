from typing import Union, List

from AwesomeByBit.base.ByBitBase import ByBitBase
from AwesomeByBit.enums.AccountType import AccountType
from AwesomeByBit.models.PyBitUpgradeToUnifiedAccountResponse import PyBitUpgradeToUnifiedAccountResponse
from AwesomeByBit.models.PyBitWalletBalanceResponse import PyBitWalletBalanceResponse


class ByBitAccountAPI(ByBitBase):
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
        return [PyBitWalletBalanceResponse(**r) for r in response['result']['list']]

    @property
    async def upgrade_to_unified_account(
            self
    ) -> PyBitUpgradeToUnifiedAccountResponse:
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/upgrade-unified-account

        :return:
        """
        response = await self.send_signed_request(
            method='POST',
            endpoint='/v5/account/upgrade-to-uta'
        )
        return PyBitUpgradeToUnifiedAccountResponse(**response['result'])

    async def get_borrow_history(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/borrow-history

        :return:
        """
        ...

    async def repay_liability(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/repay-liability

        :return:
        """
        ...

    async def set_collateral_coin(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/set-collateral

        :return:
        """
        ...

    async def batch_set_collateral_coin(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/batch-set-collateral

        :return:
        """
        ...

    async def get_collateral_info(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/collateral-info

        :return:
        """
        ...

    async def get_coin_greeks(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/coin-greeks

        :return:
        """
        ...

    async def get_fee_rate(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/fee-rate

        :return:
        """
        ...

    async def get_account_info(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/account-info

        :return:
        """
        ...

    async def get_transaction_log_uta(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/transaction-log

        :return:
        """
        ...

    async def get_transaction_log_classic(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/contract-transaction-log

        :return:
        """
        ...

    async def get_smg_group_id(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/smp-group

        :return:
        """
        ...

    async def set_margin_mode(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/set-margin-mode

        :return:
        """
        ...

    async def set_spot_hedging(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/set-spot-hedge

        :return:
        """
        ...

    async def set_mmp(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/set-mmp

        :return:
        """
        ...

    async def reset_mmp(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/reset-mmp

        :return:
        """
        ...

    async def get_mmp_state(self):
        """
        Documentation Link: https://bybit-exchange.github.io/docs/v5/account/get-mmp-state

        :return:
        """
        ...

