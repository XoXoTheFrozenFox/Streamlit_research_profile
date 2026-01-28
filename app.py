import streamlit as st

st.set_page_config(
    page_title="Bernard Swanepoel — Research Profile",
    page_icon="🌞",
    layout="wide",
)

PORTFOLIO_URL = "https://xoxothefrozenfox.github.io/react-personal-portfolio/"
LINKEDIN_URL = "https://www.linkedin.com/in/bernard-swanepoel-a2777322b/"
GITHUB_URL = "https://github.com/XoXoTheFrozenFox"
EMAIL = "BernardSwanepoel1510@gmail.com"

st.markdown(
    """
<style>
/* Reduce padding so buttons don't get clipped */
.block-container{
  padding-top: 1rem !important;
  padding-left: 1rem !important;
  padding-right: 1rem !important;
}

/* Tight row */
.icon-row{
  display:flex;
  gap:8px;
  align-items:center;
  flex-wrap:wrap;
  margin: 0 0 0.4rem 0;
  padding: 0;
}

/* FORCE colors (Streamlit link styles can override unless we use !important) */
.icon-row a.icon-btn,
.icon-row a.icon-btn:visited{
  width:40px;
  height:40px;
  border-radius:999px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  text-decoration:none !important;

  background:#ffffff !important;      /* base: white circle */
  color:#111111 !important;            /* base: black icon */
  border:1px solid rgba(0,0,0,0.22) !important;

  box-shadow: 0 6px 14px rgba(0,0,0,0.12);
  transition: background 140ms ease, color 140ms ease, transform 140ms ease, box-shadow 140ms ease, border-color 140ms ease;
  cursor:pointer;
}

/* Make sure the icon always inherits the anchor color */
.icon-row a.icon-btn i{
  color: inherit !important;
  font-size: 16px;
  line-height: 1;
}

/* Hover + keyboard focus: invert */
.icon-row a.icon-btn:hover,
.icon-row a.icon-btn:focus-visible{
  background:#111111 !important;
  color:#ffffff !important;
  border-color: rgba(255,255,255,0.22) !important;
  transform: translateY(-1px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.18);
  outline: none !important;
}

.icon-row a.icon-btn:active{
  transform: translateY(0px) scale(0.98);
}

/* Prevent header overlay oddities */
header[data-testid="stHeader"]{ background: transparent; }
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""",
    unsafe_allow_html=True,
)

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
