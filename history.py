import streamlit as st
from datetime import datetime


MAX_HISTORY = 5  # Maximum number of history entries to keep


def init_history():
    """Initialize history in session state if not present."""
    if "summary_history" not in st.session_state:
        st.session_state.summary_history = []


def add_to_history(video_id: str, title: str, channel: str,
                   summary_type: str, summary_text: str, url: str):
    """
    Add a new summary to history. Keeps latest MAX_HISTORY entries.
    Avoids duplicate entries for the same video+type combination.
    """
    init_history()

    # Remove existing entry for same video+type to avoid duplicates
    st.session_state.summary_history = [
        h for h in st.session_state.summary_history
        if not (h["video_id"] == video_id and h["summary_type"] == summary_type)
    ]

    entry = {
        "video_id":    video_id,
        "title":       title,
        "channel":     channel,
        "summary_type": summary_type,
        "summary_text": summary_text,
        "url":         url,
        "timestamp":   datetime.now().strftime("%b %d, %H:%M"),
    }

    # Prepend so newest is first
    st.session_state.summary_history.insert(0, entry)

    # Trim to max
    st.session_state.summary_history = st.session_state.summary_history[:MAX_HISTORY]


def get_history() -> list:
    """Return the current history list."""
    init_history()
    return st.session_state.summary_history


def clear_history():
    """Clear all history."""
    st.session_state.summary_history = []


def render_history_panel():
    """
    Render the history panel. Clicking a history item restores its summary.
    Returns True if a history item was selected (triggers rerun).
    """
    init_history()
    history = st.session_state.summary_history

    if not history:
        st.markdown(
            '<div class="history-empty">No history yet.<br>Generate a summary to get started.</div>',
            unsafe_allow_html=True
        )
        return False

    selected = False
    for i, entry in enumerate(history):
        thumb_url = f"https://img.youtube.com/vi/{entry['video_id']}/default.jpg"

        # Render each history card
        st.markdown(
            f'''
            <div class="history-card" id="hist-{i}">
                <img src="{thumb_url}" class="history-thumb" onerror="this.style.display='none'"/>
                <div class="history-info">
                    <div class="history-title">{entry["title"][:45]}{"…" if len(entry["title"]) > 45 else ""}</div>
                    <div class="history-meta">{entry["summary_type"]} · {entry["timestamp"]}</div>
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )

        if st.button("↩ Restore", key=f"restore_{i}", use_container_width=True):
            st.session_state.summary_output    = entry["summary_text"]
            st.session_state.summary_type_used = entry["summary_type"]
            st.session_state.current_url       = entry["url"]
            st.session_state.video_metadata    = {
                "title":    entry["title"],
                "channel":  entry["channel"],
                "thumbnail": f"https://img.youtube.com/vi/{entry['video_id']}/0.jpg",
                "thumbnail_fallback": f"https://img.youtube.com/vi/{entry['video_id']}/0.jpg",
            }
            selected = True

    if st.button("🗑️ Clear History", use_container_width=True):
        clear_history()
        st.rerun()

    return selected