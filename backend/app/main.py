from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.api.history import router as history_router
from app.api.upload import router as upload_router
from app.core.logging_config import logger
from app.database import models
from app.database.database import Base, engine

app = FastAPI(
    title="LegalMind AI",
    version="1.0.0",
    description="AI-powered Legal Document Assistant",
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():

    # Create database tables
    Base.metadata.create_all(bind=engine)

    logger.info("LegalMind AI Backend Started Successfully")


@app.get("/")
async def root():
    return {
        "message": "Welcome to LegalMind AI 🚀"
    }


# Register API routes
app.include_router(health_router)
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(history_router)