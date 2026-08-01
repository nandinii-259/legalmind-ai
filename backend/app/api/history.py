from fastapi import APIRouter

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
async def history():
    return {
        "history": []
    }