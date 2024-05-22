from pydantic import BaseModel

from AwesomeByBit.base.ByBitBase import ByBitBase


class PyBitBaseModel(BaseModel):
    client: ByBitBase

    class Config:
        arbitrary_types_allowed = True
