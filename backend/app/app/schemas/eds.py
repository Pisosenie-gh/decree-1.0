from itertools import count
from typing import Optional, List, Dict



from pydantic import BaseModel, Field, validator
from datetime import date, datetime
from .eds_provider_type import EdsProviderTypeForModels
import time

from datetime import datetime, timezone


# Shared properties


class EdsBase(BaseModel):
    signDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certStartDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certEndDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certOwner: str
    PUID: str
    cert: str
    content: str
    signedFieldsSequence: Dict[str, list]
    signedFilesIdSequence: Dict[str, list]




# Properties to receive on item creation
class EdsCreate(EdsBase):
    signDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certStartDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certEndDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certOwner: str
    PUID: str
    cert: str
    content: str
    signedFieldsSequence: Dict[str, list]
    signedFilesIdSequence: Dict[str, list]
    providerType: EdsProviderTypeForModels
    
    class Config:
        orm_mode = True



# Properties to receive on item update
class EdsUpdate(EdsBase):
    signDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certStartDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certEndDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certOwner: str
    PUID: str
    cert: str
    content: str
    signedFieldsSequence: Dict[str, list]
    signedFilesIdSequence: Dict[str, list]
    providerType: EdsProviderTypeForModels



    class Config:
        orm_mode = True
   




# Properties shared by models stored in DB
class EdsInDBBase(EdsBase):
    id: int
    signDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certStartDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certEndDate: datetime = Field(..., example="2019-04-01T00:00:00")
    certOwner: str
    PUID: str
    cert: str
    content: str
    signedFieldsSequence: Dict[str, list]
    signedFilesIdSequence: Dict[str, list]
    providerType: EdsProviderTypeForModels
    
    class Config:
        orm_mode = True




# Properties to return to client
class Eds(EdsInDBBase):
    pass


# Properties properties stored in DB
class EdsInDB(EdsInDBBase):
    pass

