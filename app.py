from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'career_compass_secret_key'

def get_skill_gap_from_ai(current_skills, career_goal):
    """
    Placeholder function to simulate AI-powered skill gap analysis.
    
    Real LLM Prompt would be:
    "Based on the current skills: '{current_skills}' and the career goal: '{career_goal}', 
    analyze the skill gaps and identify the top 3-4 most critical missing skills needed 
    to achieve this career goal. Return a concise list of specific skills, technologies, 
    or competencies that need to be developed."
    """
    # Simulated AI response based on common career transitions
    skill_gaps = []
    
    # Parse inputs to provide realistic skill gap suggestions
    current_lower = current_skills.lower()
    goal_lower = career_goal.lower()
    
    if 'data scientist' in goal_lower or 'machine learning' in goal_lower:
        if 'python' not in current_lower:
            skill_gaps.append("Advanced Python programming for data science")
        if 'machine learning' not in current_lower and 'ml' not in current_lower:
            skill_gaps.append("Machine Learning algorithms and frameworks (Scikit-learn, TensorFlow)")
        if 'statistics' not in current_lower and 'stats' not in current_lower:
            skill_gaps.append("Statistical analysis and mathematical foundations")
        if 'nlp' in goal_lower or 'natural language' in goal_lower:
            skill_gaps.append("Natural Language Processing (NLTK, spaCy, Transformers)")
    elif 'web developer' in goal_lower or 'full stack' in goal_lower:
        if 'javascript' not in current_lower and 'js' not in current_lower:
            skill_gaps.append("Modern JavaScript (ES6+) and asynchronous programming")
        if 'react' not in current_lower and 'vue' not in current_lower and 'angular' not in current_lower:
            skill_gaps.append("Frontend framework (React, Vue, or Angular)")
        if 'node' not in current_lower and 'express' not in current_lower:
            skill_gaps.append("Backend development with Node.js and Express")
        if 'database' not in current_lower and 'sql' not in current_lower:
            skill_gaps.append("Database design and management (SQL, MongoDB)")
    elif 'devops' in goal_lower or 'cloud' in goal_lower:
        if 'docker' not in current_lower:
            skill_gaps.append("Containerization with Docker and Kubernetes")
        if 'aws' not in current_lower and 'azure' not in current_lower and 'gcp' not in current_lower:
            skill_gaps.append("Cloud platforms (AWS, Azure, or Google Cloud)")
        if 'terraform' not in current_lower and 'ansible' not in current_lower:
            skill_gaps.append("Infrastructure as Code (Terraform, Ansible)")
        skill_gaps.append("CI/CD pipeline development and automation")
    else:
        # Generic skill gaps for any career transition
        skill_gaps = [
            "Industry-specific technical skills and tools",
            "Project management and collaboration methodologies",
            "Communication and presentation skills for technical topics",
            "Continuous learning and adaptation strategies"
        ]
    
    # Limit to top 4 skill gaps
    return skill_gaps[:4]

def generate_learning_roadmap_from_ai(skill_gaps, career_goal):
    """
    Placeholder function to simulate AI-generated personalized learning roadmap.
    
    Real LLM Prompt would be:
    "Based on these identified skill gaps: {skill_gaps} for the career goal: '{career_goal}', 
    create a structured learning roadmap with:
    1. Key Topics to Master: 3-4 essential concepts/technologies to learn
    2. Suggested Project Idea: One practical project that applies these new skills
    Make the roadmap actionable and specific to help achieve the career transition."
    """
    goal_lower = career_goal.lower()
    
    # Generate key topics based on skill gaps and career goal
    key_topics = []
    project_idea = ""
    
    if 'data scientist' in goal_lower or 'machine learning' in goal_lower:
        key_topics = [
            "Python libraries for data science (Pandas, NumPy, Matplotlib)",
            "Machine Learning fundamentals and supervised learning algorithms",
            "Data preprocessing and feature engineering techniques",
            "Model evaluation and deployment strategies"
        ]
        if 'nlp' in goal_lower or 'natural language' in goal_lower:
            project_idea = "Build a sentiment analysis tool for social media posts using Python, NLTK, and a machine learning classifier like Naive Bayes or SVM."
        else:
            project_idea = "Create a predictive model for house prices using a real estate dataset, implementing data cleaning, feature selection, and multiple ML algorithms for comparison."
    
    elif 'web developer' in goal_lower or 'full stack' in goal_lower:
        key_topics = [
            "Modern JavaScript ES6+ features and asynchronous programming",
            "React.js component-based architecture and state management",
            "RESTful API development with Node.js and Express",
            "Database integration and authentication systems"
        ]
        project_idea = "Build a full-stack task management application with user authentication, real-time updates, and data persistence using React frontend and Node.js/Express backend."
    
    elif 'devops' in goal_lower or 'cloud' in goal_lower:
        key_topics = [
            "Docker containerization and multi-container applications",
            "AWS core services (EC2, S3, RDS, Lambda)",
            "CI/CD pipeline setup with GitHub Actions or Jenkins",
            "Infrastructure automation with Terraform"
        ]
        project_idea = "Deploy a web application using Docker containers on AWS with automated CI/CD pipeline, load balancing, and monitoring setup."
    
    else:
        # Generic roadmap for other career goals
        key_topics = [
            "Core technical skills and industry-standard tools",
            "Project-based learning and portfolio development",
            "Professional networking and community engagement",
            "Certification and skill validation programs"
        ]
        project_idea = f"Create a comprehensive portfolio project that demonstrates key skills relevant to {career_goal}, including documentation and presentation materials."
    
    return {
        'key_topics': key_topics,
        'project_idea': project_idea
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        current_skills = request.form.get('current_skills', '').strip()
        career_goal = request.form.get('career_goal', '').strip()
        
        # Validate inputs
        if not current_skills or not career_goal:
            error_message = "Please fill in both your current skills and career goal."
            return render_template('index.html', error=error_message)
        
        # Get skill gaps from AI
        skill_gaps = get_skill_gap_from_ai(current_skills, career_goal)
        
        # Generate learning roadmap from AI
        roadmap = generate_learning_roadmap_from_ai(skill_gaps, career_goal)
        
        # Render template with results
        return render_template('index.html', 
                             current_skills=current_skills,
                             career_goal=career_goal,
                             skill_gaps=skill_gaps,
                             key_topics=roadmap['key_topics'],
                             project_idea=roadmap['project_idea'],
                             results_available=True)
    
    # GET request - show empty form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)