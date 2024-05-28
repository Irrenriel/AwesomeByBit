from typing import Optional

from AwesomeByBit.enums.UpgradeStatus import UpgradeStatus
from AwesomeByBit.models.PyBitBaseModel import PyBitBaseModel


class PyBitUpgradeToUnifiedAccountResponse(PyBitBaseModel):
    unifiedUpdateStatus: UpgradeStatus
    unifiedUpdateMsg: Optional[dict]
