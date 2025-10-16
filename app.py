import streamlit as st

st.set_page_config(page_title="Os Sparnauê 🍻", layout="wide")

st.navigation([
    st.Page("pages/1_Home.py", title="Home 🏠", icon="🏠"),
    st.Page("pages/2_Cadastro.py", title="Cadastro 🔐", icon="🧾"),
    st.Page("pages/3_Dashboard.py", title="Dashboard 📊", icon="📊"),
],position="top").run()
