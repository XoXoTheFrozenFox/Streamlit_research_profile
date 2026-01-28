from urllib.parse import quote

import streamlit as st
import streamlit.components.v1 as components

import os
import glob
import time

import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Bernard Swanepoel — Research Profile",
    page_icon="🌞",
    layout="wide",
)

# -----------------------------
# Links / info
# -----------------------------
TAGLINE = ""

PORTFOLIO_URL = "https://xoxothefrozenfox.github.io/react-personal-portfolio/"
LINKEDIN_URL = "https://www.linkedin.com/in/bernard-swanepoel-a2777322b/"
GITHUB_URL = "https://github.com/XoXoTheFrozenFox"
EMAIL = "BernardSwanepoel1510@gmail.com"

STATIC_PREFIX = "Hi🌞, my name is Bernard Swanepoel. "

ROTATING = [
    "Masters student✏️",
    "Researcher🥸",
    "Computer Scientist💻",
    "Coffee addict☕",
    "Space enthusiast💫",
]

# -----------------------------
# Theme sync (Python <-> topbar)
# Uses URL query param: ?theme=orange|green|blue|pink
# -----------------------------
THEMES = {
    "orange": {
        "color": "rgba(255,122,24,0.95)",
        "grid": "rgba(255,122,24,0.14)",
        "axis": "rgba(255,122,24,0.28)",
        "border": "rgba(255,122,24,0.45)",
    },
    "green": {
        "color": "rgba(57,255,20,0.95)",
        "grid": "rgba(57,255,20,0.14)",
        "axis": "rgba(57,255,20,0.28)",
        "border": "rgba(57,255,20,0.45)",
    },
    "blue": {
        "color": "rgba(0,231,255,0.95)",
        "grid": "rgba(0,231,255,0.14)",
        "axis": "rgba(0,231,255,0.28)",
        "border": "rgba(0,231,255,0.45)",
    },
    "pink": {
        "color": "rgba(255,43,214,0.95)",
        "grid": "rgba(255,43,214,0.14)",
        "axis": "rgba(255,43,214,0.28)",
        "border": "rgba(255,43,214,0.45)",
    },
}

def get_theme() -> str:
    # Streamlit versions differ: support both APIs
    try:
        t = st.query_params.get("theme", "orange")
        if isinstance(t, list):
            t = t[0] if t else "orange"
        theme = str(t).strip().lower()
    except Exception:
        qp = st.experimental_get_query_params()
        theme = (qp.get("theme", ["orange"])[0] or "orange").strip().lower()

    return theme if theme in THEMES else "orange"

ACTIVE_THEME = get_theme()

# Ensure the root html has the right theme attribute on load
st.markdown(
    f"<script>document.documentElement.setAttribute('data-theme', '{ACTIVE_THEME}');</script>",
    unsafe_allow_html=True,
)

# -----------------------------
# Global terminal aesthetic
# -----------------------------
st.markdown(
    """
<style>
/* Hide Streamlit default UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Remove the "chain/link" icon next to headings */
a.stMarkdownHeaderLink,
a[data-testid="stHeaderLink"],
[data-testid="stHeader"] a,
[data-testid="stHeader"] svg,
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a { 
  display: none !important; 
  opacity: 0 !important;
  visibility: hidden !important;
}

/* Theme vars */
:root{
  --bg:#050505;

  --orange:#ff7a18;
  --green:#39ff14;
  --blue:#00e7ff;
  --pink:#ff2bd6;

  --border-orange:rgba(255,122,24,0.45);
  --border-green:rgba(57,255,20,0.45);
  --border-blue:rgba(0,231,255,0.45);
  --border-pink:rgba(255,43,214,0.45);

  --panel: rgba(0,0,0,0.35);
}

/* Default theme = ORANGE */
html, body, [data-testid="stAppViewContainer"]{
  background: var(--bg) !important;
  color: var(--orange) !important;
}
*{ color: var(--orange) !important; }

.block-container{
  padding-top: 0.55rem !important;
  padding-bottom: 1.25rem !important;
}

/* Divider */
hr{
  border: none !important;
  border-top: 1px solid var(--border-orange) !important;
  opacity: 1 !important;
  margin: 0.18rem 0 0.55rem 0 !important;
}

/* Metrics */
div[data-testid="stMetric"]{
  background: var(--panel) !important;
  border: 1px solid var(--border-orange) !important;
  border-radius: 14px !important;
  padding: 12px 12px !important;
  box-shadow: none !important;
}

/* Alerts */
div[data-testid="stAlert"]{
  background: var(--panel) !important;
  border: 1px solid var(--border-orange) !important;
  border-radius: 14px !important;
}

/* st.info bg (if ever used) */
div[data-testid="stAlert"][data-baseweb="notification"]{
  background: #050505 !important;
}
div[data-testid="stAlert"][data-baseweb="notification"] *{
  background: transparent !important;
}

p, li, label, div{
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

/* -----------------------------
   TRUE BLACK inputs + remove ANY red wrapper ring
------------------------------ */
div[data-testid="stTextInput"],
div[data-testid="stTextArea"]{
  position: relative !important;
}

/* Kill wrapper borders/box-shadows */
div[data-testid="stTextInput"] > div,
div[data-testid="stTextArea"] > div,
div[data-testid="stTextInput"] [data-baseweb],
div[data-testid="stTextArea"] [data-baseweb],
div[data-testid="stTextInput"] [data-baseweb] *:not(input),
div[data-testid="stTextArea"] [data-baseweb] *:not(textarea){
  background: var(--bg) !important;
  border-color: transparent !important;
  box-shadow: none !important;
  outline: none !important;
}

div[data-testid="stTextInput"]:focus-within,
div[data-testid="stTextArea"]:focus-within{
  box-shadow: none !important;
  outline: none !important;
  border-color: transparent !important;
}

div[data-testid="stTextArea"] [data-baseweb="textarea"],
div[data-testid="stTextInput"] [data-baseweb="base-input"]{
  background: var(--bg) !important;
  border: none !important;
  box-shadow: none !important;
  outline: none !important;
}

/* Actual input/textarea = ONLY border you want */
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea{
  background: var(--bg) !important;
  color: var(--orange) !important;

  border: 1px solid var(--border-orange) !important;
  border-radius: 14px !important;

  box-shadow: none !important;
  outline: none !important;

  background-clip: padding-box !important;
}

div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus,
div[data-testid="stTextInput"] input:focus-visible,
div[data-testid="stTextArea"] textarea:focus-visible,
div[data-testid="stTextInput"] input[aria-invalid="true"],
div[data-testid="stTextArea"] textarea[aria-invalid="true"]{
  border: 1px solid var(--border-orange) !important;
  box-shadow: none !important;
  outline: none !important;
}

div[data-testid="stTextInput"] input::placeholder,
div[data-testid="stTextArea"] textarea::placeholder{
  color: rgba(255,122,24,0.65) !important;
}

/* Autofill */
div[data-testid="stTextInput"] input:-webkit-autofill,
div[data-testid="stTextInput"] input:-webkit-autofill:hover,
div[data-testid="stTextInput"] input:-webkit-autofill:focus{
  -webkit-box-shadow: 0 0 0 1000px var(--bg) inset !important;
  -webkit-text-fill-color: var(--orange) !important;
  caret-color: var(--orange) !important;
  border: 1px solid var(--border-orange) !important;
}

/* Bottom-right hint */
div[data-testid="stTextInput"]:has(input:placeholder-shown):not(:focus-within)::after{
  content: "Field empty!";
  position: absolute;
  right: 14px;
  top: 44px;
  font-size: 12px;
  opacity: 0.75;
  pointer-events: none;
}
div[data-testid="stTextArea"]:has(textarea:placeholder-shown):not(:focus-within)::after{
  content: "Field empty!";
  position: absolute;
  right: 14px;
  top: 44px;
  font-size: 12px;
  opacity: 0.75;
  pointer-events: none;
}

/* Buttons */
.stButton > button, div[data-testid="stFormSubmitButton"] button{
  background: var(--bg) !important;
  color: var(--orange) !important;
  border: 1px solid var(--border-orange) !important;
  border-radius: 14px !important;
  padding: 0.55rem 0.95rem !important;
  box-shadow: none !important;
}
.stButton > button:hover, div[data-testid="stFormSubmitButton"] button:hover{
  background: rgba(255,122,24,0.08) !important;
}

/* Mailto button */
a.send-mailto-btn{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none !important;
  background: var(--bg) !important;
  color: var(--orange) !important;
  border: 1px solid var(--border-orange) !important;
  border-radius: 14px !important;
  padding: 0.55rem 0.95rem !important;
  box-shadow: none !important;
  transition: transform 140ms ease, background 140ms ease;
  user-select: none;
  cursor: pointer;
}
a.send-mailto-btn:hover{
  background: rgba(255,122,24,0.08) !important;
  transform: translateY(-1px);
}
a.send-mailto-btn.is-disabled{
  opacity: 0.55;
  cursor: not-allowed;
  pointer-events: none;
  transform: none !important;
}

/* -----------------------------
   THEME OVERRIDES (Green / Blue / Pink)
------------------------------ */

/* GREEN */
html[data-theme="green"] body,
html[data-theme="green"] [data-testid="stAppViewContainer"]{ color: var(--green) !important; }
html[data-theme="green"] *{ color: var(--green) !important; }
html[data-theme="green"] hr{ border-top: 1px solid var(--border-green) !important; }
html[data-theme="green"] div[data-testid="stMetric"],
html[data-theme="green"] div[data-testid="stAlert"]{ border: 1px solid var(--border-green) !important; }

html[data-theme="green"] div[data-testid="stTextInput"] input,
html[data-theme="green"] div[data-testid="stTextArea"] textarea{
  color: var(--green) !important;
  border: 1px solid var(--border-green) !important;
}
html[data-theme="green"] div[data-testid="stTextInput"] input:focus,
html[data-theme="green"] div[data-testid="stTextArea"] textarea:focus,
html[data-theme="green"] div[data-testid="stTextInput"] input[aria-invalid="true"],
html[data-theme="green"] div[data-testid="stTextArea"] textarea[aria-invalid="true"]{
  border: 1px solid var(--border-green) !important;
  box-shadow: none !important;
  outline: none !important;
}
html[data-theme="green"] div[data-testid="stTextInput"] input::placeholder,
html[data-theme="green"] div[data-testid="stTextArea"] textarea::placeholder{ color: rgba(57,255,20,0.65) !important; }
html[data-theme="green"] .stButton > button,
html[data-theme="green"] div[data-testid="stFormSubmitButton"] button,
html[data-theme="green"] a.send-mailto-btn{
  color: var(--green) !important;
  border: 1px solid var(--border-green) !important;
}
html[data-theme="green"] .stButton > button:hover,
html[data-theme="green"] div[data-testid="stFormSubmitButton"] button:hover,
html[data-theme="green"] a.send-mailto-btn:hover{ background: rgba(57,255,20,0.08) !important; }

/* BLUE */
html[data-theme="blue"] body,
html[data-theme="blue"] [data-testid="stAppViewContainer"]{ color: var(--blue) !important; }
html[data-theme="blue"] *{ color: var(--blue) !important; }
html[data-theme="blue"] hr{ border-top: 1px solid var(--border-blue) !important; }
html[data-theme="blue"] div[data-testid="stMetric"],
html[data-theme="blue"] div[data-testid="stAlert"]{ border: 1px solid var(--border-blue) !important; }

html[data-theme="blue"] div[data-testid="stTextInput"] input,
html[data-theme="blue"] div[data-testid="stTextArea"] textarea{
  color: var(--blue) !important;
  border: 1px solid var(--border-blue) !important;
}
html[data-theme="blue"] div[data-testid="stTextInput"] input:focus,
html[data-theme="blue"] div[data-testid="stTextArea"] textarea:focus,
html[data-theme="blue"] div[data-testid="stTextInput"] input[aria-invalid="true"],
html[data-theme="blue"] div[data-testid="stTextArea"] textarea[aria-invalid="true"]{
  border: 1px solid var(--border-blue) !important;
  box-shadow: none !important;
  outline: none !important;
}
html[data-theme="blue"] div[data-testid="stTextInput"] input::placeholder,
html[data-theme="blue"] div[data-testid="stTextArea"] textarea::placeholder{ color: rgba(0,231,255,0.65) !important; }
html[data-theme="blue"] .stButton > button,
html[data-theme="blue"] div[data-testid="stFormSubmitButton"] button,
html[data-theme="blue"] a.send-mailto-btn{
  color: var(--blue) !important;
  border: 1px solid var(--border-blue) !important;
}
html[data-theme="blue"] .stButton > button:hover,
html[data-theme="blue"] div[data-testid="stFormSubmitButton"] button:hover,
html[data-theme="blue"] a.send-mailto-btn:hover{ background: rgba(0,231,255,0.08) !important; }

/* PINK */
html[data-theme="pink"] body,
html[data-theme="pink"] [data-testid="stAppViewContainer"]{ color: var(--pink) !important; }
html[data-theme="pink"] *{ color: var(--pink) !important; }
html[data-theme="pink"] hr{ border-top: 1px solid var(--border-pink) !important; }
html[data-theme="pink"] div[data-testid="stMetric"],
html[data-theme="pink"] div[data-testid="stAlert"]{ border: 1px solid var(--border-pink) !important; }

html[data-theme="pink"] div[data-testid="stTextInput"] input,
html[data-theme="pink"] div[data-testid="stTextArea"] textarea{
  color: var(--pink) !important;
  border: 1px solid var(--border-pink) !important;
}
html[data-theme="pink"] div[data-testid="stTextInput"] input:focus,
html[data-theme="pink"] div[data-testid="stTextArea"] textarea:focus,
html[data-theme="pink"] div[data-testid="stTextInput"] input[aria-invalid="true"],
html[data-theme="pink"] div[data-testid="stTextArea"] textarea[aria-invalid="true"]{
  border: 1px solid var(--border-pink) !important;
  box-shadow: none !important;
  outline: none !important;
}
html[data-theme="pink"] div[data-testid="stTextInput"] input::placeholder,
html[data-theme="pink"] div[data-testid="stTextArea"] textarea::placeholder{ color: rgba(255,43,214,0.65) !important; }
html[data-theme="pink"] .stButton > button,
html[data-theme="pink"] div[data-testid="stFormSubmitButton"] button,
html[data-theme="pink"] a.send-mailto-btn{
  color: var(--pink) !important;
  border: 1px solid var(--border-pink) !important;
}
html[data-theme="pink"] .stButton > button:hover,
html[data-theme="pink"] div[data-testid="stFormSubmitButton"] button:hover,
html[data-theme="pink"] a.send-mailto-btn:hover{ background: rgba(255,43,214,0.08) !important; }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Topbar component (cycles theme and writes ?theme=... then reloads)
# -----------------------------
topbar_html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
  :root {{
    --orange:#ff7a18;
    --green:#39ff14;
    --blue:#00e7ff;
    --pink:#ff2bd6;

    --border-orange:rgba(255,122,24,0.45);
    --border-green:rgba(57,255,20,0.45);
    --border-blue:rgba(0,231,255,0.45);
    --border-pink:rgba(255,43,214,0.45);
  }}

  html, body {{
    overflow: visible !important;
    height: auto !important;
  }}

  body {{
    margin: 0;
    padding: 10px 8px 12px 8px;
    background: transparent;
    color: var(--orange);
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
                 "Courier New", "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", monospace;
    box-sizing: border-box;
  }}

  html[data-theme="green"] body {{ color: var(--green); }}
  html[data-theme="blue"]  body {{ color: var(--blue); }}
  html[data-theme="pink"]  body {{ color: var(--pink); }}

  #wrap {{
    width: 100%;
    display: block;
    overflow: visible;
  }}

  .row1 {{
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: start;
    gap: 12px;
    width: 100%;
  }}

  .text-col {{
    padding: 16px 16px 8px 16px;
  }}

  .terminal-title {{
    font-size: clamp(1.08rem, 2.05vw, 1.62rem);
    font-weight: 700;
    line-height: 1.22;
    margin: 0;
    min-width: 0;
    white-space: normal;
    overflow: visible;
    overflow-wrap: anywhere;
    word-break: break-word;
    padding-top: 2px;
  }}

  .typing-line {{ display: inline; }}
  .prompt {{ display: inline; white-space: nowrap; }}
  #prefix, #word {{ display: inline; }}

  .cursor {{
    display:inline-block;
    width: 10px;
    margin-left: 2px;
    animation: blink 1s steps(1) infinite;
  }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}

  .icon-row {{
    display:flex;
    gap:10px;
    align-items:center;
    justify-content:flex-end;
    flex-wrap: wrap;
    padding: 10px 8px 10px 8px;
    overflow: visible;
  }}

  a.icon-btn, button.icon-btn {{
    width:44px;
    height:44px;
    border-radius:999px;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    text-decoration:none;
    color: currentColor;

    box-sizing: border-box;
    border:1px solid var(--border-orange);
    background: rgba(0,0,0,0.25);
    box-shadow: 0 0 0 1px rgba(255,122,24,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
    transition: transform 140ms ease, background 140ms ease, border-color 140ms ease, box-shadow 140ms ease;
    -webkit-tap-highlight-color: transparent;
    user-select:none;
    cursor: pointer;

    line-height: 1;
    overflow: visible;
    padding: 0;
  }}

  html[data-theme="green"] a.icon-btn, html[data-theme="green"] button.icon-btn {{
    border-color: var(--border-green);
    box-shadow: 0 0 0 1px rgba(57,255,20,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
  }}
  html[data-theme="blue"] a.icon-btn, html[data-theme="blue"] button.icon-btn {{
    border-color: var(--border-blue);
    box-shadow: 0 0 0 1px rgba(0,231,255,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
  }}
  html[data-theme="pink"] a.icon-btn, html[data-theme="pink"] button.icon-btn {{
    border-color: var(--border-pink);
    box-shadow: 0 0 0 1px rgba(255,43,214,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
  }}

  a.icon-btn i, button.icon-btn i {{
    font-size: 18px;
    pointer-events:none;
  }}

  a.icon-btn:hover, button.icon-btn:hover {{
    transform: translateY(-1px);
    background: rgba(255,122,24,0.12);
    box-shadow: 0 0 12px rgba(255,122,24,0.18), 0 10px 18px rgba(0,0,0,0.45);
  }}
  html[data-theme="green"] a.icon-btn:hover, html[data-theme="green"] button.icon-btn:hover {{
    background: rgba(57,255,20,0.12);
    box-shadow: 0 0 12px rgba(57,255,20,0.18), 0 10px 18px rgba(0,0,0,0.45);
  }}
  html[data-theme="blue"] a.icon-btn:hover, html[data-theme="blue"] button.icon-btn:hover {{
    background: rgba(0,231,255,0.12);
    box-shadow: 0 0 12px rgba(0,231,255,0.18), 0 10px 18px rgba(0,0,0,0.45);
  }}
  html[data-theme="pink"] a.icon-btn:hover, html[data-theme="pink"] button.icon-btn:hover {{
    background: rgba(255,43,214,0.12);
    box-shadow: 0 0 12px rgba(255,43,214,0.18), 0 10px 18px rgba(0,0,0,0.45);
  }}

  a.icon-btn:active, button.icon-btn:active {{
    transform: translateY(0px) scale(0.98);
  }}

  a.email-btn {{ position: relative; }}
  a.email-btn i {{
    position: absolute;
    inset: 0;
    display:flex;
    align-items:center;
    justify-content:center;
    pointer-events:none;
  }}
  a.email-btn .email-open {{ opacity: 0; }}
  a.email-btn .email-closed {{ opacity: 1; }}
  a.email-btn:hover .email-open {{ opacity: 1; }}
  a.email-btn:hover .email-closed {{ opacity: 0; }}

  .tagline {{
    margin-top: 10px;
    margin-bottom: 0;
    font-size: clamp(1.00rem, 1.45vw, 1.18rem);
    font-weight: 650;
    opacity: 0.95;
    white-space: normal;
    overflow: visible;
    overflow-wrap: anywhere;
  }}

  @media (max-width: 640px) {{
    body {{ padding: 12px 10px 14px 10px; }}

    .row1 {{
      grid-template-columns: 1fr;
      gap: 8px;
    }}

    .text-col {{ padding: 0; }}

    .terminal-title {{
      font-size: 1.10rem;
      line-height: 1.25;
      padding-top: 0;
    }}

    .icon-row {{
      justify-content: flex-start;
      gap: 8px;
      padding: 0 0 12px 0;
      overflow: visible;
    }}

    a.icon-btn, button.icon-btn {{ width: 38px; height: 38px; }}
    a.icon-btn i, button.icon-btn i {{ font-size: 16px; }}

    .tagline {{
      font-size: 1.02rem;
      line-height: 1.25;
      margin-top: 6px;
    }}
  }}
</style>
</head>

<body>
  <div id="wrap">
    <div class="row1">
      <div class="text-col">
        <div class="terminal-title">
          <span class="typing-line">
            <span class="prompt">$&nbsp;</span>
            <span id="prefix"></span><span id="word"></span><span class="cursor">▌</span>
          </span>
        </div>

        <div class="tagline">{TAGLINE}</div>
      </div>

      <div class="icon-row">
        <button class="icon-btn" id="themeToggle" type="button" title="Toggle theme (Orange/Green/Blue/Pink)">
          <i class="fa-solid fa-palette"></i>
        </button>

        <a class="icon-btn" href="{PORTFOLIO_URL}" target="_blank" rel="noopener" title="Portfolio"><i class="fa-solid fa-globe"></i></a>
        <a class="icon-btn" href="{GITHUB_URL}" target="_blank" rel="noopener" title="GitHub"><i class="fa-brands fa-github"></i></a>
        <a class="icon-btn" href="{LINKEDIN_URL}" target="_blank" rel="noopener" title="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>

        <a class="icon-btn email-btn" href="mailto:{EMAIL}" title="Email">
          <i class="fa-solid fa-envelope email-closed"></i>
          <i class="fa-solid fa-envelope-open email-open"></i>
        </a>

        <a class="icon-btn" href="https://www.nwu.ac.za/" target="_blank" rel="noopener" title="North-West University"><i class="fa-solid fa-building-columns"></i></a>
      </div>
    </div>
  </div>

<script>
(function () {{
  const wrap = document.getElementById("wrap");
  const themes = ["orange", "green", "blue", "pink"];

  function setTheme(theme) {{
    const t = themes.includes(theme) ? theme : "orange";
    document.documentElement.setAttribute("data-theme", t);
    try {{
      if (window.parent && window.parent.document) {{
        window.parent.document.documentElement.setAttribute("data-theme", t);
      }}
    }} catch (e) {{}}
  }}

  // init from server (python)
  const initialTheme = {ACTIVE_THEME!r};
  setTheme(initialTheme);

  const toggleBtn = document.getElementById("themeToggle");
  toggleBtn.addEventListener("click", function () {{
    const cur = document.documentElement.getAttribute("data-theme") || "orange";
    const i = themes.indexOf(cur);
    const next = themes[(i + 1 + themes.length) % themes.length];

    // write ?theme=next then reload (so Python can match plot colors)
    try {{
      const url = new URL(window.parent.location.href);
      url.searchParams.set("theme", next);
      window.parent.location.href = url.toString();
    }} catch (e) {{
      setTheme(next);
    }}
  }});

  function getHeight() {{
    const b = wrap.getBoundingClientRect().height;
    const sh = wrap.scrollHeight;
    return Math.ceil(Math.max(b, sh));
  }}

  let raf = null;
  let lastH = 0;

  function resizeFrame() {{
    if (raf) cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {{
      try {{
        const h = Math.min(340, Math.max(70, getHeight() + 14));
        if (Math.abs(h - lastH) > 1 && window.frameElement) {{
          lastH = h;
          window.frameElement.style.height = h + "px";
        }}
      }} catch (e) {{}}
    }});
  }}

  window.addEventListener("load", () => resizeFrame());
  window.addEventListener("resize", () => setTimeout(resizeFrame, 60));
  new MutationObserver(() => resizeFrame()).observe(wrap, {{
    childList: true, subtree: true, characterData: true
  }});

  const staticPrefix = {STATIC_PREFIX!r};
  const words = {ROTATING!r};

  const prefixEl = document.getElementById("prefix");
  const wordEl = document.getElementById("word");
  prefixEl.textContent = staticPrefix;

  let idx = 0;
  let char = 0;
  let deleting = false;

  const typeSpeed = 45;
  const deleteSpeed = 25;
  const holdFull = 900;
  const holdEmpty = 260;

  function step() {{
    const glyphs = Array.from(words[idx]);

    if (!deleting) {{
      char++;
      wordEl.textContent = glyphs.slice(0, char).join("");
      resizeFrame();

      if (char >= glyphs.length) {{
        setTimeout(() => {{
          deleting = true;
          step();
        }}, holdFull);
        return;
      }}
      setTimeout(step, typeSpeed);
    }} else {{
      char--;
      wordEl.textContent = glyphs.slice(0, Math.max(0, char)).join("");
      resizeFrame();

      if (char <= 0) {{
        deleting = false;
        idx = (idx + 1) % words.length;
        setTimeout(step, holdEmpty);
        return;
      }}
      setTimeout(step, deleteSpeed);
    }}
  }}

  wordEl.textContent = "";
  step();

  setTimeout(resizeFrame, 120);
  setTimeout(resizeFrame, 350);
  setTimeout(resizeFrame, 700);
}})();
</script>
</body>
</html>
"""
components.html(topbar_html, height=93)
st.divider()

# -----------------------------
# Mailto builder
# -----------------------------
def build_mailto(to_email: str, subject: str, body: str) -> str:
    return f"mailto:{to_email}?subject={quote(subject)}&body={quote(body)}"

# -----------------------------
# Spectrum helpers
# -----------------------------
@st.cache_data(show_spinner=False)
def read_spectrum_csv(folder: str) -> pd.DataFrame:
    """
    Expects exactly 1 CSV inside data/<CLASS>/.
    Columns: wavelength_A, flux, ivar
    Handles comma / tab / whitespace delimited files.
    """
    paths = sorted(glob.glob(os.path.join(folder, "*.csv")))
    if not paths:
        raise FileNotFoundError(f"No CSV found in: {folder}")
    path = paths[0]

    df = None
    for kwargs in (dict(sep=","), dict(sep="\t"), dict(sep=r"\s+")):
        try:
            tmp = pd.read_csv(path, engine="python", **kwargs)
            if tmp.shape[1] >= 3:
                df = tmp
                break
        except Exception:
            continue

    if df is None or df.shape[1] < 3:
        raise ValueError(f"Could not parse CSV: {path}")

    df.columns = [c.strip() for c in df.columns]

    col_w = next((c for c in df.columns if c.lower().startswith("wavelength")), None)
    col_f = next((c for c in df.columns if c.lower() == "flux"), None)
    col_i = next((c for c in df.columns if c.lower() == "ivar"), None)

    if not (col_w and col_f and col_i):
        raise ValueError(f"Expected columns wavelength_A/flux/ivar. Got: {list(df.columns)}")

    out = df[[col_w, col_f, col_i]].rename(columns={col_w: "wavelength_A", col_f: "flux", col_i: "ivar"}).copy()

    out["wavelength_A"] = pd.to_numeric(out["wavelength_A"], errors="coerce")
    out["flux"] = pd.to_numeric(out["flux"], errors="coerce")

    out = out.dropna(subset=["wavelength_A", "flux"])
    out = out.sort_values("wavelength_A").reset_index(drop=True)
    return out

def make_fig(df: pd.DataFrame, n_scatter: int, n_line: int, title: str, theme_key: str) -> go.Figure:
    theme = THEMES.get(theme_key, THEMES["orange"])
    line_color = theme["color"]
    grid_color = theme["grid"]
    axis_color = theme["axis"]

    x = df["wavelength_A"].to_numpy()
    y = df["flux"].to_numpy()

    n_scatter = int(np.clip(n_scatter, 2, len(df)))
    n_line = int(np.clip(n_line, 0, len(df)))

    fig = go.Figure()

    fig.add_trace(
        go.Scattergl(
            x=x[:n_scatter],
            y=y[:n_scatter],
            mode="markers",
            marker=dict(size=4, opacity=0.95, color=line_color),
            hovertemplate="λ=%{x:.1f} Å<br>flux=%{y:.4f}<extra></extra>",
        )
    )

    if n_line > 0:
        fig.add_trace(
            go.Scattergl(
                x=x[:n_line],
                y=y[:n_line],
                mode="lines",
                line=dict(width=2.2, color=line_color),
                hoverinfo="skip",
            )
        )

    fig.update_layout(
        title=dict(text=title, x=0.02, xanchor="left"),
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        margin=dict(l=22, r=18, t=52, b=40),
        font=dict(
            family='ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
            color=line_color,
            size=13,
        ),
        showlegend=False,
    )

    fig.update_xaxes(
        title_text="wavelength (Å)",
        showgrid=True,
        gridcolor=grid_color,
        zeroline=False,
        ticks="outside",
        tickcolor=axis_color,
        linecolor=axis_color,
        mirror=True,
    )
    fig.update_yaxes(
        title_text="flux",
        showgrid=True,
        gridcolor=grid_color,
        zeroline=False,
        ticks="outside",
        tickcolor=axis_color,
        linecolor=axis_color,
        mirror=True,
    )

    return fig

# -----------------------------
# Main content
# -----------------------------
left, right = st.columns([1.35, 1.0], gap="large")

with left:
    st.markdown("## Background about me")
    st.write(
        "I’m Bernard Swanepoel, a Computer Science master’s student focused on applying deep learning to solar physics—"
        "especially automated sunspot detection and McIntosh classification. "
        "Outside of research, I’m into gaming (Destiny, League of Legends, and pretty much anything Nintendo), "
        "I sing opera, and I enjoy 3D printing—mostly figures and fun prints."
    )

    # -----------------------------
    # Education section (ONE-LINE BULLETS)
    # -----------------------------
    st.markdown("## Education")
    st.markdown(
        """
- **MSc Computer Science** — NWU *(2025–2027)*  
- **BSc Hons Computer Science and Information Technology** — NWU *(2023–2024)*  
- **BSc Information Technology** — NWU *(2021–2023)*  
- **TEFL (180 hours)** — i-to-i *(2023)*  
- **Matric certificate** — Wesvalia *(2016–2020)*  
        """.strip()
    )

    st.markdown("## Research interests")
    st.markdown(
        "- Machine learning\n"
        "- Deep learning\n"
        "- Distributed systems\n"
        "- Cloud computing\n"
        "- Cybersecurity\n"
        "- Astrophysics\n"
        "- Solar physics\n"
    )

    st.markdown("## Research titles")
    st.markdown(
        """
- **Master’s dissertation:** Sunspot classification using deep learning techniques  
- **Honours project:** Assessing the cybersecurity awareness of staff members in a higher educational institution
        """.strip()
    )

    st.markdown("## Current research summary")
    st.write(
        "Higher sunspot numbers on the Sun usually mean higher solar activity and a greater chance of space-weather events "
        "that can disrupt power grids, telecommunications, and other critical electronic systems. "
        "Some complex McIntosh sunspot group types are linked to higher probabilities of solar flares and coronal mass ejections (CMEs), "
        "which motivates the need for automated, reliable classification. "
        "For my dissertation, I built a dataset from Solar Dynamics Observatory (SDO) images accessed via the Joint Science Operations Center (JSOC): "
        "3,501 full-disk solar photos containing 14,014 sunspots. "
        "I created four datasets—one for detection and three for classification using the McIntosh–Zurich Zpc scheme "
        "(Zurich class Z, leading-spot penumbra p, and interior compactness c)—and split them into 85% training, 10% validation, and 5% testing. "
        "I evaluated multiple detection models (YOLO, RT-DETR, Faster R-CNN), with YOLOv8 performing best (83.30% precision, 76.00% recall). "
        "For classification, transformer-based models (ViT, Swin) generally outperformed traditional CNNs, and ConvNeXt achieved the best overall accuracy "
        "(70.27%) across the Z, p, and c subclassifications."
    )

    st.markdown("## Current research tools and technologies used")
    st.markdown(
        """
- **Data sources:** SDO, JSOC  
- **Deep learning:** PyTorch  
- **Core Python stack:** NumPy, Pandas  
- **Visualization:** Matplotlib, Seaborn  
- **Detection:** YOLOv8, RT-DETR, Faster R-CNN  
- **Classification:** ViT, Swin, ResNet, EfficientNet, ConvNeXt  
- **Evaluation:** Precision/Recall, Confusion matrices, ROC/PR analysis  
- **UI / Apps:** Streamlit, Tkinter  
- **Dev tools:** Visual Studio Code, Jupyter Notebooks, PyCharm  
- **Environments:** Conda, Windows Subsystem for Linux (WSL)
        """.strip()
    )

    st.markdown("## Hobby project: Star classification")
    st.write(
        """
The goal of this project was to classify stars from their spectra using the Morgan–Keenan (MK) spectral classification scheme, which defines seven primary spectral classes: **O, B, A, F, G, K, and M** (ordered from **hottest to coolest**).

Spectral data were collected from **SDSS** using a custom Python pipeline built with **Astropy**, resulting in a dataset of **10,955** stellar spectra. The extracted numerical spectral features were first used as input to a **1D Transformer** model. In a subsequent approach, each spectrum was converted into a **2D spectrogram** representation, which was then used to train a **2D Transformer** model.

The distribution and characteristics of the seven spectral classes can be visualized below:
        """.strip()
    )

    # -----------------------------
    # Hobby project: Spectrum explorer (FIXED + theme-colored)
    # -----------------------------
    st.markdown(
        """
<style>
/* Make the selectbox compact */
div[data-testid="stSelectbox"]{
  max-width: 230px !important;
}
div[data-testid="stSelectbox"] label{
  display:none !important;
}

/* Fancy plot wrapper */
.spectrum-wrap{
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 16px;
  padding: 12px 12px 6px 12px;
  background: rgba(0,0,0,0.28);
  margin-top: 8px;
  margin-bottom: 6px;
}
</style>
""",
        unsafe_allow_html=True,
    )

    classes = list("OBAFGKM")
    default_idx = classes.index("A")

    c1, c2 = st.columns([0.32, 0.68], gap="small")
    with c1:
        spec_class = st.selectbox(
            "Spectral class",
            options=classes,
            index=default_idx,
            label_visibility="collapsed",
            key="spec_class_select",
        )

    with c2:
        st.markdown(
            f"""
<div class="spectrum-wrap">
  <div style="font-size:12px; opacity:0.85;">
    $ spectrum viewer — MK class <b>{spec_class}</b>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

    plot_slot = st.empty()

    # No animation on first render; animate only when selection changes
    if "prev_spec_class" not in st.session_state:
        st.session_state.prev_spec_class = spec_class
        st.session_state.spec_initialized = False

    changed = (spec_class != st.session_state.prev_spec_class)

    data_root = "data"
    class_dir = os.path.join(data_root, spec_class)

    try:
        df_spec = read_spectrum_csv(class_dir)
    except Exception as e:
        plot_slot.error(f"Could not load spectrum for class '{spec_class}' from '{class_dir}': {e}")
        df_spec = None

    if df_spec is not None:
        title = f"$ MK spectral class {spec_class} — spectrum"
        N = len(df_spec)

        if not st.session_state.spec_initialized:
            fig = make_fig(df_spec, n_scatter=N, n_line=N, title=title, theme_key=ACTIVE_THEME)
            plot_slot.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
            st.session_state.spec_initialized = True

        elif changed:
            frames = 56
            sleep_s = 0.016

            # Phase 1: reveal points
            for k in range(2, frames + 1):
                n_scatter = int(np.interp(k, [2, frames], [max(16, N * 0.06), N]))
                fig = make_fig(df_spec, n_scatter=n_scatter, n_line=0, title=title, theme_key=ACTIVE_THEME)
                plot_slot.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
                time.sleep(sleep_s)

            # Phase 2: draw the line through
            for k in range(2, frames + 1):
                n_line = int(np.interp(k, [2, frames], [2, N]))
                fig = make_fig(df_spec, n_scatter=N, n_line=n_line, title=title, theme_key=ACTIVE_THEME)
                plot_slot.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
                time.sleep(sleep_s)

        else:
            fig = make_fig(df_spec, n_scatter=N, n_line=N, title=title, theme_key=ACTIVE_THEME)
            plot_slot.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    st.session_state.prev_spec_class = spec_class

    # -----------------------------
    # Rest of your content
    # -----------------------------
    st.markdown("## Hobby project: Metrics and visualisation")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Best Macro-F1", "—")
    m2.metric("Classes", "—")
    m3.metric("Images", "—")
    m4.metric("Backbone", "—")

    st.divider()

    st.markdown("## Contact")
    st.write("Send me a message directly from this page:")

    name = st.text_input("Name", placeholder="Your name")
    subject = st.text_input("Subject", placeholder="What is this about?")
    message = st.text_area("Message", placeholder="Type your message here...", height=160)

    name_s = (name or "").strip()
    subject_s = (subject or "").strip()
    message_s = (message or "").strip()

    ready = bool(name_s and subject_s and message_s)

    if ready:
        body = (
            "New website message\n\n"
            f"Name: {name_s}\n"
            f"Subject: {subject_s}\n\n"
            "Message:\n"
            f"{message_s}\n"
        )
        mailto = build_mailto(
            to_email=EMAIL,
            subject=f"[Website] {subject_s}",
            body=body,
        )
        st.markdown(
            f'<a class="send-mailto-btn" href="{mailto}">Send message</a>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<a class="send-mailto-btn is-disabled" href="#">Send message</a>',
            unsafe_allow_html=True,
        )

st.divider()
st.caption("© 2026 Bernard Swanepoel")
