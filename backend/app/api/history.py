from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database.crud import (
    clear_chat_history,
    get_chat_history,
)
from app.database.database import SessionLocal
from app.schemas.history import HistoryItem

router = APIRouter(
    prefix="/history",
    tags=["History"],
)


@router.get(
    "/",
    response_model=list[HistoryItem],
)
async def history():

    db: Session = SessionLocal()

    try:
        history = get_chat_history(db)
        return history

    finally:
        db.close()


@router.delete("/")
async def delete_history():

    db: Session = SessionLocal()

    try:
        clear_chat_history(db)

        return {
            "message": "Chat history cleared successfully."
        }

    finally:
        db.close()