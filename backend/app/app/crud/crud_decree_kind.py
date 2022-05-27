from typing import List, Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.decree_kind import DecreeKind


class CRUDDecreeKind(CRUDBase[DecreeKind, None, None]):
    pass

decree_kind = CRUDDecreeKind(DecreeKind)


