from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, VARCHAR


from app.db.base_class import Base



class Signer(Base):
    __tablename__ = "signer"

    id = Column(Integer, primary_key=True, index=True)
    employeeId = Column(Integer)
    fullNameRu = Column(VARCHAR(255))
    fullNameKz = Column(VARCHAR(255))
    positionRu = Column(VARCHAR(255))
    positionKz = Column(VARCHAR(255))
    departmentRu = Column(VARCHAR(255))
    departmentKz = Column(VARCHAR(255))
