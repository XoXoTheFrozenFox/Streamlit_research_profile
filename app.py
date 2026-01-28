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

# -----------------------------
# CSS (tight spacing + fully visible + white base, invert on hover)
# -----------------------------
st.markdown(
    """
<style>
/* Pull content up a bit and reduce side padding so icons don't get clipped */
.block-container{
  padding-top: 1.25rem;
  padding-left: 1.2rem;
  padding-right: 1.2rem;
}

/* Tight icon row aligned left */
.icon-row{
  display:flex;
  gap:8px;               /* closer together */
  align-items:center;
  flex-wrap:wrap;
  margin: 0 0 0.4rem 0;  /* less vertical space */
  padding: 0;
}

/* White circle, black icon */
.icon-btn{
  width:40px;            /* slightly smaller so always fits */
  height:40px;
  border-radius:999px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  text-decoration:none !important;

  background:#ffffff;
  color:#111111;

  border: 1px solid rgba(0,0,0,0.18);
  transition: transform 140ms ease, background 140ms ease, color 140ms ease, box-shadow 140ms ease, border-color 140ms ease;
  box-shadow: 0 6px 14px rgba(0,0,0,0.10);
}

.icon-btn:hover{
  background:#111111;    /* invert */
  color:#ffffff;
  border-color: rgba(255,255,255,0.22);
  transform: translateY(-1px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.16);
}

.icon-btn:active{
  transform: translateY(0px) scale(0.98);
}

.icon-btn i{
  font-size: 16px;
  line-height: 1;
}

/* Optional: make the very top toolbar area less likely to overlap content */
header[data-testid="stHeader"]{
  background: transparent;
}
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Top-left icon buttons (no extra text)
# -----------------------------
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
</div>
""",
    unsafe_allow_html=True,
)

# Minimal header text (remove if you want ONLY buttons)
st.title(NAME)
st.subheader(TAGLINE)
