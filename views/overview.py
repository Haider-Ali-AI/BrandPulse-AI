import streamlit as st

from src.analytics.compare import compare_groups
from src.ui import brand_label, get_data, median_ci_chart, sidebar_filters, source_banner

loaded = get_data()
st.title("BrandPulse AI 📊")
st.caption("Cross-Brand YouTube Content Intelligence & Evidence-Based Engagement Analytics for Top Apparel Brands.")
source_banner(loaded)

videos = sidebar_filters(loaded.data.videos)
if videos.empty:
    st.info("No videos match the current filters.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Brands Tracked", videos["brand_id"].nunique())
c2.metric("Videos Analysed", f"{len(videos):,}")
c3.metric("Median Engagement Rate", f"{videos['er_views'].median():.2%}",
          help="(likes + comments) ÷ views, median across the filtered videos")
c4.metric("Comments Processed", f"{len(loaded.data.comments):,}")

st.markdown("<br>", unsafe_allow_html=True)

summary = compare_groups(videos, "brand_id", "er_views")
st.plotly_chart(median_ci_chart(summary, "Median engagement rate by brand (95% bootstrap CI)", "Engagement rate",
                                label=brand_label, reference=videos["er_views"].median()),
                width="stretch")
st.caption("Dot = median, line = 95% bootstrap confidence interval, dotted line = overall cohort median. "
           "Brand differences partly reflect audience size and paid distribution; use **Content Attributes** for "
           "within-brand controlled comparisons.")

with st.expander("Key Methodological Guardrails & Principles"):
    st.markdown(
        "- **Pakistan-focused brand content, not verified audience location:** YouTube API does not reveal viewer geography.\n"
        "- **Strict statistical testing:** Mann-Whitney U, Cliff's delta, and Benjamini-Hochberg FDR adjustments.\n"
        "- **Paid view filtering:** Videos showing artificial view spikes without proportional likes are quarantined by default.\n"
        "- **Sample size thresholds:** Cohorts with n < 20 are preserved for transparency but excluded from statistical hypothesis testing."
    )
