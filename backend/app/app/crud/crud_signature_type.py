from typing import List, Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.signature_type import SignatureType


class CRUDSignatureType(CRUDBase[SignatureType, None, None]):
    pass

signature_type = CRUDSignatureType(SignatureType)


