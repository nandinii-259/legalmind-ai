from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.documents import router as documents_router
from app.api.health import router as health_router
from app.api.history import router as history_router
from app.api.upload import router as upload_router
from app.core.logging_config import logger

app = FastAPI(
    title="LegalMind AI",
    description="AI-powered Legal Assistant using RAG",
    version="1.0.0",
)


@app.on_event("startup")
async def startup_event():
    logger.info("LegalMind AI Backend Started Successfully")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("LegalMind AI Backend Stopped")


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to LegalMind AI 🚀"
    }


app.include_router(health_router)
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(documents_router)
app.include_router(history_router)