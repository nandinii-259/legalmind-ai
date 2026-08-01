from fastapi import FastAPI
from app.database import Base, engine
from app.models import document
from app.api import upload

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LegalMind AI")

app.include_router(upload.router)


@app.get("/")
def read_root():
    return {"message": "LegalMind AI backend is alive"}