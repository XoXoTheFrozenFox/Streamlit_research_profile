from urllib.parse import quote

import streamlit as st
import streamlit.components.v1 as components

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
# Global aesthetic + hide Streamlit chrome
# Dark-blue neon base + neon pink accent
# -----------------------------
st.markdown(
    """
<style>
/* Hide Streamlit default UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Remove the little "link" icon Streamlit shows next to headers on hover */
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a { display:none !important; }
/* Newer Streamlit adds an anchor icon element; hide it too */
[data-testid="stHeader"] a,
[data-testid="stHeader"] svg,
a[data-testid="stHeaderLink"],
a.stMarkdownHeaderLink { display:none !important; opacity:0 !important; }

/* Theme vars */
:root{
  --bg:#050A1A;                 /* deep dark blue */
  --panel: rgba(2, 10, 28, 0.62);
  --text:#CDE7FF;               /* icy blue text */
  --muted: rgba(205,231,255,0.70);

  --pink:#FF2BD6;               /* neon pink */
  --cyan:#00E7FF;               /* neon cyan */
  --border: rgba(255,43,214,0.55);

  --shadowPink: 0 0 16px rgba(255,43,214,0.18);
  --shadowCyan: 0 0 16px rgba(0,231,255,0.14);
}

/* App background + default text */
html, body, [data-testid="stAppViewContainer"]{
  background: radial-gradient(1200px 700px at 15% 0%, rgba(0,231,255,0.10), transparent 55%),
              radial-gradient(900px 600px at 85% 10%, rgba(255,43,214,0.10), transparent 55%),
              var(--bg) !important;
  color: var(--text) !important;
}
*{ color: var(--text) !important; }

.block-container{
  padding-top: 0.55rem !important;
  padding-bottom: 1.25rem !important;
}

/* Divider */
hr{
  border: none !important;
  border-top: 1px solid rgba(255,43,214,0.35) !important;
  opacity: 1 !important;
  margin: 0.18rem 0 0.55rem 0 !important;
}

/* Typography */
p, li, label, div, span{
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
small, .stCaption { color: var(--muted) !important; }

/* Markdown headings a little brighter */
h1, h2, h3 { text-shadow: var(--shadowCyan); }

/* Metrics & alerts */
div[data-testid="stMetric"]{
  background: linear-gradient(180deg, rgba(2, 10, 28, 0.65), rgba(2, 10, 28, 0.45)) !important;
  border: 1px solid rgba(0,231,255,0.22) !important;
  border-radius: 14px !important;
  padding: 12px 12px !important;
  box-shadow: 0 0 0 1px rgba(0,231,255,0.10) inset, var(--shadowCyan);
}
div[data-testid="stAlert"]{
  background: var(--panel) !important;
  border: 1px solid rgba(255,43,214,0.28) !important;
  border-radius: 14px !important;
  box-shadow: var(--shadowPink);
}

/* -----------------------------
   Neon form widgets
------------------------------ */
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea{
  background: rgba(3, 10, 26, 0.85) !important;
  color: var(--text) !important;
  border: 1px solid rgba(255,43,214,0.45) !important;
  border-radius: 14px !important;
  box-shadow: 0 0 0 1px rgba(255,43,214,0.10) inset, var(--shadowPink) !important;
}
div[data-testid="stTextInput"] input::placeholder,
div[data-testid="stTextArea"] textarea::placeholder{
  color: rgba(205,231,255,0.55) !important;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus{
  outline: none !important;
  border: 1px solid rgba(0,231,255,0.55) !important;
  box-shadow: 0 0 0 1px rgba(0,231,255,0.16) inset, var(--shadowCyan) !important;
}

/* Streamlit buttons (kept, even though we use mailto <a>) */
.stButton > button, div[data-testid="stFormSubmitButton"] button{
  background: rgba(3, 10, 26, 0.80) !important;
  color: var(--text) !important;
  border: 1px solid rgba(0,231,255,0.35) !important;
  border-radius: 14px !important;
  padding: 0.55rem 0.95rem !important;
  box-shadow: 0 0 0 1px rgba(0,231,255,0.10) inset, var(--shadowCyan) !important;
}
.stButton > button:hover, div[data-testid="stFormSubmitButton"] button:hover{
  background: rgba(0,231,255,0.07) !important;
  border-color: rgba(255,43,214,0.55) !important;
  box-shadow: 0 0 0 1px rgba(255,43,214,0.12) inset, var(--shadowPink) !important;
}

/* Mailto "Send message" link styled like a neon button */
a.send-mailto-btn{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none !important;
  background: rgba(3, 10, 26, 0.80) !important;
  color: var(--text) !important;
  border: 1px solid rgba(255,43,214,0.55) !important;
  border-radius: 14px !important;
  padding: 0.55rem 0.95rem !important;
  box-shadow: 0 0 0 1px rgba(255,43,214,0.10) inset, var(--shadowPink) !important;
  transition: transform 140ms ease, background 140ms ease, border-color 140ms ease, box-shadow 140ms ease;
  user-select: none;
  cursor: pointer;
}
a.send-mailto-btn:hover{
  background: rgba(255,43,214,0.08) !important;
  border-color: rgba(0,231,255,0.55) !important;
  box-shadow: 0 0 0 1px rgba(0,231,255,0.12) inset, var(--shadowCyan) !important;
  transform: translateY(-1px);
}

/* Disabled-look */
a.send-mailto-btn.is-disabled{
  opacity: 0.55;
  cursor: not-allowed;
  pointer-events: none;
  transform: none !important;
  box-shadow: none !important;
  border-color: rgba(205,231,255,0.18) !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Topbar component (keep same layout; now neon cyan/pink)
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
    --text:#CDE7FF;
    --pink:#FF2BD6;
    --cyan:#00E7FF;
    --borderP: rgba(255,43,214,0.55);
    --borderC: rgba(0,231,255,0.40);
  }}

  html, body {{
    overflow: visible !important;
    height: auto !important;
  }}

  body {{
    margin: 0;
    padding: 10px 8px 12px 8px;
    background: transparent;
    color: var(--text);
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
                 "Courier New", "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", monospace;
    box-sizing: border-box;
  }}

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
    text-shadow: 0 0 14px rgba(0,231,255,0.18);
  }}

  .typing-line {{ display: inline; }}
  .prompt {{ display: inline; white-space: nowrap; color: var(--cyan); }}
  #prefix, #word {{ display: inline; }}

  .cursor {{
    display:inline-block;
    width: 10px;
    margin-left: 2px;
    color: var(--cyan);
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
    color: var(--text);

    box-sizing: border-box;
    border:1px solid var(--borderC);
    background: rgba(3, 10, 26, 0.45);
    box-shadow: 0 0 0 1px rgba(0,231,255,0.10) inset, 0 0 16px rgba(0,231,255,0.10), 0 10px 22px rgba(0,0,0,0.35);
    transition: transform 140ms ease, background 140ms ease, border-color 140ms ease, box-shadow 140ms ease;
    -webkit-tap-highlight-color: transparent;
    user-select:none;
    cursor: pointer;

    line-height: 1;
    overflow: visible;
    padding: 0;
  }}

  a.icon-btn i, button.icon-btn i {{
    font-size: 18px;
    pointer-events:none;
  }}

  a.icon-btn:hover, button.icon-btn:hover {{
    transform: translateY(-1px);
    background: rgba(255,43,214,0.10);
    border-color: var(--borderP);
    box-shadow: 0 0 0 1px rgba(255,43,214,0.12) inset, 0 0 18px rgba(255,43,214,0.16), 0 10px 18px rgba(0,0,0,0.45);
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

  // Resize without infinite growth
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

  // Typing
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
# Mailto builder (FREE)
# -----------------------------
def build_mailto(to_email: str, subject: str, body: str) -> str:
    return f"mailto:{to_email}?subject={quote(subject)}&body={quote(body)}"

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

    st.markdown("## Research titles")
    st.markdown(
        """
- **Master’s dissertation:** Sunspot classification using deep learning techniques  
- **Honours project:** Assessing the cybersecurity awareness of staff members in a higher educational institution
        """.strip()
    )

    st.markdown("## Research summary")
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

    st.markdown("## Tools and technologies used")
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

    st.markdown("## Highlights")
    st.info("Replace these placeholders with your real results (macro-F1, dataset size, best model, key findings).")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Best Macro-F1", "—")
    m2.metric("Classes", "—")
    m3.metric("Images", "—")
    m4.metric("Backbone", "—")

    st.divider()

    st.markdown("## Contact")
    st.write("Send me a message directly from this page:")

    # Inputs (no email field, as requested)
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

        if name or subject or message:
            if not name_s:
                st.error("Please enter your name.")
            elif not subject_s:
                st.error("Please enter a subject.")
            elif not message_s:
                st.error("Please enter a message.")

st.divider()
st.caption("© 2026 Bernard Swanepoel")
