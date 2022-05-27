from typing import List, Union, Dict, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.decree_type import DecreeType
from app.schemas.decree_type import DecreeTypeCreate, DecreeTypeUpdate
from app.schemas.activity_patch import ActivityPatch

class CRUDDecreeType(CRUDBase[DecreeType, DecreeTypeCreate, DecreeTypeUpdate]):
    def create(
        self, db: Session, *, obj_in: DecreeTypeCreate
    ) -> DecreeType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def patch(
        self,
        db: Session,
        *,
        db_obj: DecreeType,
        obj_in: Union[ActivityPatch, Dict[str, Any]]
    ) -> DecreeType:
        data_dict = obj_in.dict(exclude_unset=True)

        for key, value in data_dict.items():
            setattr(db_obj, key, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

decree_type = CRUDDecreeType(DecreeType)


