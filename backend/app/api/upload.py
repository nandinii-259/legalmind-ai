from fastapi import APIRouter

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_document():
    return {
        "message": "Upload endpoint coming soon."
    }