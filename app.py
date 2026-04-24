import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Validate API key early ────────────────────────────────────────────────────
if not os.getenv("GOOGLE_API_KEY"):
    st.error(
        "❌ **GOOGLE_API_KEY not found.**\n\n"
        "Please create a `.env` file with:\n```\nGOOGLE_API_KEY=your_key_here\n```"
    )
    st.stop()

from styles      import CUSTOM_CSS
from prompts     import PROMPTS, WORD_LIMITS, ICONS, SUMMARY_OPTIONS
from transcript  import extract_video_id, extract_transcript, fetch_video_metadata
from gemini_client import generate_summary
from history     import init_history, add_to_history, render_history_panel
from export      import export_txt, export_markdown, get_export_filename

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="YT Summarizer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ── Session state defaults ────────────────────────────────────────────────────
DEFAULTS = {
    "summary_length":   "Medium",
    "summary_output":   None,
    "summary_type_used": None,
    "current_url":      "",
    "video_metadata":   None,
    "summary_history":  [],
    "show_history":     False,
}
for key, val in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = val

init_history()

# ── Helper: compute word count & reading time ─────────────────────────────────
def get_stats(text: str) -> tuple[int, int]:
    words = len(text.split())
    read_time = max(1, round(words / 200))
    return words, read_time

# ══════════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════════
header_col, hist_toggle_col = st.columns([8, 2])
with header_col:
    st.markdown('<div class="app-title">🎬 YouTube AI Summarizer</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">'
        'Paste any YouTube link · Choose your format · Get instant AI-powered notes'
        '</div>',
        unsafe_allow_html=True
    )
with hist_toggle_col:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button(
        "🕘 History" if not st.session_state.show_history else "✖ Close History",
        use_container_width=True
    ):
        st.session_state.show_history = not st.session_state.show_history
        st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HISTORY DRAWER (shown above main layout when toggled)
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.show_history:
    st.markdown('<div class="section-label">🕘 Recent Summaries</div>', unsafe_allow_html=True)
    render_history_panel()
    st.markdown("<hr>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MAIN LAYOUT — left (inputs) | right (output)
# ══════════════════════════════════════════════════════════════════════════════
left_col, right_col = st.columns([3, 7], gap="large")

# ─────────────────────────────────────────────────────────────────────────────
# LEFT PANEL — Inputs
# ─────────────────────────────────────────────────────────────────────────────
with left_col:

    # ── URL input ─────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">🔗 Video URL</div>', unsafe_allow_html=True)
    youtube_link = st.text_input(
        label="YouTube link",
        value=st.session_state.current_url,
        placeholder="https://www.youtube.com/watch?v=...",
        label_visibility="collapsed",
        key="url_input"
    )

    # Sync URL to session
    if youtube_link != st.session_state.current_url:
        st.session_state.current_url  = youtube_link
        st.session_state.video_metadata = None  # Reset metadata on URL change

    # ── Thumbnail + metadata preview ──────────────────────────────────────────
    if youtube_link:
        video_id = extract_video_id(youtube_link)
        if video_id:
            # Fetch and cache metadata
            if st.session_state.video_metadata is None:
                with st.spinner("Loading video info..."):
                    st.session_state.video_metadata = fetch_video_metadata(video_id)

            meta = st.session_state.video_metadata
            st.image(meta.get("thumbnail_fallback", meta["thumbnail"]), use_container_width=True)
            st.markdown(
                f'''<div class="video-meta-card">
                    <div class="video-meta-title">{meta["title"]}</div>
                    <div class="video-meta-channel">📺 {meta["channel"]}</div>
                </div>''',
                unsafe_allow_html=True
            )
        else:
            st.warning("⚠️ Invalid YouTube URL format.")

    # ── Summary format selector ───────────────────────────────────────────────
    st.markdown('<div class="section-label" style="margin-top:1.3rem;">🎛️ Summary Format</div>', unsafe_allow_html=True)

    radio_labels  = [f"{icon} {name}" for icon, name in SUMMARY_OPTIONS]
    label_to_key  = {f"{icon} {name}": name for icon, name in SUMMARY_OPTIONS}

    # Find current index
    current_key   = st.session_state.summary_length
    current_label = next(
        (f"{icon} {name}" for icon, name in SUMMARY_OPTIONS if name == current_key),
        radio_labels[1]
    )
    current_idx = radio_labels.index(current_label) if current_label in radio_labels else 1

    summary_format = st.radio(
        label="Summary format",
        options=radio_labels,
        index=current_idx,
        label_visibility="collapsed",
        horizontal=False
    )

    selected_key = label_to_key[summary_format]
    st.session_state.summary_length = selected_key

    st.markdown(
        f'<div style="color:#5a6380;font-size:0.76rem;margin-top:0.3rem;">'
        f'{WORD_LIMITS[selected_key]}</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Generate button ───────────────────────────────────────────────────────
    generate_clicked = st.button("🚀 Generate Summary", use_container_width=True)

    if generate_clicked:
        if not youtube_link:
            st.warning("⚠️ Please enter a YouTube URL first.")
        else:
            vid_id = extract_video_id(youtube_link)
            if not vid_id:
                st.error("❌ Could not parse video ID from this URL.")
            else:
                # Step-by-step progress
                step1 = st.empty()
                step2 = st.empty()
                step3 = st.empty()

                step1.markdown(
                    '<div class="progress-step active"><span class="step-icon">📥</span>Fetching transcript…</div>',
                    unsafe_allow_html=True
                )
                try:
                    transcript_text = extract_transcript(youtube_link)

                    step1.markdown(
                        '<div class="progress-step done"><span class="step-icon">✅</span>Transcript fetched</div>',
                        unsafe_allow_html=True
                    )
                    step2.markdown(
                        '<div class="progress-step active"><span class="step-icon">🤖</span>Generating summary…</div>',
                        unsafe_allow_html=True
                    )

                    selected_prompt = PROMPTS[selected_key]
                    summary = generate_summary(transcript_text, selected_prompt)

                    step2.markdown(
                        '<div class="progress-step done"><span class="step-icon">✅</span>Summary generated</div>',
                        unsafe_allow_html=True
                    )
                    step3.markdown(
                        '<div class="progress-step done"><span class="step-icon">🎉</span>Done!</div>',
                        unsafe_allow_html=True
                    )

                    # Save to session
                    st.session_state.summary_output    = summary
                    st.session_state.summary_type_used = selected_key

                    # Save to history
                    meta = st.session_state.video_metadata or {}
                    add_to_history(
                        video_id     = vid_id,
                        title        = meta.get("title", "Unknown Title"),
                        channel      = meta.get("channel", "Unknown"),
                        summary_type = selected_key,
                        summary_text = summary,
                        url          = youtube_link,
                    )

                except RuntimeError as e:
                    step1.empty()
                    step2.empty()
                    step3.empty()
                    st.error(str(e))

# ─────────────────────────────────────────────────────────────────────────────
# RIGHT PANEL — Output
# ─────────────────────────────────────────────────────────────────────────────
with right_col:
    if st.session_state.summary_output:
        length_used  = st.session_state.summary_type_used
        icon         = ICONS.get(length_used, "📄")
        summary_text = st.session_state.summary_output
        words, read_time = get_stats(summary_text)

        # ── Header row ────────────────────────────────────────────────────────
        head_col, dl_col = st.columns([6, 4])
        with head_col:
            st.markdown(
                f'<div class="summary-header">{icon} {length_used} Summary</div>',
                unsafe_allow_html=True
            )
        with dl_col:
            # Export as TXT
            meta       = st.session_state.video_metadata or {}
            vid_title  = meta.get("title", "video")
            vid_url    = st.session_state.current_url

            dl1, dl2 = st.columns(2)
            with dl1:
                st.download_button(
                    label="📄 TXT",
                    data=export_txt(summary_text, length_used, vid_title),
                    file_name=get_export_filename(length_used, "txt"),
                    mime="text/plain",
                    use_container_width=True
                )
            with dl2:
                st.download_button(
                    label="📝 MD",
                    data=export_markdown(summary_text, length_used, vid_title, vid_url),
                    file_name=get_export_filename(length_used, "md"),
                    mime="text/markdown",
                    use_container_width=True
                )

        # ── Stats badges ──────────────────────────────────────────────────────
        st.markdown(
            f'''<div class="summary-stats">
                <span class="stat-badge">📝 {words} words</span>
                <span class="stat-badge">⏱️ ~{read_time} min read</span>
                <span class="stat-badge">🎛️ {length_used}</span>
            </div>''',
            unsafe_allow_html=True
        )

        # ── Summary content ───────────────────────────────────────────────────
        # Use st.markdown for proper markdown rendering inside a styled container
        st.markdown(f'<div class="summary-box">{summary_text}</div>', unsafe_allow_html=True)

    else:
        # ── Empty state ───────────────────────────────────────────────────────
        st.markdown(
            '''
            <div class="empty-state">
                <div class="empty-icon">🎬</div>
                <div class="empty-title">Your summary will appear here</div>
                <div>
                    Enter a YouTube URL on the left,<br>
                    choose a format, and hit <b>Generate</b>.
                </div>
                <div style="margin-top:0.5rem;font-size:0.8rem;color:#3a4360;">
                    Supports: Short · Medium · Detailed · Flashcards · Tweet Thread · Study Notes
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )