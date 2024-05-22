from pydantic import BaseModel

from base.AsyncByBitBase import AsyncByBitBase


class PyBitBaseModel(BaseModel):
    client: AsyncByBitBase

    class Config:
        arbitrary_types_allowed = True
