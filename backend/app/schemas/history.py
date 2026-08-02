from datetime import datetime

from pydantic import BaseModel


class HistoryItem(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }