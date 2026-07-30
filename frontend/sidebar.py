"""Sidebar: brand header, new chat action, conversation history, user footer."""

import streamlit as st

from utils import session

MAX_VISIBLE_TITLE = 28


def _truncate(title: str) -> str:
    if len(title) <= MAX_VISIBLE_TITLE:
        return title
    return title[:MAX_VISIBLE_TITLE].rstrip() + "…"


def _render_conversation_row(chat_id: str, chat_data: dict) -> None:
    is_active = chat_id == st.session_state.current_chat_id
    row_key = f"chat_row_active_{chat_id}" if is_active else f"chat_row_{chat_id}"

    with st.container(key=row_key):
        col_main, col_menu = st.columns([0.84, 0.16], gap="small")

        with col_main:
            if st.button(
                _truncate(chat_data["title"]),
                key=f"switch_{chat_id}",
                use_container_width=True,
                help=chat_data["title"] if len(chat_data["title"]) > MAX_VISIBLE_TITLE else None,
            ):
                session.switch_chat(chat_id)
                st.rerun()

        with col_menu:
            with st.popover(
                "",
                icon=":material/more_horiz:",
                use_container_width=True,
            ):
                if st.session_state.renaming_chat_id == chat_id:
                    with st.form(key=f"rename_form_{chat_id}", border=False):
                        new_title = st.text_input(
                            "Rename chat",
                            value=chat_data["title"],
                            label_visibility="collapsed",
                        )
                        col_save, col_cancel = st.columns(2, gap="small")
                        with col_save:
                            if st.form_submit_button("Save", use_container_width=True):
                                session.save_rename(chat_id, new_title)
                                st.rerun()
                        with col_cancel:
                            if st.form_submit_button("Cancel", use_container_width=True):
                                session.cancel_rename()
                                st.rerun()
                else:
                    if st.button("Rename", key=f"rename_{chat_id}", use_container_width=True):
                        session.start_rename(chat_id)
                        st.rerun()

                    if st.button("Delete", key=f"delete_{chat_id}", use_container_width=True):
                        session.delete_chat(chat_id)
                        st.rerun()


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand-row">
                <span class="sidebar-mark">E</span>
                <div>
                    <div class="sidebar-brand">EncoderX</div>
                    <div class="sidebar-sub">AI Learning Assistant</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.container(key="new_chat_container"):
            if st.button("New chat", use_container_width=True, icon=":material/edit_square:"):
                session.create_chat_if_needed()
                st.rerun()

        st.markdown('<div class="sidebar-section-label">Recent</div>', unsafe_allow_html=True)

        with st.container(key="history_scroll"):
            for chat_id, chat_data in list(st.session_state.chats.items()):
                _render_conversation_row(chat_id, chat_data)

        st.markdown('<div class="sidebar-spacer"></div>', unsafe_allow_html=True)

        with st.container(key="sidebar_footer"):
            col_user, col_settings = st.columns([0.82, 0.18], gap="small", vertical_alignment="center")

            with col_user:
                st.markdown(
                    """
                    <div class="sidebar-user">
                        <span class="sidebar-user-avatar">S</span>
                        <div class="sidebar-user-meta">
                            <div class="sidebar-user-name">Student</div>
                            <div class="sidebar-user-role">Free plan</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col_settings:
                st.button(
                    "",
                    icon=":material/settings:",
                    key="settings_button",
                    help="Settings (coming soon)",
                    disabled=True,
                )
