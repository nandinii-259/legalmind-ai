from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
async def health_check():
    return {
        "status": "healthy",
        "service": "LegalMind AI Backend",
        "version": "1.0.0"
    }