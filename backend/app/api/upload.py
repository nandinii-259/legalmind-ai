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

    pdf_path = await DocumentService.save_pdf(file)

    extracted_text = DocumentService.extract_text(pdf_path)

    return UploadResponse(
        message="PDF uploaded and processed successfully.",
        filename=pdf_path.name,
        extracted_characters=len(extracted_text),
    )