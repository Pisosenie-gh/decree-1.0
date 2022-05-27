from typing import Optional

from pydantic import BaseModel


# Shared properties
class SignatureResolutionBase(BaseModel):
    nameRu: str
    nameKz: str




# Properties shared by models stored in DB
class SignatureResolutionInDBBase(BaseModel):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class SignatureResolution(SignatureResolutionInDBBase):
    pass


# Properties properties stored in DB
class SignatureResolutionInDB(SignatureResolutionInDBBase):
    pass
