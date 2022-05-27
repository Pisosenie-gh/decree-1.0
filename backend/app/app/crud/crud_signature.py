from typing import List, Union, Dict, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.signature import Signature
from app.models.eds_provider_type import EdsProviderType
from app.models.eds import Eds
from app.models.signer import Signer
from app.schemas.signature import SignatureCreate, SignatureUpdate
from app.schemas.activity_patch import ActivityPatch
from app.models.replaced import Replaced
from app.models.replacement_type import ReplacementType




class CRUDSignature(CRUDBase[Signature, SignatureCreate, SignatureUpdate]):
    def create(
        self, db: Session, *, obj_in: SignatureCreate
    ) -> Signature:

        edsType = jsonable_encoder(obj_in.eds.providerType)
        eds_obj = jsonable_encoder(obj_in.eds)
        replaced_obj = jsonable_encoder(obj_in.replaced)
        replaced_type_obj = jsonable_encoder(obj_in.replaced.replacementType)
        replaced_obj.pop("replacementType")
        eds_obj.pop("providerType")
        signer_obj = jsonable_encoder(obj_in.signer)
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data.pop("eds")
        obj_in_data.pop("signer")
        obj_in_data.pop("replaced")

        db_obj = self.model(**obj_in_data, replaced = Replaced(**replaced_obj, replacementType = ReplacementType(**replaced_type_obj)  ),\
             signer = Signer(**signer_obj), eds = Eds(**eds_obj, providerType = EdsProviderType(**edsType)))
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        db_eds = db.query(Eds).filter(Eds.id == db_obj.edsId).first()
        sign_id = {"signatureId": db_obj.id}


        for key, value in sign_id.items():
            setattr(db_eds, key, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def patch(
        self,
        db: Session,
        *,
        db_obj: Signature,
        obj_in: Union[ActivityPatch, Dict[str, Any]]
    ) -> Signature:
        data_dict = obj_in.dict(exclude_unset=True)

        for key, value in data_dict.items():
            setattr(db_obj, key, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def update(
        self,
        db: Session,
        *,
        db_obj: Signature,
        obj_in: Union[SignatureUpdate, Dict[str, Any]], id: int
    ) -> Signature:
        obj_data = jsonable_encoder(db_obj)
        
        eds_update = obj_in.eds
        eds_providers_update = obj_in.eds.providerType
        signer_update = obj_in.signer
        replaced_update = obj_in.replaced
        replcement_type_update = obj_in.replaced.replacementType

        db_eds = db.query(Eds).filter(Eds.id == obj_data['edsId']).first() #Забрать eds
        providerTypeId = jsonable_encoder(db_eds)['providerTypeId'] #Забрать providerTypeId
        db_eds_type = db.query(EdsProviderType).filter(EdsProviderType.id == providerTypeId).first() #Забрать EdsProviderType
        db_signer = db.query(Signer).filter(Signer.id == obj_data['signerId']).first() #Забрать Signer
        db_replaced = db.query(Replaced).filter(Replaced.id == obj_data['replacedId']).first()
        replacementTypeId = jsonable_encoder(db_replaced)['replacementTypeId'] #Забрать replacementTypeId
        db_replacement_type = db.query(ReplacementType).filter(ReplacementType.id == replacementTypeId).first()



        obj_eds = jsonable_encoder(db_eds)
        obj_eds_type = jsonable_encoder(db_eds_type)
        obj_signer = jsonable_encoder(db_signer)
        obj_replaced = jsonable_encoder(db_replaced)
        obj_replacement_type = jsonable_encoder(db_replacement_type)
        

        
        if isinstance(obj_in, dict):
            update_data = obj_in
            eds_update_data = eds_update
            eds_provider_update_data = eds_providers_update
            signer_update_data = signer_update
            replaced_update_data = replaced_update
            replcement_type_update_data = replcement_type_update
        else:
            update_data = obj_in.dict(exclude_unset=True)
            eds_update_data = eds_update.dict(exclude_unset=True)
            eds_provider_update_data = eds_providers_update.dict(exclude_unset=True)
            signer_update_data = signer_update.dict(exclude_unset=True)
            replaced_update_data = replaced_update.dict(exclude_unset=True)
            replcement_type_update_data = replcement_type_update.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        for field in obj_eds:
            if field in eds_update_data:
                setattr(db_eds, field, eds_update_data[field])

        for field in obj_eds_type:
            if field in eds_provider_update_data:
                setattr(db_eds_type, field, eds_provider_update_data[field])

        for field in obj_signer:
            if field in signer_update_data:
                setattr(db_signer, field, signer_update_data[field])

        for field in obj_replaced:
            if field in replaced_update_data:
                setattr(db_replaced, field, replaced_update_data[field])

        for field in obj_replacement_type:
            if field in eds_provider_update_data:
                setattr(db_replacement_type, field, replcement_type_update_data[field])               

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

signature = CRUDSignature(Signature)


