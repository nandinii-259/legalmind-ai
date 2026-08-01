from fastapi import FastAPI

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


@app.get("/")
async def root():
    return {
        "message": "Welcome to LegalMind AI 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "LegalMind AI Backend",
        "version": "1.0.0",
    }