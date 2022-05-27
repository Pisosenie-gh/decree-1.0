from typing import Optional

from pydantic import BaseModel


# Shared properties
class SignatureTypeBase(BaseModel):
    nameRu: str
    nameKz: str




# Properties shared by models stored in DB
class SignatureTypeInDBBase(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class SignatureType(SignatureTypeInDBBase):
    pass


# Properties properties stored in DB
class SignatureTypeInDB(SignatureTypeInDBBase):
    pass
