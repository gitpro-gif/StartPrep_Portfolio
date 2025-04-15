import streamlit as st

about_page = st.Page(
    page="views/about_me.py",
    title="About us",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/dashboard.py",
    title="Company Progress Dashboard",
    icon=":material/bar_chart:",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="StartPrep Buddy",
    icon=":material/smart_toy:",
)


# SHARED LOGO ON ALL PAGES
# st.sidebar.image("assets/bg-removed-logo.png", use_column_width=True)
# st.sidebar.markdown("---")  # Horizontal line

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)


st.sidebar.text("Start Your Preparation Now")

pg.run()