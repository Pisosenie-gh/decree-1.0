from email.policy import default

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date, VARCHAR
from sqlalchemy.orm import relationship


from app.db.base_class import Base

if TYPE_CHECKING:
    from .decree_kind import DecreeKind
    from .counter import Counter



class DecreeType(Base):
    __tablename__ = "decree_type"

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(VARCHAR(255))
    nameKz = Column(VARCHAR(255))
    registrationIndex = Column(VARCHAR(255))
    registrationPrefix = Column(VARCHAR(255))
    isActive = Column(Integer, default=1)
    kindId = Column(Integer, ForeignKey('decree_kind.id'))
    counterId = Column(Integer, ForeignKey('counter.id'))

    kind = relationship("DecreeKind", backref="kind", viewonly=True)
    counter = relationship("Counter", backref="init", viewonly=True)
