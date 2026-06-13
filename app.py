import streamlit as st

st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="📄",
    layout="wide"
)

# Styling
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #f8f9fa, #f3e8ff);
}

.main-title {
    text-align: center;
    color: #4b0082;
    font-size: 45px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #666666;
    font-size: 18px;
    margin-bottom: 30px;
}

.resume-box {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-top: 20px;
}

.stButton > button {
    width: 100%;
    background-color: #8e44ad;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background-color: #6c3483;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    "<div class='main-title'>📄 AI Resume & Portfolio Builder</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Create Professional Resumes in Seconds with AI</div>",
    unsafe_allow_html=True
)

# Input Fields
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Full Name")
    education = st.text_input("🎓 Education")
    email = st.text_input("📧 Email")

with col2:
    skills = st.text_area("💻 Skills")
    projects = st.text_area("🚀 Projects")
    achievements = st.text_area("🏆 Achievements")

# Resume Score
score = 50

if len(skills) > 20:
    score += 15

if len(projects) > 20:
    score += 15

if achievements:
    score += 10

if score > 100:
    score = 100

# Generate Resume
if st.button("✨ Generate Resume"):

    resume = f"""
# {name}

## Professional Summary
Motivated and enthusiastic individual with strong technical and problem-solving skills. Passionate about learning new technologies and contributing effectively to projects.

## Education
{education}

## Skills
{skills}

## Projects
{projects}

## Achievements
{achievements}

## Contact
Email: {email}

## Career Objective
Seeking opportunities to utilize my knowledge, enhance my skills, and contribute to organizational success while continuing professional growth.
"""

    st.success("✅ Resume Generated Successfully!")

    st.metric("📊 Resume Score", f"{score}/100")

    # Career Suggestions
    career = []

    skills_lower = skills.lower()

    if "python" in skills_lower:
        career.append("Python Developer")

    if "machine learning" in skills_lower or "ai" in skills_lower:
        career.append("AI Engineer")

    if "data" in skills_lower:
        career.append("Data Analyst")

    if "web" in skills_lower:
        career.append("Web Developer")

    if career:
        st.subheader("💼 Recommended Career Paths")

        for role in career:
            st.write("✅", role)

    # Resume Display
    st.markdown(
        f"<div class='resume-box'>{resume}</div>",
        unsafe_allow_html=True
    )

    # Download Button
    st.download_button(
        label="📥 Download Resume",
        data=resume,
        file_name="resume.txt",
        mime="text/plain"
    )
    # Cover Letter

    cover_letter = f"""
Dear Hiring Manager,

I am excited to apply for opportunities that match my skills in {skills}.

My educational background in {education} and experience gained through projects such as {projects} have helped me develop strong technical and problem-solving abilities.

I am eager to contribute to your organization and continue learning in a professional environment.

Thank you for your time and consideration.

Sincerely,
{name}
"""

    st.subheader("📄 AI Generated Cover Letter")

    st.text_area(
        "Cover Letter",
        cover_letter,
        height=250
    )

    # Portfolio Summary

    portfolio = f"""
👤 About Me
{name} is a motivated learner with expertise in {skills}.

🎓 Education
{education}

🚀 Projects
{projects}

🏆 Achievements
{achievements}
"""

    st.subheader("🌟 Portfolio Summary")

    st.text_area(
        "Portfolio",
        portfolio,
        height=200
    )

    st.balloons()