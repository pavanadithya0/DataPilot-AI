from pathlib import Path
import sys

# ---------------------------------------------------
# Add Project Root to Python Path
# ---------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# ---------------------------------------------------
# Imports
# ---------------------------------------------------

import streamlit as st

from ai.sql_generator import generate_sql
from ai.sql_executor import execute_sql
from utils.chart_generator import generate_chart
from ai.insights import generate_insights
from utils.kpi import get_kpis

# ---------------------------------------------------
# Cache SQL Generation
# ---------------------------------------------------

@st.cache_data(show_spinner=False)
def cached_generate_sql(question):
    return generate_sql(question)


# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="DataPilot AI",
    page_icon="📊",
    layout="wide"
)
# ---------------------------------
# Initialize Session State
# ---------------------------------

if "history" not in st.session_state:
    st.session_state["history"] = []

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("📊 DataPilot AI")

st.caption("AI Powered Business Intelligence Dashboard")

st.divider()

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------

kpis = get_kpis()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Customers", f"{kpis['customers']:,}")

with col2:
    st.metric("Orders", f"{kpis['orders']:,}")

with col3:
    st.metric("Revenue", f"${kpis['revenue']:,.2f}")

with col4:
    st.metric("Average Order", f"${kpis['avg_order']:,.2f}")

st.divider()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.title("📊 DataPilot AI")

    st.markdown("---")

    st.subheader("Example Questions")

    st.info("""
• Show top 10 customers by revenue

• Monthly revenue

• Revenue by state

• Revenue by category

• Top selling products

• Orders by region

• Average order value

• Payment method distribution

• Inventory below reorder level
""")

    st.markdown("---")

    st.success("Natural Language ➜ SQL")

    st.success("Interactive Charts")

    st.success("AI Business Insights")

    st.success("CSV Download")

    st.markdown("---")

    st.markdown("---")
    st.subheader("🕒 Recent Questions")

history = st.session_state.get("history", [])

if history:
    for q in history[-5:][::-1]:
        st.write(f"• {q}")
else:
    st.write("No questions yet.")
    
    st.caption("Built with Python + Streamlit + Gemini")

# ---------------------------------------------------
# User Input
# ---------------------------------------------------

question = st.text_input(
    "Ask a business question",
    placeholder="Example: Show top 10 customers by revenue"
)

ask = st.button("Ask AI")
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------------------------------------------
# Main Logic
# ---------------------------------------------------

if ask:

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    # ------------------------
    # Generate SQL
    # ------------------------
    try:
         with st.spinner("🤖 Generating SQL..."):
           sql = cached_generate_sql(question)

    # Save question to history
         st.session_state.history.append(question)

    except Exception as e:
        st.error("❌ Failed to generate SQL.")
        st.exception(e)
        st.stop()
    # ------------------------
    # Show SQL
    # ------------------------

    st.subheader("📝 Generated SQL")

    st.code(sql, language="sql")

    # ------------------------
    # Execute SQL
    # ------------------------

    # ------------------------------
# Execute SQL
# ------------------------------

    # ------------------------
    # Execute SQL
    # ------------------------

    try:
        with st.spinner("🗄 Executing Query..."):
            df = execute_sql(sql)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Rows Returned", len(df))

        with col2:
            st.metric("Columns", len(df.columns))

    except Exception as e:
        st.error("❌ Database Error")
        st.exception(e)
        st.stop()

    # ------------------------
    # Empty Result
    # ------------------------

    if df.empty:

        st.warning("No records found.")

        st.stop()

    # ------------------------
    # Show Table
    # ------------------------

    st.subheader("📋 Query Results")

    st.dataframe(
        df,
        use_container_width=True
    )

    # ------------------------
    # Download CSV
    # ------------------------

    st.download_button(
        "📥 Download Results (CSV)",
        data=df.to_csv(index=False),
        file_name="query_results.csv",
        mime="text/csv"
    )

    # ------------------------
    # Chart
    # ------------------------

    fig = generate_chart(df)

    if fig:

        st.subheader("📊 Visualization")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ------------------------
    # AI Insights
    # ------------------------

    try:

        with st.spinner("💡 Generating AI Insights..."):

            insights = generate_insights(question, df)

        st.subheader("🤖 AI Business Insights")

        st.markdown(insights)

    except Exception:

        st.warning("Unable to generate AI insights.")

st.divider()

st.caption(
    """
🚀 DataPilot AI

Built using Python • Streamlit • SQLite • SQLAlchemy • Plotly • Google Gemini
"""
)