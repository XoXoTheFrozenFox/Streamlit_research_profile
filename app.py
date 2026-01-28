import streamlit as st

st.set_page_config(
    page_title="Bernard Swanepoel — Research Profile",
    page_icon="🌞",
    layout="wide",
)

# -----------------------------
# Links / info
# -----------------------------
TAGLINE = "MSc Computer Science — Sunspot Classification with Deep Learning"

PORTFOLIO_URL = "https://xoxothefrozenfox.github.io/react-personal-portfolio/"
LINKEDIN_URL = "https://www.linkedin.com/in/bernard-swanepoel-a2777322b/"
GITHUB_URL = "https://github.com/XoXoTheFrozenFox"
EMAIL = "BernardSwanepoel1510@gmail.com"
UNIVERSITY = "North-West University, Potchefstroom"

# Header text pieces (exactly as requested)
STATIC_PREFIX = "Hi🌞, my name is Bernard Swanepoel."
ROTATING = ["{MSc. student}", "{Reasearcher}", "{Computer Scientist}"]

# -----------------------------
# Terminal aesthetic + typing (rotating suffix) + neon green everywhere
# -----------------------------
st.markdown(
    """
<style>
:root{
  --bg:#050505;
  --panel:rgba(0,0,0,0.55);
  --green:#39ff14;          /* neon */
  --greenDim:rgba(57,255,20,0.30);
  --border:rgba(57,255,20,0.45);
}

/* Global terminal look */
html, body, [data-testid="stAppViewContainer"]{
  background: var(--bg) !important;
  color: var(--green) !important;
}

/* Make basically all text neon green */
*{
  color: var(--green) !important;
}

/* Streamlit sidebar */
[data-testid="stSidebar"]{
  background:#070707 !important;
}

/* Container spacing */
.block-container{
  padding-top: 1.2rem !important;
  padding-bottom: 2rem !important;
}

/* Remove/neutralize Streamlit overlays that can steal clicks */
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

/* Top bar layout */
.topbar{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:14px;
  flex-wrap:wrap;
  margin: 0.2rem 0 0.4rem 0;
}

/* Typing line */
.terminal-title{
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 1.65rem;
  font-weight: 700;
  line-height: 1.25;
  margin: 0;
  text-shadow: 0 0 18px rgba(57,255,20,0.12);
}

.terminal-title .prompt{
  margin-right: 10px;
  text-shadow: 0 0 20px rgba(57,255,20,0.20);
}

.cursor{
  display:inline-block;
  width: 10px;
  margin-left: 2px;
  animation: blink 1s steps(1) infinite;
}
@keyframes blink{
  50%{ opacity: 0; }
}

/* Bigger tagline */
.tagline{
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 1.2rem;          /* bigger */
  font-weight: 600;
  opacity: 0.95;
  margin-top: 0.1rem;
}

/* Icon row (right side) */
.icon-row{
  display:flex;
  gap:10px;
  align-items:center;
  flex-wrap:wrap;
  margin: 0;
  padding: 0;
  position: relative;
  z-index: 9999;
}

.icon-row a.icon-btn,
.icon-row a.icon-btn:visited{
  width:44px;
  height:44px;
  border-radius:999px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  text-decoration:none !important;

  border:1px solid var(--border) !important;
  background: rgba(0,0,0,0.25) !important;
  box-shadow: 0 0 0 1px rgba(57,255,20,0.12) inset, 0 10px 22px rgba(0,0,0,0.35);
  transition: transform 160ms ease, background 160ms ease, border-color 160ms ease, box-shadow 160ms ease, filter 160ms ease;
  cursor: pointer !important;
  pointer-events: auto !important;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
}

/* Icons */
.icon-row a.icon-btn i{
  font-size: 18px;
  pointer-events: none;
}

/* Hover glow */
.icon-row a.icon-btn:hover,
.icon-row a.icon-btn:focus-visible{
  transform: translateY(-2px);
  background: rgba(57,255,20,0.12) !important;
  border-color: rgba(57,255,20,0.85) !important;
  box-shadow: 0 0 18px rgba(57,255,20,0.18), 0 12px 26px rgba(0,0,0,0.45);
  outline: none !important;
}

.icon-row a.icon-btn:active{
  transform: translateY(0px) scale(0.98);
}

/* Email icon swap: closed -> open */
.icon-row a.email-btn{
  position: relative;
}
.icon-row a.email-btn i{
  position: absolute;
  inset: 0;
  display:flex;
  align-items:center;
  justify-content:center;
  pointer-events: none;
  font-size: 18px;
}
.icon-row a.email-btn .email-open{ opacity: 0; }
.icon-row a.email-btn .email-closed{ opacity: 1; }

.icon-row a.email-btn:hover .email-open,
.icon-row a.email-btn:focus-visible .email-open{ opacity: 1; }
.icon-row a.email-btn:hover .email-closed,
.icon-row a.email-btn:focus-visible .email-closed{ opacity: 0; }

/* Fix “stuck hover” on touch devices */
@media (hover: none) and (pointer: coarse){
  .icon-row a.icon-btn:hover,
  .icon-row a.icon-btn:focus-visible{
    transform:none !important;
    background: rgba(0,0,0,0.25) !important;
    border-color: var(--border) !important;
    box-shadow: 0 0 0 1px rgba(57,255,20,0.12) inset, 0 10px 22px rgba(0,0,0,0.35) !important;
  }
  .icon-row a.icon-btn:active{
    background: rgba(57,255,20,0.12) !important;
    border-color: rgba(57,255,20,0.85) !important;
    box-shadow: 0 0 18px rgba(57,255,20,0.18), 0 12px 26px rgba(0,0,0,0.45) !important;
  }
}

/* Streamlit metric cards */
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

/* Make lists/p text readable in terminal style */
p, li{
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

/* Make Streamlit default input outlines neon if you add later */
*:focus{
  outline-color: rgba(57,255,20,0.7) !important;
}
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""",
    unsafe_allow_html=True,
)

# JS: rotating suffix typing animation + mobile focus blur
st.markdown(
    f"""
<script>
(function () {{
  const staticPrefix = {repr(STATIC_PREFIX)};
  const words = {repr(ROTATING)};
  const prefixId = "typed_prefix";
  const wordId = "typed_word";

  // wait until elements exist (Streamlit reruns)
  function whenReady(fn) {{
    let tries = 0;
    const t = setInterval(() => {{
      tries++;
      const p = document.getElementById(prefixId);
      const w = document.getElementById(wordId);
      if (p && w) {{
        clearInterval(t);
        fn(p, w);
      }}
      if (tries > 120) clearInterval(t);
    }}, 50);
  }}

  function runTyping(prefixEl, wordEl) {{
    prefixEl.textContent = staticPrefix + " ";
    let idx = 0;
    let char = 0;
    let deleting = false;

    const typeSpeed = 45;
    const deleteSpeed = 25;
    const holdFull = 900;
    const holdEmpty = 280;

    function step() {{
      const current = words[idx];

      if (!deleting) {{
        char++;
        wordEl.textContent = current.slice(0, char);
        if (char >= current.length) {{
          // hold then delete
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
          // move to next word
          deleting = false;
          idx = (idx + 1) % words.length;
          setTimeout(step, holdEmpty);
          return;
        }}
        setTimeout(step, deleteSpeed);
      }}
    }}

    // start
    wordEl.textContent = "";
    idx = 0;
    char = 0;
    deleting = false;
    step();
  }}

  whenReady(runTyping);

  // prevent stuck focus on mobile when coming back
  function blurActive() {{
    try {{ document.activeElement && document.activeElement.blur && document.activeElement.blur(); }} catch(e) {{}}
  }}
  window.addEventListener("pageshow", blurActive);
  document.addEventListener("visibilitychange", function() {{
    if (!document.hidden) blurActive();
  }});
}})();
</script>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Header: static prefix always visible + rotating suffix typed, icons right
# -----------------------------
st.markdown(
    f"""
<div class="topbar">
  <div class="terminal-title">
    <span class="prompt">$</span>
    <span id="typed_prefix"></span><span id="typed_word"></span><span class="cursor">▌</span>
  </div>

  <div class="icon-row">
    <a class="icon-btn" href="{PORTFOLIO_URL}" target="_blank" rel="noopener" title="Portfolio" onclick="this.blur();">
      <i class="fa-solid fa-globe"></i>
    </a>
    <a class="icon-btn" href="{GITHUB_URL}" target="_blank" rel="noopener" title="GitHub" onclick="this.blur();">
      <i class="fa-brands fa-github"></i>
    </a>
    <a class="icon-btn" href="{LINKEDIN_URL}" target="_blank" rel="noopener" title="LinkedIn" onclick="this.blur();">
      <i class="fa-brands fa-linkedin-in"></i>
    </a>
    <a class="icon-btn email-btn" href="mailto:{EMAIL}" title="Email" onclick="this.blur();">
      <i class="fa-solid fa-envelope email-closed"></i>
      <i class="fa-solid fa-envelope-open email-open"></i>
    </a>
    <a class="icon-btn" href="https://www.nwu.ac.za/" target="_blank" rel="noopener" title="North-West University" onclick="this.blur();">
      <i class="fa-solid fa-building-columns"></i>
    </a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# Bigger tagline (and green due to global CSS)
st.markdown(f'<div class="tagline">{TAGLINE}</div>', unsafe_allow_html=True)

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
