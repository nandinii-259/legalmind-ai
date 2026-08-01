from google import genai

from app.core.config import settings


class GeminiGenerator:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(
        self,
        question: str,
        context: str,
    ):

        prompt = f"""
You are LegalMind AI.

Answer ONLY using the provided context.

If the answer cannot be found in the context, reply exactly:

"I could not find the answer in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

        print(f"Using model: {settings.MODEL_NAME}")

        response = self.client.models.generate_content(
            model=settings.MODEL_NAME,
            contents=prompt,
        )

        print(response)

        return response.text