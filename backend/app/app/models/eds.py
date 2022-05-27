from email.policy import default

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ARRAY, VARCHAR, JSON
from sqlalchemy.orm import relationship


from app.db.base_class import Base

if TYPE_CHECKING:
    from .eds_provider_type import EdsProviderType
    from .signature import Signature



class Eds(Base):
    __tablename__ = "eds"

    id = Column(Integer, primary_key=True, index=True)
    signDate = Column(DateTime)
    certStartDate = Column(DateTime)
    certEndDate = Column(DateTime)
    certOwner = Column(VARCHAR(255))
    PUID = Column(VARCHAR(255))
    cert = Column(VARCHAR(255))
    content = Column(VARCHAR(255))
    signedFilesIdSequence = Column(JSON)
    signedFieldsSequence = Column(JSON)
    



    providerTypeId = Column(Integer, ForeignKey('eds_provider_type.id'), nullable=False)

    providerType = relationship("EdsProviderType", backref="type", foreign_keys='Eds.providerTypeId')

    signatureId = Column(Integer, ForeignKey('signature.id'), nullable=True, index=True)

    signature = relationship("Signature", backref="sign",  foreign_keys='Eds.signatureId')