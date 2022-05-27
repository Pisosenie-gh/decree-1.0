from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Signature])
def read_signatures(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей
    """

    signature = crud.signature.get_multi(db, skip=skip, limit=limit)


    return signature


@router.post("/", response_model=schemas.SignatureCreate)
def create_signature(
    *,
    db: Session = Depends(deps.get_db),
    signature_in: schemas.SignatureCreate,

) -> Any:
    """
    Добавление записи
    """
    signature = crud.signature.create(db=db, obj_in=signature_in)
    return signature


@router.put("/{id}", response_model=schemas.SignatureUpdate)
def update_signature(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    signature_in: schemas.SignatureUpdate,
) -> Any:
    """
    Обновление записи
    """
    signature = crud.signature.get(db=db, id=id)
    if not signature:
        raise HTTPException(status_code=404,  detail="signature {id} not found ".format(id=id))

    signature = crud.signature.update(db=db, db_obj=signature, obj_in=signature_in, id=id)
    return signature


@router.get("/{id}", response_model=schemas.Signature)
def read_signature(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
   Возвращает запись по id
    """
    signature = crud.signature.get(db=db, id=id)
    if not signature:
        raise HTTPException(status_code=404,  detail="signature {id} not found ".format(id=id))

    return signature


@router.patch("/{id}", response_model=schemas.Signature)
def patch_signature(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    signature_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    signature = crud.signature.get(db=db, id=id)
    if not signature:
        raise HTTPException(status_code=404, detail="signature {id} not found ".format(id=id))

    signature = crud.signature.patch(db=db, db_obj=signature, obj_in=signature_in)
    return signature