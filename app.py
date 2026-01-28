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
# CSS (icon buttons + hover invert)
# -----------------------------
st.markdown(
    """
<style>
.block-container { padding-top: 2.2rem; padding-bottom: 2rem; }
h1, h2, h3 { letter-spacing: -0.02em; }

.icon-row{
  display:flex;
  gap:14px;
  align-items:center;
  flex-wrap:wrap;
  margin-top: 0.25rem;
}

.icon-btn{
  width:46px;
  height:46px;
  border-radius:999px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  text-decoration:none !important;
  border: 1px solid rgba(255,255,255,0.22);
  background: rgba(20, 20, 20, 0.55);
  color: rgba(255,255,255,0.92);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  transition: transform 160ms ease, background 160ms ease, color 160ms ease, border-color 160ms ease, box-shadow 160ms ease;
  box-shadow: 0 6px 18px rgba(0,0,0,0.25);
}

.icon-btn:hover{
  transform: translateY(-2px);
  background: rgba(255,255,255,0.92);
  color: rgba(10,10,10,0.95);
  border-color: rgba(0,0,0,0.18);
  box-shadow: 0 10px 26px rgba(0,0,0,0.30);
}

.icon-btn:active{
  transform: translateY(0px) scale(0.98);
}

.icon-btn i{
  font-size: 18px;
}

div[data-testid="stAlert"]{ padding-top: 0.8rem; padding-bottom: 0.8rem; }
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
st.title(NAME)
st.subheader(TAGLINE)

col1, col3 = st.columns([1.4, 1.0], gap="large")

with col1:
    st.markdown(
        f"""
**Focus:** Automated sunspot classification using deep learning  
**Interests:** Solar physics • Computer vision • Imbalanced learning • Explainability  
**University:** {UNIVERSITY}  
""".strip()
    )

with col3:
    st.markdown("### Contact")
    st.markdown(f"**Email:** {EMAIL}")
    st.markdown(f"**University:** {UNIVERSITY}")

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

with right:
    st.markdown("## Links")
    st.caption("Hover to invert colors ✨")

    st.markdown(
        f"""
<div class="icon-row">
  <a class="icon-btn" href="{PORTFOLIO_URL}" target="_blank" rel="noopener" title="Portfolio">
    <i class="fa-solid fa-globe"></i>
  </a>
  <a class="icon-btn" href="{GITHUB_URL}" target="_blank" rel="noopener" title="GitHub">
    <i class="fa-brands fa-github"></i>
  </a>
  <a class="icon-btn" href="{LINKEDIN_URL}" target="_blank" rel="noopener" title="LinkedIn">
    <i class="fa-brands fa-linkedin-in"></i>
  </a>
  <a class="icon-btn" href="mailto:{EMAIL}" title="Email">
    <i class="fa-solid fa-envelope"></i>
  </a>
  <a class="icon-btn" href="https://www.nwu.ac.za/" target="_blank" rel="noopener" title="North-West University">
    <i class="fa-solid fa-building-columns"></i>
  </a>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("## Live profile")
    st.write("If an embed gets blocked by headers, these buttons always work:")
    r1, r2 = st.columns(2)
    with r1:
        st.link_button("🌍 Portfolio", PORTFOLIO_URL, use_container_width=True)
        st.link_button("💼 LinkedIn", LINKEDIN_URL, use_container_width=True)
    with r2:
        st.link_button("💻 GitHub", GITHUB_URL, use_container_width=True)
        st.link_button("✉️ Email me", f"mailto:{EMAIL}", use_container_width=True)

st.divider()
st.caption("© 2026 Bernard Swanepoel • Built with Streamlit")
