from typing import Optional

from pydantic import BaseModel


# Shared properties
class ReplacementTypeBase(BaseModel):
    nameRu: str
    nameKz: str


class ReplacementTypeCreate(BaseModel):
    nameRu: str
    nameKz: str
    
    class Config:
        orm_mode = True


# Properties shared by models stored in DB
class ReplacementTypeInDBBase(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class ReplacementType(ReplacementTypeInDBBase):
    pass


# Properties properties stored in DB
class ReplacementTypeInDB(ReplacementTypeInDBBase):
    pass
