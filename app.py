from urllib.parse import quote
import os
import glob
import json

import numpy as np
import pandas as pd

import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# PAGE CONFIG (static; dynamic favicon is handled via JS)
# Default theme = GREEN
# ============================================================
st.set_page_config(
    page_title="Bernard Swanepoel — Research Profile",
    page_icon="👽",   # default tab icon; JS will override favicon dynamically
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

# NOTE: no emoji here — emoji is injected dynamically in the topbar JS based on theme
STATIC_PREFIX = "Hi, my name is Bernard Swanepoel. "

ROTATING = [
    "Masters student✏️",
    "Researcher🥸",
    "Computer Scientist💻",
    "Coffee addict☕",
    "Space enthusiast💫",
]


# ============================================================
# GLOBAL TERMINAL AESTHETIC (DEFAULT = GREEN)
# ============================================================
st.markdown(
    """
<style>
/* Hide Streamlit default UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Remove heading link icons */
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

/* Divider */
hr{
  border: none !important;
  border-top: 1px solid var(--border-green) !important;
  opacity: 1 !important;
  margin: 0.18rem 0 0.55rem 0 !important;
}

/* Metrics */
div[data-testid="stMetric"]{
  background: var(--panel) !important;
  border: 1px solid var(--border-green) !important;
  border-radius: 14px !important;
  padding: 12px 12px !important;
  box-shadow: none !important;
}

/* Alerts */
div[data-testid="stAlert"]{
  background: var(--panel) !important;
  border: 1px solid var(--border-green) !important;
  border-radius: 14px !important;
}

/* st.info bg */
div[data-testid="stAlert"][data-baseweb="notification"]{
  background: #050505 !important;
}
div[data-testid="stAlert"][data-baseweb="notification"] *{
  background: transparent !important;
}

p, li, label, div{
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

/* TRUE BLACK inputs + remove rings */
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

/* input border = GREEN default */
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

/* Autofill */
div[data-testid="stTextInput"] input:-webkit-autofill,
div[data-testid="stTextInput"] input:-webkit-autofill:hover,
div[data-testid="stTextInput"] input:-webkit-autofill:focus{
  -webkit-box-shadow: 0 0 0 1000px var(--bg) inset !important;
  -webkit-text-fill-color: var(--green) !important;
  caret-color: var(--green) !important;
  border: 1px solid var(--border-green) !important;
}

/* Bottom-right "Field empty!" */
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

/* Buttons (default green) */
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

/* Mailto button */
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

/* ORANGE OVERRIDE */
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

/* BLUE OVERRIDE */
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

/* PINK OVERRIDE */
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
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# TOPBAR (theme toggle is JS-only; also updates favicon + "Hi{emoji}")
# ============================================================
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
    color: var(--green);
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
                 "Courier New", "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", monospace;
    box-sizing: border-box;
  }}

  html[data-theme="orange"] body {{ color: var(--orange); }}
  html[data-theme="green"]  body {{ color: var(--green); }}
  html[data-theme="blue"]   body {{ color: var(--blue); }}
  html[data-theme="pink"]   body {{ color: var(--pink); }}

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
    border:1px solid var(--border-green);
    background: rgba(0,0,0,0.25);
    box-shadow: 0 0 0 1px rgba(57,255,20,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
    transition: transform 140ms ease, background 140ms ease, border-color 140ms ease, box-shadow 140ms ease;
    -webkit-tap-highlight-color: transparent;
    user-select:none;
    cursor: pointer;

    line-height: 1;
    overflow: visible;
    padding: 0;
  }}

  html[data-theme="orange"] a.icon-btn, html[data-theme="orange"] button.icon-btn {{
    border-color: var(--border-orange);
    box-shadow: 0 0 0 1px rgba(255,122,24,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
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
    background: rgba(57,255,20,0.12);
    box-shadow: 0 0 12px rgba(57,255,20,0.18), 0 10px 18px rgba(0,0,0,0.45);
  }}
  html[data-theme="orange"] a.icon-btn:hover, html[data-theme="orange"] button.icon-btn:hover {{
    background: rgba(255,122,24,0.12);
    box-shadow: 0 0 12px rgba(255,122,24,0.18), 0 10px 18px rgba(0,0,0,0.45);
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
        <button class="icon-btn" id="themeToggle" type="button" title="Toggle theme (Green → Blue → Pink → Orange)">
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
  const themes = ["green", "blue", "pink", "orange"];

  const emojiMap = {{
    orange: "🌞",
    blue: "🌚",
    green: "👽",
    pink: "🛸"
  }};

  function setFaviconEmoji(em) {{
    const svg = `
      <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64">
        <text y="50" x="6" font-size="52">${{em}}</text>
      </svg>`;
    const url = "data:image/svg+xml," + encodeURIComponent(svg);

    function apply(doc) {{
      if (!doc) return;
      let link = doc.querySelector("link[rel*='icon']");
      if (!link) {{
        link = doc.createElement("link");
        link.rel = "icon";
        doc.head.appendChild(link);
      }}
      link.href = url;
    }}

    apply(document);
    try {{
      apply(window.parent.document);
    }} catch(e) {{}}
  }}

  function setTheme(theme) {{
    const t = themes.includes(theme) ? theme : "green";

    // set on this component doc
    document.documentElement.setAttribute("data-theme", t);

    // set on parent streamlit doc
    try {{
      if (window.parent && window.parent.document) {{
        window.parent.document.documentElement.setAttribute("data-theme", t);
      }}
    }} catch (e) {{}}

    // update favicon
    const em = emojiMap[t] || "👽";
    setFaviconEmoji(em);

    // update "Hi{emoji}" prefix in typing header
    const prefixEl = document.getElementById("prefix");
    const base = {STATIC_PREFIX!r}; // "Hi, my name is ..."
    // Replace starting "Hi," with "Hi{emoji},"
    const patched = base.replace(/^Hi,/, "Hi" + em + ",");
    prefixEl.textContent = patched;
  }}

  // default theme green
  setTheme("green");

  // toggle
  const toggleBtn = document.getElementById("themeToggle");
  toggleBtn.addEventListener("click", function () {{
    const cur = (window.parent?.document?.documentElement?.getAttribute("data-theme")) || "green";
    const i = themes.indexOf(cur);
    const next = themes[(i + 1 + themes.length) % themes.length];
    setTheme(next);
  }});

  // typing animation
  const words = {ROTATING!r};
  const wordEl = document.getElementById("word");

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

  // auto-resize iframe
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
}})();
</script>
</body>
</html>
"""
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


def spectrum_plot_html(x, y, title: str, autoplay: bool, div_id: str) -> str:
    payload = {
        "x": list(map(float, x)),
        "y": list(map(float, y)),
        "title": title,
        "autoplay": bool(autoplay),
        "div_id": div_id,
    }

    return f"""
<div id="{div_id}" style="width:100%;"></div>
<script src="https://cdn.plot.ly/plotly-2.30.0.min.js"></script>
<script>
(function() {{
  const P = {json.dumps(payload)};
  const el = document.getElementById(P.div_id);

  function parseRGB(s) {{
    // "rgb(r, g, b)" or "rgba(r,g,b,a)"
    const m = (s || "").match(/rgba?\\((\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)(?:\\s*,\\s*([\\d\\.]+))?\\)/i);
    if (!m) return [57,255,20,1];
    return [parseInt(m[1]), parseInt(m[2]), parseInt(m[3]), m[4] ? parseFloat(m[4]) : 1];
  }}
  function rgba(rgb, a) {{
    return `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, ${a})`;
  }}

  function getThemeColors() {{
    let doc = document;
    try {{ if (window.parent && window.parent.document) doc = window.parent.document; }} catch(e) {{}}
    const root = doc.documentElement;
    const body = doc.body || root;

    const c = getComputedStyle(body).color; // theme text color
    const rgb = parseRGB(c);

    // tuned for a dark terminal plot
    const line = rgba(rgb, 0.95);
    const font = rgba(rgb, 0.95);
    const grid = rgba(rgb, 0.14);
    const axis = rgba(rgb, 0.28);
    return {{ rgb, line, font, grid, axis }};
  }}

  function makeLayout(colors) {{
    return {{
      title: {{ text: P.title, x: 0.02, xanchor: "left" }},
      paper_bgcolor: "#050505",
      plot_bgcolor: "#050505",
      margin: {{ l: 22, r: 18, t: 52, b: 40 }},
      font: {{
        family: 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
        color: colors.font,
        size: 13
      }},
      showlegend: false,
      xaxis: {{
        title: {{ text: "wavelength (Å)" }},
        showgrid: true,
        gridcolor: colors.grid,
        zeroline: false,
        ticks: "outside",
        tickcolor: colors.axis,
        linecolor: colors.axis,
        mirror: true
      }},
      yaxis: {{
        title: {{ text: "flux" }},
        showgrid: true,
        gridcolor: colors.grid,
        zeroline: false,
        ticks: "outside",
        tickcolor: colors.axis,
        linecolor: colors.axis,
        mirror: true
      }}
    }};
  }}

  function render(initialFull) {{
    const colors = getThemeColors();

    const traceLine = {{
      type: "scattergl",
      mode: "lines",
      x: initialFull ? P.x : [],
      y: initialFull ? P.y : [],
      line: {{ width: 2.4, color: colors.line }},
      hovertemplate: "λ=%{{x:.1f}} Å<br>flux=%{{y:.4f}}<extra></extra>"
    }};

    const fig = {{
      data: [traceLine],
      layout: makeLayout(colors),
      config: {{ displayModeBar: false, responsive: true }}
    }};

    return Plotly.newPlot(el, fig.data, fig.layout, fig.config).then(() => {{
      if (P.autoplay) animateReveal();
    }});
  }}

  function restyleToTheme() {{
    const colors = getThemeColors();
    Plotly.restyle(el, {{
      "line.color": [colors.line]
    }}, [0]);

    Plotly.relayout(el, makeLayout(colors));
  }}

  function animateReveal() {{
    // "fade in from left to right" => reveal line x[:k] while also ramping opacity
    const N = P.x.length;
    if (N < 3) {{
      Plotly.restyle(el, {{ x: [P.x], y: [P.y] }}, [0]);
      return;
    }}

    const colors = getThemeColors();
    const start = performance.now();
    const duration = 1300; // ms
    const minAlpha = 0.08;

    function step(now) {{
      const t = Math.min(1, (now - start) / duration);
      const k = Math.max(2, Math.floor(2 + t * (N - 2)));

      const alpha = minAlpha + (0.95 - minAlpha) * t;
      const col = rgba(colors.rgb, alpha);

      Plotly.restyle(el, {{
        x: [P.x.slice(0, k)],
        y: [P.y.slice(0, k)],
        "line.color": [col]
      }}, [0]);

      if (t < 1) {{
        requestAnimationFrame(step);
      }} else {{
        // lock final state at full opacity + full line
        const finalColors = getThemeColors();
        Plotly.restyle(el, {{
          x: [P.x],
          y: [P.y],
          "line.color": [finalColors.line]
        }}, [0]);
      }}
    }}

    requestAnimationFrame(step);
  }}

  // 1) first render: if autoplay -> start empty, else show full line
  render(!P.autoplay);

  // 2) if theme changes while page is open, update plot colors live
  let parentRoot = null;
  try {{
    parentRoot = window.parent.document.documentElement;
  }} catch(e) {{
    parentRoot = document.documentElement;
  }}

  new MutationObserver(() => {{
    // reapply theme styling immediately
    restyleToTheme();
  }}).observe(parentRoot, {{ attributes: true, attributeFilter: ["data-theme"] }});

}})();
</script>
"""


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

The distribution and characteristics of the seven spectral classes can be visualized below:
        """.strip()
    )

    # ------------------------------------------------------------
    # Spectrum viewer (new animation: line reveals left→right with fade)
    # Plot colors update LIVE when theme changes (no Python rerun needed)
    # ------------------------------------------------------------
    st.markdown(
        """
<style>
div[data-testid="stSelectbox"]{
  max-width: 230px !important;
}
div[data-testid="stSelectbox"] label{
  display:none !important;
}
.spectrum-wrap{
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 16px;
  padding: 12px 12px 10px 12px;
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

    if "prev_spec_class" not in st.session_state:
        st.session_state.prev_spec_class = spec_class
        st.session_state.spec_initialized = False

    changed = (spec_class != st.session_state.prev_spec_class)

    data_root = "data"
    class_dir = os.path.join(data_root, spec_class)

    try:
        df_spec = read_spectrum_csv(class_dir)
    except Exception as e:
        st.error(f"Could not load spectrum for class '{spec_class}' from '{class_dir}': {e}")
        df_spec = None

    if df_spec is not None:
        title = f"$ MK spectral class {spec_class} — spectrum"

        # no animation on first ever render
        autoplay = bool(st.session_state.spec_initialized and changed)

        x = df_spec["wavelength_A"].to_numpy()
        y = df_spec["flux"].to_numpy()

        div_id = f"spectrum_plot_{spec_class}"
        components.html(
            spectrum_plot_html(x, y, title=title, autoplay=autoplay, div_id=div_id),
            height=460,
            scrolling=False,
        )

        st.session_state.spec_initialized = True
        st.session_state.prev_spec_class = spec_class

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
