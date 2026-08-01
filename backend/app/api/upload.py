from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.upload import UploadResponse
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

document_service = DocumentService()


@router.post("/", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    pdf_data = await document_service.process_pdf(file)

    return UploadResponse(**pdf_data)