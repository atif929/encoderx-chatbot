"""Chat log rendering, input handling, and response display.

Streaming note: backend.chatbot.get_response() calls Gemini synchronously
and returns the full answer in one shot (no stream=True on the backend).
To give the response a natural streamed feel without touching backend
logic, the already-complete answer is revealed progressively in the UI via
st.write_stream — a purely cosmetic, frontend-only reveal.
"""

import time
from collections.abc import Iterator

import streamlit as st

from backend.chatbot import get_response
from utils import session

_STREAM_DELAY_SECONDS = 0.012

_AVATARS = {
    "user": ":material/person:",
    "assistant": ":material/auto_awesome:",
}


def render_messages(chat: dict) -> None:
    for message in chat["messages"]:
        with st.chat_message(message["role"], avatar=_AVATARS[message["role"]]):
            st.markdown(message["content"])


def render_input() -> str | None:
    return st.chat_input("Ask anything")


def _reveal(text: str) -> Iterator[str]:
    for word in text.split(" "):
        yield word + " "
        time.sleep(_STREAM_DELAY_SECONDS)


def handle_user_message(chat: dict, question: str) -> None:
    chat["messages"].append({"role": "user", "content": question})

    with st.chat_message("user", avatar=_AVATARS["user"]):
        st.markdown(question)

    with st.chat_message("assistant", avatar=_AVATARS["assistant"]):
        with st.spinner("Thinking..."):
            answer = get_response(question, chat["history"])
        st.write_stream(_reveal(answer))

    session.record_answer(chat, question, answer)
    st.rerun()
