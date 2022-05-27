from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.SignatureType])
def read_signature_type(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника Тип криптопровайдера
    """

    signature_type = crud.signature_type.get_multi(db, skip=skip, limit=limit)


    return signature_type

@router.get("/{id}", response_model=schemas.SignatureType)
def read_signature_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника типов криптопровайдера по id
    """
    signature_type = crud.signature_type.get(db=db, id=id)
    if not signature_type:
        raise HTTPException(status_code=404, detail="signature_type {id} not found ".format(id=id))

    return signature_type

