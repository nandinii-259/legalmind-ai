from google import genai
from google.genai.errors import ClientError

from app.core.config import settings
from app.prompts.system_prompt import SYSTEM_PROMPT


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
{SYSTEM_PROMPT}

-------------------------
DOCUMENT CONTEXT
-------------------------

{context}

-------------------------
USER QUESTION
-------------------------

{question}

-------------------------
ANSWER
-------------------------
"""


        try:

            response = self.client.models.generate_content(
                model=settings.MODEL_NAME,
                contents=prompt,
            )

            return response.text

        except ClientError as e:

            print(f"Gemini API Error: {e}")

            return (
                "Sorry, I couldn't generate an answer because the AI service "
                "is currently unavailable or its quota has been exceeded. "
                "Please try again later."
            )

        except Exception as e:

            print(f"Unexpected Error: {e}")

            return (
                "An unexpected error occurred while generating the answer."
            )