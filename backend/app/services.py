from typing import TYPE_CHECKING, List

from . import db
from . import models
from . import schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return db.Base.metadata.create_all(bind=db.engine)


def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


async def create_item(
        item: schemas.CreateItem,
        db_session: "Session") -> schemas.Item:
    db_item = models.Item(**item.dict())
    db_session.add(db_item)
    db_session.commit()
    db_session.refresh(db_item)
    return schemas.Item.from_orm(db_item)


async def get_all_items(db_session: "Session",
                        skip: int = 0,
                        limit: int = 100) -> List[schemas.Item]:
    items = db_session.query(models.Item).offset(skip).limit(limit).all()
    return [schemas.Item.from_orm(item) for item in items]


async def get_item(db_session: "Session", item_id: int) -> schemas.Item | None:
    item = db_session.query(
        models.Item).filter(
        models.Item.id == item_id).first()
    if item:
        return schemas.Item.from_orm(item)
    return None


async def delete_item(
        db_session: "Session",
        item_id: int) -> schemas.Item | None:
    item = db_session.query(
        models.Item).filter(
        models.Item.id == item_id).first()
    if item:
        db_session.delete(item)
        db_session.commit()
        return schemas.Item.from_orm(item)
    return None


async def update_item(
        db_session: "Session",
        item_id: int,
        item: schemas.CreateItem) -> schemas.Item | None:
    db_item = db_session.query(
        models.Item).filter(
        models.Item.id == item_id).first()
    if db_item:
        for key, value in item.dict().items():
            setattr(db_item, key, value)
        db_session.commit()
        db_session.refresh(db_item)
        return schemas.Item.from_orm(db_item)
    return None
