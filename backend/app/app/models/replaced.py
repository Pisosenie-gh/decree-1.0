from email.policy import default

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR
from sqlalchemy.orm import relationship


from app.db.base_class import Base

if TYPE_CHECKING:
    from .replacement_type import ReplacementType



class Replaced(Base):
    __tablename__ = "signature_replaced"

    id = Column(Integer, primary_key=True, index=True)
    employeeId = Column(Integer)
    fullNameRu = Column(VARCHAR(255))
    fullNameKz = Column(VARCHAR(255))
    positionRu = Column(VARCHAR(255))
    positionKz = Column(VARCHAR(255))
    departmentRu = Column(VARCHAR(255))
    departmentKz = Column(VARCHAR(255))

    replacementTypeId = Column(Integer, ForeignKey('replacement_type.id'), nullable=True)

    replacementType = relationship("ReplacementType", backref="init")

