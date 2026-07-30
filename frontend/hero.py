"""Landing hero shown before the first message in a chat."""

import streamlit as st


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero">
            <h1>What are we exploring today?</h1>
            <p class="hero-subtitle">
                Ask about programming, AI, machine learning, or software engineering.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
