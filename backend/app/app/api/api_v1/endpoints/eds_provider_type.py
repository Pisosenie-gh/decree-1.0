from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.EdsProviderType])
def read_eds_provider_type(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника Тип криптопровайдера
    """

    eds_provider_type = crud.eds_provider_type.get_multi(db, skip=skip, limit=limit)


    return eds_provider_type

@router.get("/{id}", response_model=schemas.EdsProviderType)
def read_eds_provider_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника типов криптопровайдера по id
    """
    eds_provider_type = crud.eds_provider_type.get(db=db, id=id)
    if not eds_provider_type:
        raise HTTPException(status_code=404, detail="eds_provider_type {id} not found ".format(id=id))

    return eds_provider_type

