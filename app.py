import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Career Compass AI",
    page_icon="🧭",
    layout="centered", # Use 'centered' for a cleaner look on most screens
    initial_sidebar_state="auto"
)

# --- Custom CSS for Professional Styling ---
# This CSS will inject a custom style into the app for colors, buttons, etc.
st.markdown("""
<style>
    /* Main background color */
    .stApp {
        background-color: #0F172A; /* Deep navy blue */
    }

    /* Title styling */
    h1 {
        color: #FFFFFF; /* White text */
        text-shadow: 2px 2px 4px #000000;
    }

    /* Subheader styling */
    p, .stMarkdown {
        color: #CBD5E1; /* Light gray for text */
    }

    /* Button styling */
    .stButton>button {
        background-color: #14B8A6; /* Teal accent color */
        color: #FFFFFF; /* White text on button */
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #0D9488; /* Darker teal on hover */
    }

    /* Text input and text area styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1E293B; /* Slightly lighter navy */
        color: #FFFFFF;
        border-radius: 8px;
    }

</style>
""", unsafe_allow_html=True)


# --- Helper Functions (Your AI Logic Goes Here) ---
def get_skill_gap_from_ai(current_skills, desired_role):
    """Placeholder function to simulate an AI call for skill gap analysis."""
    time.sleep(2) # Simulate AI processing time
    gaps = [
        "Advanced proficiency in Deep Learning frameworks (TensorFlow/PyTorch)",
        "Experience with Natural Language Processing (NLP) libraries like Hugging Face Transformers",
        "Cloud computing knowledge (AWS Sagemaker or Google AI Platform)",
        "Understanding of MLOps principles and tools (e.g., Docker, Kubernetes)"
    ]
    return gaps

def get_roadmap_from_ai(skill_gaps):
    """Placeholder function to simulate an AI call for generating a roadmap."""
    time.sleep(1) # Simulate AI processing time
    roadmap = {
        "Key Topics to Master": [
            "1. Deep Learning Specialization (Coursera - Andrew Ng)",
            "2. Natural Language Processing with Transformers (Hugging Face Course)",
            "3. Cloud ML Engineering Fundamentals"
        ],
        "Suggested Project Idea": "Build a sentiment analysis application for customer reviews using a pre-trained model like BERT and deploy it as a simple API."
    }
    return roadmap

# --- Streamlit App UI ---

# Initialize session state to hold the results
if 'results' not in st.session_state:
    st.session_state.results = None

# Centered Title and Subheader
st.markdown("<h1 style='text-align: center;'>🧭 Career Compass AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94A3B8;'>Your personalized career and skill advisor powered by AI</p>", unsafe_allow_html=True)

st.write("---")

# User Inputs
current_skills = st.text_area(
    "**Your Current Skills & Experience**",
    height=150,
    placeholder="Describe your current skills, technologies you know, and relevant experience..."
)

desired_role = st.text_input(
    "**Your Desired Career Goal**",
    placeholder="For example: 'Data Scientist specializing in NLP' or 'Full Stack Developer'"
)

# Analyze Button - In a two-column layout for better alignment
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Analyze My Career Path", use_container_width=True, type="primary"):
        if current_skills and desired_role:
            with st.spinner('Analyzing your profile and generating your roadmap... This may take a moment.'):
                # --- Backend Logic ---
                skill_gaps = get_skill_gap_from_ai(current_skills, desired_role)
                roadmap = get_roadmap_from_ai(skill_gaps)
                
                # Store results in session state
                st.session_state.results = {"gaps": skill_gaps, "roadmap": roadmap}
                
            st.success('✅ Your personalized analysis is complete! See results below.')
            st.balloons() # Fun little interactive element
        else:
            st.warning("⚠️ Please fill in both fields to get your analysis.")

# Add a 'Start Over' button that clears the results
with col2:
    if st.session_state.results:
        if st.button("Start Over", use_container_width=True):
            st.session_state.results = None
            st.experimental_rerun() # Rerun the app to clear the view

# --- Display Results ---
# Only show this section if results exist in the session state
if st.session_state.results:
    st.write("---")
    st.markdown("## 📊 Your Personalized Analysis")

    # Use an expander to keep the UI clean
    with st.expander("Click here to view your detailed analysis", expanded=True):
        
        # Display Skill Gaps
        st.subheader("Identified Skill Gaps")
        for gap in st.session_state.results["gaps"]:
            st.markdown(f"- {gap}")
        
        st.write("\n") # Add some space

        # Display Learning Roadmap
        st.subheader("🚀 Your Recommended Learning Roadmap")
        st.markdown("**Key Topics to Master:**")
        for topic in st.session_state.results["roadmap"]["Key Topics to Master"]:
            st.markdown(f"  - {topic}")
        
        st.markdown("\n**Suggested Project Idea:**")
        st.info(st.session_state.results["roadmap"]["Suggested Project Idea"])
