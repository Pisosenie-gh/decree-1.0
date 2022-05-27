from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.SignatureResolution])
def read_signature_resolution(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника резолюций подписи
    """

    signature_resolution = crud.signature_resolution.get_multi(db, skip=skip, limit=limit)


    return signature_resolution

@router.get("/{id}", response_model=schemas.SignatureResolution)
def read_signature_resolution(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника резолюций подписи по id
    """
    signature_resolution = crud.signature_resolution.get(db=db, id=id)
    if not signature_resolution:
        raise HTTPException(status_code=404, detail="signature_resolution {id} not found ".format(id=id))

    return signature_resolution

