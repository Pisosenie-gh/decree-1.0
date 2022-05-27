from typing import Optional

from pydantic import BaseModel


# Shared properties
class EdsProviderTypeBase(BaseModel):
    nameRu: str
    nameKz: str



# Properties shared by models stored in DB
class EdsProviderTypeInDBBase(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True

class EdsProviderTypeForModels(BaseModel):
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True   
# Properties to return to client
class EdsProviderType(EdsProviderTypeInDBBase):
    pass


# Properties properties stored in DB
class EdsProviderTypeInDB(EdsProviderTypeInDBBase):
    pass
