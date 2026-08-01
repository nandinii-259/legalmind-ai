from app.prompts.system_prompt import SYSTEM_PROMPT

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