from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, VARCHAR


from app.db.base_class import Base



class EdsProviderType(Base):
    __tablename__ = "eds_provider_type"

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(VARCHAR(255))
    nameKz = Column(VARCHAR(255))
