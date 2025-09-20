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
    /* Main background color - light and clean */
    .stApp {
        background-color: #F8F9FA; /* Very light gray/off-white */
    }

    /* Header (Career Compass AI) */
    h1 {
        color: #2C3E50; /* Darker blue for prominence */
        text-align: center;
        margin-bottom: 0.5em;
    }
    
    /* Subheader (Your personalized career and skill advisor powered by AI) */
    p {
        color: #7F8C8D; /* Muted gray for body text */
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 2em;
    }

    /* Container for inputs and results */
    .css-1r6dm7m, .css-znku1x { /* Specific Streamlit container classes for general content */
        background-color: #FFFFFF; /* White card background */
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* Soft shadow for depth */
        padding: 25px;
        margin-bottom: 20px;
    }
    
    /* Input field labels */
    label {
        color: #2C3E50 !important; /* Darker blue for labels */
        font-size: 1.1em;
        font-weight: 600;
    }

    /* Text input and text area styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #ECF0F1; /* Light gray for input fields */
        color: #34495E; /* Dark text in inputs */
        border-radius: 8px;
        border: 1px solid #BDC3C7; /* Subtle border */
        padding: 10px;
        font-size: 1em;
    }

    /* Primary Button styling (Analyze My Career Path) */
    .stButton>button.primary {
        background-color: #3498DB; /* Bright blue */
        color: #FFFFFF;
        border-radius: 8px;
        border: none;
        padding: 12px 25px;
        font-weight: bold;
        font-size: 1.1em;
        transition: background-color 0.2s;
    }
    .stButton>button.primary:hover {
        background-color: #2980B9; /* Darker blue on hover */
    }

    /* Secondary Button styling (Start Over) */
    .stButton>button:not(.primary) {
        background-color: #BDC3C7; /* Muted gray */
        color: #34495E;
        border-radius: 8px;
        border: none;
        padding: 12px 25px;
        font-weight: bold;
        font-size: 1.1em;
        transition: background-color 0.2s;
    }
    .stButton>button:not(.primary):hover {
        background-color: #95A5A6; /* Darker gray on hover */
    }

    /* Success message style */
    .stSuccess {
        background-color: #D4EDDA; /* Light green */
        color: #155724; /* Dark green text */
        border-color: #C3E6CB;
        border-radius: 8px;
    }

    /* Warning message style */
    .stWarning {
        background-color: #FFF3CD; /* Light yellow */
        color: #856404; /* Dark yellow text */
        border-color: #FFEBA2;
        border-radius: 8px;
    }

    /* Info message style (for Suggested Project Idea) */
    .stInfo {
        background-color: #D1ECF1; /* Light blue */
        color: #0C5460; /* Dark blue text */
        border-color: #BEE5EB;
        border-radius: 8px;
    }

    /* Expander styling for results */
    .streamlit-expanderHeader {
        background-color: #ECF0F1; /* Light gray header for expander */
        color: #2C3E50;
        border-radius: 8px;
        padding: 10px;
        font-size: 1.1em;
        font-weight: 600;
        margin-top: 20px;
    }
    .streamlit-expanderContent {
        background-color: #FDFEFE; /* Slightly lighter content area */
        border-bottom-left-radius: 8px;
        border-bottom-right-radius: 8px;
        padding: 15px;
    }
    
    /* Styling for the Skill Gap items (red outline like your image) */
    .stExpander .stMarkdown > p > strong:nth-child(2), /* Targeting the specific bold text */
    .stExpander .stMarkdown > ul > li {
        background-color: #F8D7DA; /* Light red background */
        border-left: 5px solid #DC3545; /* Red left border */
        padding: 8px 15px;
        margin: 8px 0;
        border-radius: 4px;
        color: #721C24; /* Dark red text */
    }

    /* Styling for the Roadmap items (green outline like your image) */
    .stExpander .stMarkdown > h3 + ul > li { /* Target UL immediately after H3 */
        background-color: #D4EDDA; /* Light green background */
        border-left: 5px solid #28A745; /* Green left border */
        padding: 8px 15px;
        margin: 8px 0;
        border-radius: 4px;
        color: #155724; /* Dark green text */
    }

    /* Specific title for "Identified Skill Gaps" within expander */
    .stExpander h3:first-of-type {
        color: #DC3545; /* Red for skill gaps title */
        font-weight: bold;
    }
    /* Specific title for "Recommended Learning Roadmap" within expander */
    .stExpander h3:nth-of-type(2) {
        color: #28A745; /* Green for roadmap title */
        font-weight: bold;
    }
    
    /* Custom divider */
    hr {
        border-top: 1px solid #E0E0E0; /* Light gray divider */
        margin-top: 25px;
        margin-bottom: 25px;
    }

</style>
""", unsafe_allow_html=True)


# --- Helper Functions (Your AI Logic Goes Here) ---
def get_skill_gap_from_ai(current_skills, desired_role):
    """Placeholder function to simulate an AI call for skill gap analysis."""
    time.sleep(2) # Simulate AI processing time
    gaps = [
        "Industry-specific technical skills and tools (e.g., advanced Excel functions for financial analysis, specific industry software)",
        "Project management and collaboration methodologies (e.g., Agile, Scrum)",
        "Communication and presentation skills for technical topics to non-technical stakeholders",
        "Continuous learning and adaptation strategies in a fast-evolving data landscape"
    ]
    return gaps

def get_roadmap_from_ai(skill_gaps):
    """Placeholder function to simulate an AI call for generating a roadmap."""
    time.sleep(1) # Simulate AI processing time
    roadmap = {
        "Key Topics to Master": [
            "Core technical skills and industry-standard tools for Data Analysts (e.g., Python for data manipulation, advanced SQL for complex queries, Power BI/Tableau for visualization)",
            "Project-based learning and portfolio development (e.g., real-world data analysis projects)",
            "Professional networking and community engagement for data professionals",
            "Certification and skill validation programs relevant to Data Analyst roles (e.g., Microsoft Certified: Data Analyst Associate)"
        ],
        "Suggested Project Idea": "Create a comprehensive portfolio project that demonstrates key skills relevant to a Data Analyst, including data cleaning, analysis, visualization, documentation, and presentation materials. For example, analyze a public dataset on customer churn or sales performance."
    }
    return roadmap

# --- Streamlit App UI ---

# Initialize session state to hold the results
if 'results' not in st.session_state:
    st.session_state.results = None

# Centered Title and Subheader
st.markdown("<h1>🧭 Career Compass AI</h1>", unsafe_allow_html=True)
st.markdown("<p>Your personalized career and skill advisor powered by AI</p>", unsafe_allow_html=True)

st.write("---")

# Input Card
st.markdown("<h3>Your Career Path Input</h3>", unsafe_allow_html=True) # Custom title for input section
current_skills = st.text_area(
    "**Your Current Skills & Experience**",
    height=150,
    placeholder="Describe your current skills, technologies you know, and relevant experience. For example: 'I know Python and SQL, and have experience creating dashboards with Tableau. I've worked on data analysis projects for 2 years.'"
)

desired_role = st.text_input(
    "**Your Desired Career Goal**",
    placeholder="What career role are you aiming for? For example: 'Data Scientist specializing in NLP' or 'Full Stack Developer'"
)

# Buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Analyze My Career Path", use_container_width=True, type="primary"):
        if current_skills and desired_role:
            with st.spinner('Analyzing your profile and generating your roadmap... This may take a moment.'):
                # --- Backend Logic ---
                skill_gaps = get_skill_gap_from_ai(current_skills, desired_role)
                roadmap = get_roadmap_from_ai(skill_gaps)
                
                # Store results in session state
                st.session_state.results = {"gaps": skill_gaps, "roadmap": roadmap, "input_skills": current_skills, "input_goal": desired_role}
                
            st.success('✅ Your personalized analysis is complete! See results below.')
            st.balloons()
        else:
            st.warning("⚠️ Please fill in both fields to get your analysis.")

with col2:
    if st.session_state.results:
        if st.button("Start Over", use_container_width=True):
            st.session_state.results = None
            st.experimental_rerun()

# --- Display Results ---
if st.session_state.results:
    st.write("---")
    st.markdown("<h2>📊 Your Personalized Analysis</h2>", unsafe_allow_html=True)

    # Display User Inputs inside a card-like structure
    st.markdown(f"""
    <div style="background-color: #EBF5FB; padding: 15px; border-radius: 8px; margin-bottom: 20px; border-left: 5px solid #3498DB;">
        <h4 style="color: #2C3E50; margin-top: 0;">Career Goal</h4>
        <p style="color: #34495E; text-align: left; font-style: italic;">"{st.session_state.results["input_goal"]}"</p>
        <h4 style="color: #2C3E50; margin-top: 15px;">Current Skills</h4>
        <p style="color: #34495E; text-align: left; font-style: italic;">"{st.session_state.results["input_skills"]}"</p>
    </div>
    """, unsafe_allow_html=True)

    # Use an expander for the detailed analysis
    with st.expander("Click here to view your detailed analysis", expanded=True):
        # Display Skill Gaps
        st.markdown("<h3 style='color: #DC3545;'>⚠️ Identified Skill Gaps</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #721C24; text-align: left; font-size: 0.95em;'>Based on your current skills and career goal, here are the most critical areas to focus on:</p>", unsafe_allow_html=True)
        for gap in st.session_state.results["gaps"]:
            st.markdown(f"<ul><li>{gap}</li></ul>", unsafe_allow_html=True) # Wrap in ul/li for list styling

        st.write("\n") # Add some space

        # Display Learning Roadmap
        st.markdown("<h3 style='color: #28A745;'>📖 Your Personalized Learning Roadmap</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #155724; text-align: left; font-size: 0.95em;'>Here's a strategic path to acquire the necessary skills and advance your career:</p>", unsafe_allow_html=True)
        st.markdown("**Key Topics to Master:**", unsafe_allow_html=True)
        for topic in st.session_state.results["roadmap"]["Key Topics to Master"]:
            st.markdown(f"<ul><li>{topic}</li></ul>", unsafe_allow_html=True) # Wrap in ul/li for list styling
        
        st.markdown("<h4 style='color: #0C5460; margin-top: 20px;'>💡 Suggested Project Idea</h4>", unsafe_allow_html=True)
        st.info(st.session_state.results["roadmap"]["Suggested Project Idea"])
