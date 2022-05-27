from typing import List, Union, Dict, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.decree import Decree
from app.models.counter import Counter
from app.models.decree_type import DecreeType

from app.schemas.decree import DecreeCreate, DecreeUpdate
from app.schemas.activity_patch import ActivityPatch

class CRUDDecree(CRUDBase[Decree, DecreeCreate, DecreeUpdate]):
    def create(
        self, db: Session, *, obj_in: DecreeCreate
    ) -> Decree:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        db_type = db.query(DecreeType).join(Counter).filter(DecreeType.id == db_obj.typeId).first()
        registrationIndex = db_type.registrationIndex
        registrationPrefix = db_type.registrationPrefix
        counter = db_type.counter.counter 
        counter+=1
        number = f"{registrationPrefix}{counter}{registrationIndex}"

        number_data = {"number": number}
        counter_data = {"counter": counter}


        for key, value in number_data.items():
            setattr(db_obj, key, value)

        for key, value in counter_data.items():
            setattr(db_type.counter, key, value)




        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)



        return db_obj

    def patch(
        self,
        db: Session,
        *,
        db_obj: Decree,
        obj_in: Union[ActivityPatch, Dict[str, Any]]
    ) -> Decree:
        data_dict = obj_in.dict(exclude_unset=True)

        for key, value in data_dict.items():
            setattr(db_obj, key, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

decree = CRUDDecree(Decree)


