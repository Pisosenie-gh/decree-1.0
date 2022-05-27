
from email.policy import default
from sqlalchemy import Column, Integer, String


from app.db.base_class import Base



class Counter(Base):
    __tablename__ = "counter"

    id = Column(Integer, primary_key=True, index=True)
    counter = Column(Integer)
    isActive = Column(Integer, default=1)
