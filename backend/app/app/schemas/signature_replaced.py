from itertools import count
from typing import Optional

from pydantic import BaseModel, Field
from datetime import date
from .replacement_type import ReplacementTypeCreate



# Shared properties
class ReplacedBase(BaseModel):
    employeeId: int
    fullNameRu: str
    fullNameKz: str
    positionRu: str
    positionKz: str
    departmentRu: str
    departmentKz: str



# Properties to receive on item creation
class ReplacedCreate(ReplacedBase):
    employeeId: int
    fullNameRu: str
    fullNameKz: str
    positionRu: str
    positionKz: str
    departmentRu: str
    departmentKz: str

    replacementType: ReplacementTypeCreate

    class Config:
        orm_mode = True


# Properties to receive on item update
class ReplacedUpdate(ReplacedBase):
    replacementType: ReplacementTypeCreate



    class Config:
        orm_mode = True



# Properties shared by models stored in DB
class ReplacedInDBBase(ReplacedBase):
    id: int
    employeeId: int
    fullNameRu: str
    fullNameKz: str
    positionRu: str
    positionKz: str
    departmentRu: str
    departmentKz: str
    replacementType: ReplacementTypeCreate


    class Config:
        orm_mode = True


# Properties to return to client
class Replaced(ReplacedInDBBase):
    pass


# Properties properties stored in DB
class ReplacedInDB(ReplacedInDBBase):
    pass

