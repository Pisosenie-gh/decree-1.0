from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.DecreeKind])
def read_decree_kind(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника видов распорядительного документа
    """

    decree_kind = crud.decree_kind.get_multi(db, skip=skip, limit=limit)


    return decree_kind

@router.get("/{id}", response_model=schemas.DecreeKind)
def read_decree_kind(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника вид распорядительного документа по id
    """
    decree_kind = crud.decree_kind.get(db=db, id=id)
    if not decree_kind:
        raise HTTPException(status_code=404, detail="decree_kind {id} not found ".format(id=id))

    return decree_kind

