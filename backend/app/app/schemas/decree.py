from itertools import count
from typing import Optional

from pydantic import BaseModel, Field, validator
from datetime import date
from .decree_change_action import DecreeChangeAction
from .decree_type import DecreeType


# Shared properties
class DecreeBase(BaseModel):
    content: str
    mainId: int
    date: date



# Properties to receive on item creation
class DecreeCreate(DecreeBase):
    typeId: int
    changeTypeId: int

# Properties to receive on item update
class DecreeUpdate(DecreeBase):
    typeId: int
    changeTypeId: int




# Properties shared by models stored in DB
class DecreeInDBBase(DecreeBase):
    id: int
    content: str
    mainId: int
    number: str
    date: date
    isActive: int
    type: DecreeType
    changeType: DecreeChangeAction



    class Config:
        orm_mode = True


# Properties to return to client
class Decree(DecreeInDBBase):
    id: int
    content: str
    mainId: int
    number: str
    date: date
    isActive: int
    type: DecreeType
    changeType: DecreeChangeAction

    class Config:
        orm_mode = True


# Properties properties stored in DB
class DecreeInDB(DecreeInDBBase):
    pass

