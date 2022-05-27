from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Decree])
def read_decrees(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив распорядительных документов
    """

    decree = crud.decree.get_multi(db, skip=skip, limit=limit)


    return decree


@router.post("/", response_model=schemas.Decree)
def create_decree(
    *,
    db: Session = Depends(deps.get_db),
    decree_in: schemas.DecreeCreate,

) -> Any:
    """
    Добавление записи распорядительного документа
    """
    decree = crud.decree.create(db=db, obj_in=decree_in)
    return decree


@router.put("/{id}", response_model=schemas.Decree)
def update_decree(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    decree_in: schemas.DecreeUpdate,
) -> Any:
    """
    Обновление записи распорядительного документа
    """
    decree = crud.decree.get(db=db, id=id)
    if not decree:
        raise HTTPException(status_code=404,  detail="decree {id} not found ".format(id=id))

    decree = crud.decree.update(db=db, db_obj=decree, obj_in=decree_in)
    return decree


@router.get("/{id}", response_model=schemas.Decree)
def read_decree(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
   Возвращает запись распорядительного документа
    """
    decree = crud.decree.get(db=db, id=id)
    if not decree:
        raise HTTPException(status_code=404,  detail="decree {id} not found ".format(id=id))

    return decree


@router.patch("/{id}", response_model=schemas.Decree)
def patch_decree(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    decree_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    decree = crud.decree.get(db=db, id=id)
    if not decree:
        raise HTTPException(status_code=404, detail="decree {id} not found ".format(id=id))

    decree = crud.decree.patch(db=db, db_obj=decree, obj_in=decree_in)
    return decree