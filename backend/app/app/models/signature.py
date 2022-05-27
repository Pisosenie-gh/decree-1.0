from email.policy import default

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, VARCHAR
from sqlalchemy.orm import relationship


from app.db.base_class import Base

if TYPE_CHECKING:
    from .decree import Decree
    from .signature_resolution import SignatureResolution
    from .signature_type import SignatureType
    from .signer import Signer
    from .replaced import Replaced

class Signature(Base):
    __tablename__ = "signature"

    id = Column(Integer, primary_key=True, index=True)
    decreeId = Column(Integer, ForeignKey("decree.id"))
    resolutionId = Column(Integer, ForeignKey("signature_resolution.id"))
    typeId = Column(Integer, ForeignKey("signature_type.id"))
    signDate = Column(DateTime)
    isActive = Column(Integer, default=1)

    signerId = Column(Integer, ForeignKey("signer.id"), nullable=True)
    replacedId = Column(Integer, ForeignKey("signature_replaced.id"), nullable=True)
    edsId = Column(Integer, ForeignKey("eds.id"), nullable=True)

    signer = relationship("Signer", backref="init")
    replaced = relationship("Replaced", backref="init")
    eds = relationship("Eds", backref="init", foreign_keys='Signature.edsId')