import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Us")
def show_contact_form():
    contact_form()

#  Hero Section
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("assets/2.svg", width=250)
    
with col2:
    st.title("StartPrep ✨", anchor=False)
    st.write("Start Your Preparation Now")
    st.write("StartPrep is a smart career prep platform built to guide students through personalized learning roadmaps, real-time progress tracking, and skill-based training. From mock tests to mentorship, it bridges the gap between academics and industry, helping you prepare with purpose, clarity, and confidence.")
    
    if st.button("📩 Contact Us"):
        show_contact_form()
        
# Add from here
st.markdown("---")

st.subheader(":material/rocket_launch: What We Offer")

# For Students
st.markdown("### :material/school: For Students")
st.markdown(
    """
    - :material/directions: Personalized Learning Roadmaps  
    - :material/assignment: Mock Tests & Assessments  
    - :material/track_changes: Real-Time Progress Tracking  
    - :material/badge: Resume Building & Interview Prep  
    - :material/leaderboard: Smart Dashboard & Leaderboards  
    """
)

# Divider
st.markdown("")

# For Colleges
st.markdown("### :material/apartment: For Colleges (T&P Cells)")
st.markdown(
    """
    - :material/insights: Student Performance Dashboards  
    - :material/extension: Custom Training Modules  
    - :material/analytics: Placement Readiness Analysis  
    - :material/menu_book: Industry-Aligned Prep Content  
    - :material/auto_graph: Weekly Progress Reports  
    """
)

# Divider
st.markdown("")

# For Companies
st.markdown("### :material/business_center: For Companies")
st.markdown(
    """
    - :material/person_search: Pre-Screened Candidate Access  
    - :material/tune: Role-Based Shortlisting Tools  
    - :material/handshake: Partnership for Campus Drives  
    - :material/quiz: Skill-Specific Assessment Insights  
    - :material/insights: Data-Driven Hiring Support  
    """
)

st.markdown("---")
