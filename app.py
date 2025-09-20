import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Career Compass AI",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Custom CSS for Vibrant & Professional Styling (Inspired by your images) ---
st.markdown("""
<style>
    /* Gradient background for the entire page */
    .stApp {
        background-image: linear-gradient(170deg, #EBF5FB 0%, #D6EAF8 100%);
    }

    /* Main container for inputs - the white card */
    .main-container {
        background-color: #FFFFFF;
        border-radius: 15px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        padding: 2em;
        margin-top: -100px; /* Pulls the card up to overlap the header */
        z-index: 1;
        position: relative;
    }

    /* Header with the vibrant blue gradient */
    .header {
        background-image: linear-gradient(90deg, #3498DB 0%, #2980B9 100%);
        padding: 3em 1em;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2em;
    }
    .header h1 {
        font-size: 2.5em;
        font-weight: bold;
        margin: 0;
    }
    .header p {
        font-size: 1.2em;
        margin-top: 0.5em;
    }

    /* Input field labels */
    label {
        color: #2C3E50 !important;
        font-size: 1.1em;
        font-weight: 600;
        margin-bottom: 0.5em;
    }

    /* Text input and text area styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #F8F9FA;
        border: 1px solid #BDC3C7;
        border-radius: 8px;
    }
    
    /* Primary Button styling (Analyze My Career Path) */
    .stButton>button.primary {
        background-color: #3498DB;
        color: #FFFFFF;
        border: none;
        border-radius: 8px;
        padding: 12px 0;
        font-weight: bold;
        font-size: 1.1em;
        transition: background-color 0.3s ease;
    }
    .stButton>button.primary:hover {
        background-color: #2980B9;
    }

    /* Secondary Button styling (Start Over) */
    .stButton>button:not(.primary) {
        background-color: #ECF0F1;
        color: #7F8C8D;
        border: 1px solid #BDC3C7;
        padding: 12px 0;
        font-weight: bold;
        font-size: 1.1em;
        transition: all 0.3s ease;
    }
    .stButton>button:not(.primary):hover {
        background-color: #BDC3C7;
        color: #FFFFFF;
    }

    /* Styling for Skill Gaps and Roadmap (from your images) */
    .skill-gap-item {
        background-color: #FADBD8;
        border-left: 5px solid #E74C3C;
        padding: 12px 15px;
        margin: 10px 0;
        border-radius: 5px;
        color: #A93226;
        font-weight: 500;
    }
    .roadmap-item {
        background-color: #D5F5E3;
        border-left: 5px solid #2ECC71;
        padding: 12px 15px;
        margin: 10px 0;
        border-radius: 5px;
        color: #239B56;
        font-weight: 500;
    }
    .project-idea {
        background-image: linear-gradient(90deg, #A9DFBF 0%, #76D7C4 100%);
        padding: 20px;
        border-radius: 8px;
        color: #145A32;
    }
    .project-idea h4 {
        color: #145A32;
        margin-bottom: 0.5em;
    }

</style>
""", unsafe_allow_html=True)

# --- Helper Functions (Your AI Logic) ---
def get_skill_gap_from_ai(current_skills, desired_role):
    time.sleep(1.5)
    gaps = [
        "Industry-specific technical skills and tools",
        "Project management and collaboration methodologies",
        "Communication and presentation skills for technical topics",
        "Continuous learning and adaptation strategies"
    ]
    return gaps

def get_roadmap_from_ai(skill_gaps):
    time.sleep(1)
    roadmap = {
        "Key Topics to Master": [
            "Core technical skills and industry-standard tools",
            "Project-based learning and portfolio development",
            "Professional networking and community engagement",
            "Certification and skill validation programs"
        ],
        "Suggested Project Idea": "Create a comprehensive portfolio project that demonstrates key skills relevant to a Data Analyst, including data cleaning, analysis, visualization, documentation, and presentation materials."
    }
    return roadmap

# --- Streamlit App UI ---

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = None

# Header
st.markdown("""
<div class="header">
    <h1>🧭 Career Compass AI</h1>
    <p>Your personalized career and skill advisor powered by AI</p>
</div>
""", unsafe_allow_html=True)

# Main container for the input form
st.markdown('<div class="main-container">', unsafe_allow_html=True)

current_skills = st.text_area(
    "**Your Current Skills & Experience**",
    height=150,
    placeholder="Describe your current skills, technologies you know, and relevant experience..."
)

desired_role = st.text_input(
    "**Your Desired Career Goal**",
    placeholder="For example: 'Data Scientist specializing in NLP' or 'Full Stack Developer'"
)

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Analyze My Career Path", use_container_width=True, type="primary"):
        if current_skills and desired_role:
            with st.spinner('Analyzing your profile and generating your roadmap...'):
                skill_gaps = get_skill_gap_from_ai(current_skills, desired_role)
                roadmap = get_roadmap_from_ai(skill_gaps)
                st.session_state.results = {"gaps": skill_gaps, "roadmap": roadmap}
            st.success('✅ Analysis Complete!')
            st.balloons()
        else:
            st.warning("⚠️ Please fill in both fields.")

with col2:
    if st.session_state.results:
        if st.button("Start Over", use_container_width=True):
            st.session_state.results = None
            st.rerun() # <-- THE FIX IS HERE!

st.markdown('</div>', unsafe_allow_html=True) # Close the main container

# --- Display Results ---
if st.session_state.results:
    st.markdown('<div class="main-container">', unsafe_allow_html=True) # Results in a separate card

    # Skill Gaps
    st.markdown("<h3 style='color: #E74C3C;'>⚠️ Identified Skill Gaps</h3>", unsafe_allow_html=True)
    st.write("Based on your current skills and career goal, here are the most critical areas to focus on:")
    for gap in st.session_state.results["gaps"]:
        st.markdown(f'<div class="skill-gap-item">{gap}</div>', unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)

    # Learning Roadmap
    st.markdown("<h3 style='color: #2ECC71;'>📖 Your Personalized Learning Roadmap</h3>", unsafe_allow_html=True)
    st.write("Here's a strategic path to acquire the necessary skills and advance your career:")
    for topic in st.session_state.results["roadmap"]["Key Topics to Master"]:
        st.markdown(f'<div class="roadmap-item">{topic}</div>', unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)

    # Suggested Project
    st.markdown(f"""
    <div class="project-idea">
        <h4>💡 Suggested Project Idea</h4>
        <p>{st.session_state.results["roadmap"]["Suggested Project Idea"]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
