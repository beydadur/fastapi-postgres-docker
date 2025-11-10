import fastapi as fastapi
from typing import TYPE_CHECKING, List
import sqlalchemy.orm as orm
from fastapi.responses import FileResponse
import os
from pathlib import Path

from . import models, schemas, services
from . import db as database

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

BASE_DIR = Path(__file__).resolve().parent

app = fastapi.FastAPI()


@app.on_event("startup")
def on_startup():
    services._add_tables()


@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse(BASE_DIR / "index.html")


@app.post("/api/items/", response_model=schemas.Item)
async def create_item(
    item: schemas.CreateItem,
    db_session: "Session" = fastapi.Depends(
        services.get_db)):
    return await services.create_item(item=item, db_session=db_session)


@app.get("/api/items/", response_model=List[schemas.Item])
async def read_items(
    skip: int = 0,
    limit: int = 100,
    db_session: "Session" = fastapi.Depends(
        services.get_db)):
    items = await services.get_all_items(db_session=db_session, skip=skip, limit=limit)
    return items


@app.get("/api/items/{item_id}", response_model=schemas.Item)
async def read_item(
    item_id: int,
    db_session: "Session" = fastapi.Depends(
        services.get_db)):
    db_item = await services.get_item(db_session=db_session, item_id=item_id)
    if db_item is None:
        raise fastapi.HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.delete("/api/items/{item_id}", response_model=schemas.Item)
async def delete_item(
    item_id: int,
    db_session: "Session" = fastapi.Depends(
        services.get_db)):
    db_item = await services.delete_item(db_session=db_session, item_id=item_id)
    if db_item is None:
        raise fastapi.HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.put("/api/items/{item_id}", response_model=schemas.Item)
async def update_item(
    item_id: int,
    item: schemas.CreateItem,
    db_session: "Session" = fastapi.Depends(
        services.get_db)):
    db_item = await services.update_item(db_session=db_session, item_id=item_id, item=item)
    if db_item is None:
        raise fastapi.HTTPException(status_code=404, detail="Item not found")
    return db_item
