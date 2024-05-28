from enum import Enum


class UpgradeStatus(Enum):
    FAIL = "FAIL"
    PROCESS = "PROCESS"
    SUCCESS = "SUCCESS"
