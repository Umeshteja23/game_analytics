import streamlit as st
import psycopg2
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Tennis Analytics Dashboard",
    page_icon="🎾",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    text-align: center;
}
.metric-value {
    font-size: 32px;
    font-weight: bold;
}
.metric-label {
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align:center; color:#1f77b4;'>🎾 Tennis Data Analytics Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Powered by SportRadar API • PostgreSQL • Streamlit</p>",
    unsafe_allow_html=True
)

# ---------------- DB CONNECTION ----------------
conn = psycopg2.connect(
    host="localhost",
    database="game_analytics",
    user="postgres",
    password="postgres123",
    port=5432,
    options="-c search_path=game_analytics"
)

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔎 Filters")

competition_type = st.sidebar.selectbox(
    "Competition Type",
    ["All", "singles", "doubles"]
)

# ---------------- OVERVIEW METRICS ----------------
overview_query = """
SELECT
    (SELECT COUNT(*) FROM competitions) AS competitions,
    (SELECT COUNT(*) FROM categories) AS categories,
    (SELECT COUNT(*) FROM venues) AS venues,
    (SELECT COUNT(*) FROM competitors) AS competitors;
"""
overview = pd.read_sql(overview_query, conn).iloc[0]

col1, col2, col3, col4 = st.columns(4)

def metric_card(col, value, label, icon):
    col.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{icon} {value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)

metric_card(col1, overview.competitions, "Competitions", "🏆")
metric_card(col2, overview.categories, "Categories", "📂")
metric_card(col3, overview.venues, "Venues", "📍")
metric_card(col4, overview.competitors, "Competitors", "👥")

st.markdown("---")

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(["🏆 Competitions", "🌍 Venues", "🥇 Rankings"])

# ---------------- TAB 1: COMPETITIONS ----------------
with tab1:
    st.subheader("Competition Explorer")

    comp_query = """
    SELECT competition_name, type, gender
    FROM competitions
    """
    if competition_type != "All":
        comp_query += f" WHERE type = '{competition_type}'"

    comp_df = pd.read_sql(comp_query, conn)
    st.dataframe(comp_df, use_container_width=True)

# ---------------- TAB 2: VENUES ----------------
with tab2:
    st.subheader("Venues by Country")

    venue_query = """
    SELECT country_name, COUNT(*) AS venue_count
    FROM venues
    GROUP BY country_name
    ORDER BY venue_count DESC
    LIMIT 10;
    """
    venue_df = pd.read_sql(venue_query, conn)

    st.bar_chart(
        venue_df.set_index("country_name"),
        use_container_width=True
    )

# ---------------- TAB 3: RANKINGS ----------------
with tab3:
    st.subheader("Doubles Rankings")

    ranking_query = """
    SELECT c.name, r.rank, r.points, r.competitions_played
    FROM competitor_rankings r
    JOIN competitors c
    ON r.competitor_id = c.competitor_id
    ORDER BY r.rank;
    """
    ranking_df = pd.read_sql(ranking_query, conn)

    st.table(ranking_df)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built by Umesh Teja Chowdary | Data Analytics Project</p>",
    unsafe_allow_html=True
)

conn.close() 

