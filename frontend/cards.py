"""Suggestion cards shown on the landing state to seed a first prompt."""

import streamlit as st

from utils import session

SUGGESTIONS = [
    {
        "title": "Explain a concept",
        "description": "Break down a tricky programming or CS topic simply.",
        "prompt": "Explain how recursion works, with a simple example.",
    },
    {
        "title": "Debug my code",
        "description": "Walk through an error and how to fix it.",
        "prompt": "Help me debug a Python IndexError in my code.",
    },
    {
        "title": "Learn ML basics",
        "description": "Get a clear, practical intro to a machine learning idea.",
        "prompt": "Give me a beginner-friendly overview of how neural networks learn.",
    },
    {
        "title": "System design tips",
        "description": "Understand a software architecture pattern.",
        "prompt": "Explain the difference between monolithic and microservice architectures.",
    },
]


def render_suggestion_cards() -> None:
    columns = st.columns(len(SUGGESTIONS), gap="small")

    for index, (column, suggestion) in enumerate(zip(columns, SUGGESTIONS)):
        with column:
            with st.container(key=f"card_{index}"):
                clicked = st.button(
                    f"**{suggestion['title']}**  \n{suggestion['description']}",
                    key=f"use_{index}",
                    use_container_width=True,
                )
                if clicked:
                    session.set_pending_prompt(suggestion["prompt"])
                    st.rerun()
