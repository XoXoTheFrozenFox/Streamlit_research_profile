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
/* Layout padding */
.block-container{
  padding-top: 1rem !important;
  padding-left: 1rem !important;
  padding-right: 1rem !important;
}

/* Streamlit top overlays can sit above your buttons (blocks top-half clicks).
   Turn them "transparent to clicks". */
header[data-testid="stHeader"],
div[data-testid="stToolbar"],
div[data-testid="stDecoration"]{
  background: transparent !important;
  pointer-events: none !important;
}

/* Make sure our icon bar is above everything and fully clickable */
.icon-wrap{
  position: fixed;
  top: 0.75rem;
  left: 0.75rem;
  z-index: 2147483647;
  pointer-events: auto !important;
}

/* Tight row */
.icon-row{
  display:flex;
  gap:8px;
  align-items:center;
  flex-wrap:wrap;
  margin: 0;
  padding: 0;
  pointer-events: auto !important;
}

/* Full-circle clickable area */
.icon-row a.icon-btn,
.icon-row a.icon-btn:visited{
  width:44px;
  height:44px;
  border-radius:999px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  text-decoration:none !important;
  padding:0 !important;

  background:#ffffff !important;
  color:#111111 !important;
  border:1px solid rgba(0,0,0,0.22) !important;

  box-shadow: 0 6px 14px rgba(0,0,0,0.12);
  transition: background 120ms ease, color 120ms ease, transform 120ms ease, box-shadow 120ms ease, border-color 120ms ease;
  cursor:pointer !important;

  pointer-events: auto !important;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
}

/* Base icon */
.icon-row a.icon-btn i{
  color: inherit !important;
  font-size: 17px;
  line-height: 1;
  pointer-events: none; /* keep clicks on the anchor */
}

/* Hover + focus invert (desktop/hover devices) */
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

/* Email icon swap: closed -> open */
.icon-row a.email-btn{
  position: relative;
}

/* stack the two email icons exactly centered */
.icon-row a.email-btn i{
  position: absolute;
  inset: 0;
  display:flex;
  align-items:center;
  justify-content:center;
  pointer-events: none;
  color: inherit !important;
  font-size: 17px;
  line-height: 1;
}

.icon-row a.email-btn .email-open{ opacity: 0; }
.icon-row a.email-btn .email-closed{ opacity: 1; }

.icon-row a.email-btn:hover .email-open,
.icon-row a.email-btn:focus-visible .email-open{
  opacity: 1;
}
.icon-row a.email-btn:hover .email-closed,
.icon-row a.email-btn:focus-visible .email-closed{
  opacity: 0;
}

/* Fix “stuck hover” on touch devices (tap + back keeps hover on iOS sometimes).
   On touch devices, disable hover/focus styling and keep only :active feedback. */
@media (hover: none) and (pointer: coarse){
  .icon-row a.icon-btn:hover,
  .icon-row a.icon-btn:focus-visible{
    background:#ffffff !important;
    color:#111111 !important;
    border:1px solid rgba(0,0,0,0.22) !important;
    transform:none !important;
    box-shadow: 0 6px 14px rgba(0,0,0,0.12) !important;
  }

  .icon-row a.icon-btn:active{
    background:#111111 !important;
    color:#ffffff !important;
    border-color: rgba(255,255,255,0.22) !important;
    transform: translateY(0px) scale(0.98) !important;
    box-shadow: 0 10px 20px rgba(0,0,0,0.18) !important;
  }
}
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""",
    unsafe_allow_html=True,
)

# IMPORTANT: no leading spaces at the start of lines below (prevents markdown code-block rendering)
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

<a class="icon-btn email-btn" href="mailto:{EMAIL}" title="Email">
<i class="fa-solid fa-envelope email-closed"></i>
<i class="fa-solid fa-envelope-open email-open"></i>
</a>
</div>
</div>
""",
    unsafe_allow_html=True,
)
