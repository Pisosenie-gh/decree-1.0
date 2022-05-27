from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.DecreeType])
def read_decree_types(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника типов распорядительного документа
    """

    decree_type = crud.decree_type.get_multi(db, skip=skip, limit=limit)


    return decree_type


@router.post("/", response_model=schemas.DecreeType)
def create_decree_type(
    *,
    db: Session = Depends(deps.get_db),
    decree_type_in: schemas.DecreeTypeCreate,

) -> Any:
    """
    Добавление записи справочника типов распорядительного документа
    """
    decree_type = crud.decree_type.create(db=db, obj_in=decree_type_in)
    return decree_type


@router.put("/{id}", response_model=schemas.DecreeType)
def update_decree_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    decree_type_in: schemas.DecreeTypeUpdate,
) -> Any:
    """
    Обновление записи справочника типов распорядительного документа
    """
    decree_type = crud.decree_type.get(db=db, id=id)
    if not decree_type:
        raise HTTPException(status_code=404,  detail="decree_type {id} not found ".format(id=id))

    decree_type = crud.decree_type.update(db=db, db_obj=decree_type, obj_in=decree_type_in)
    return decree_type


@router.get("/{id}", response_model=schemas.DecreeType)
def read_decree_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
   Возвращает запись справочника Тип распорядительного документа по id
    """
    decree_type = crud.decree_type.get(db=db, id=id)
    if not decree_type:
        raise HTTPException(status_code=404,  detail="decree_type {id} not found ".format(id=id))

    return decree_type


@router.patch("/{id}", response_model=schemas.DecreeType)
def patch_decree_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    decree_type_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    decree_type = crud.decree_type.get(db=db, id=id)
    if not decree_type:
        raise HTTPException(status_code=404, detail="decree_type {id} not found ".format(id=id))

    decree_type = crud.decree_type.patch(db=db, db_obj=decree_type, obj_in=decree_type_in)
    return decree_type