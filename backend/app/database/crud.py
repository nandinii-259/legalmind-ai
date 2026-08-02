from sqlalchemy.orm import Session

from app.database.models import ChatHistory


def save_chat(
    db: Session,
    question: str,
    answer: str,
):

    chat = ChatHistory(
        question=question,
        answer=answer,
    )

    db.add(chat)

    db.commit()

    db.refresh(chat)

    return chat


def get_chat_history(
    db: Session,
):

    return (
        db.query(ChatHistory)
        .order_by(ChatHistory.created_at.desc())
        .all()
    )


def clear_chat_history(
    db: Session,
):

    db.query(ChatHistory).delete()

    db.commit()