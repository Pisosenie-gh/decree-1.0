from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.DecreeChangeAction])
def read_decree_change_action(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника типов изменения распорядительного документа
    """

    decree_change_action = crud.decree_change_action.get_multi(db, skip=skip, limit=limit)


    return decree_change_action

@router.get("/{id}", response_model=schemas.DecreeChangeAction)
def read_decree_change_action(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника типов изменения распорядительного документа по id
    """
    decree_change_action = crud.decree_change_action.get(db=db, id=id)
    if not decree_change_action:
        raise HTTPException(status_code=404, detail="decree_change_action {id} not found ".format(id=id))

    return decree_change_action

