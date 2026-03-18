import streamlit as st

detection_app_page = st.Page(
    page="app_pages/detection_app.py", 
    title="E-Waste Detection Application",
    icon="🤖",
)

# Navigation Setup
pg = st.navigation(
    {
        "Projects": [detection_app_page],
    }
)

# Share on All Pages
st.sidebar.text("Created by 🎧 Kanon14")

# Run Application
pg.run()