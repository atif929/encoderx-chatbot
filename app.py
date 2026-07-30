import streamlit as st
import uuid

from backend.chatbot import get_response

st.set_page_config(
    page_title="AI Educational Assistant",
    layout="wide"
)

with open("styles/style.css") as file:
    st.markdown(
        f"<style>{file.read()}</style>",
        unsafe_allow_html=True
    )


def create_chat():
    chat_id = str(uuid.uuid4())
    st.session_state.chats[chat_id] = {
        "title": "New Chat",
        "messages": [],
        "history": []
    }
    st.session_state.current_chat_id = chat_id
    return chat_id


def safe_container(key):
    try:
        return st.container(key=key)
    except TypeError:
        return st.container()


has_popover = hasattr(st, "popover")

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

if "renaming_chat_id" not in st.session_state:
    st.session_state.renaming_chat_id = None

if not st.session_state.chats:
    create_chat()

if st.session_state.current_chat_id not in st.session_state.chats:
    st.session_state.current_chat_id = next(iter(st.session_state.chats))

current_chat = st.session_state.chats[st.session_state.current_chat_id]
is_empty = len(current_chat["messages"]) == 0

with st.sidebar:

    st.markdown('<div class="sidebar-brand">AI Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">Educational Chatbot</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    with safe_container("new_chat_container"):
        if st.button("+   New chat", use_container_width=True):
            if current_chat["messages"]:
                create_chat()
                st.rerun()

    st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section-label">Recent</div>', unsafe_allow_html=True)

    for chat_id, chat_data in list(st.session_state.chats.items()):

        is_active = chat_id == st.session_state.current_chat_id
        row_key = f"chat_row_active_{chat_id}" if is_active else f"chat_row_{chat_id}"

        with safe_container(row_key):

            col_main, col_menu = st.columns([0.82, 0.18])

            with col_main:
                if st.button(chat_data["title"], key=f"switch_{chat_id}", use_container_width=True):
                    st.session_state.current_chat_id = chat_id
                    st.session_state.renaming_chat_id = None
                    st.rerun()

            with col_menu:

                def render_rename_delete(container):
                    with container:
                        if st.session_state.renaming_chat_id == chat_id:

                            new_title = st.text_input(
                                "Rename chat",
                                value=chat_data["title"],
                                key=f"rename_input_{chat_id}",
                                label_visibility="collapsed"
                            )

                            if st.button("Save", key=f"save_{chat_id}", use_container_width=True):
                                st.session_state.chats[chat_id]["title"] = new_title.strip() or "Untitled Chat"
                                st.session_state.renaming_chat_id = None
                                st.rerun()

                        else:
                            if st.button("Rename", key=f"rename_{chat_id}", use_container_width=True):
                                st.session_state.renaming_chat_id = chat_id
                                st.rerun()

                        if st.button("Delete", key=f"delete_{chat_id}", use_container_width=True):
                            del st.session_state.chats[chat_id]
                            if not st.session_state.chats:
                                create_chat()
                            elif st.session_state.current_chat_id == chat_id:
                                st.session_state.current_chat_id = next(iter(st.session_state.chats))
                            st.session_state.renaming_chat_id = None
                            st.rerun()

                if has_popover:
                    render_rename_delete(st.popover("⋯", use_container_width=True))
                else:
                    render_rename_delete(st.container())

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    st.markdown('<div class="sidebar-footer">Ask about programming, AI &amp; software engineering.</div>', unsafe_allow_html=True)


if is_empty:
    st.markdown('<div class="hero"><h1>Ready when you are.</h1></div>', unsafe_allow_html=True)
    st.markdown(
        """<style>
        div[data-testid="stBottomBlockContainer"],
        div[data-testid="stBottom"] > div{
            top:50% !important;
            bottom:auto !important;
            transform:translateY(-50%) !important;
        }
        </style>""",
        unsafe_allow_html=True
    )

for message in current_chat["messages"]:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

question = st.chat_input("Ask anything")

if question:

    current_chat["messages"].append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = get_response(
                question,
                current_chat["history"]
            )

            st.markdown(answer)

    current_chat["messages"].append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    current_chat["history"].append(
        {
            "role": "user",
            "parts": [question]
        }
    )

    current_chat["history"].append(
        {
            "role": "model",
            "parts": [answer]
        }
    )

    if current_chat["title"] == "New Chat":
        current_chat["title"] = question[:40] + ("..." if len(question) > 40 else "")

    st.rerun()