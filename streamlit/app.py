import streamlit as st

st.set_page_config(
    page_title="Personal Finance Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "https://github.com/ddvkhanh/personal-finance-tracker",
    }
)

pages = [
    st.Page("pages/overview.py" ,title="Home"),
]

pg = st.navigation(pages)

with st.sidebar:
    st.markdown("## Personal Finance Dashboard")
    st.markdown("This dashboard helps you track your personal finances")
    
pg.run()