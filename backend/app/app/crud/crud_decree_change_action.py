from typing import List, Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.decree_change_action import DecreeChangeAction


class CRUDDecreeChangeAction(CRUDBase[DecreeChangeAction, None, None]):
    pass

decree_change_action = CRUDDecreeChangeAction(DecreeChangeAction)


