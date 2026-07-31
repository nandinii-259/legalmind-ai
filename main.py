from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()


@app.get("/")
def read_root():
    return {"message": "LegalMind AI backend is alive"}