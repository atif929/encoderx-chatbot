import os

from groq import Groq
from dotenv import load_dotenv

from backend.prompts import SYSTEM_PROMPT

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "openai/gpt-oss-20b"


def get_response(question, history):

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for turn in history:
        role = "assistant" if turn["role"] == "model" else "user"
        messages.append({"role": role, "content": turn["parts"][0]})

    messages.append({"role": "user", "content": question})

    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

<<<<<<< HEAD
    reply = chat.send_message(question)

    return reply.text
=======
    return completion.choices[0].message.content
>>>>>>> db80e6d (changes API key)
