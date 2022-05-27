from typing import Optional

from pydantic import BaseModel


# Shared properties
class SignerBase(BaseModel):
    employeeId: int
    fullNameRu: str
    fullNameKz: str
    positionRu: str
    positionKz: str
    departmentRu: str
    departmentKz: str




# Properties shared by models stored in DB
class SignerInDBBase(BaseModel):
    employeeId: int
    fullNameRu: str
    fullNameKz: str
    positionRu: str
    positionKz: str
    departmentRu: str
    departmentKz: str

    class Config:
        orm_mode = True


# Properties to return to client
class Signer(SignerInDBBase):
    pass


# Properties properties stored in DB
class SignerInDB(SignerInDBBase):
    pass
