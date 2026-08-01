from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.upload import UploadResponse
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    filename = await DocumentService.save_pdf(file)

    return UploadResponse(
        message="PDF uploaded successfully.",
        filename=filename,
    )