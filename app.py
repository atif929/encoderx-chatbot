import streamlit as st

from frontend import cards, chat, hero, sidebar
from utils import session

st.set_page_config(
    page_title="EncoderX — AI Learning Assistant",
    layout="wide",
    initial_sidebar_state="expanded",
)

with open("styles/style.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

session.init_session()
sidebar.render_sidebar()

current_chat = session.get_current_chat()
is_empty = len(current_chat["messages"]) == 0

if is_empty:
    hero.render_hero()
    cards.render_suggestion_cards()
else:
    chat.render_messages(current_chat)

question = chat.render_input() or session.pop_pending_prompt()

if question:
    chat.handle_user_message(current_chat, question)
