from itertools import count
from typing import Optional, List

from pydantic import BaseModel, Field, validator
from datetime import date, datetime
from .signer import Signer
from .signature_replaced import ReplacedCreate, Replaced
from .eds import EdsCreate, Eds



# Shared properties
class SignatureBase(BaseModel):
    decreeId: int
    resolutionId: int
    typeId: int
    signDate: datetime = Field(..., example="2019-04-01T00:00:00")
    signer: Signer
    replaced: ReplacedCreate
    eds: EdsCreate



# Properties to receive on item creation
class SignatureCreate(SignatureBase):
    decreeId: int
    resolutionId: int
    typeId: int
    signDate: datetime = Field(..., example="2019-04-01T00:00:00")
    signer: Signer
    replaced: ReplacedCreate
    eds: EdsCreate


    class Config:
        orm_mode = True

# Properties to receive on item update
class SignatureUpdate(SignatureBase):
    decreeId: int
    resolutionId: int
    typeId: int
    signDate: datetime = Field(..., example="2019-04-01T00:00:00")
    signer: Signer
    replaced: ReplacedCreate
    eds: EdsCreate



    class Config:
        orm_mode = True



# Properties shared by models stored in DB
class SignatureInDBBase(SignatureBase):
    id: int
    isActive: int
    decreeId: int
    resolutionId: int
    typeId: int
    signDate: datetime = Field(..., example="2019-04-01T00:00:00")
    signer: Signer
    replaced: Replaced
    eds: Eds

    class Config:
        orm_mode = True


# Properties to return to client
class Signature(SignatureInDBBase):
    pass


# Properties properties stored in DB
class SignatureInDB(SignatureInDBBase):
    pass

