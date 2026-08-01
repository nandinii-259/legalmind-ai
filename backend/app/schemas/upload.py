from pydantic import BaseModel


class UploadResponse(BaseModel):
    message: str
    filename: str
    file_size: str
    page_count: int
    character_count: int
    chunk_count: int