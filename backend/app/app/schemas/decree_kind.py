from typing import Optional

from pydantic import BaseModel


# Shared properties
class DecreeKindBase(BaseModel):
    nameRu: str
    nameKz: str




# Properties shared by models stored in DB
class DecreeKindInDBBase(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class DecreeKind(DecreeKindInDBBase):
    pass


# Properties properties stored in DB
class DecreeKindInDB(DecreeKindInDBBase):
    pass
