import streamlit as st

st.set_page_config(
    page_title="Bernard Swanepoel — Research Profile",
    page_icon="🌞",
    layout="wide",
)

# -----------------------------
# Your links / info
# -----------------------------
NAME = "🌞 Bernard Swanepoel"
TAGLINE = "MSc Computer Science — Sunspot Classification with Deep Learning"

PORTFOLIO_URL = "https://xoxothefrozenfox.github.io/react-personal-portfolio/"
LINKEDIN_URL = "https://www.linkedin.com/in/bernard-swanepoel-a2777322b/"
GITHUB_URL = "https://github.com/XoXoTheFrozenFox"
EMAIL = "BernardSwanepoel1510@gmail.com"
UNIVERSITY = "North-West University, Potchefstroom"

# -----------------------------
# CSS (title row + icon buttons + hover invert + email icon swap + mobile hover reset)
# -----------------------------
st.markdown(
    """
<style>
/* Make Streamlit a touch cleaner */
.block-container { padding-top: 1.4rem; padding-bottom: 2rem; }
h1, h2, h3 { letter-spacing: -0.02em; }
small, .stCaption { opacity: 0.85; }

/* Kill Streamlit overlays that can steal clicks */
header[data-testid="stHeader"],
div[data-testid="stToolbar"],
div[data-testid="stDecoration"]{
  background: transparent !important;
  pointer-events: none !important;
}

/* --- Title row (name left, icons right) --- */
.topbar{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:14px;
  flex-wrap:wrap;
  margin: 0.25rem 0 0.15rem 0;
}
.topbar .title{
  font-size: 2.35rem;
  font-weight: 700;
  line-height: 1.12;
  margin: 0;
}

/* Icon row (right side) */
.icon-row{
  display:flex;
  gap:12px;
  align-items:center;
  flex-wrap:wrap;
  margin: 0;
  padding: 0;
  position: relative;
  z-index: 9999;
}

/* Round icon button with hover invert */
.icon-row a.icon-btn,
.icon-row a.icon-btn:visited{
  width:44px;
  height:44px;
  border-radius:999px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  text-decoration:none !important;
  border: 1px solid rgba(0,0,0,0.16);
  background: rgba(255,255,255,0.78);
  color: rgba(10,10,10,0.92);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  transition: transform 160ms ease, background 160ms ease, color 160ms ease, border-color 160ms ease, box-shadow 160ms ease;
  box-shadow: 0 6px 18px rgba(0,0,0,0.18);
  cursor: pointer !important;
  pointer-events: auto !important;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
}

/* Icons don't steal pointer events */
.icon-row a.icon-btn i{
  font-size: 18px;
  pointer-events: none;
}

/* Hover invert (desktop/hover devices) */
.icon-row a.icon-btn:hover,
.icon-row a.icon-btn:focus-visible{
  transform: translateY(-2px);
  background: rgba(10,10,10,0.92);
  color: rgba(255,255,255,0.96);
  border-color: rgba(255,255,255,0.22);
  box-shadow: 0 10px 26px rgba(0,0,0,0.26);
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

/* Fix “stuck hover” on touch/mobile devices */
@media (hover: none) and (pointer: coarse){
  .icon-row a.icon-btn:hover,
  .icon-row a.icon-btn:focus-visible{
    transform:none !important;
    background: rgba(255,255,255,0.78) !important;
    color: rgba(10,10,10,0.92) !important;
    border: 1px solid rgba(0,0,0,0.16) !important;
    box-shadow: 0 6px 18px rgba(0,0,0,0.18) !important;
  }
  .icon-row a.icon-btn:active{
    transform: translateY(0px) scale(0.98) !important;
    background: rgba(10,10,10,0.92) !important;
    color: rgba(255,255,255,0.96) !important;
    border-color: rgba(255,255,255,0.22) !important;
    box-shadow: 0 10px 26px rgba(0,0,0,0.26) !important;
  }
}
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""",
    unsafe_allow_html=True,
)

# JS: blur active element when coming back (prevents “stuck focus/hover” on mobile)
st.markdown(
    """
<script>
(function () {
  function blurActive() {
    try { document.activeElement && document.activeElement.blur && document.activeElement.blur(); } catch(e) {}
  }
  window.addEventListener("pageshow", blurActive);
  document.addEventListener("visibilitychange", function() {
    if (!document.hidden) blurActive();
  });
})();
</script>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Header: NAME left, ICONS right (same line)
# -----------------------------
st.markdown(
    f"""
<div class="topbar">
  <div class="title">{NAME}</div>

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

# Tagline still uses Streamlit for nice sizing
st.subheader(TAGLINE)

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
