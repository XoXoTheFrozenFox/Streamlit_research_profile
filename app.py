import streamlit as st

st.set_page_config(page_title="Bernard Swanepoel — Research Profile", page_icon="🌞", layout="wide")

# --- Header ---
st.title("🌞 Bernard Swanepoel")
st.subheader("MSc Computer Science — Sunspot Classification with Deep Learning")

col1, col2, col3 = st.columns([1.2, 1.0, 1.0])
with col1:
    st.markdown(
        """
**Focus:** Automated sunspot classification using deep learning  
**Interests:** Solar physics • Computer vision • Imbalanced learning • Explainability  
**Portfolio:** https://xoxothefrozenfox.github.io/react-personal-portfolio/
        """
    )
with col2:
    st.markdown("### Quick links")
    st.markdown("- Portfolio website")
    st.markdown("- GitHub")
    st.markdown("- LinkedIn")
with col3:
    st.markdown("### Contact")
    st.markdown("- Email: (add yours)")
    st.markdown("- University: (add yours)")

st.divider()

# --- Main content ---
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
        """
    )

    st.markdown("## Highlights")
    st.info(
        "Tip: Replace these placeholders with your real results (accuracy/F1, dataset size, best model, and key findings)."
    )
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Best Macro-F1", "—")
    m2.metric("Classes", "—")
    m3.metric("Images", "—")
    m4.metric("Backbone", "—")

with right:
    st.markdown("## Live profile embed")
    st.write("If the embed is blocked by the site’s headers, the button below still works.")
    st.link_button("Open my portfolio", "https://xoxothefrozenfox.github.io/react-personal-portfolio/")

    st.markdown("## Repo / artifacts")
    st.markdown(
        """
- Paper / thesis draft: (add link)  
- Dataset: (add link)  
- Demo notebook: (add link)  
        """
    )

st.divider()

# --- Footer ---
st.caption("© 2026 Bernard Swanepoel • Built with Streamlit")
