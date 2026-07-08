from pathlib import Path

import duckdb
import streamlit as st

st.title('Overview')

DB_PATH = Path(__file__).resolve().parents[2] / "data" / "mart.duckdb"


@st.cache_resource
def get_connection():
    return duckdb.connect(str(DB_PATH), read_only=True)


con = get_connection()

trend = con.sql("""
    select
        transaction_date,
        sum(-amount) as total_spend
    from main_marts.mart_transactions
    where status = 'SETTLED'
    group by 1
    order by 1
""").df()

by_category = con.sql("""
    select
        category_id,
        sum(-amount) as total_spend
    from main_marts.mart_transactions
    where status = 'SETTLED'
    group by 1
    order by 2 desc
""").df()

st.subheader("Spend Trend")
st.line_chart(trend, x="transaction_date", y="total_spend")

st.subheader("Spend by Category")
st.bar_chart(by_category, x="category_id", y="total_spend")
