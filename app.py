from urllib.parse import quote
import os
import glob
import json
import time

import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# ✅ MUST be the first Streamlit command
st.set_page_config(
    page_title="BS — Research profile",
    page_icon="🧑‍💻",
    layout="wide",
)

# -----------------------------
# Helpers
# -----------------------------
def get_secret(key: str, default: str = "") -> str:
    """
    ✅ Prevents StreamlitSecretNotFoundError when no secrets.toml exists.
    Falls back to environment variables, then default.
    """
    try:
        return st.secrets.get(key, default)
    except Exception:
        return os.environ.get(key, default)


def build_mailto(to_email: str, subject: str, body: str) -> str:
    return f"mailto:{to_email}?subject={quote(subject)}&body={quote(body)}"


# -----------------------------
# Basic config
# -----------------------------
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

TAGLINE = ""

PORTFOLIO_URL = "https://xoxothefrozenfox.github.io/react-personal-portfolio/"
LINKEDIN_URL = "https://www.linkedin.com/in/bernard-swanepoel-a2777322b/"
GITHUB_URL = "https://github.com/XoXoTheFrozenFox"
EMAIL = "BernardSwanepoel1510@gmail.com"

STATIC_PREFIX = "Hi, my name is Bernard Swanepoel. "

ROTATING = [
    "Masters student✏️",
    "Researcher🥸",
    "Computer Scientist💻",
    "Coffee addict☕",
    "Space enthusiast💫",
]

# ✅ Safe secrets (won't crash if missing)
EMAILJS_PUBLIC_KEY = get_secret("EMAILJS_PUBLIC_KEY", "")
EMAILJS_SERVICE_ID = get_secret("EMAILJS_SERVICE_ID", "")
EMAILJS_TEMPLATE_ID = get_secret("EMAILJS_TEMPLATE_ID", "")

EMAILJS_READY = all([EMAILJS_PUBLIC_KEY, EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID])

# -----------------------------
# ✅ Theme bridge (FIXES “theme change breaks app” without setInterval spam)
# - Installs ONE message-bridge on the parent window (guarded)
# - Palette button posts {type:'bs_theme', theme:'...'}
# - Parent applies html[data-theme], localStorage, favicon emoji, then broadcasts to all iframes
# -----------------------------
THEME_BRIDGE_HTML = r"""
<script>
(function(){
  try {
    const P = window.parent;
    if (!P || P === window) return;

    if (P.__bsThemeBridgeInstalled) return;
    P.__bsThemeBridgeInstalled = true;

    const THEMES = ["green","blue","pink","orange"];
    const KEY = "bs_theme";
    const emojiMap = { orange:"🌞", blue:"🌚", green:"👽", pink:"🛸" };

    function safeTheme(t){
      return (t && THEMES.includes(t)) ? t : "green";
    }

    function getTheme(){
      try {
        const t = P.localStorage.getItem(KEY);
        if (t && THEMES.includes(t)) return t;
      } catch(e) {}
      try {
        const t2 = P.document.documentElement.getAttribute("data-theme");
        if (t2 && THEMES.includes(t2)) return t2;
      } catch(e) {}
      return "green";
    }

    function setFaviconEmoji(em){
      const svg =
        '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">' +
        '<rect width="64" height="64" fill="transparent"/>' +
        '<text x="32" y="34" text-anchor="middle" dominant-baseline="middle" ' +
        'font-size="50" font-family="Apple Color Emoji, Segoe UI Emoji, Noto Color Emoji, sans-serif">' +
        em +
        '</text></svg>';

      const url = "data:image/svg+xml," + encodeURIComponent(svg);

      try {
        let link = P.document.querySelector("link[rel*='icon']");
        if (!link) {
          link = P.document.createElement("link");
          link.rel = "icon";
          P.document.head.appendChild(link);
        }
        link.href = url;
      } catch(e) {}
    }

    function broadcastTheme(theme){
      try {
        const iframes = Array.from(P.document.querySelectorAll("iframe"));
        for (const fr of iframes){
          try {
            if (fr && fr.contentWindow) {
              fr.contentWindow.postMessage({ type:"bs_theme", theme }, "*");
            }
          } catch(e) {}
        }
      } catch(e) {}
    }

    function applyTheme(theme){
      const t = safeTheme(theme);
      try { P.localStorage.setItem(KEY, t); } catch(e) {}
      try { P.document.documentElement.setAttribute("data-theme", t); } catch(e) {}
      setFaviconEmoji(emojiMap[t] || "👽");
      broadcastTheme(t);
      return t;
    }

    // Public helper (optional)
    P.__bsSetTheme = applyTheme;

    // Receive from children
    P.addEventListener("message", (ev) => {
      try {
        const d = ev && ev.data;
        if (!d) return;

        if (d.type === "bs_theme") {
          applyTheme(d.theme);
          return;
        }

        if (d.type === "bs_theme_get") {
          const t = getTheme();
          if (ev.source && ev.source.postMessage) {
            ev.source.postMessage({ type:"bs_theme", theme:t }, "*");
          }
        }
      } catch(e) {}
    });

    // Initial apply once
    applyTheme(getTheme());

  } catch(e) {}
})();
</script>
"""
components.html(THEME_BRIDGE_HTML, height=0)

# -----------------------------
# Global CSS
# -----------------------------
st.markdown(
    """
<style>

div[data-testid="stToolbar"]{display:none !important; visibility:hidden !important;}
div[data-testid="stToolbarActions"]{display:none !important; visibility:hidden !important;}
div[data-testid="stStatusWidget"]{display:none !important; visibility:hidden !important;}
div[data-testid="stDeployButton"]{display:none !important; visibility:hidden !important;}
div[data-testid="stDecoration"]{display:none !important; visibility:hidden !important;}
div[data-testid="stActionButtonIcon"]{display:none !important; visibility:hidden !important;}
div[data-testid="stAppToolbar"]{display:none !important; visibility:hidden !important;}
button[title="View app settings"]{display:none !important;}
button[title="Settings"]{display:none !important;}
button[aria-label="View app settings"]{display:none !important;}
button[aria-label="Settings"]{display:none !important;}
div[class*="st-emotion-cache"][class*="toolbar"]{display:none !important;}
div[class*="st-emotion-cache"][style*="position: fixed"][style*="bottom"]{display:none !important;}

a.stMarkdownHeaderLink,
a[data-testid="stHeaderLink"],
[data-testid="stHeader"] a,
[data-testid="stHeader"] svg,
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
  display: none !important;
  opacity: 0 !important;
  visibility: hidden !important;
}

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

html, body, [data-testid="stAppViewContainer"]{
  background: var(--bg) !important;
  color: var(--green) !important;
}
*{ color: var(--green) !important; }

.block-container{
  padding-top: 0.55rem !important;
  padding-bottom: 1.25rem !important;
}

@media (max-width: 640px){
  .block-container{
    padding-left: 0.85rem !important;
    padding-right: 0.85rem !important;
  }
}

hr{
  border: none !important;
  border-top: 1px solid var(--border-green) !important;
  opacity: 1 !important;
  margin: 0.18rem 0 0.55rem 0 !important;
}

div[data-testid="stMetric"]{
  background: var(--panel) !important;
  border: 1px solid var(--border-green) !important;
  border-radius: 14px !important;
  padding: 12px 12px !important;
  box-shadow: none !important;
}

div[data-testid="stAlert"]{
  background: var(--panel) !important;
  border: 1px solid var(--border-green) !important;
  border-radius: 14px !important;
}

div[data-testid="stAlert"][data-baseweb="notification"]{
  background: #050505 !important;
}
div[data-testid="stAlert"][data-baseweb="notification"] *{
  background: transparent !important;
}

p, li, label, div{
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

div[data-testid="stTextInput"],
div[data-testid="stTextArea"]{
  position: relative !important;
}

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

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea{
  background: var(--bg) !important;
  color: var(--green) !important;
  border: 1px solid var(--border-green) !important;
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
  border: 1px solid var(--border-green) !important;
  box-shadow: none !important;
  outline: none !important;
}

div[data-testid="stTextInput"] input::placeholder,
div[data-testid="stTextArea"] textarea::placeholder{
  color: rgba(57,255,20,0.65) !important;
}

div[data-testid="stTextInput"] input:-webkit-autofill,
div[data-testid="stTextInput"] input:-webkit-autofill:hover,
div[data-testid="stTextInput"] input:-webkit-autofill:focus{
  -webkit-box-shadow: 0 0 0 1000px var(--bg) inset !important;
  -webkit-text-fill-color: var(--green) !important;
  caret-color: var(--green) !important;
  border: 1px solid var(--border-green) !important;
}

/* ✅ "Field empty!" bottom-right in each Streamlit input */
div[data-testid="stTextInput"]:has(input:placeholder-shown):not(:focus-within)::after{
  content: "Field empty!";
  position: absolute;
  right: 14px;
  bottom: 10px;
  font-size: 12px;
  opacity: 0.75;
  line-height: 1;
  pointer-events: none;
}
div[data-testid="stTextArea"]:has(textarea:placeholder-shown):not(:focus-within)::after{
  content: "Field empty!";
  position: absolute;
  right: 14px;
  bottom: 10px;
  font-size: 12px;
  opacity: 0.75;
  line-height: 1;
  pointer-events: none;
}

.stButton > button, div[data-testid="stFormSubmitButton"] button{
  background: var(--bg) !important;
  color: var(--green) !important;
  border: 1px solid var(--border-green) !important;
  border-radius: 14px !important;
  padding: 0.55rem 0.95rem !important;
  box-shadow: none !important;
}
.stButton > button:hover, div[data-testid="stFormSubmitButton"] button:hover{
  background: rgba(57,255,20,0.08) !important;
}

a.send-mailto-btn{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none !important;
  background: var(--bg) !important;
  color: var(--green) !important;
  border: 1px solid var(--border-green) !important;
  border-radius: 14px !important;
  padding: 0.55rem 0.95rem !important;
  box-shadow: none !important;
  transition: transform 140ms ease, background 140ms ease;
  user-select: none;
  cursor: pointer;
}
a.send-mailto-btn:hover{
  background: rgba(57,255,20,0.08) !important;
  transform: translateY(-1px);
}
a.send-mailto-btn.is-disabled{
  opacity: 0.55;
  cursor: not-allowed;
  pointer-events: none;
  transform: none !important;
}

div[data-testid="stSelectbox"]{
  width: 120px !important;
  max-width: 120px !important;
}
div[data-testid="stSelectbox"] label{ display:none !important; }

div[data-testid="stSelectbox"] [data-baseweb],
div[data-testid="stSelectbox"] [data-baseweb] *{
  box-shadow: none !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] > div{
  background: #050505 !important;
  border: 1px solid var(--border-green) !important;
  border-radius: 14px !important;
  box-shadow: none !important;
  outline: none !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within{
  border: 1px solid var(--border-green) !important;
  box-shadow: none !important;
}

div[data-testid="stSelectbox"] [role="listbox"]{
  background: #050505 !important;
  border: 1px solid var(--border-green) !important;
  border-radius: 14px !important;
  box-shadow: none !important;
}

div[data-testid="stCheckbox"]{
  padding: 6px 10px !important;
  border-radius: 14px !important;
  background: #050505 !important;
  border: 1px solid var(--border-green) !important;
}
div[data-testid="stCheckbox"] *{
  background: transparent !important;
}
div[data-testid="stCheckbox"] input{
  accent-color: var(--green) !important;
}

/* Theme overrides driven by html[data-theme="..."] */
html[data-theme="orange"] body,
html[data-theme="orange"] [data-testid="stAppViewContainer"]{ color: var(--orange) !important; }
html[data-theme="orange"] *{ color: var(--orange) !important; }
html[data-theme="orange"] hr{ border-top: 1px solid var(--border-orange) !important; }
html[data-theme="orange"] div[data-testid="stMetric"],
html[data-theme="orange"] div[data-testid="stAlert"]{ border: 1px solid var(--border-orange) !important; }
html[data-theme="orange"] div[data-testid="stTextInput"] input,
html[data-theme="orange"] div[data-testid="stTextArea"] textarea{
  color: var(--orange) !important;
  border: 1px solid var(--border-orange) !important;
}
html[data-theme="orange"] div[data-testid="stTextInput"] input::placeholder,
html[data-theme="orange"] div[data-testid="stTextArea"] textarea::placeholder{ color: rgba(255,122,24,0.65) !important; }
html[data-theme="orange"] .stButton > button,
html[data-theme="orange"] div[data-testid="stFormSubmitButton"] button,
html[data-theme="orange"] a.send-mailto-btn{
  color: var(--orange) !important;
  border: 1px solid var(--border-orange) !important;
}
html[data-theme="orange"] .stButton > button:hover,
html[data-theme="orange"] div[data-testid="stFormSubmitButton"] button:hover,
html[data-theme="orange"] a.send-mailto-btn:hover{ background: rgba(255,122,24,0.08) !important; }
html[data-theme="orange"] div[data-testid="stCheckbox"]{ border: 1px solid var(--border-orange) !important; }
html[data-theme="orange"] div[data-testid="stCheckbox"] input{ accent-color: var(--orange) !important; }
html[data-theme="orange"] div[data-testid="stSelectbox"] [data-baseweb="select"] > div{ border: 1px solid var(--border-orange) !important; }
html[data-theme="orange"] div[data-testid="stSelectbox"] [role="listbox"]{ border: 1px solid var(--border-orange) !important; }

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
html[data-theme="blue"] div[data-testid="stCheckbox"]{ border: 1px solid var(--border-blue) !important; }
html[data-theme="blue"] div[data-testid="stCheckbox"] input{ accent-color: var(--blue) !important; }
html[data-theme="blue"] div[data-testid="stSelectbox"] [data-baseweb="select"] > div{ border: 1px solid var(--border-blue) !important; }
html[data-theme="blue"] div[data-testid="stSelectbox"] [role="listbox"]{ border: 1px solid var(--border-blue) !important; }

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
html[data-theme="pink"] div[data-testid="stCheckbox"]{ border: 1px solid var(--border-pink) !important; }
html[data-theme="pink"] div[data-testid="stCheckbox"] input{ accent-color: var(--pink) !important; }
html[data-theme="pink"] div[data-testid="stSelectbox"] [data-baseweb="select"] > div{ border: 1px solid var(--border-pink) !important; }
html[data-theme="pink"] div[data-testid="stSelectbox"] [role="listbox"]{ border: 1px solid var(--border-pink) !important; }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Topbar
# -----------------------------
TOPBAR_TEMPLATE = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
  :root {
    --orange:#ff7a18;
    --green:#39ff14;
    --blue:#00e7ff;
    --pink:#ff2bd6;

    --border-orange:rgba(255,122,24,0.45);
    --border-green:rgba(57,255,20,0.45);
    --border-blue:rgba(0,231,255,0.45);
    --border-pink:rgba(255,43,214,0.45);
  }

  html, body { overflow: visible !important; height: auto !important; }

  body{
    margin:0;
    padding: 10px 8px 12px 8px;
    background: transparent;
    color: var(--green);
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
                 "Courier New", "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", monospace;
    box-sizing:border-box;
  }

  html[data-theme="orange"] body { color: var(--orange); }
  html[data-theme="green"]  body { color: var(--green); }
  html[data-theme="blue"]   body { color: var(--blue); }
  html[data-theme="pink"]   body { color: var(--pink); }

  #wrap { width:100%; display:block; overflow:visible; }

  .row1{
    display:grid;
    grid-template-columns: 1fr auto;
    align-items:start;
    gap:12px;
    width:100%;
  }

  .text-col{ padding: 16px 16px 8px 16px; }

  .terminal-title{
    font-size: clamp(1.08rem, 2.05vw, 1.62rem);
    font-weight:700;
    line-height:1.22;
    margin:0;
    min-width:0;
    white-space:normal;
    overflow:visible;
    overflow-wrap:anywhere;
    word-break:break-word;
    padding-top:2px;
  }

  .typing-line{ display:inline; }
  .prompt{ display:inline; white-space:nowrap; }
  #prefix, #word{ display:inline; }

  .cursor{
    display:inline-block;
    width:10px;
    margin-left:2px;
    animation: blink 1s steps(1) infinite;
  }
  @keyframes blink { 50% { opacity: 0; } }

  .icon-row{
    display:flex;
    gap:10px;
    align-items:center;
    justify-content:flex-end;
    flex-wrap:wrap;
    padding: 10px 8px 10px 8px;
    overflow:visible;
  }

  a.icon-btn, button.icon-btn{
    width:44px;
    height:44px;
    border-radius:999px;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    text-decoration:none;
    color: currentColor;

    box-sizing:border-box;
    border:1px solid var(--border-green);
    background: rgba(0,0,0,0.25);
    box-shadow: 0 0 0 1px rgba(57,255,20,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
    transition: transform 140ms ease, background 140ms ease, border-color 140ms ease, box-shadow 140ms ease;
    -webkit-tap-highlight-color: transparent;
    user-select:none;
    cursor:pointer;
    line-height:1;
    padding:0;
  }

  html[data-theme="orange"] a.icon-btn, html[data-theme="orange"] button.icon-btn{
    border-color: var(--border-orange);
    box-shadow: 0 0 0 1px rgba(255,122,24,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
  }
  html[data-theme="green"] a.icon-btn, html[data-theme="green"] button.icon-btn{
    border-color: var(--border-green);
    box-shadow: 0 0 0 1px rgba(57,255,20,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
  }
  html[data-theme="blue"] a.icon-btn, html[data-theme="blue"] button.icon-btn{
    border-color: var(--border-blue);
    box-shadow: 0 0 0 1px rgba(0,231,255,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
  }
  html[data-theme="pink"] a.icon-btn, html[data-theme="pink"] button.icon-btn{
    border-color: var(--border-pink);
    box-shadow: 0 0 0 1px rgba(255,43,214,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
  }

  a.icon-btn i, button.icon-btn i{
    font-size:18px;
    pointer-events:none;
  }

  a.icon-btn:hover, button.icon-btn:hover{
    transform: translateY(-1px);
    background: rgba(57,255,20,0.12);
    box-shadow: 0 0 12px rgba(57,255,20,0.18), 0 10px 18px rgba(0,0,0,0.45);
  }
  html[data-theme="orange"] a.icon-btn:hover, html[data-theme="orange"] button.icon-btn:hover{
    background: rgba(255,122,24,0.12);
    box-shadow: 0 0 12px rgba(255,122,24,0.18), 0 10px 18px rgba(0,0,0,0.45);
  }
  html[data-theme="blue"] a.icon-btn:hover, html[data-theme="blue"] button.icon-btn:hover{
    background: rgba(0,231,255,0.12);
    box-shadow: 0 0 12px rgba(0,231,255,0.18), 0 10px 18px rgba(0,0,0,0.45);
  }
  html[data-theme="pink"] a.icon-btn:hover, html[data-theme="pink"] button.icon-btn:hover{
    background: rgba(255,43,214,0.12);
    box-shadow: 0 0 12px rgba(255,43,214,0.18), 0 10px 18px rgba(0,0,0,0.45);
  }

  a.email-btn{ position:relative; }
  a.email-btn i{
    position:absolute;
    inset:0;
    display:flex;
    align-items:center;
    justify-content:center;
    pointer-events:none;
  }
  a.email-btn .email-open{ opacity:0; }
  a.email-btn .email-closed{ opacity:1; }
  a.email-btn:hover .email-open{ opacity:1; }
  a.email-btn:hover .email-closed{ opacity:0; }

  .tagline{
    margin-top:10px;
    margin-bottom:0;
    font-size: clamp(1.00rem, 1.45vw, 1.18rem);
    font-weight:650;
    opacity:0.95;
    overflow-wrap:anywhere;
  }

  @media (max-width: 640px){
    body{ padding: 12px 10px 14px 10px; }
    .row1{ grid-template-columns: 1fr; gap:8px; }
    .text-col{ padding:0; }
    .terminal-title{ font-size:1.10rem; line-height:1.25; padding-top:0; }
    .icon-row{ justify-content:flex-start; gap:8px; padding: 0 0 12px 0; }
    a.icon-btn, button.icon-btn{ width:38px; height:38px; }
    a.icon-btn i, button.icon-btn i{ font-size:16px; }
    .tagline{ font-size:1.02rem; line-height:1.25; margin-top:6px; }
  }
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
        <div class="tagline">__TAGLINE__</div>
      </div>

      <div class="icon-row">
        <button class="icon-btn" id="themeToggle" type="button" title="Toggle theme (Green → Blue → Pink → Orange)">
          <i class="fa-solid fa-palette"></i>
        </button>

        <a class="icon-btn" href="__PORTFOLIO__" target="_blank" rel="noopener" title="Portfolio"><i class="fa-solid fa-globe"></i></a>
        <a class="icon-btn" href="__GITHUB__" target="_blank" rel="noopener" title="GitHub"><i class="fa-brands fa-github"></i></a>
        <a class="icon-btn" href="__LINKEDIN__" target="_blank" rel="noopener" title="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>

        <a class="icon-btn email-btn" href="mailto:__EMAIL__" title="Email">
          <i class="fa-solid fa-envelope email-closed"></i>
          <i class="fa-solid fa-envelope-open email-open"></i>
        </a>

        <a class="icon-btn" href="https://www.nwu.ac.za/" target="_blank" rel="noopener" title="North-West University"><i class="fa-solid fa-building-columns"></i></a>
      </div>
    </div>
  </div>

<script>
(function () {
  const themes = ["green", "blue", "pink", "orange"];
  const STORAGE_KEY = "bs_theme";

  const emojiMap = {
    orange: "🌞",
    blue: "🌚",
    green: "👽",
    pink: "🛸"
  };

  const BASE_PREFIX = __STATIC_PREFIX__;
  const WORDS = __ROTATING__;

  function safeGetSavedTheme() {
    try {
      const t = localStorage.getItem(STORAGE_KEY);
      if (t && themes.includes(t)) return t;
    } catch(e) {}
    // try parent attribute (if present)
    try {
      const t2 = (window.parent && window.parent.document)
        ? window.parent.document.documentElement.getAttribute("data-theme")
        : null;
      if (t2 && themes.includes(t2)) return t2;
    } catch(e) {}
    return "green";
  }

  function setTheme(theme) {
    const t = themes.includes(theme) ? theme : "green";
    try { localStorage.setItem(STORAGE_KEY, t); } catch(e) {}

    // apply inside this iframe
    document.documentElement.setAttribute("data-theme", t);

    // update the greeting emoji
    const em = emojiMap[t] || "👽";
    const prefixEl = document.getElementById("prefix");
    const patched = BASE_PREFIX.replace(/^Hi,/, "Hi" + em + ",");
    prefixEl.textContent = patched;

    // ✅ tell parent (bridge will apply + broadcast to all iframes)
    try { window.parent.postMessage({ type:"bs_theme", theme:t }, "*"); } catch(e) {}
  }

  // ✅ initial
  setTheme(safeGetSavedTheme());

  // ✅ receive broadcasts (when other iframes change theme)
  window.addEventListener("message", (ev) => {
    try {
      const d = ev && ev.data;
      if (d && d.type === "bs_theme" && themes.includes(d.theme)) {
        document.documentElement.setAttribute("data-theme", d.theme);
        const em = emojiMap[d.theme] || "👽";
        const prefixEl = document.getElementById("prefix");
        const patched = BASE_PREFIX.replace(/^Hi,/, "Hi" + em + ",");
        prefixEl.textContent = patched;
      }
    } catch(e) {}
  });

  // request current theme once (if bridge is already installed)
  try { window.parent.postMessage({ type:"bs_theme_get" }, "*"); } catch(e) {}

  document.getElementById("themeToggle").addEventListener("click", function () {
    const cur = safeGetSavedTheme();
    const i = themes.indexOf(cur);
    const next = themes[(i + 1 + themes.length) % themes.length];
    setTheme(next);
  });

  const wordEl = document.getElementById("word");
  let idx = 0, char = 0, deleting = false;
  const typeSpeed = 45, deleteSpeed = 25, holdFull = 900, holdEmpty = 260;

  function step() {
    const glyphs = Array.from(WORDS[idx]);
    if (!deleting) {
      char++;
      wordEl.textContent = glyphs.slice(0, char).join("");
      if (char >= glyphs.length) {
        setTimeout(() => { deleting = true; step(); }, holdFull);
        return;
      }
      setTimeout(step, typeSpeed);
    } else {
      char--;
      wordEl.textContent = glyphs.slice(0, Math.max(0, char)).join("");
      if (char <= 0) {
        deleting = false;
        idx = (idx + 1) % WORDS.length;
        setTimeout(step, holdEmpty);
        return;
      }
      setTimeout(step, deleteSpeed);
    }
  }
  wordEl.textContent = "";
  step();

  // keep iframe height correct
  const wrap = document.getElementById("wrap");
  function getHeight() {
    const b = wrap.getBoundingClientRect().height;
    const sh = wrap.scrollHeight;
    return Math.ceil(Math.max(b, sh));
  }
  let raf = null;
  let lastH = 0;
  function resizeFrame() {
    if (raf) cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      try {
        const h = Math.min(340, Math.max(70, getHeight() + 14));
        if (Math.abs(h - lastH) > 1 && window.frameElement) {
          lastH = h;
          window.frameElement.style.height = h + "px";
        }
      } catch (e) {}
    });
  }
  window.addEventListener("load", () => resizeFrame());
  window.addEventListener("resize", () => setTimeout(resizeFrame, 60));
  new MutationObserver(() => resizeFrame()).observe(wrap, { childList: true, subtree: true, characterData: true });
})();
</script>
</body>
</html>
"""

topbar_html = (
    TOPBAR_TEMPLATE
    .replace("__TAGLINE__", TAGLINE)
    .replace("__PORTFOLIO__", PORTFOLIO_URL)
    .replace("__GITHUB__", GITHUB_URL)
    .replace("__LINKEDIN__", LINKEDIN_URL)
    .replace("__EMAIL__", EMAIL)
    .replace("__STATIC_PREFIX__", json.dumps(STATIC_PREFIX, ensure_ascii=False))
    .replace("__ROTATING__", json.dumps(ROTATING, ensure_ascii=False))
)

components.html(topbar_html, height=93)
st.divider()

# -----------------------------
# Data helpers
# -----------------------------
@st.cache_data(show_spinner=False)
def read_spectrum_csv(folder: str) -> pd.DataFrame:
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


def downsample_xy(x: np.ndarray, y: np.ndarray, max_points: int = 3500):
    n = int(len(x))
    if n <= max_points:
        return x, y
    idx = np.linspace(0, n - 1, num=max_points, dtype=int)
    return x[idx], y[idx]


def smart_yrange(y: np.ndarray) -> tuple[float, float]:
    yy = np.asarray(y, dtype=float)
    yy = yy[np.isfinite(yy)]
    if yy.size < 3:
        return (0.0, 1.0)

    lo, hi = np.percentile(yy, [1.0, 99.0])
    if not np.isfinite(lo) or not np.isfinite(hi) or lo == hi:
        lo, hi = float(np.min(yy)), float(np.max(yy))
        if lo == hi:
            lo -= 1.0
            hi += 1.0

    span = hi - lo
    pad = 0.08 * span if span > 0 else 0.5
    return float(lo - pad), float(hi + pad)


# -----------------------------
# Plotly spectrum template (UPDATED: listens to bs_theme postMessage)
# -----------------------------
SPECTRUM_TEMPLATE = r"""
<div id="__DIV__" style="width:100%;"></div>
<script src="https://cdn.plot.ly/plotly-2.30.0.min.js"></script>
<script>
(function() {
  const P = __PAYLOAD__;
  const el = document.getElementById(P.div_id);
  const STORAGE_KEY = "bs_theme";
  const THEMES = ["green","blue","pink","orange"];

  function themeToRgb(t){
    switch(t){
      case "orange": return [255,122,24];
      case "blue":   return [0,231,255];
      case "pink":   return [255,43,214];
      default:       return [57,255,20];
    }
  }
  function rgba(rgb, a){ return `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, ${a})`; }

  function getTheme(){
    try {
      const t = localStorage.getItem(STORAGE_KEY);
      if (t && THEMES.includes(t)) return t;
    } catch(e) {}
    const t2 = document.documentElement.getAttribute("data-theme");
    if (t2 && THEMES.includes(t2)) return t2;
    return "green";
  }

  function colorsForTheme(theme){
    const rgb = themeToRgb(theme);
    return {
      line: rgba(rgb, 0.95),
      font: rgba(rgb, 0.95),
      grid: rgba(rgb, 0.14),
      axis: rgba(rgb, 0.28)
    };
  }

  function isMobile(w){ return w <= 640; }

  function getContainerWidth(){
    try {
      const r = el.getBoundingClientRect();
      const w = Math.max(0, r.width || 0);
      if (w > 0) return w;
    } catch(e) {}
    return Math.max(320, Math.min(980, window.innerWidth || 420));
  }

  function computeHeight(w){
    const m = isMobile(w);
    const h = m ? Math.round(Math.max(320, Math.min(520, w * 0.82 + 90))) : 440;
    return h;
  }

  function makeLayout(colors, yRange, w){
    const m = isMobile(w);
    const h = computeHeight(w);

    return {
      title: {
        text: P.title,
        x: 0.02,
        xanchor: "left",
        font: { size: m ? 13 : 16 }
      },
      paper_bgcolor: "#050505",
      plot_bgcolor: "#050505",
      height: h,
      margin: m ? { l: 50, r: 14, t: 56, b: 48 } : { l: 60, r: 18, t: 58, b: 46 },
      font: {
        family: 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
        color: colors.font,
        size: m ? 11 : 13
      },
      showlegend: false,
      xaxis: {
        title: { text: "wavelength (Å)", font: { size: m ? 11 : 13 } },
        showgrid: true,
        gridcolor: colors.grid,
        zeroline: false,
        ticks: "outside",
        tickcolor: colors.axis,
        linecolor: colors.axis,
        mirror: true,
        tickfont: { size: m ? 10 : 12 },
        automargin: true
      },
      yaxis: {
        title: { text: "flux", standoff: m ? 6 : 12, font: { size: m ? 11 : 13 } },
        automargin: true,
        range: yRange,
        showgrid: true,
        gridcolor: colors.grid,
        zeroline: false,
        ticks: "outside",
        tickcolor: colors.axis,
        linecolor: colors.axis,
        mirror: true,
        tickfont: { size: m ? 10 : 12 }
      }
    };
  }

  function setXY(xArr, yArr){
    Plotly.restyle(el, { x: [xArr], y: [yArr] }, [0]);
  }

  function updateFrameHeight(){
    try {
      const w = getContainerWidth();
      const h = computeHeight(w) + 18;
      if (window.frameElement) window.frameElement.style.height = h + "px";
    } catch(e) {}
  }

  function restyleToTheme(){
    const w = getContainerWidth();
    const colors = colorsForTheme(getTheme());
    Plotly.restyle(el, { "line.color": [colors.line] }, [0]);
    const cur = (el.layout && el.layout.yaxis && el.layout.yaxis.range) ? el.layout.yaxis.range : P.y_range_new;
    Plotly.relayout(el, makeLayout(colors, cur, w));
    try { Plotly.Plots.resize(el); } catch(e) {}
    updateFrameHeight();
  }

  function wipeLeftToRight(xFull, yFull, durationMs){
    return new Promise((resolve) => {
      const N = xFull.length;
      if (N < 3) { setXY([], []); resolve(); return; }
      const t0 = performance.now();

      function step(now){
        const t = Math.min(1, (now - t0) / durationMs);
        const start = Math.floor(t * (N - 1));
        setXY(xFull.slice(start), yFull.slice(start));
        if (t < 1) requestAnimationFrame(step);
        else { setXY([], []); resolve(); }
      }
      requestAnimationFrame(step);
    });
  }

  function revealLeftToRight(xFull, yFull, durationMs){
    return new Promise((resolve) => {
      const N = xFull.length;
      if (N < 3) { setXY(xFull, yFull); resolve(); return; }
      const t0 = performance.now();

      function step(now){
        const t = Math.min(1, (now - t0) / durationMs);
        const end = Math.max(2, Math.floor(2 + t * (N - 2)));
        setXY(xFull.slice(0, end), yFull.slice(0, end));
        if (t < 1) requestAnimationFrame(step);
        else { setXY(xFull, yFull); resolve(); }
      }
      requestAnimationFrame(step);
    });
  }

  async function runSequence(){
    const hasOld = Array.isArray(P.x_old) && P.x_old.length > 0;

    const WIPE_MS = 1150;
    const REVEAL_MS = 2700;
    const PAUSE_MS = 170;

    if (hasOld){
      await wipeLeftToRight(P.x_old, P.y_old, WIPE_MS);
      await new Promise(r => setTimeout(r, PAUSE_MS));

      const w = getContainerWidth();
      const colors = colorsForTheme(getTheme());
      Plotly.relayout(el, makeLayout(colors, P.y_range_new, w));
      updateFrameHeight();

      await new Promise(r => setTimeout(r, 70));
      await revealLeftToRight(P.x_new, P.y_new, REVEAL_MS);
      updateFrameHeight();
    } else {
      const w = getContainerWidth();
      const colors = colorsForTheme(getTheme());
      Plotly.relayout(el, makeLayout(colors, P.y_range_new, w));
      setXY([], []);
      updateFrameHeight();
      await revealLeftToRight(P.x_new, P.y_new, REVEAL_MS);
      updateFrameHeight();
    }
  }

  (function render(){
    const w = getContainerWidth();
    const colors = colorsForTheme(getTheme());
    const hasOld = Array.isArray(P.x_old) && P.x_old.length > 0;

    const initX = hasOld ? P.x_old : [];
    const initY = hasOld ? P.y_old : [];

    const trace = {
      type: "scatter",
      mode: "lines",
      x: initX,
      y: initY,
      line: { width: isMobile(w) ? 2.0 : 2.4, color: colors.line },
      hovertemplate: "λ=%{x:.1f} Å<br>flux=%{y:.4f}<extra></extra>"
    };

    const yStart = hasOld ? P.y_range_old : P.y_range_new;

    Plotly.newPlot(
      el,
      [trace],
      makeLayout(colors, yStart, w),
      { displayModeBar: false, responsive: true }
    ).then(() => {
      updateFrameHeight();
      runSequence().then(() => updateFrameHeight());
    });
  })();

  // ✅ now supports parent broadcasts
  window.addEventListener("message", (ev) => {
    try {
      const d = ev && ev.data;
      if (d && d.type === "bs_theme" && THEMES.includes(d.theme)) {
        document.documentElement.setAttribute("data-theme", d.theme);
        restyleToTheme();
      }
    } catch(e) {}
  });

  window.addEventListener("storage", (ev) => {
    if (ev && ev.key === STORAGE_KEY) restyleToTheme();
  });

  new MutationObserver(() => restyleToTheme())
    .observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });

  const ro = new ResizeObserver(() => restyleToTheme());
  try { ro.observe(el); } catch(e) {}
  window.addEventListener("resize", () => setTimeout(restyleToTheme, 50));

})();
</script>
"""


def spectrum_plot_html(
    x_new,
    y_new,
    title: str,
    div_id: str,
    x_old=None,
    y_old=None,
    y_range_new=(0.0, 1.0),
    y_range_old=(0.0, 1.0),
) -> str:
    payload = {
        "div_id": div_id,
        "title": title,
        "x_new": [float(v) for v in x_new],
        "y_new": [float(v) for v in y_new],
        "x_old": [float(v) for v in (x_old if x_old is not None else [])],
        "y_old": [float(v) for v in (y_old if y_old is not None else [])],
        "y_range_new": [float(y_range_new[0]), float(y_range_new[1])],
        "y_range_old": [float(y_range_old[0]), float(y_range_old[1])],
    }
    return (
        SPECTRUM_TEMPLATE
        .replace("__DIV__", div_id)
        .replace("__PAYLOAD__", json.dumps(payload))
    )


# -----------------------------
# Confusion matrix template (UPDATED: listens to bs_theme postMessage)
# -----------------------------
CM_TEMPLATE = r"""
<div class="cm-wrap" id="__WRAP__">
  <div id="__DIV__" style="width:100%;"></div>
</div>

<script src="https://cdn.plot.ly/plotly-2.30.0.min.js"></script>
<script>
(function() {
  const P = __PAYLOAD__;
  const wrap = document.getElementById(P.wrap_id);
  const el = document.getElementById(P.div_id);

  const STORAGE_KEY = "bs_theme";
  const THEMES = ["green","blue","pink","orange"];

  (function setupFade(){
    if (!wrap) return;

    wrap.style.opacity = "0";
    wrap.style.transform = "translateY(10px)";
    wrap.style.transition = "opacity 600ms ease, transform 600ms ease";
    wrap.style.willChange = "opacity, transform";

    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          wrap.style.opacity = "1";
          wrap.style.transform = "translateY(0px)";
          setTimeout(() => { try { Plotly.Plots.resize(el); } catch(_){} }, 80);
          io.unobserve(wrap);
        }
      });
    }, { threshold: 0.18 });

    io.observe(wrap);
  })();

  function themeToRgb(t){
    switch(t){
      case "orange": return [255,122,24];
      case "blue":   return [0,231,255];
      case "pink":   return [255,43,214];
      default:       return [57,255,20];
    }
  }
  function rgba(rgb, a){ return `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, ${a})`; }

  function getTheme(){
    try {
      const t = localStorage.getItem(STORAGE_KEY);
      if (t && THEMES.includes(t)) return t;
    } catch(e) {}
    const t2 = document.documentElement.getAttribute("data-theme");
    if (t2 && THEMES.includes(t2)) return t2;
    return "green";
  }

  function colorsForTheme(theme){
    const rgb = themeToRgb(theme);
    return {
      rgb,
      font: rgba(rgb, 0.95),
      axis: rgba(rgb, 0.35),
      black: "#050505"
    };
  }

  function makeColorscale(rgb){
    const c0 = "rgb(5,5,5)";
    const c1 = `rgba(${rgb[0]},${rgb[1]},${rgb[2]},0.30)`;
    const c2 = `rgba(${rgb[0]},${rgb[1]},${rgb[2]},0.60)`;
    const c3 = `rgba(${rgb[0]},${rgb[1]},${rgb[2]},0.92)`;
    return [
      [0.00, c0],
      [0.25, c1],
      [0.60, c2],
      [1.00, c3],
    ];
  }

  function getWidth(){
    try {
      const r = el.getBoundingClientRect();
      const w = Math.max(0, r.width || 0);
      if (w > 0) return w;
    } catch(e) {}
    return Math.max(320, Math.min(980, window.innerWidth || 420));
  }

  function isMobile(w){ return w <= 640; }

  function computeHeight(w){
    const m = isMobile(w);
    const h = m ? Math.round(Math.max(380, Math.min(760, w * 0.98 + 120))) : 560;
    return h;
  }

  function buildAnnotations(z, labels, fontColor, w){
    const m = isMobile(w);
    const anns = [];
    const fs = m ? 11 : 16;
    for (let i = 0; i < labels.length; i++){
      for (let j = 0; j < labels.length; j++){
        const v = z[i][j];
        const txt = (typeof v === "number") ? v.toFixed(2) : String(v);
        const col = (v >= 0.62) ? "#050505" : fontColor;
        anns.push({
          x: labels[j],
          y: labels[i],
          text: txt,
          showarrow: false,
          font: { color: col, size: fs, family: 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace' }
        });
      }
    }
    return anns;
  }

  function makeLayout(C, w){
    const m = isMobile(w);
    const h = computeHeight(w);
    return {
      title: {
        text: P.title,
        x: 0.02,
        xanchor: "left",
        font: { size: m ? 13 : 16 }
      },
      paper_bgcolor: C.black,
      plot_bgcolor: C.black,
      height: h,
      margin: m ? { l: 58, r: 12, t: 64, b: 74 } : { l: 70, r: 28, t: 64, b: 56 },
      font: {
        family: 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
        color: C.font,
        size: m ? 11 : 13
      },
      xaxis: {
        title: { text: "Predicted label", font: { size: m ? 11 : 13 } },
        type: "category",
        tickmode: "array",
        tickvals: P.labels,
        ticktext: P.labels,
        ticks: "outside",
        tickcolor: C.axis,
        linecolor: C.axis,
        mirror: true,
        showgrid: false,
        zeroline: false,
        tickfont: { size: m ? 10 : 12 },
        tickangle: m ? -45 : 0,
        automargin: true
      },
      yaxis: {
        title: { text: "True label", font: { size: m ? 11 : 13 } },
        type: "category",
        tickmode: "array",
        tickvals: P.labels,
        ticktext: P.labels,
        ticks: "outside",
        tickcolor: C.axis,
        linecolor: C.axis,
        mirror: true,
        autorange: "reversed",
        showgrid: false,
        zeroline: false,
        tickfont: { size: m ? 10 : 12 },
        automargin: true
      }
    };
  }

  function makeTrace(C, w){
    const m = isMobile(w);
    return {
      type: "heatmap",
      z: P.z,
      x: P.labels,
      y: P.labels,
      zmin: 0,
      zmax: 1,
      colorscale: makeColorscale(C.rgb),
      hovertemplate: "True=%{y}<br>Pred=%{x}<br>Value=%{z:.2f}<extra></extra>",
      colorbar: {
        thickness: m ? 10 : 12,
        len: m ? 0.86 : 0.92,
        outlinewidth: 0,
        tickfont: { color: C.font, size: m ? 10 : 12 },
        title: { text: "", font: { color: C.font } }
      }
    };
  }

  function updateFrameHeight(){
    try {
      const w = getWidth();
      const h = computeHeight(w) + 18;
      if (window.frameElement) window.frameElement.style.height = h + "px";
    } catch(e) {}
  }

  function render(){
    const w = getWidth();
    const C = colorsForTheme(getTheme());
    const layout = makeLayout(C, w);
    layout.annotations = buildAnnotations(P.z, P.labels, C.font, w);

    Plotly.newPlot(
      el,
      [makeTrace(C, w)],
      layout,
      { displayModeBar: false, responsive: true }
    ).then(() => {
      try {
        el.style.opacity = "0";
        el.style.transform = "scale(0.996)";
        el.style.transition = "opacity 380ms ease, transform 380ms ease";
        requestAnimationFrame(() => {
          el.style.opacity = "1";
          el.style.transform = "scale(1)";
        });
      } catch(_) {}
      updateFrameHeight();
      try { Plotly.Plots.resize(el); } catch(_) {}
      updateFrameHeight();
    });
  }

  function restyleToTheme(){
    const w = getWidth();
    const C = colorsForTheme(getTheme());
    const layout = makeLayout(C, w);
    layout.annotations = buildAnnotations(P.z, P.labels, C.font, w);

    Plotly.restyle(el, { colorscale: [makeColorscale(C.rgb)] }, [0]);
    Plotly.relayout(el, layout);
    try { Plotly.Plots.resize(el); } catch(_) {}
    updateFrameHeight();
  }

  render();

  // ✅ now supports parent broadcasts
  window.addEventListener("message", (ev) => {
    try {
      const d = ev && ev.data;
      if (d && d.type === "bs_theme" && THEMES.includes(d.theme)) {
        document.documentElement.setAttribute("data-theme", d.theme);
        restyleToTheme();
      }
    } catch(e) {}
  });

  window.addEventListener("storage", (ev) => {
    if (ev && ev.key === STORAGE_KEY) restyleToTheme();
  });

  new MutationObserver(() => restyleToTheme())
    .observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });

  const ro = new ResizeObserver(() => restyleToTheme());
  try { ro.observe(el); } catch(e) {}
  window.addEventListener("resize", () => setTimeout(restyleToTheme, 50));

})();
</script>
"""


def confusion_matrix_plot_html(
    z: np.ndarray,
    labels: list[str],
    title: str,
    div_id: str,
    wrap_id: str,
) -> str:
    z_list = [[float(v) for v in row] for row in np.asarray(z, dtype=float)]
    payload = {
        "div_id": div_id,
        "wrap_id": wrap_id,
        "title": title,
        "labels": labels,
        "z": z_list,
    }
    return (
        CM_TEMPLATE
        .replace("__DIV__", div_id)
        .replace("__WRAP__", wrap_id)
        .replace("__PAYLOAD__", json.dumps(payload))
    )


# -----------------------------
# ✅ EmailJS contact form (UPDATED: can send multiple times reliably + timeout + theme broadcasts)
# -----------------------------
EMAILJS_CONTACT_TEMPLATE = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<style>
  :root{
    --bg:#050505;
    --panel: rgba(0,0,0,0.35);

    --accent: rgba(57,255,20,0.95);
    --border: rgba(57,255,20,0.45);
    --placeholder: rgba(57,255,20,0.65);
    --hover: rgba(57,255,20,0.08);
    --chip: rgba(57,255,20,0.10);
    --chipBorder: rgba(57,255,20,0.32);
  }

  html, body{
    margin:0;
    padding:0;
    background: transparent;
    color: var(--accent);
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  }
  *{ box-sizing:border-box; }

  .outer{ width:100%; padding: 6px 0 2px 0; }

  .panel{
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 14px 14px 12px 14px;
    box-shadow: none;
  }

  .hdr{
    display:flex;
    align-items:flex-start;
    justify-content:space-between;
    gap: 10px;
    margin-bottom: 10px;
  }

  .title{
    margin:0;
    font-size: 14px;
    font-weight: 800;
    line-height: 1.15;
  }

  .hint{
    font-size: 11px;
    opacity: 0.82;
    padding-top: 2px;
    white-space:nowrap;
    user-select:none;
  }

  .grid{
    display:grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  .field{ position:relative; width:100%; }
  .full{ grid-column: 1 / -1; }

  input, textarea{
    width:100%;
    background: var(--bg);
    color: var(--accent);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 12px 14px;
    outline: none;
    box-shadow: none;
    font-size: 14px;
    line-height: 1.25;
    appearance: none;
    -webkit-appearance: none;
    background-clip: padding-box;
  }

  textarea{ min-height: 160px; resize: vertical; }

  input::placeholder, textarea::placeholder{ color: var(--placeholder); }

  input:-webkit-autofill,
  input:-webkit-autofill:hover,
  input:-webkit-autofill:focus{
    -webkit-box-shadow: 0 0 0 1000px var(--bg) inset !important;
    -webkit-text-fill-color: var(--accent) !important;
    caret-color: var(--accent) !important;
    border: 1px solid var(--border) !important;
  }

  .field:has(input:placeholder-shown):not(:focus-within)::after{
    content: "Field empty!";
    position:absolute;
    right: 14px;
    bottom: 10px;
    font-size: 12px;
    opacity: 0.75;
    line-height: 1;
    pointer-events:none;
    color: var(--accent);
  }
  .field:has(textarea:placeholder-shown):not(:focus-within)::after{
    content: "Field empty!";
    position:absolute;
    right: 14px;
    bottom: 12px;
    font-size: 12px;
    opacity: 0.75;
    line-height: 1;
    pointer-events:none;
    color: var(--accent);
  }

  .btn-row{
    display:flex;
    gap: 10px;
    align-items:center;
    justify-content:space-between;
    margin-top: 12px;
    flex-wrap: wrap;
  }

  .btn{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    gap: 8px;

    border: 1px solid var(--border);
    background: var(--bg);
    color: var(--accent);
    border-radius: 14px;
    padding: 0.55rem 0.95rem;
    cursor:pointer;
    box-shadow:none;
    outline:none;
    font-size: 14px;
    user-select:none;
    transition: transform 140ms ease, background 140ms ease;
    white-space:nowrap;
  }

  .btn:hover{
    background: var(--hover);
    transform: translateY(-1px);
  }

  .btn[disabled]{
    opacity: 0.55;
    cursor: not-allowed;
    transform: none !important;
  }

  .status{
    min-height: 18px;
    font-size: 12px;
    opacity: 0.92;
    display:flex;
    align-items:center;
    justify-content:flex-end;
    gap: 8px;
    flex: 1 1 auto;
  }

  .pill{
    display:inline-flex;
    align-items:center;
    gap: 8px;
    padding: 6px 10px;
    border-radius: 999px;
    border: 1px solid var(--chipBorder);
    background: var(--chip);
    line-height: 1;
  }

  .pill small{ font-size: 11px; opacity: 0.95; }

  @media (max-width: 640px){
    .grid{ grid-template-columns: 1fr; gap: 10px; }
    .hint{ display:none; }
    .btn-row{ flex-direction: column; align-items: stretch; }
    .btn{ width:100%; }
    .status{ justify-content:flex-start; width:100%; }
  }
</style>
</head>
<body>
  <div class="outer">
    <div class="panel">
      <div class="hdr">
        <p class="title">Send me a message</p>
        <div class="hint" aria-hidden="true">Secure via EmailJS</div>
      </div>

      <div class="grid">
        <div class="field">
          <input id="from_name" type="text" placeholder="Your name" autocomplete="name" />
        </div>
        <div class="field">
          <input id="reply_to" type="email" placeholder="Your email" autocomplete="email" />
        </div>
        <div class="field full">
          <input id="subject" type="text" placeholder="What is this about?" />
        </div>
        <div class="field full">
          <textarea id="message" placeholder="Type your message here..."></textarea>
        </div>
      </div>

      <div class="btn-row">
        <button class="btn" id="sendBtn" type="button" disabled>
          <span aria-hidden="true">➤</span>
          <span>Send message</span>
        </button>

        <div class="status" id="statusWrap">
          <span class="pill" id="statusPill" style="display:none;">
            <span id="statusIcon" aria-hidden="true">…</span>
            <small id="statusText">…</small>
          </span>
        </div>
      </div>
    </div>
  </div>

<script>
(function(){
  const PUBLIC_KEY = __PUBLIC_KEY__;
  const SERVICE_ID = __SERVICE_ID__;
  const TEMPLATE_ID = __TEMPLATE_ID__;
  const TO_EMAIL = __TO_EMAIL__;

  const STORAGE_KEY = "bs_theme";
  const THEMES = ["green","blue","pink","orange"];

  let inFlight = false;
  let hideTimer = null;

  function themeVars(t){
    switch(t){
      case "orange":
        return { accent:"rgba(255,122,24,0.95)", border:"rgba(255,122,24,0.45)", ph:"rgba(255,122,24,0.65)", hover:"rgba(255,122,24,0.08)", chip:"rgba(255,122,24,0.10)", chipB:"rgba(255,122,24,0.32)" };
      case "blue":
        return { accent:"rgba(0,231,255,0.95)", border:"rgba(0,231,255,0.45)", ph:"rgba(0,231,255,0.65)", hover:"rgba(0,231,255,0.08)", chip:"rgba(0,231,255,0.10)", chipB:"rgba(0,231,255,0.32)" };
      case "pink":
        return { accent:"rgba(255,43,214,0.95)", border:"rgba(255,43,214,0.45)", ph:"rgba(255,43,214,0.65)", hover:"rgba(255,43,214,0.08)", chip:"rgba(255,43,214,0.10)", chipB:"rgba(255,43,214,0.32)" };
      default:
        return { accent:"rgba(57,255,20,0.95)", border:"rgba(57,255,20,0.45)", ph:"rgba(57,255,20,0.65)", hover:"rgba(57,255,20,0.08)", chip:"rgba(57,255,20,0.10)", chipB:"rgba(57,255,20,0.32)" };
    }
  }

  function getTheme(){
    try{
      const t = localStorage.getItem(STORAGE_KEY);
      if (t && THEMES.includes(t)) return t;
    }catch(e){}
    const t2 = document.documentElement.getAttribute("data-theme");
    if (t2 && THEMES.includes(t2)) return t2;
    return "green";
  }

  function applyTheme(){
    const t = getTheme();
    document.documentElement.setAttribute("data-theme", t);
    const V = themeVars(t);
    const root = document.documentElement.style;
    root.setProperty("--accent", V.accent);
    root.setProperty("--border", V.border);
    root.setProperty("--placeholder", V.ph);
    root.setProperty("--hover", V.hover);
    root.setProperty("--chip", V.chip);
    root.setProperty("--chipBorder", V.chipB);
  }

  function updateFrameHeight(){
    try{
      const h = Math.ceil(document.body.scrollHeight + 10);
      if (window.frameElement) window.frameElement.style.height = h + "px";
    }catch(e){}
  }

  applyTheme();
  updateFrameHeight();

  // ✅ accept parent broadcasts
  window.addEventListener("message", (ev) => {
    try {
      const d = ev && ev.data;
      if (d && d.type === "bs_theme" && THEMES.includes(d.theme)) {
        document.documentElement.setAttribute("data-theme", d.theme);
        applyTheme();
        setTimeout(updateFrameHeight, 60);
      }
    } catch(e) {}
  });

  // keep old support
  window.addEventListener("storage", (ev) => {
    if (ev && ev.key === STORAGE_KEY) { applyTheme(); setTimeout(updateFrameHeight, 60); }
  });

  function qs(id){ return document.getElementById(id); }
  const nameEl = qs("from_name");
  const replyEl = qs("reply_to");
  const subjEl = qs("subject");
  const msgEl  = qs("message");
  const btnEl  = qs("sendBtn");

  const pill = qs("statusPill");
  const icon = qs("statusIcon");
  const text = qs("statusText");

  function clearStatusSoon(ms){
    if (hideTimer) { clearTimeout(hideTimer); hideTimer = null; }
    hideTimer = setTimeout(() => setStatus("", ""), ms);
  }

  function setStatus(kind, msg){
    if (!msg){
      pill.style.display = "none";
      updateFrameHeight();
      return;
    }
    pill.style.display = "inline-flex";
    if (kind === "ok"){ icon.textContent = "✓"; }
    else if (kind === "err"){ icon.textContent = "✕"; }
    else { icon.textContent = "…"; }
    text.textContent = msg;
    updateFrameHeight();
  }

  function validEmail(v){
    const s = String(v || "").trim();
    if (!s) return false;
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s);
  }

  function isReady(){
    const n = (nameEl.value || "").trim();
    const r = (replyEl.value || "").trim();
    const s = (subjEl.value || "").trim();
    const m = (msgEl.value || "").trim();
    return Boolean(n && r && s && m && validEmail(r));
  }

  function setButtonState(){
    btnEl.disabled = inFlight || !isReady();
  }

  function clearStatusOnType(){
    // if user starts typing again after a send/fail, drop the pill quickly
    if (pill.style.display !== "none") setStatus("", "");
  }

  ["input","change","blur","keyup","focus"].forEach(evt => {
    nameEl.addEventListener(evt, () => { clearStatusOnType(); setButtonState(); });
    replyEl.addEventListener(evt, () => { clearStatusOnType(); setButtonState(); });
    subjEl.addEventListener(evt, () => { clearStatusOnType(); setButtonState(); });
    msgEl.addEventListener(evt,  () => { clearStatusOnType(); setButtonState(); });
  });

  // Enter to send (but keep Enter inside textarea as newline)
  [nameEl, replyEl, subjEl].forEach(el => {
    el.addEventListener("keydown", (e) => {
      if (e.key === "Enter"){
        e.preventDefault();
        if (!btnEl.disabled) send();
      }
    });
  });

  setButtonState();

  function ensureConfig(){
    return Boolean(PUBLIC_KEY && SERVICE_ID && TEMPLATE_ID);
  }

  function withTimeout(promise, ms){
    return Promise.race([
      promise,
      new Promise((_, rej) => setTimeout(() => rej(new Error("timeout")), ms))
    ]);
  }

  async function send(){
    if (inFlight) return;

    if (!ensureConfig()){
      setStatus("err", "EmailJS not configured.");
      clearStatusSoon(2600);
      return;
    }
    if (!isReady()){
      setStatus("err", "Please fill in all fields.");
      clearStatusSoon(2600);
      return;
    }

    inFlight = true;
    setButtonState();
    setStatus("", "Sending…");

    const params = {
      to_email: TO_EMAIL,
      from_name: (nameEl.value || "").trim(),
      reply_to: (replyEl.value || "").trim(),
      subject: (subjEl.value || "").trim(),
      message: (msgEl.value || "").trim()
    };

    try{
      emailjs.init({ publicKey: PUBLIC_KEY });

      // ✅ timeout prevents stuck “can’t send again”
      await withTimeout(emailjs.send(SERVICE_ID, TEMPLATE_ID, params), 12000);

      setStatus("ok", "Sent.");

      // clear fields
      nameEl.value = "";
      replyEl.value = "";
      subjEl.value = "";
      msgEl.value = "";

      clearStatusSoon(2200);

      try { nameEl.focus(); } catch(e) {}
    }catch(e){
      setStatus("err", "Failed to send. Try again.");
      clearStatusSoon(2800);
    } finally {
      // ✅ ALWAYS release the lock
      inFlight = false;
      setButtonState();
    }
  }

  btnEl.addEventListener("click", send);

  window.addEventListener("resize", () => setTimeout(updateFrameHeight, 60));

  // request current theme once
  try { window.parent.postMessage({ type:"bs_theme_get" }, "*"); } catch(e) {}
})();
</script>
</body>
</html>
"""


def emailjs_contact_form_html(public_key: str, service_id: str, template_id: str, to_email: str) -> str:
    return (
        EMAILJS_CONTACT_TEMPLATE
        .replace("__PUBLIC_KEY__", json.dumps(public_key or ""))
        .replace("__SERVICE_ID__", json.dumps(service_id or ""))
        .replace("__TEMPLATE_ID__", json.dumps(template_id or ""))
        .replace("__TO_EMAIL__", json.dumps(to_email or ""))
    )


# -----------------------------
# Layout
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

    st.markdown("## Education")
    st.markdown(
        """
- **MSc Computer Science** — NWU *(2025–2026)*
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
- **UI / Apps:** Tkinter
- **Dev tools:** Visual Studio Code, Jupyter Notebooks, PyCharm
- **Environments:** Conda, Windows Subsystem for Linux (WSL)
        """.strip()
    )

    st.markdown("## Hobby project: Star classification")
    st.write(
        """
The goal of this project was to classify stars from their spectra using the Morgan–Keenan (MK) spectral classification scheme, which defines seven primary spectral classes: **O, B, A, F, G, K, and M** (ordered from **hottest to coolest**).

Spectral data were collected from **SDSS** using a custom Python pipeline built with **Astropy**, resulting in a dataset of **10,955** stellar spectra.
        """.strip()
    )

    spec_class = st.selectbox(
        "Spectral class",
        options=list("OBAFGKM"),
        index=list("OBAFGKM").index("A"),
        label_visibility="collapsed",
        key="spec_class_select",
    )
    st.caption(f"$ spectrum viewer — MK class **{spec_class}**")

    if "prev_spec_class" not in st.session_state:
        st.session_state.prev_spec_class = spec_class
        st.session_state.prev_x = None
        st.session_state.prev_y = None
        st.session_state.prev_yrange = (0.0, 1.0)

    changed = spec_class != st.session_state.prev_spec_class

    data_root = "data"
    class_dir = os.path.join(data_root, spec_class)

    try:
        df_spec = read_spectrum_csv(class_dir)
    except Exception as e:
        st.error(f"Could not load spectrum for class '{spec_class}' from '{class_dir}': {e}")
        df_spec = None

    if df_spec is not None:
        x = df_spec["wavelength_A"].to_numpy(dtype=float)
        y = df_spec["flux"].to_numpy(dtype=float)
        x, y = downsample_xy(x, y, max_points=3500)

        y_range_new = smart_yrange(y)

        x_old = st.session_state.prev_x if changed else None
        y_old = st.session_state.prev_y if changed else None
        y_range_old = st.session_state.prev_yrange if changed else y_range_new

        title = f"$ MK spectral class {spec_class} — spectrum"
        div_id = "spectrum_plot_main"

        components.html(
            spectrum_plot_html(
                x_new=x,
                y_new=y,
                x_old=x_old,
                y_old=y_old,
                title=title,
                div_id=div_id,
                y_range_new=y_range_new,
                y_range_old=y_range_old,
            ),
            height=560,
            scrolling=False,
        )

        st.session_state.prev_spec_class = spec_class
        st.session_state.prev_x = x
        st.session_state.prev_y = y
        st.session_state.prev_yrange = y_range_new

    st.markdown("## Hobby project: Metrics")
    st.markdown("#### 1D-Transformer")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Accuracy", "90.33%")
    m2.metric("Precision", "90.36%")
    m3.metric("Recall", "90.33%")
    m4.metric("F1-score", "90.12%")
    st.markdown("#### 2D-Transformer")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Accuracy", "83.94%")
    m2.metric("Precision", "85.13%")
    m3.metric("Recall", "83.94%")
    m4.metric("F1-score", "83.28%")

    st.markdown("## Hobby project: Confusion matrices")
    cm_labels = list("OBAFGKM")

    cm_1d = np.array([
        [0.85, 0.12, 0.00, 0.00, 0.00, 0.00, 0.04],
        [0.02, 0.91, 0.04, 0.00, 0.00, 0.02, 0.02],
        [0.00, 0.00, 0.99, 0.01, 0.00, 0.00, 0.00],
        [0.00, 0.01, 0.04, 0.72, 0.18, 0.05, 0.00],
        [0.01, 0.00, 0.00, 0.08, 0.88, 0.03, 0.00],
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.97, 0.03],
        [0.00, 0.01, 0.00, 0.00, 0.01, 0.00, 0.98],
    ], dtype=float)

    cm_2d = np.array([
        [0.85, 0.12, 0.00, 0.00, 0.00, 0.00, 0.04],
        [0.08, 0.91, 0.00, 0.02, 0.00, 0.00, 0.00],
        [0.00, 0.09, 0.87, 0.04, 0.00, 0.00, 0.00],
        [0.00, 0.02, 0.07, 0.49, 0.34, 0.07, 0.00],
        [0.00, 0.02, 0.00, 0.02, 0.94, 0.01, 0.00],
        [0.00, 0.00, 0.00, 0.01, 0.02, 0.93, 0.04],
        [0.00, 0.01, 0.00, 0.00, 0.01, 0.03, 0.94],
    ], dtype=float)

    st.markdown("#### 1D-Transformer")
    components.html(
        confusion_matrix_plot_html(
            z=cm_1d,
            labels=cm_labels,
            title="Confusion Matrix (Test) — Normalized (1D-Transformer)",
            div_id="cm_plot_1d",
            wrap_id="cm_wrap_1d",
        ),
        height=740,
        scrolling=False,
    )

    st.markdown("#### 2D-Transformer")
    components.html(
        confusion_matrix_plot_html(
            z=cm_2d,
            labels=cm_labels,
            title="Confusion Matrix (Test) — Normalized (2D-Transformer)",
            div_id="cm_plot_2d",
            wrap_id="cm_wrap_2d",
        ),
        height=740,
        scrolling=False,
    )

    st.divider()

    st.markdown("## Contact")
    st.write("Send me a message directly from this page:")

    components.html(
        emailjs_contact_form_html(
            public_key=EMAILJS_PUBLIC_KEY,
            service_id=EMAILJS_SERVICE_ID,
            template_id=EMAILJS_TEMPLATE_ID,
            to_email=EMAIL,
        ),
        height=420,
        scrolling=False,
    )

    if False:
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
