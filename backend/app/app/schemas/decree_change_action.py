from typing import Optional

from pydantic import BaseModel


# Shared properties
class DecreeChangeActionBase(BaseModel):
    nameRu: str
    nameKz: str




# Properties shared by models stored in DB
class DecreeChangeActionInDBBase(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class DecreeChangeAction(DecreeChangeActionInDBBase):
    pass


# Properties properties stored in DB
class DecreeChangeActionInDB(DecreeChangeActionInDBBase):
    pass
