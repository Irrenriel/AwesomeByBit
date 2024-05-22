from enum import Enum


class AccountType(Enum):
    """
    Unified Trading Account (UTA):
        CONTRACT - Inverse Derivatives Account
        UNIFIED - Unified Trading Account
        FUND - Funding Account

    # Classic account:
        SPOT - Spot Account
        CONTRACT - Derivatives Account
        OPTION - USDC Derivatives
        FUND - Funding Account
    """
    CONTRACT = 'CONTRACT'
    UNIFIED = 'UNIFIED'
    FUND = 'FUND'
    SPOT = 'SPOT'
    OPTION = 'OPTION'
