from pydantic import BaseModel


class UploadResponse(BaseModel):
    message: str
    filename: str
    extracted_characters: int