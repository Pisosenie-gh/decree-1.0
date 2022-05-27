from typing import Optional

from pydantic import BaseModel


# Shared properties
class CounterBase(BaseModel):
    counter: int

class CounterCreate(CounterBase):
    counter: int



class CounterUpdate(CounterBase):
    counter: int




# Properties shared by models stored in DB
class CounterInDBBase(BaseModel):
    id: int
    counter: int
    isActive: int
    class Config:
        orm_mode = True


# Properties to return to client
class Counter(CounterInDBBase):
    pass


# Properties properties stored in DB
class CounterInDB(CounterInDBBase):
    pass
