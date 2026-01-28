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
TAGLINE = "Research project title: Sunspot classification using deep learning techniques"

PORTFOLIO_URL = "https://xoxothefrozenfox.github.io/react-personal-portfolio/"
LINKEDIN_URL = "https://www.linkedin.com/in/bernard-swanepoel-a2777322b/"
GITHUB_URL = "https://github.com/XoXoTheFrozenFox"
EMAIL = "BernardSwanepoel1510@gmail.com"
UNIVERSITY = "North-West University, Potchefstroom"

STATIC_PREFIX = "Hi🌞, my name is Bernard Swanepoel."
ROTATING = [" Masters student✏️", " Researcher🥸", " Computer Scientist💻"," Coffee addict☕"]

# -----------------------------
# Global terminal aesthetic (applies to whole Streamlit page)
# -----------------------------
st.markdown(
    """
<style>
:root{
  --bg:#050505;
  --green:#39ff14;
  --border:rgba(57,255,20,0.45);
}

/* Global: neon green everywhere */
html, body, [data-testid="stAppViewContainer"]{
  background: var(--bg) !important;
  color: var(--green) !important;
}
*{ color: var(--green) !important; }

[data-testid="stSidebar"]{ background:#070707 !important; }

.block-container{
  padding-top: 1.2rem !important;
  padding-bottom: 2rem !important;
}

/* Streamlit overlays that can steal clicks */
header[data-testid="stHeader"],
div[data-testid="stToolbar"],
div[data-testid="stDecoration"]{
  background: transparent !important;
  pointer-events: none !important;
}

/* Neon divider */
hr{
  border: none !important;
  border-top: 1px solid var(--border) !important;
  opacity: 1 !important;
}

/* Metric cards */
div[data-testid="stMetric"]{
  background: rgba(0,0,0,0.35) !important;
  border: 1px solid var(--border) !important;
  border-radius: 14px !important;
  padding: 12px 12px !important;
  box-shadow: 0 0 0 1px rgba(57,255,20,0.10) inset;
}

/* Info box */
div[data-testid="stAlert"]{
  background: rgba(0,0,0,0.35) !important;
  border: 1px solid var(--border) !important;
}

/* Terminal text feel */
p, li{
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# IMPORTANT: Typing animation must be done inside components.html
# because Streamlit often strips/doesn't execute <script> in st.markdown.
# This block renders the whole topbar (typing + icons) as one unit.
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
    --green:#39ff14;
    --border:rgba(57,255,20,0.45);
  }}

  body {{
    margin: 0;
    background: transparent;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    color: var(--green);
  }}

  .topbar {{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap: 14px;
    flex-wrap:wrap;
    width: 100%;
    box-sizing: border-box;
  }}

  .terminal-title {{
    font-size: 1.65rem;
    font-weight: 700;
    line-height: 1.25;
    margin: 0;
    display:flex;
    align-items:center;
    flex-wrap:wrap;
    gap: 0.15rem;
    text-shadow: 0 0 18px rgba(57,255,20,0.12);
  }}

  .prompt {{
    margin-right: 10px;
  }}

  .cursor {{
    display:inline-block;
    width: 10px;
    margin-left: 2px;
    animation: blink 1s steps(1) infinite;
  }}
  @keyframes blink {{
    50% {{ opacity: 0; }}
  }}

  .tagline {{
    margin-top: 0.35rem;
    font-size: 1.25rem;
    font-weight: 650;
    opacity: 0.95;
  }}

  .icon-row {{
    display:flex;
    gap:10px;
    align-items:center;
    flex-wrap:wrap;
  }}

  a.icon-btn {{
    width:44px;
    height:44px;
    border-radius:999px;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    text-decoration:none;
    color: var(--green);
    border:1px solid var(--border);
    background: rgba(0,0,0,0.25);
    box-shadow: 0 0 0 1px rgba(57,255,20,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
    transition: transform 160ms ease, background 160ms ease, border-color 160ms ease, box-shadow 160ms ease, filter 160ms ease;
    -webkit-tap-highlight-color: transparent;
    user-select:none;
  }}

  a.icon-btn i {{
    font-size: 18px;
    pointer-events:none;
  }}

  a.icon-btn:hover {{
    transform: translateY(-2px);
    background: rgba(57,255,20,0.12);
    border-color: rgba(57,255,20,0.85);
    box-shadow: 0 0 18px rgba(57,255,20,0.18), 0 12px 26px rgba(0,0,0,0.45);
  }}

  a.icon-btn:active {{
    transform: translateY(0px) scale(0.98);
  }}

  /* Email icon swap */
  a.email-btn {{
    position: relative;
  }}
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

  /* On touch devices: avoid "stuck hover" */
  @media (hover: none) and (pointer: coarse) {{
    a.icon-btn:hover {{
      transform:none;
      background: rgba(0,0,0,0.25);
      border-color: var(--border);
      box-shadow: 0 0 0 1px rgba(57,255,20,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
    }}
    a.icon-btn:active {{
      background: rgba(57,255,20,0.12);
      border-color: rgba(57,255,20,0.85);
      box-shadow: 0 0 18px rgba(57,255,20,0.18), 0 12px 26px rgba(0,0,0,0.45);
    }}
  }}
</style>
</head>

<body>
  <div class="topbar">
    <div class="terminal-title">
      <span class="prompt">$</span>
      <span id="prefix"></span>
      <span id="word"></span>
      <span class="cursor">▌</span>
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

  <div class="tagline">{TAGLINE}</div>

<script>
(function () {{
  const staticPrefix = {STATIC_PREFIX!r} + " ";
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
    const current = words[idx];

    if (!deleting) {{
      char++;
      wordEl.textContent = current.slice(0, char);

      if (char >= current.length) {{
        setTimeout(() => {{
          deleting = true;
          step();
        }}, holdFull);
        return;
      }}

      setTimeout(step, typeSpeed);
    }} else {{
      char--;
      wordEl.textContent = current.slice(0, Math.max(0, char));

      if (char <= 0) {{
        deleting = false;
        idx = (idx + 1) % words.length;
        setTimeout(step, holdEmpty);
        return;
      }}

      setTimeout(step, deleteSpeed);
    }}
  }}

  // Kick off
  wordEl.textContent = "";
  step();

  // Prevent stuck focus when coming back (mobile)
  function blurActive() {{
    try {{ document.activeElement && document.activeElement.blur && document.activeElement.blur(); }} catch(e) {{}}
  }}
  window.addEventListener("pageshow", blurActive);
  document.addEventListener("visibilitychange", function() {{
    if (!document.hidden) blurActive();
  }});
}})();
</script>
</body>
</html>
"""

# Height needs to fit title + tagline
components.html(topbar_html, height=120)

st.divider()

# -----------------------------
# Main content
# -----------------------------
left, right = st.columns([1.35, 1.0], gap="large")

with left:
    st.markdown("## Research overview")
    st.write(
        "My research explores deep learning methods for classifying sunspot groups from solar imagery, "
        "with emphasis on robust generalization, handling class imbalance, and producing interpretable predictions."
    )

    st.markdown("## What I’m building")
    st.markdown(
        """
- **End-to-end classification pipeline** (data → training → evaluation → deployment)
- **Model families:** CNN/ViT-style backbones for image-based classification
- **Imbalance handling:** class weights, focal loss, oversampling, calibrated thresholds
- **Evaluation:** macro-F1, per-class metrics, confusion matrices, ROC/PR curves
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
st.caption("© 2026 Bernard Swanepoel • Built with Streamlit")
