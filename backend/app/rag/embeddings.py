from google import genai

from app.core.config import settings


class GeminiEmbedding:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def embed(self, text: str):
        response = self.client.models.embed_content(
            model="text-embedding-004",
            contents=text,
        )

        return response.embeddings[0].values