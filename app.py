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

# Typed header text (exactly as requested)
TYPED_FULL = "Hi🌞, my name is Bernard Swanepoel. {MSc student} {Reasearcher} {Computerscientist}"

# -----------------------------
# Terminal aesthetic + typing header + neon green accents
# -----------------------------
st.markdown(
    f"""
<style>
:root {{
  --bg: #050505;
  --panel: rgba(0,0,0,0.55);
  --text: #f5f5f5;
  --neon: #39ff14;      /* neon green */
  --neon2: rgba(57,255,20,0.22);
  --border: rgba(57,255,20,0.35);
}}

html, body, [data-testid="stAppViewContainer"] {{
  background: var(--bg) !important;
  color: var(--text) !important;
}}

[data-testid="stSidebar"] {{
  background: #070707 !important;
}}

.block-container {{
  padding-top: 1.2rem !important;
  padding-bottom: 2rem !important;
}}

h1, h2, h3, p, li, span, div {{
  color: var(--text);
}}

/* Streamlit overlays can steal clicks */
header[data-testid="stHeader"],
div[data-testid="stToolbar"],
div[data-testid="stDecoration"]{{
  background: transparent !important;
  pointer-events: none !important;
}}

/* Make Streamlit divider neon */
hr {{
  border: none !important;
  border-top: 1px solid var(--border) !important;
  opacity: 1 !important;
}}

/* Streamlit captions */
.stCaption, small {{
  color: rgba(245,245,245,0.78) !important;
}}

/* Metric cards: terminal-ish */
div[data-testid="stMetric"] {{
  background: rgba(0,0,0,0.35) !important;
  border: 1px solid var(--border) !important;
  border-radius: 14px !important;
  padding: 12px 12px !important;
  box-shadow: 0 0 0 1px rgba(57,255,20,0.08) inset;
}}
div[data-testid="stMetric"] * {{
  color: var(--text) !important;
}}
div[data-testid="stMetric"] [data-testid="stMetricLabel"] {{
  color: rgba(245,245,245,0.82) !important;
}}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {{
  color: var(--neon) !important;
}}

/* Info box */
div[data-testid="stAlert"] {{
  background: rgba(0,0,0,0.35) !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
}}
div[data-testid="stAlert"] * {{
  color: var(--text) !important;
}}

/* --- Top bar --- */
.topbar {{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:14px;
  flex-wrap:wrap;
  margin: 0.2rem 0 0.35rem 0;
}}

.terminal-title {{
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 1.55rem;
  font-weight: 700;
  line-height: 1.25;
  margin: 0;
  color: var(--text);
}}

.terminal-title .prompt {{
  color: var(--neon);
  text-shadow: 0 0 18px rgba(57,255,20,0.25);
}}

.typed {{
  white-space: nowrap;
  overflow: hidden;
}}

.cursor {{
  display:inline-block;
  width: 10px;
  margin-left: 2px;
  color: var(--neon);
  animation: blink 1s steps(1) infinite;
}}
@keyframes blink {{
  50% {{ opacity: 0; }}
}}

/* --- Icon row (right side) --- */
.icon-row {{
  display:flex;
  gap:10px;
  align-items:center;
  flex-wrap:wrap;
  margin: 0;
  padding: 0;
  position: relative;
  z-index: 9999;
}}

.icon-row a.icon-btn,
.icon-row a.icon-btn:visited {{
  width:44px;
  height:44px;
  border-radius:999px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  text-decoration:none !important;

  border: 1px solid var(--border);
  background: rgba(0,0,0,0.25);
  color: var(--neon);

  box-shadow: 0 0 0 1px rgba(57,255,20,0.10) inset, 0 10px 22px rgba(0,0,0,0.35);
  transition: transform 160ms ease, background 160ms ease, color 160ms ease, border-color 160ms ease, box-shadow 160ms ease, filter 160ms ease;
  cursor: pointer !important;
  pointer-events: auto !important;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
}}

.icon-row a.icon-btn i {{
  font-size: 18px;
  pointer-events: none;
}}

.icon-row a.icon-btn:hover,
.icon-row a.icon-btn:focus-visible {{
  transform: translateY(-2px);
  background: rgba(57,255,20,0.12);
  color: var(--neon);
  border-color: rgba(57,255,20,0.75);
  box-shadow: 0 0 18px rgba(57,255,20,0.18), 0 12px 26px rgba(0,0,0,0.45);
  outline: none !important;
}}

.icon-row a.icon-btn:active {{
  transform: translateY(0px) scale(0.98);
}}

/* Email icon swap: closed -> open */
.icon-row a.email-btn {{
  position: relative;
}}
.icon-row a.email-btn i {{
  position: absolute;
  inset: 0;
  display:flex;
  align-items:center;
  justify-content:center;
  pointer-events: none;
  font-size: 18px;
}}
.icon-row a.email-btn .email-open {{ opacity: 0; }}
.icon-row a.email-btn .email-closed {{ opacity: 1; }}

.icon-row a.email-btn:hover .email-open,
.icon-row a.email-btn:focus-visible .email-open {{ opacity: 1; }}
.icon-row a.email-btn:hover .email-closed,
.icon-row a.email-btn:focus-visible .email-closed {{ opacity: 0; }}

/* Fix “stuck hover” on touch devices */
@media (hover: none) and (pointer: coarse) {{
  .icon-row a.icon-btn:hover,
  .icon-row a.icon-btn:focus-visible {{
    transform:none !important;
    background: rgba(0,0,0,0.25) !important;
    border-color: var(--border) !important;
    box-shadow: 0 0 0 1px rgba(57,255,20,0.10) inset, 0 10px 22px rgba(0,0,0,0.35) !important;
  }}
  .icon-row a.icon-btn:active {{
    background: rgba(57,255,20,0.12) !important;
    border-color: rgba(57,255,20,0.75) !important;
    box-shadow: 0 0 18px rgba(57,255,20,0.18), 0 12px 26px rgba(0,0,0,0.45) !important;
  }}
}}

/* Make links/buttons look terminal */
a {{
  color: var(--neon) !important;
}}
a:hover {{
  filter: brightness(1.1);
}}

/* Remove extra top spacing from Streamlit title/subheader (we'll render our own header) */
h1#hi-my-name-is-bernard-swanepoel-msc-student-reasearcher-computerscientist {{
  margin-top: 0 !important;
}}
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""",
    unsafe_allow_html=True,
)

# JS: typing forward/back with cursor + blur active element when coming back
st.markdown(
    f"""
<script>
(function () {{
  // --- typing animation (type -> pause -> delete -> pause -> loop) ---
  const full = {repr(TYPED_FULL)};
  const elId = "typed_title_target";

  function startTyping() {{
    const el = document.getElementById(elId);
    if (!el) return;

    let i = 0;
    let dir = 1; // 1 = typing forward, -1 = deleting
    const typeSpeed = 42;     // ms per char typing
    const deleteSpeed = 24;   // ms per char deleting
    const pauseEnd = 900;     // pause at full text
    const pauseStart = 450;   // pause at empty

    function tick() {{
      // If element disappears (rerun), stop
      if (!document.getElementById(elId)) return;

      i += dir;

      if (i >= full.length) {{
        i = full.length;
        el.textContent = full.slice(0, i);
        setTimeout(() => {{
          dir = -1;
          setTimeout(tick, deleteSpeed);
        }}, pauseEnd);
        return;
      }}

      if (i <= 0) {{
        i = 0;
        el.textContent = "";
        setTimeout(() => {{
          dir = 1;
          setTimeout(tick, typeSpeed);
        }}, pauseStart);
        return;
      }}

      el.textContent = full.slice(0, i);
      setTimeout(tick, dir === 1 ? typeSpeed : deleteSpeed);
    }}

    // initialize
    el.textContent = "";
    i = 0;
    dir = 1;
    tick();
  }}

  // Streamlit reruns can recreate DOM; try a few times to attach
  let tries = 0;
  const iv = setInterval(() => {{
    tries += 1;
    const el = document.getElementById(elId);
    if (el) {{
      clearInterval(iv);
      startTyping();
    }}
    if (tries > 80) clearInterval(iv);
  }}, 75);

  // --- prevent stuck focus when coming back on mobile ---
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
# Header: typing line left, icons right (same line)
# -----------------------------
st.markdown(
    f"""
<div class="topbar">
  <div class="terminal-title">
    <span class="prompt">$</span>
    <span class="typed" id="typed_title_target"></span><span class="cursor">▌</span>
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

st.caption(TAGLINE)
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
