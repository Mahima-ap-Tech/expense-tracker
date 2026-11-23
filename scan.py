
import streamlit as st
from login import show_login

st.set_page_config(
    page_title="My Expense Tracker",
    page_icon="🪙"
)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "budget" not in st.session_state:
    st.session_state.budget = 0

if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Login page
if not st.session_state.logged_in:
    show_login()
    st.stop()


st.markdown("""
<style>

/* Main page background */
.stApp {
    background-color:#344B3F;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color:#938BA3;
}

/* Main page font */
.stApp p,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp label {
    color: white;
}

/* Sidebar font */
[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)


# Create separate pages
home_pg = st.Page(
    "home.py",
    title="Home",
    url_path="home",
    default=True
)

about_pg = st.Page(
    "aboutus.py",
    title="About Us",
    url_path="aboutus"
)

dash_pg = st.Page(
    "dashboard.py",
    title="Dashboard",
    url_path="dashboard"
)

help_pg = st.Page(
    "help.py",
    title="Help",
    url_path="help"
)

# Navigation
pg = st.navigation(
    [home_pg, about_pg, dash_pg, help_pg],
    position="hidden"
)

# Sidebar
st.sidebar.title("Spend Wise 💳")

if st.sidebar.button("Home 🏠", use_container_width=True):
    st.switch_page(home_pg)

if st.sidebar.button("About Us 👥", use_container_width=True):
    st.switch_page(about_pg)

if st.sidebar.button("Dashboard 📊", use_container_width=True):
    st.switch_page(dash_pg)

if st.sidebar.button("Help 💡", use_container_width=True):
    st.switch_page(help_pg)

if st.sidebar.button("Logout 🔓", use_container_width=True):
    st.session_state.logged_in = False
    st.rerun()

# Display selected page
pg.run()













