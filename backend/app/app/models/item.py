from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(255), index=True)
    description = Column(VARCHAR(255), index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
