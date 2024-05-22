from AwesomeByBit.models.PyBitBaseModel import PyBitBaseModel


class PyBitServerTimeResponse(PyBitBaseModel):
    timeSecond: str
    timeNano: str
