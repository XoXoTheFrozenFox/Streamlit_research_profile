from urllib.parse import quote
import os
import glob
import json

import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Bernard Swanepoel — Research Profile",
    page_icon="👽",
    layout="wide",
)

# ============================================================
# LINKS / INFO
# ============================================================
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


# ============================================================
# GLOBAL CSS (theme handled by html[data-theme] OR fallback green)
# ============================================================
st.markdown(
    """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

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

/* DEFAULT = GREEN */
html, body, [data-testid="stAppViewContainer"]{
  background: var(--bg) !important;
  color: var(--green) !important;
}
*{ color: var(--green) !important; }

.block-container{
  padding-top: 0.55rem !important;
  padding-bottom: 1.25rem !important;
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

/* inputs */
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

/* buttons */
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

/* SELECTBOX: keep it compact */
div[data-testid="stSelectbox"]{ width: 120px !important; max-width: 120px !important; }
div[data-testid="stSelectbox"] label{ display:none !important; }

/* CHECKBOX: force black bg + theme border */
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

/* ORANGE */
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
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# TOPBAR (stores theme in localStorage so plots can sync reliably)
# ============================================================
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
    return "green";
  }

  function setFaviconEmoji(em) {
    const svg =
      '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64">' +
      '<text y="50" x="6" font-size="52">' + em + '</text>' +
      '</svg>';
    const url = "data:image/svg+xml," + encodeURIComponent(svg);

    function apply(doc) {
      if (!doc) return;
      let link = doc.querySelector("link[rel*='icon']");
      if (!link) {
        link = doc.createElement("link");
        link.rel = "icon";
        doc.head.appendChild(link);
      }
      link.href = url;
    }

    apply(document);
    try { apply(window.parent.document); } catch(e) {}
  }

  function setTheme(theme) {
    const t = themes.includes(theme) ? theme : "green";

    // Save theme so other iframes (plots) can sync
    try { localStorage.setItem(STORAGE_KEY, t); } catch(e) {}

    // Set on this doc
    document.documentElement.setAttribute("data-theme", t);

    // Best effort: set on parent doc for your CSS
    try {
      if (window.parent && window.parent.document) {
        window.parent.document.documentElement.setAttribute("data-theme", t);
      }
    } catch (e) {}

    // Emoji + favicon
    const em = emojiMap[t] || "👽";
    setFaviconEmoji(em);

    // Prefix emoji injection: "Hi{emoji}, ..."
    const prefixEl = document.getElementById("prefix");
    const patched = BASE_PREFIX.replace(/^Hi,/, "Hi" + em + ",");
    prefixEl.textContent = patched;
  }

  // initial
  setTheme(safeGetSavedTheme());

  document.getElementById("themeToggle").addEventListener("click", function () {
    const cur = safeGetSavedTheme();
    const i = themes.indexOf(cur);
    const next = themes[(i + 1 + themes.length) % themes.length];
    setTheme(next);
  });

  // rotating typing (emoji-safe)
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

  // height fit
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


# ============================================================
# MAILTO BUILDER
# ============================================================
def build_mailto(to_email: str, subject: str, body: str) -> str:
    return f"mailto:{to_email}?subject={quote(subject)}&body={quote(body)}"


# ============================================================
# SPECTRUM HELPERS
# ============================================================
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


def downsample_xy(x: np.ndarray, y: np.ndarray, max_points: int = 4000):
    """Stable downsample to prevent Plotly freezes / artifacts."""
    n = int(len(x))
    if n <= max_points:
        return x, y
    idx = np.linspace(0, n - 1, num=max_points, dtype=int)
    return x[idx], y[idx]


# ============================================================
# PLOTLY HTML (NO scattergl; no per-point animation; clean crossfade)
# - Uses localStorage theme set by topbar, so color changes ALWAYS work.
# ============================================================
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
    // 1) localStorage (authoritative, shared across iframes)
    try {
      const t = localStorage.getItem(STORAGE_KEY);
      if (t && THEMES.includes(t)) return t;
    } catch(e) {}

    // 2) attribute fallback
    try {
      const t2 = document.documentElement.getAttribute("data-theme");
      if (t2 && THEMES.includes(t2)) return t2;
    } catch(e) {}
    return "green";
  }

  function colorsForTheme(theme){
    const rgb = themeToRgb(theme);
    return {
      rgb,
      lineStrong: rgba(rgb, 0.95),
      lineSoft: rgba(rgb, 0.10),
      font: rgba(rgb, 0.95),
      grid: rgba(rgb, 0.14),
      axis: rgba(rgb, 0.28)
    };
  }

  function makeLayout(colors){
    return {
      title: { text: P.title, x: 0.02, xanchor: "left" },
      paper_bgcolor: "#050505",
      plot_bgcolor: "#050505",
      margin: { l: 26, r: 18, t: 56, b: 44 },
      font: {
        family: 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
        color: colors.font,
        size: 13
      },
      showlegend: false,
      transition: { duration: 420, easing: "cubic-in-out" },
      xaxis: {
        title: { text: "wavelength (Å)" },
        showgrid: true,
        gridcolor: colors.grid,
        zeroline: false,
        ticks: "outside",
        tickcolor: colors.axis,
        linecolor: colors.axis,
        mirror: true
      },
      yaxis: {
        title: { text: "flux" },
        showgrid: true,
        gridcolor: colors.grid,
        zeroline: false,
        ticks: "outside",
        tickcolor: colors.axis,
        linecolor: colors.axis,
        mirror: true
      }
    };
  }

  // two traces = crossfade (no random dots, no WebGL artifacts)
  function tracesFor(colors){
    const hasOld = Array.isArray(P.x_old) && P.x_old.length > 0;

    const tOld = {
      type: "scatter",
      mode: "lines",
      x: hasOld ? P.x_old : P.x_new,
      y: hasOld ? P.y_old : P.y_new,
      line: { width: 2.4, color: colors.lineStrong },
      opacity: hasOld ? 1.0 : 0.0,
      hovertemplate: "λ=%{x:.1f} Å<br>flux=%{y:.4f}<extra></extra>"
    };

    const tNew = {
      type: "scatter",
      mode: "lines",
      x: P.x_new,
      y: P.y_new,
      line: { width: 2.4, color: colors.lineStrong },
      opacity: hasOld ? 0.0 : 1.0,
      hovertemplate: "λ=%{x:.1f} Å<br>flux=%{y:.4f}<extra></extra>"
    };

    return { hasOld, data: [tOld, tNew] };
  }

  function render(){
    const theme = getTheme();
    const colors = colorsForTheme(theme);
    const { hasOld, data } = tracesFor(colors);

    Plotly.newPlot(
      el,
      data,
      makeLayout(colors),
      { displayModeBar: false, responsive: true }
    ).then(() => {
      // Fade-in / crossfade
      setTimeout(() => {
        if (hasOld){
          Plotly.restyle(el, { opacity: 0.0 }, [0]); // old out
          Plotly.restyle(el, { opacity: 1.0 }, [1]); // new in
        } else {
          // start hidden then fade in
          Plotly.restyle(el, { opacity: 0.0 }, [1]);
          setTimeout(() => Plotly.restyle(el, { opacity: 1.0 }, [1]), 30);
        }
      }, 30);
    });
  }

  function restyleToTheme(){
    const theme = getTheme();
    const colors = colorsForTheme(theme);

    // update both lines + axes/fonts
    Plotly.restyle(el, { "line.color": [colors.lineStrong] }, [0]);
    Plotly.restyle(el, { "line.color": [colors.lineStrong] }, [1]);
    Plotly.relayout(el, makeLayout(colors));
  }

  render();

  // sync theme changes:
  // 1) storage event (topbar writes localStorage)
  window.addEventListener("storage", (ev) => {
    if (ev && ev.key === STORAGE_KEY) restyleToTheme();
  });

  // 2) also react if this iframe's data-theme changes
  new MutationObserver(() => restyleToTheme())
    .observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });

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
) -> str:
    payload = {
        "div_id": div_id,
        "title": title,
        "x_new": [float(v) for v in x_new],
        "y_new": [float(v) for v in y_new],
        "x_old": [float(v) for v in (x_old if x_old is not None else [])],
        "y_old": [float(v) for v in (y_old if y_old is not None else [])],
    }
    return (
        SPECTRUM_TEMPLATE
        .replace("__DIV__", div_id)
        .replace("__PAYLOAD__", json.dumps(payload))
    )


# ============================================================
# MAIN CONTENT
# ============================================================
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
        """.strip()
    )

    # compact selector ONLY (remove duplicate right-side pill)
    classes = list("OBAFGKM")
    default_idx = classes.index("A")

    st.markdown(
        """
<style>
/* keep this selector tight even inside a wide column */
div[data-testid="stSelectbox"]{
  width: 120px !important;
  max-width: 120px !important;
}
</style>
""",
        unsafe_allow_html=True,
    )

    spec_class = st.selectbox(
        "Spectral class",
        options=classes,
        index=default_idx,
        label_visibility="collapsed",
        key="spec_class_select",
    )
    st.caption(f"$ spectrum viewer — MK class **{spec_class}**")

    # session tracking for crossfade (old->new)
    if "prev_spec_class" not in st.session_state:
        st.session_state.prev_spec_class = spec_class
        st.session_state.prev_x = None
        st.session_state.prev_y = None

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

        # downsample to keep Plotly rock-solid and prevent freezes/dots
        x, y = downsample_xy(x, y, max_points=4500)

        x_old = st.session_state.prev_x if changed else None
        y_old = st.session_state.prev_y if changed else None

        title = f"$ MK spectral class {spec_class} — spectrum"
        div_id = "spectrum_plot_main"  # constant id for stability

        components.html(
            spectrum_plot_html(
                x_new=x,
                y_new=y,
                x_old=x_old,
                y_old=y_old,
                title=title,
                div_id=div_id,
            ),
            height=460,
            scrolling=False,
        )

        # update stored previous after render
        st.session_state.prev_spec_class = spec_class
        st.session_state.prev_x = x
        st.session_state.prev_y = y

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
