import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Career Compass AI",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Custom CSS for Vibrant & Professional Styling ---
st.markdown("""
<style>
    /* Gradient background for the entire page */
    .stApp {
        background-image: linear-gradient(170deg, #EBF5FB 0%, #D6EAF8 100%);
        color: #2C3E50; /* Default text color */
    }

    /* Main container for inputs and results - the white card */
    .main-container {
        background-color: #FFFFFF;
        border-radius: 15px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        padding: 2em;
        margin-top: 20px;
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
        margin-bottom: -50px; /* Pull the main container up */
        position: relative;
        z-index: 2;
    }
    .header h1 {
        font-size: 2.5em;
        font-weight: bold;
        margin: 0;
        color: white !important;
    }
    .header p {
        font-size: 1.2em;
        margin-top: 0.5em;
        color: white !important;
    }
    .header .emoji {
        margin-right: 10px;
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
        color: #34495E;
    }
    
    /* Primary Button styling */
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

    /* Secondary Button styling */
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

    /* Styling for Skill Gaps and Roadmap */
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

# --- ✨ DYNAMIC HELPER FUNCTIONS (AI Logic Simulation) ---
def get_skill_gap_from_ai(current_skills, desired_role):
    """
    Simulates an AI call for skill gap analysis.
    This function now uses the user's input to create generalized gaps.
    """
    time.sleep(1.5)
    # The f-string (f"...") allows us to insert variables like desired_role directly into the text.
    gaps = [
        f"Advanced proficiency in frameworks and tools specific to a **{desired_role}**.",
        f"A portfolio of projects demonstrating skills beyond the ones listed: '{current_skills}'.",
        f"Deep understanding of the core theoretical principles and best practices for the **{desired_role}** field.",
        "Experience with industry-standard collaboration and version control tools (e.g., Git, Jira)."
    ]
    return gaps

def get_roadmap_from_ai(desired_role):
    """
    Simulates an AI call for generating a roadmap.
    This function now uses the user's input to create a generalized roadmap.
    """
    time.sleep(1)
    
    # Simple logic to suggest a different project type based on keywords
    project_suggestion = f"Build an end-to-end project that showcases the typical workflow of a **{desired_role}**. Document the process and host the code on GitHub to demonstrate your capabilities."
    if 'data' in desired_role.lower() or 'analyst' in desired_role.lower():
        project_suggestion = f"Analyze a complex dataset related to an industry you're passionate about. Create a detailed report and an interactive dashboard to showcase the typical workflow of a **{desired_role}**."
    elif 'engineer' in desired_role.lower() or 'developer' in desired_role.lower():
        project_suggestion = f"Develop a full-stack application that solves a real-world problem. This should demonstrate the complete development lifecycle required for a **{desired_role}**."

    roadmap = {
        "Key Topics to Master": [
            f"Specialized online courses (e.g., on Coursera, edX) that focus on the core competencies of a **{desired_role}**.",
            f"Study of foundational algorithms and system design principles pertinent to the **{desired_role}** field.",
            f"Mastery of key libraries and software used by professionals in the **{desired_role}** industry."
        ],
        "Suggested Project Idea": project_suggestion
    }
    return roadmap

# --- Streamlit App UI ---

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = None

# Header
st.markdown("""
<div class="header">
    <h1><span class="emoji">🧭</span> Career Compass AI</h1>
    <p>Your personalized career and skill advisor powered by AI</p>
</div>
""", unsafe_allow_html=True)

# Main container for the input form
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown("<h2>Your Career Path Input</h2>", unsafe_allow_html=True)

current_skills = st.text_area(
    "**Your Current Skills & Experience**",
    height=150,
    placeholder="e.g., Python, SQL, Tableau, project management"
)

desired_role = st.text_input(
    "**Your Desired Career Goal**",
    placeholder="e.g., Machine Learning Engineer, UI/UX Designer, Full-Stack Developer"
)

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Analyze My Career Path", use_container_width=True, type="primary"):
        if current_skills and desired_role:
            with st.spinner('Analyzing your profile and generating your roadmap...'):
                skill_gaps = get_skill_gap_from_ai(current_skills, desired_role)
                roadmap = get_roadmap_from_ai(desired_role) # Pass desired_role here
                st.session_state.results = {"gaps": skill_gaps, "roadmap": roadmap}
            st.success('✅ Analysis Complete!')
            st.balloons()
        else:
            st.warning("⚠️ Please fill in both fields.")

with col2:
    if st.session_state.results:
        if st.button("Start Over", use_container_width=True):
            st.session_state.results = None
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Close the main input container

# --- Display Results ---
if st.session_state.results:
    st.markdown('<div class="main-container">', unsafe_allow_html=True) # Results in a separate card

    st.markdown("<h3 style='color: #E74C3C;'>⚠️ Identified Skill Gaps</h3>", unsafe_allow_html=True)
    for gap in st.session_state.results["gaps"]:
        st.markdown(f'<div class="skill-gap-item">{gap}</div>', unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)

    st.markdown("<h3 style='color: #2ECC71;'>📖 Your Personalized Learning Roadmap</h3>", unsafe_allow_html=True)
    for topic in st.session_state.results["roadmap"]["Key Topics to Master"]:
        st.markdown(f'<div class="roadmap-item">{topic}</div>', unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="project-idea">
        <h4>💡 Suggested Project Idea</h4>
        <p>{st.session_state.results["roadmap"]["Suggested Project Idea"]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
