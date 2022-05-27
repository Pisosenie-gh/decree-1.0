from typing import List, Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.eds_provider_type import EdsProviderType


class CRUDEdsProviderType(CRUDBase[EdsProviderType, None, None]):
    pass

eds_provider_type = CRUDEdsProviderType(EdsProviderType)


