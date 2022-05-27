from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Counter])
def read_counters(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей
    """

    counter = crud.counter.get_multi(db, skip=skip, limit=limit)


    return counter


@router.post("/", response_model=schemas.Counter)
def create_counter(
    *,
    db: Session = Depends(deps.get_db),
    counter_in: schemas.CounterCreate,

) -> Any:
    """
    Добавление записи
    """
    counter = crud.counter.create(db=db, obj_in=counter_in)
    return counter


@router.put("/{id}", response_model=schemas.Counter)
def update_counter(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    counter_in: schemas.CounterUpdate,
) -> Any:
    """
    Обновление записи
    """
    counter = crud.counter.get(db=db, id=id)
    if not counter:
        raise HTTPException(status_code=404,  detail="counter {id} not found ".format(id=id))

    counter = crud.counter.update(db=db, db_obj=counter, obj_in=counter_in)
    return counter


@router.get("/{id}", response_model=schemas.Counter)
def read_counter(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
   Возвращает запись по id
    """
    counter = crud.counter.get(db=db, id=id)
    if not counter:
        raise HTTPException(status_code=404,  detail="counter {id} not found ".format(id=id))

    return counter


@router.patch("/{id}", response_model=schemas.Counter)
def patch_counter(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    counter_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    counter = crud.counter.get(db=db, id=id)
    if not counter:
        raise HTTPException(status_code=404, detail="counter {id} not found ".format(id=id))

    counter = crud.counter.patch(db=db, db_obj=counter, obj_in=counter_in)
    return counter