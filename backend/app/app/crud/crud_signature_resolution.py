from typing import List, Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.signature_resolution import SignatureResolution


class CRUDSignatureResolution(CRUDBase[SignatureResolution, None, None]):
    pass

signature_resolution = CRUDSignatureResolution(SignatureResolution)


