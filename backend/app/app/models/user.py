from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, VARCHAR
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(VARCHAR(255), index=True)
    email = Column(VARCHAR(255), unique=True, index=True, nullable=False)
    hashed_password = Column(VARCHAR(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
