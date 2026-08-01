from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

chat_service = ChatService()


class ChatRequest(BaseModel):
    question: str


@router.post("/")
async def chat(request: ChatRequest):

    response = chat_service.ask(request.question)

    return response