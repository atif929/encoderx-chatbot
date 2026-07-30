"""Session-state management for the chat application.

Owns all st.session_state reads/writes related to chats. Contains no
rendering logic — frontend modules call into this to read or mutate state.
"""

import uuid

import streamlit as st

MAX_TITLE_LENGTH = 40


def init_session() -> None:
    """Ensure all session-state keys exist before the page renders."""
    if "chats" not in st.session_state:
        st.session_state.chats = {}

    if "current_chat_id" not in st.session_state:
        st.session_state.current_chat_id = None

    if "renaming_chat_id" not in st.session_state:
        st.session_state.renaming_chat_id = None

    if "pending_prompt" not in st.session_state:
        st.session_state.pending_prompt = None

    if not st.session_state.chats:
        create_chat()

    if st.session_state.current_chat_id not in st.session_state.chats:
        st.session_state.current_chat_id = next(iter(st.session_state.chats))


def create_chat() -> str:
    """Create a new empty chat and make it the active one."""
    chat_id = str(uuid.uuid4())
    st.session_state.chats[chat_id] = {
        "title": "New Chat",
        "messages": [],
        "history": [],
    }
    st.session_state.current_chat_id = chat_id
    return chat_id


def create_chat_if_needed() -> None:
    """Start a new chat only if the current one already has messages.

    Prevents piling up empty "New Chat" entries when the user repeatedly
    clicks New Chat without sending anything.
    """
    if get_current_chat()["messages"]:
        create_chat()


def get_current_chat() -> dict:
    return st.session_state.chats[st.session_state.current_chat_id]


def switch_chat(chat_id: str) -> None:
    st.session_state.current_chat_id = chat_id
    st.session_state.renaming_chat_id = None


def delete_chat(chat_id: str) -> None:
    del st.session_state.chats[chat_id]

    if not st.session_state.chats:
        create_chat()
    elif st.session_state.current_chat_id == chat_id:
        st.session_state.current_chat_id = next(iter(st.session_state.chats))

    st.session_state.renaming_chat_id = None


def start_rename(chat_id: str) -> None:
    st.session_state.renaming_chat_id = chat_id


def cancel_rename() -> None:
    st.session_state.renaming_chat_id = None


def save_rename(chat_id: str, new_title: str) -> None:
    st.session_state.chats[chat_id]["title"] = new_title.strip() or "Untitled Chat"
    st.session_state.renaming_chat_id = None


def set_pending_prompt(text: str) -> None:
    """Queue a prompt (e.g. from a suggestion card) to be sent on next run."""
    st.session_state.pending_prompt = text


def pop_pending_prompt() -> str | None:
    prompt = st.session_state.pending_prompt
    st.session_state.pending_prompt = None
    return prompt


def record_answer(chat: dict, question: str, answer: str) -> None:
    """Record the assistant's answer and derive a title on first message.

    The user message is appended separately by the caller so it can be
    displayed immediately, before the (potentially slow) model call.
    """
    chat["messages"].append({"role": "assistant", "content": answer})

    chat["history"].append({"role": "user", "parts": [question]})
    chat["history"].append({"role": "model", "parts": [answer]})

    if chat["title"] == "New Chat":
        chat["title"] = (
            question[:MAX_TITLE_LENGTH] + "..."
            if len(question) > MAX_TITLE_LENGTH
            else question
        )
