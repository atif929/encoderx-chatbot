import os

import google.generativeai as genai
from dotenv import load_dotenv

from backend.prompts import SYSTEM_PROMPT

load_dotenv()

genai.configure(
        api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)       

def get_response(question, history):

    chat = model.start_chat(
        history=history
    )

    reply = chat.send_message(question)

    return reply.text
