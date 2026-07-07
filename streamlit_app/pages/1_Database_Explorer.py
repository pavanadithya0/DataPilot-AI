import sqlite3
import pandas as pd
import streamlit as st

DATABASE = "database/business.db"

conn = sqlite3.connect(DATABASE)

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

st.title("🗄 Database Explorer")

table = st.selectbox(
    "Select Table",
    tables["name"]
)

df = pd.read_sql(
    f"SELECT * FROM {table}",
    conn
)

st.dataframe(
    df,
    use_container_width=True
)