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
.block-container{
  padding-top: 1rem !important;
  padding-left: 1rem !important;
  padding-right: 1rem !important;
}

/* Header can steal hover */
header[data-testid="stHeader"]{
  background: transparent !important;
  pointer-events: none !important;
}

/* Keep our buttons above overlays */
.icon-wrap{ position: relative; z-index: 9999; }

.icon-row{
  display:flex;
  gap:8px;
  align-items:center;
  flex-wrap:wrap;
  margin: 0 0 0.4rem 0;
  padding: 0;
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

  background:#ffffff !important;
  color:#111111 !important;
  border:1px solid rgba(0,0,0,0.22) !important;

  box-shadow: 0 6px 14px rgba(0,0,0,0.12);
  transition: background 120ms ease, color 120ms ease, transform 120ms ease, box-shadow 120ms ease, border-color 120ms ease;
  cursor:pointer !important;
  pointer-events:auto !important;
}

/* Icon inherits color, and pointer stays on anchor */
.icon-row a.icon-btn i{
  color: inherit !important;
  font-size: 17px;
  line-height: 1;
  pointer-events:none;
}

/* Default icon visibility */
.icon-row a.icon-btn .ico-default{ display:block; }
.icon-row a.icon-btn .ico-hover{ display:none; }

/* Hover invert */
.icon-row a.icon-btn:hover,
.icon-row a.icon-btn:focus-visible{
  background:#111111 !important;
  color:#ffffff !important;
  border-color: rgba(255,255,255,0.22) !important;
  transform: translateY(-1px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.18);
  outline:none !important;
}

/* Swap ONLY the email icon on hover (closed -> open) */
.icon-row a.icon-btn.email:hover .ico-default,
.icon-row a.icon-btn.email:focus-visible .ico-default{
  display:none;
}
.icon-row a.icon-btn.email:hover .ico-hover,
.icon-row a.icon-btn.email:focus-visible .ico-hover{
  display:block;
}

.icon-row a.icon-btn:active{
  transform: translateY(0px) scale(0.98);
}
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="icon-wrap">
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

    <a class="icon-btn email" href="mailto:{EMAIL}" title="Email">
      <span class="ico-default"><i class="fa-solid fa-envelope"></i></span>
      <span class="ico-hover"><i class="fa-solid fa-envelope-open"></i></span>
    </a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)
