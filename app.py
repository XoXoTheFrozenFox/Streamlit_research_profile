import re
import json
import requests
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
# Global terminal aesthetic + hide Streamlit chrome
# + form widgets styled dark
# -----------------------------
st.markdown(
    """
<style>
/* Hide Streamlit default UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Theme vars */
:root{
  --bg:#050505;
  --orange:#ff7a18;
  --green:#39ff14;
  --border-orange:rgba(255,122,24,0.45);
  --border-green:rgba(57,255,20,0.45);
  --panel: rgba(0,0,0,0.35);
  --panel2: rgba(0,0,0,0.45);
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

div[data-testid="stMetric"]{
  background: var(--panel) !important;
  border: 1px solid var(--border-orange) !important;
  border-radius: 14px !important;
  padding: 12px 12px !important;
  box-shadow: 0 0 0 1px rgba(255,122,24,0.10) inset;
}

div[data-testid="stAlert"]{
  background: var(--panel) !important;
  border: 1px solid var(--border-orange) !important;
}

p, li{
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

/* -----------------------------
   Form widgets: dark background + orange border/text
------------------------------ */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea{
  background: var(--panel2) !important;
  color: var(--orange) !important;
  border: 1px solid var(--border-orange) !important;
  border-radius: 14px !important;
  box-shadow: 0 0 0 1px rgba(255,122,24,0.10) inset !important;
}
[data-testid="stTextInput"] input::placeholder,
[data-testid="stTextArea"] textarea::placeholder{
  color: rgba(255,122,24,0.65) !important;
}

/* Streamlit buttons */
.stButton > button{
  background: var(--panel2) !important;
  color: var(--orange) !important;
  border: 1px solid var(--border-orange) !important;
  border-radius: 14px !important;
  padding: 0.55rem 0.95rem !important;
  box-shadow: 0 0 0 1px rgba(255,122,24,0.10) inset !important;
}
.stButton > button:hover{
  background: rgba(255,122,24,0.10) !important;
}

/* Green theme (set by JS) */
html[data-theme="green"] body,
html[data-theme="green"] [data-testid="stAppViewContainer"]{
  color: var(--green) !important;
}
html[data-theme="green"] *{
  color: var(--green) !important;
}
html[data-theme="green"] hr{
  border-top: 1px solid var(--border-green) !important;
}
html[data-theme="green"] div[data-testid="stMetric"]{
  border: 1px solid var(--border-green) !important;
  box-shadow: 0 0 0 1px rgba(57,255,20,0.10) inset;
}
html[data-theme="green"] div[data-testid="stAlert"]{
  border: 1px solid var(--border-green) !important;
}
html[data-theme="green"] [data-testid="stTextInput"] input,
html[data-theme="green"] [data-testid="stTextArea"] textarea{
  color: var(--green) !important;
  border: 1px solid var(--border-green) !important;
  box-shadow: 0 0 0 1px rgba(57,255,20,0.10) inset !important;
}
html[data-theme="green"] [data-testid="stTextInput"] input::placeholder,
html[data-theme="green"] [data-testid="stTextArea"] textarea::placeholder{
  color: rgba(57,255,20,0.65) !important;
}
html[data-theme="green"] .stButton > button{
  color: var(--green) !important;
  border: 1px solid var(--border-green) !important;
  box-shadow: 0 0 0 1px rgba(57,255,20,0.10) inset !important;
}
html[data-theme="green"] .stButton > button:hover{
  background: rgba(57,255,20,0.10) !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Topbar component (orange default; toggle to green)
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
    --border-orange:rgba(255,122,24,0.45);
    --border-green:rgba(57,255,20,0.45);
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

  html[data-theme="green"] a.icon-btn,
  html[data-theme="green"] button.icon-btn {{
    border-color: var(--border-green);
    box-shadow: 0 0 0 1px rgba(57,255,20,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
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
  html[data-theme="green"] a.icon-btn:hover,
  html[data-theme="green"] button.icon-btn:hover {{
    background: rgba(57,255,20,0.12);
    box-shadow: 0 0 12px rgba(57,255,20,0.18), 0 10px 18px rgba(0,0,0,0.45);
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
        <button class="icon-btn" id="themeToggle" type="button" title="Toggle theme (Orange/Green)">
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

  function setTheme(theme) {{
    const t = (theme === "green") ? "green" : "orange";
    document.documentElement.setAttribute("data-theme", t);
    try {{
      if (window.parent && window.parent.document) {{
        window.parent.document.documentElement.setAttribute("data-theme", t);
      }}
    }} catch (e) {{}}
  }}

  // ALWAYS start ORANGE
  setTheme("orange");

  const toggleBtn = document.getElementById("themeToggle");
  toggleBtn.addEventListener("click", function () {{
    const cur = document.documentElement.getAttribute("data-theme") || "orange";
    setTheme(cur === "green" ? "orange" : "green");
  }});

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
# Email sending (Brevo Transactional API)
# -----------------------------
def _is_valid_email(addr: str) -> bool:
    if not addr:
        return False
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", addr.strip()) is not None

def send_contact_email_brevo(
    *,
    from_name: str,
    from_email: str,
    subject: str,
    message: str,
) -> tuple[bool, str]:
    """
    Sends email to YOU using Brevo Transactional Email API (HTTPS).
    Requires st.secrets["BREVO_API_KEY"] and a verified sender email in Brevo.
    """
    api_key = st.secrets.get("BREVO_API_KEY", "")
    sender_email = st.secrets.get("BREVO_SENDER_EMAIL", "")
    sender_name = st.secrets.get("BREVO_SENDER_NAME", "Website Contact Form")
    to_email = EMAIL

    if not api_key:
        return False, "Missing BREVO_API_KEY in Streamlit secrets."
    if not sender_email:
        return False, "Missing BREVO_SENDER_EMAIL in Streamlit secrets."
    if not _is_valid_email(sender_email):
        return False, "BREVO_SENDER_EMAIL is not a valid email address."

    # Build a clean body (avoid weird wrapping)
    safe_from_name = (from_name or "").strip()
    safe_from_email = (from_email or "").strip()
    safe_subject = (subject or "").strip()
    safe_message = (message or "").strip()

    if not safe_message:
        return False, "Message cannot be empty."

    html_content = f"""
    <div style="font-family: ui-monospace, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;">
      <h3>New website message</h3>
      <p><b>Name:</b> {safe_from_name}</p>
      <p><b>Email:</b> {safe_from_email}</p>
      <p><b>Subject:</b> {safe_subject}</p>
      <hr/>
      <pre style="white-space: pre-wrap;">{safe_message}</pre>
    </div>
    """

    payload = {
        "sender": {"name": sender_name, "email": sender_email},
        "to": [{"email": to_email, "name": "Bernard Swanepoel"}],
        "replyTo": {"email": safe_from_email or sender_email, "name": safe_from_name or "Website Visitor"},
        "subject": f"[Website] {safe_subject}" if safe_subject else "[Website] New message",
        "htmlContent": html_content,
    }

    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json",
    }

    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload), timeout=20)
        if 200 <= r.status_code < 300:
            return True, "Sent ✅"
        # show a readable error
        try:
            err = r.json()
        except Exception:
            err = {"error": r.text}
        return False, f"Brevo error ({r.status_code}): {err}"
    except Exception as e:
        return False, f"Request failed: {e}"

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

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name", placeholder="Your name")
        email = st.text_input("Email", placeholder="you@example.com")
        subject = st.text_input("Subject", placeholder="What is this about?")
        message = st.text_area("Message", placeholder="Type your message here...", height=160)

        submitted = st.form_submit_button("Send message")

    if submitted:
        if not name.strip():
            st.error("Please enter your name.")
        elif not _is_valid_email(email):
            st.error("Please enter a valid email address.")
        elif not message.strip():
            st.error("Please enter a message.")
        else:
            ok, info = send_contact_email_brevo(
                from_name=name,
                from_email=email,
                subject=subject,
                message=message,
            )
            if ok:
                st.success("Message sent successfully ✅")
            else:
                st.error(info)

st.divider()
st.caption("© 2026 Bernard Swanepoel")
