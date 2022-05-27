from itertools import count
from typing import Optional

from pydantic import BaseModel, Field
from datetime import date
from .counter import Counter
from .decree_kind import DecreeKind


# Shared properties
class DecreeTypeBase(BaseModel):
    nameRu: str
    nameKz: str
    registrationIndex: str
    registrationPrefix: str


# Properties to receive on item creation
class DecreeTypeCreate(DecreeTypeBase):
    kindId: int
    counterId: int

# Properties to receive on item update
class DecreeTypeUpdate(DecreeTypeBase):
    kindId: int
    counterId: int



# Properties shared by models stored in DB
class DecreeTypeInDBBase(DecreeTypeBase):
    id: int
    nameRu: str
    nameKz: str
    registrationIndex: str
    registrationPrefix: str
    isActive: int
    kind: DecreeKind
    counter: Counter


    class Config:
        orm_mode = True


# Properties to return to client
class DecreeType(DecreeTypeInDBBase):
    id: int
    nameRu: str
    nameKz: str
    registrationIndex: str
    registrationPrefix: str
    isActive: int
    kind: DecreeKind
    counter: Counter


    class Config:
        orm_mode = True



# Properties properties stored in DB
class DecreeTypeInDB(DecreeTypeInDBBase):
    pass

