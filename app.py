"""BrandPulse AI — Presentation layer and navigation router."""

import streamlit as st

st.set_page_config(
    page_title="BrandPulse AI · Audience & Content Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom header styling
st.markdown("""
<style>
    [data-testid="stHeader"] {
        background: transparent;
    }
    .stApp {
        background-color: #090D16;
    }
    div[data-testid="stMetric"] {
        background-color: #111A2E;
        padding: 16px 20px;
        border-radius: 10px;
        border: 1px solid #243456;
    }
    div[data-testid="stMetricValue"] > div {
        color: #38BDF8;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

pages = st.navigation([
    st.Page("views/overview.py", title="Executive Overview", icon="📈", default=True),
    st.Page("views/recommendations.py", title="What to Post Next", icon="💡"),
    st.Page("views/brands.py", title="Brand Benchmarks", icon="🏷️"),
    st.Page("views/content.py", title="Content Attributes", icon="🎬"),
    st.Page("views/timing.py", title="Posting Timing & Rhythm", icon="⏱️"),
    st.Page("views/adjusted.py", title="Adjusted Mixed-Effects", icon="🔬"),
    st.Page("views/sentiment.py", title="Multilingual Sentiment", icon="💬"),
    st.Page("views/exports.py", title="Reports & Exports", icon="📑"),
    st.Page("views/method.py", title="Methodology & Rigor", icon="📖"),
])
pages.run()
