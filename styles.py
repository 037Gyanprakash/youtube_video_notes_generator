# CUSTOM_CSS = """
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

# /* ── Root variables ─────────────────────────────────────────── */
# :root {
#     --bg:         #0a0d14;
#     --surface:    #111520;
#     --surface2:   #161b2e;
#     --accent:     #4f8ef7;
#     --accent2:    #a259ff;
#     --glow-blue:  0 0 12px #4f8ef799, 0 0 32px #4f8ef744;
#     --glow-purple:0 0 12px #a259ff99, 0 0 32px #a259ff44;
#     --text:       #e8eaf6;
#     --muted:      #6b7280;
#     --border:     #1e2640;
#     --radius:     14px;
# }

# /* ── Global reset ───────────────────────────────────────────── */
# html, body, [data-testid="stAppViewContainer"] {
#     background: var(--bg) !important;
#     color: var(--text) !important;
#     font-family: 'DM Sans', sans-serif !important;
# }

# [data-testid="stSidebar"] { display: none !important; }
# [data-testid="stHeader"]  { background: transparent !important; }

# /* ── Title ──────────────────────────────────────────────────── */
# .app-title {
#     font-family: 'Syne', sans-serif;
#     font-weight: 800;
#     font-size: 2.2rem;
#     background: linear-gradient(135deg, var(--accent), var(--accent2));
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     margin-bottom: 0.2rem;
#     animation: fadeSlideDown 0.7s ease both;
# }
# .app-subtitle {
#     color: var(--muted);
#     font-size: 0.95rem;
#     margin-bottom: 1.5rem;
#     animation: fadeSlideDown 0.9s ease both;
# }

# /* ── Panel cards — target Streamlit's column containers ────── */
# [data-testid="stColumns"] > div:first-child > [data-testid="stVerticalBlock"] {
#     background: var(--surface);
#     border: 1px solid var(--border);
#     border-radius: var(--radius);
#     padding: 1.6rem 1.4rem !important;
#     min-height: 520px;
#     animation: fadeIn 0.8s ease both;
# }
# [data-testid="stColumns"] > div:last-child > [data-testid="stVerticalBlock"] {
#     background: var(--surface2);
#     border: 1px solid var(--border);
#     border-radius: var(--radius);
#     padding: 1.6rem 1.4rem !important;
#     min-height: 520px;
#     animation: fadeIn 0.95s ease both;
# }

# /* ── Input field glow ───────────────────────────────────────── */
# [data-testid="stTextInput"] input {
#     background: #0d1120 !important;
#     border: 1.5px solid var(--border) !important;
#     border-radius: 10px !important;
#     color: var(--text) !important;
#     font-family: 'DM Sans', sans-serif !important;
#     padding: 0.65rem 1rem !important;
#     transition: border-color 0.3s ease, box-shadow 0.3s ease !important;
# }
# [data-testid="stTextInput"] input:focus {
#     border-color: var(--accent) !important;
#     box-shadow: var(--glow-blue) !important;
#     outline: none !important;
# }
# [data-testid="stTextInput"] input::placeholder { color: var(--muted) !important; }

# /* ── Thumbnail ──────────────────────────────────────────────── */
# .thumb-wrap {
#     border-radius: 10px;
#     overflow: hidden;
#     border: 1.5px solid var(--border);
#     margin-top: 0.8rem;
#     transition: box-shadow 0.3s ease;
#     animation: fadeIn 0.5s ease both;
# }
# .thumb-wrap:hover { box-shadow: var(--glow-blue); }

# /* ── Length selector buttons ────────────────────────────────── */
# .length-btn-row {
#     display: flex;
#     gap: 0.5rem;
#     margin: 1rem 0 0.4rem;
# }
# .length-btn {
#     flex: 1;
#     padding: 0.55rem 0.4rem;
#     border-radius: 9px;
#     border: 1.5px solid var(--border);
#     background: #0d1120;
#     color: var(--muted);
#     font-family: 'Syne', sans-serif;
#     font-size: 0.82rem;
#     font-weight: 600;
#     cursor: pointer;
#     transition: all 0.25s ease;
#     text-align: center;
# }
# .length-btn:hover {
#     border-color: var(--accent);
#     color: var(--accent);
#     box-shadow: var(--glow-blue);
#     transform: translateY(-2px);
# }
# .length-btn.active {
#     background: linear-gradient(135deg, #1a2a4a, #1e1538);
#     border-color: var(--accent2);
#     color: #fff;
#     box-shadow: var(--glow-purple);
# }

# /* ── Streamlit radio override ───────────────────────────────── */
# [data-testid="stRadio"] label {
#     background: #0d1120;
#     border: 1.5px solid var(--border);
#     border-radius: 9px;
#     padding: 0.45rem 0.9rem !important;
#     margin: 0.2rem !important;
#     color: var(--muted) !important;
#     font-family: 'Syne', sans-serif !important;
#     font-size: 0.85rem !important;
#     font-weight: 600 !important;
#     cursor: pointer;
#     transition: all 0.25s ease !important;
# }
# [data-testid="stRadio"] label:hover {
#     border-color: var(--accent) !important;
#     color: var(--accent) !important;
#     box-shadow: var(--glow-blue) !important;
# }
# [data-testid="stRadio"] [aria-checked="true"] + label,
# [data-testid="stRadio"] label:has(input:checked) {
#     background: linear-gradient(135deg, #1a2a4a, #1e1538) !important;
#     border-color: var(--accent2) !important;
#     color: #fff !important;
#     box-shadow: var(--glow-purple) !important;
# }
# [data-testid="stRadio"] > div { flex-wrap: wrap; gap: 0.4rem; }

# /* ── Generate button ────────────────────────────────────────── */
# [data-testid="stButton"] > button {
#     width: 100%;
#     background: linear-gradient(135deg, var(--accent), var(--accent2)) !important;
#     color: #fff !important;
#     border: none !important;
#     border-radius: 10px !important;
#     font-family: 'Syne', sans-serif !important;
#     font-size: 0.95rem !important;
#     font-weight: 700 !important;
#     padding: 0.7rem 1.2rem !important;
#     cursor: pointer;
#     transition: all 0.3s ease !important;
#     box-shadow: 0 4px 20px #4f8ef733 !important;
#     letter-spacing: 0.04em !important;
#     animation: pulseGlow 3s ease-in-out infinite;
# }
# [data-testid="stButton"] > button:hover {
#     transform: translateY(-3px) !important;
#     box-shadow: var(--glow-blue), 0 8px 30px #4f8ef733 !important;
#     filter: brightness(1.1) !important;
# }
# [data-testid="stButton"] > button:active {
#     transform: translateY(0px) !important;
# }

# /* ── Summary output area ────────────────────────────────────── */
# .summary-box {
#     background: #0d1120;
#     border: 1.5px solid var(--border);
#     border-radius: var(--radius);
#     padding: 1.4rem 1.6rem;
#     color: var(--text);
#     font-family: 'DM Sans', sans-serif;
#     font-size: 0.95rem;
#     line-height: 1.75;
#     animation: fadeSlideUp 0.5s ease both;
#     min-height: 200px;
# }
# .summary-header {
#     font-family: 'Syne', sans-serif;
#     font-size: 1.1rem;
#     font-weight: 700;
#     color: var(--accent);
#     margin-bottom: 0.9rem;
#     display: flex;
#     align-items: center;
#     gap: 0.5rem;
# }
# .empty-state {
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     justify-content: center;
#     height: 380px;
#     color: var(--muted);
#     font-size: 0.9rem;
#     gap: 0.8rem;
#     text-align: center;
# }
# .empty-icon {
#     font-size: 3rem;
#     opacity: 0.3;
#     animation: float 3s ease-in-out infinite;
# }
# .badge {
#     display: inline-block;
#     padding: 0.2rem 0.7rem;
#     border-radius: 20px;
#     font-size: 0.75rem;
#     font-weight: 600;
#     font-family: 'Syne', sans-serif;
#     margin-bottom: 0.8rem;
# }
# .badge-blue   { background: #1a2a4a; color: var(--accent);  border: 1px solid var(--accent); }
# .badge-purple { background: #1e1538; color: var(--accent2); border: 1px solid var(--accent2); }

# /* ── Section labels ─────────────────────────────────────────── */
# .section-label {
#     font-family: 'Syne', sans-serif;
#     font-size: 0.75rem;
#     font-weight: 700;
#     letter-spacing: 0.1em;
#     text-transform: uppercase;
#     color: var(--muted);
#     margin-bottom: 0.5rem;
#     margin-top: 1.2rem;
# }

# /* ── Download button override ───────────────────────────────── */
# [data-testid="stDownloadButton"] > button {
#     background: transparent !important;
#     border: 1.5px solid var(--accent) !important;
#     color: var(--accent) !important;
#     border-radius: 9px !important;
#     font-family: 'Syne', sans-serif !important;
#     font-size: 0.82rem !important;
#     font-weight: 600 !important;
#     padding: 0.45rem 1rem !important;
#     transition: all 0.25s ease !important;
#     box-shadow: none !important;
#     animation: none !important;
# }
# [data-testid="stDownloadButton"] > button:hover {
#     background: #1a2a4a !important;
#     box-shadow: var(--glow-blue) !important;
#     transform: translateY(-2px) !important;
# }

# /* ── Spinner ────────────────────────────────────────────────── */
# [data-testid="stSpinner"] { color: var(--accent) !important; }

# /* ── Divider ────────────────────────────────────────────────── */
# hr { border-color: var(--border) !important; margin: 1rem 0 !important; }

# /* ── Scrollbar ──────────────────────────────────────────────── */
# ::-webkit-scrollbar       { width: 6px; }
# ::-webkit-scrollbar-track { background: var(--bg); }
# ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
# ::-webkit-scrollbar-thumb:hover { background: var(--accent); }

# /* ── Keyframes ──────────────────────────────────────────────── */
# @keyframes fadeIn {
#     from { opacity: 0; }
#     to   { opacity: 1; }
# }
# @keyframes fadeSlideDown {
#     from { opacity: 0; transform: translateY(-18px); }
#     to   { opacity: 1; transform: translateY(0); }
# }
# @keyframes fadeSlideUp {
    
#     from { opacity: 0; transform: translateY(16px); }
#     to   { opacity: 1; transform: translateY(0); }
# }
# @keyframes pulseGlow {
#     0%, 100% { box-shadow: 0 4px 20px #4f8ef733; }
#     50%       { box-shadow: 0 4px 28px #a259ff55, 0 0 20px #4f8ef744; }
# }
# @keyframes float {
#     0%, 100% { transform: translateY(0); }
#     50%       { transform: translateY(-10px); }
# }
# </style>
# """



CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

/* ── Root variables ─────────────────────────────────────────── */
:root {
    --bg:          #080b12;
    --surface:     #0f1420;
    --surface2:    #131826;
    --surface3:    #0d1120;
    --accent:      #4f8ef7;
    --accent2:     #a259ff;
    --accent3:     #00d4aa;
    --glow-blue:   0 0 12px #4f8ef799, 0 0 32px #4f8ef744;
    --glow-purple: 0 0 12px #a259ff99, 0 0 32px #a259ff44;
    --glow-teal:   0 0 12px #00d4aa88, 0 0 28px #00d4aa33;
    --text:        #e8eaf6;
    --text2:       #b0b8d0;
    --muted:       #5a6380;
    --border:      #1a2140;
    --border2:     #232d4a;
    --radius:      14px;
    --radius-sm:   9px;
}

/* ── Global reset ───────────────────────────────────────────── */
html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stSidebar"]        { display: none !important; }
[data-testid="stHeader"]         { background: transparent !important; }
.block-container { padding-left: 2rem !important; padding-right: 2rem !important; }

/* ── Ambient background glow ────────────────────────────────── */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    top: -200px; left: -200px;
    width: 600px; height: 600px;
    background: radial-gradient(circle, #4f8ef711 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}
[data-testid="stAppViewContainer"]::after {
    content: '';
    position: fixed;
    bottom: -200px; right: -200px;
    width: 500px; height: 500px;
    background: radial-gradient(circle, #a259ff0d 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

/* ── Title ──────────────────────────────────────────────────── */
.app-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 2.4rem;
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent2) 60%, var(--accent3) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.15rem;
    animation: fadeSlideDown 0.6s ease both;
    letter-spacing: -0.02em;
}
.app-subtitle {
    color: var(--muted);
    font-size: 0.93rem;
    margin-bottom: 1.2rem;
    animation: fadeSlideDown 0.8s ease both;
}

/* ── Panel cards ────────────────────────────────────────────── */
[data-testid="stColumns"] > div > [data-testid="stVerticalBlock"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.5rem 1.3rem !important;
    min-height: 540px;
    animation: fadeIn 0.8s ease both;
}

/* ── Section labels ─────────────────────────────────────────── */
.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.5rem;
    margin-top: 1.1rem;
}

/* ── Input field ────────────────────────────────────────────── */
[data-testid="stTextInput"] input {
    background: var(--surface3) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
    padding: 0.65rem 1rem !important;
    font-size: 0.9rem !important;
    transition: border-color 0.3s ease, box-shadow 0.3s ease !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: var(--accent) !important;
    box-shadow: var(--glow-blue) !important;
    outline: none !important;
}
[data-testid="stTextInput"] input::placeholder { color: var(--muted) !important; }

/* ── Video metadata card ────────────────────────────────────── */
.video-meta-card {
    background: var(--surface3);
    border: 1px solid var(--border2);
    border-radius: var(--radius-sm);
    padding: 0.75rem 0.85rem;
    margin-top: 0.65rem;
    animation: fadeIn 0.4s ease both;
}
.video-meta-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 0.84rem;
    color: var(--text);
    margin-bottom: 0.2rem;
    line-height: 1.3;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
.video-meta-channel {
    font-size: 0.77rem;
    color: var(--accent3);
    font-weight: 500;
}

/* ── Radio buttons ──────────────────────────────────────────── */
[data-testid="stRadio"] label {
    background: var(--surface3) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    padding: 0.4rem 0.82rem !important;
    margin: 0.18rem !important;
    color: var(--muted) !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.81rem !important;
    font-weight: 600 !important;
    cursor: pointer;
    transition: all 0.22s ease !important;
}
[data-testid="stRadio"] label:hover {
    border-color: var(--accent) !important;
    color: var(--accent) !important;
    box-shadow: var(--glow-blue) !important;
}
[data-testid="stRadio"] label:has(input:checked) {
    background: linear-gradient(135deg, #1a2a4a, #1e1538) !important;
    border-color: var(--accent2) !important;
    color: #fff !important;
    box-shadow: var(--glow-purple) !important;
}
[data-testid="stRadio"] > div { flex-wrap: wrap; gap: 0.35rem; }

/* ── Generate button ────────────────────────────────────────── */
[data-testid="stButton"] > button {
    width: 100%;
    background: linear-gradient(135deg, var(--accent), var(--accent2)) !important;
    color: #fff !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.93rem !important;
    font-weight: 700 !important;
    padding: 0.68rem 1.2rem !important;
    cursor: pointer;
    transition: all 0.28s ease !important;
    box-shadow: 0 4px 20px #4f8ef733 !important;
    letter-spacing: 0.05em !important;
    animation: pulseGlow 3s ease-in-out infinite;
}
[data-testid="stButton"] > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: var(--glow-blue), 0 8px 30px #4f8ef733 !important;
    filter: brightness(1.08) !important;
}
[data-testid="stButton"] > button:active { transform: translateY(0) !important; }

/* ── Summary output area ────────────────────────────────────── */
.summary-box {
    background: var(--surface3);
    border: 1.5px solid var(--border);
    border-radius: var(--radius);
    padding: 1.4rem 1.6rem;
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-size: 0.94rem;
    line-height: 1.78;
    animation: fadeSlideUp 0.45s ease both;
    min-height: 180px;
}

/* ── Summary header ─────────────────────────────────────────── */
.summary-header {
    font-family: 'Syne', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 0.7rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* ── Stats badges ───────────────────────────────────────────── */
.summary-stats {
    display: flex;
    gap: 0.6rem;
    margin-bottom: 0.85rem;
    flex-wrap: wrap;
}
.stat-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.28rem;
    padding: 0.2rem 0.62rem;
    border-radius: 20px;
    font-size: 0.71rem;
    font-weight: 600;
    font-family: 'Syne', sans-serif;
    background: #1a2a4a;
    color: var(--accent);
    border: 1px solid #2a3a6a;
}

/* ── Download buttons ───────────────────────────────────────── */
[data-testid="stDownloadButton"] > button {
    background: transparent !important;
    border: 1.5px solid var(--border2) !important;
    color: var(--text2) !important;
    border-radius: var(--radius-sm) !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    padding: 0.36rem 0.82rem !important;
    transition: all 0.22s ease !important;
    box-shadow: none !important;
    animation: none !important;
}
[data-testid="stDownloadButton"] > button:hover {
    border-color: var(--accent3) !important;
    color: var(--accent3) !important;
    background: #0a1e1a !important;
    box-shadow: var(--glow-teal) !important;
    transform: translateY(-2px) !important;
}

/* ── History cards ──────────────────────────────────────────── */
.history-card {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    background: var(--surface3);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    padding: 0.55rem 0.75rem;
    margin-bottom: 0.4rem;
    transition: border-color 0.2s ease;
}
.history-card:hover { border-color: var(--accent); }
.history-thumb {
    width: 52px;
    height: 36px;
    object-fit: cover;
    border-radius: 5px;
    flex-shrink: 0;
    border: 1px solid var(--border);
}
.history-info { flex: 1; min-width: 0; }
.history-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.77rem;
    font-weight: 600;
    color: var(--text);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.history-meta { font-size: 0.69rem; color: var(--muted); margin-top: 0.12rem; }
.history-empty {
    color: var(--muted);
    font-size: 0.81rem;
    text-align: center;
    padding: 1.2rem 0;
    line-height: 1.7;
}

/* ── Empty state ────────────────────────────────────────────── */
.empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 400px;
    color: var(--muted);
    font-size: 0.88rem;
    gap: 0.75rem;
    text-align: center;
}
.empty-icon  { font-size: 3.2rem; opacity: 0.22; animation: float 3.5s ease-in-out infinite; }
.empty-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1rem; color: var(--accent); }

/* ── Spinner / alerts ───────────────────────────────────────── */
[data-testid="stSpinner"] > div { color: var(--accent) !important; }
[data-testid="stAlert"] { border-radius: var(--radius-sm) !important; font-size: 0.87rem !important; }

/* ── Divider & scrollbar ────────────────────────────────────── */
hr { border-color: var(--border) !important; margin: 0.75rem 0 !important; }
::-webkit-scrollbar       { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }

/* ── Keyframes ──────────────────────────────────────────────── */
@keyframes fadeIn {
    from { opacity: 0; } to { opacity: 1; }
}
@keyframes fadeSlideDown {
    from { opacity: 0; transform: translateY(-16px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes pulseGlow {
    0%, 100% { box-shadow: 0 4px 20px #4f8ef733; }
    50%       { box-shadow: 0 4px 28px #a259ff55, 0 0 20px #4f8ef744; }
}
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50%       { transform: translateY(-10px); }
}

/* ── Progress steps ─────────────────────────────────────────── */
.progress-step {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    padding: 0.48rem 0.8rem;
    border-radius: var(--radius-sm);
    background: var(--surface3);
    border: 1px solid var(--border);
    font-size: 0.82rem;
    color: var(--muted);
    margin-bottom: 0.4rem;
    transition: all 0.3s ease;
    font-family: 'DM Sans', sans-serif;
}
.progress-step.active {
    border-color: var(--accent);
    color: var(--accent);
    background: #0d1a30;
    box-shadow: var(--glow-blue);
}
.progress-step.done {
    border-color: var(--accent3);
    color: var(--accent3);
    background: #0a1e1a;
}
.step-icon { font-size: 1rem; min-width: 1.2rem; }

</style>
"""