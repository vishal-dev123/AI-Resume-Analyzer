 import streamlit as st
import fitz
import re
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

 
st.markdown("""
<style>

/* ===== BACKGROUND ===== */

.stApp{
    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #111827
    );
}

/* ===== HIDE STREAMLIT ===== */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* ===== MAIN TITLE ===== */

.main-title{
    text-align:center;
    font-size:65px;
    font-weight:bold;
    color:#00ffff;

    animation: glow 2s infinite alternate;
}

@keyframes glow{

    from{
        text-shadow:
        0 0 10px #00ffff,
        0 0 20px #00ffff;
    }

    to{
        text-shadow:
        0 0 25px #00ffff,
        0 0 50px #00ffff,
        0 0 75px #00ffff;
    }
}

/* ===== SUBTITLE ===== */

.subtitle{
    text-align:center;
    color:white;
    font-size:18px;
    margin-bottom:40px;
}

/* ===== SECTION HEADERS ===== */

h1,h2,h3{
    color:#00ffff !important;
}

/* ===== NORMAL TEXT ===== */

p,label,div{
    color:white !important;
}

/* ===== GLASS CARD ===== */

.card{

    background: rgba(255,255,255,0.05);

    border:1px solid rgba(0,255,255,0.3);

    border-radius:25px;

    padding:25px;

    margin-bottom:20px;

    backdrop-filter:blur(15px);

    box-shadow:
        0 0 20px rgba(0,255,255,0.2);

    animation: floatCard 4s ease-in-out infinite;
}

@keyframes floatCard{

    0%{
        transform:translateY(0px);
    }

    50%{
        transform:translateY(-6px);
    }

    100%{
        transform:translateY(0px);
    }
}

/* ===== UPLOAD SECTION ===== */

 .upload-box{
    background:#111827;
    border:2px solid #00ffff;
    border-radius:20px;

    padding:15px;
    margin-bottom:15px;

    width:85%;
    margin-left:auto;
    margin-right:auto;

    box-shadow:
        0 0 15px rgba(0,255,255,0.3);
}

/* ===== FILE UPLOADER ===== */

 /* ===== FILE UPLOADER ===== */

[data-testid="stFileUploader"]{

    background:#111827 !important;

    border:2px solid #00ffff !important;

    border-radius:20px !important;

    padding:20px !important;

    box-shadow:0 0 20px rgba(0,255,255,0.3);
}

/* Upload Label */

[data-testid="stFileUploader"] label{

    color:white !important;

    font-weight:bold !important;

    font-size:18px !important;
}

/* Upload Button */

  [data-testid="stFileUploader"] button{

    background:#0ea5e9 !important;

    color:white !important;

    font-weight:bold !important;

    font-size:18px !important;

    border:none !important;

    border-radius:12px !important;

    padding:10px 20px !important;
}

/* File Name Text */

[data-testid="stFileUploader"] small{

    color:white !important;
}
/* ===== TEXT AREA ===== */

[data-testid="stTextArea"] textarea{

    background:#111827 !important;

    color:white !important;

    border:2px solid #00ffff !important;

    border-radius:15px !important;
}

/* ===== DOWNLOAD BUTTON ===== */

.stDownloadButton button{

    width:100%;

    background:linear-gradient(
        45deg,
        #00ffff,
        #00e6ac
    ) !important;

    color:black !important;

    font-weight:bold !important;

    border-radius:12px !important;
}

/* ===== METRIC CARDS ===== */

.metric-card{

    background:#111827;

    border:1px solid #00ffff;

    border-radius:20px;

    padding:20px;

    text-align:center;

    box-shadow:
        0 0 15px rgba(0,255,255,0.2);
}

.metric-card h2{

    color:white;
}

.metric-card p{

    color:#00ffff;

    font-size:35px;

    font-weight:bold;
}

/* ===== SUCCESS ===== */

.stSuccess{

    border-radius:15px !important;
}

/* ===== WARNING ===== */

.stWarning{

    border-radius:15px !important;
}

/* ===== ERROR ===== */

.stError{

    border-radius:15px !important;
}

</style>

<h1 class="main-title">
🤖 AI Resume Analyzer
</h1>

<p class="subtitle">
Upload • Analyze • Improve • Get Hired
</p>

""", unsafe_allow_html=True)
 
st.markdown("""
<div class="upload-box">
  <h2 style="
text-align:center;
font-size:28px;
margin-bottom:5px;
">
📂 Upload Your Resume
</h2>

 <p style="
text-align:center;
font-size:14px;
margin-top:0px;
">
Get ATS Score • Skill Analysis • AI Suggestions
</p>
</div>
""", unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# =====================================
# MAIN APP
# =====================================

if uploaded_file:

    st.success("✅ Resume Uploaded Successfully!")

    # Extract PDF Text
    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    # =====================================
    # PERSONAL INFORMATION
    # =====================================

    st.subheader("👤 Personal Information")

    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)

    phone = re.findall(r'\+?\d[\d\s-]{8,15}', text)

    lines = text.split("\n")

    name = lines[0] if lines else "Not Found"

    st.write("👤 Name:", name)

    if email:
        st.write("📧 Email:", email[0])

    if phone:
        st.write("📱 Phone:", phone[0])

    # =====================================
    # RESUME CONTENT
    # =====================================

    st.subheader("📄 Resume Content")

    st.text_area(
    "Extracted Text",
    text,
    height=300
)

    # =====================================
    # SKILL DETECTION
    # =====================================

    skills_list = [
        "Python",
        "C++",
        "Java",
        "SQL",
        "DBMS",
        "Operating System",
        "DSA",
        "Machine Learning",
        "AI",
        "Web Development",
        "Git",
        "GitHub"
    ]

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("💻 Detected Skills")

    if found_skills:
        for skill in found_skills:
            st.success(skill)
    else:
        st.warning("No skills detected")

    # =====================================
    # RESUME SCORE
    # =====================================

    score = min(len(found_skills) * 10, 100)

    st.subheader("📊 Resume Score")

    st.progress(score)

    st.markdown(f"""
<div class="card">
<h2>📊 Resume Score</h2>
<p>{score}/100</p>
</div>
""", unsafe_allow_html=True)

    # =====================================
    # CANDIDATE LEVEL
    # =====================================

    st.subheader("🎯 Candidate Level")

    if score < 40:
        level = "Fresher"
        st.warning(level)

    elif score < 70:
        level = "Intermediate"
        st.info(level)

    else:
        level = "Advanced"
        st.success(level)

    # =====================================
    # RESUME SUGGESTIONS
    # =====================================

    st.subheader("📝 Resume Suggestions")

    if "project" not in text.lower():
        st.error("❌ Add Projects Section")
    else:
        st.success("✅ Projects Section Found")

    if "github" not in text.lower():
        st.error("❌ Add GitHub Profile")
    else:
        st.success("✅ GitHub Profile Found")

    if "linkedin" not in text.lower():
        st.error("❌ Add LinkedIn Profile")
    else:
        st.success("✅ LinkedIn Profile Found")

    # =====================================
    # ATS SCORE
    # =====================================

    st.subheader("🤖 ATS Score")

    ats_score = 0

    if "skills" in text.lower():
        ats_score += 20

    if "project" in text.lower():
        ats_score += 20

    if "education" in text.lower():
        ats_score += 20

    if "github" in text.lower():
        ats_score += 20

    if "linkedin" in text.lower():
        ats_score += 20

    st.progress(ats_score)

    st.write(f"ATS Score: {ats_score}/100")

    # =====================================
    # MISSING SKILLS
    # =====================================

    st.subheader("🚀 Missing Skills Analysis")

    important_skills = [
        "Python",
        "SQL",
        "DSA",
        "Git",
        "GitHub",
        "Machine Learning",
        "Web Development"
    ]

    missing_skills = []

    for skill in important_skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    if missing_skills:

        st.warning("Skills You Should Learn:")

        for skill in missing_skills:
            st.write("❌", skill)

    else:
        st.success("🎉 No Important Skills Missing")

    # =====================================
    # RECOMMENDED COURSES
    # =====================================

    st.subheader("📚 Recommended Courses")

    recommended_courses = []

    if "Python" in found_skills:
        recommended_courses.append(
            "Python for Everybody"
        )

    if "Machine Learning" in found_skills:
        recommended_courses.append(
            "Machine Learning by Andrew Ng"
        )

    if "Web Development" in found_skills:
        recommended_courses.append(
            "Full Stack Web Development"
        )

    if "DSA" in found_skills:
        recommended_courses.append(
            "Data Structures and Algorithms"
        )

    for course in recommended_courses:
        st.write("✅", course)

    # =====================================
    # DASHBOARD
    # =====================================

        col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
            <h2>💻 Skills</h2>
            <p>{len(found_skills)}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <h2>📊 Score</h2>
            <p>{score}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
            <h2>🎯 Level</h2>
            <p>{level}</p>
        </div>
        """, unsafe_allow_html=True)

    with col1:
        st.metric(
            "Skills Found",
            len(found_skills)
        )

    with col2:
        st.metric(
            "Resume Score",
            score
        )

    with col3:
        st.metric(
            "Level",
            level
        )

    # =====================================
    # PIE CHART
    # =====================================

    if found_skills:

        fig = px.pie(
            names=found_skills,
            values=[1] * len(found_skills),
            title="Detected Skills"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # =====================================
     # =====================================
    # Skill Bar Chart
    # =====================================

    st.subheader("📊 Skill Bar Chart")

    if found_skills:

        fig2 = px.bar(
            x=found_skills,
            y=[1] * len(found_skills),
            labels={
                "x": "Skills",
                "y": "Detected"
            },
            title="Detected Skills"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # =====================================
    # Resume Strength
    # =====================================

    st.subheader("💪 Resume Strength")

    if score >= 80:
        st.success("🔥 Strong Resume")

    elif score >= 60:
        st.info("👍 Good Resume")

    else:
        st.error("⚠️ Weak Resume")

    # =====================================
    # Project Recommendation
    # =====================================

    st.subheader("🚀 Recommended Projects")

    if "Python" in found_skills:
        st.write("✅ Python Automation Tool")

    if "Machine Learning" in found_skills:
        st.write("✅ House Price Prediction")

    if "Web Development" in found_skills:
        st.write("✅ E-Commerce Website")

    if "DSA" in found_skills:
        st.write("✅ Competitive Programming Tracker")

    # =====================================
    # DOWNLOAD REPORT
    # =====================================

    st.subheader("📥 Download Resume Report")

    report = f"""
AI RESUME ANALYZER REPORT

Name: {name}

Email: {email[0] if email else "Not Found"}

Phone: {phone[0] if phone else "Not Found"}

Skills:
{', '.join(found_skills)}

Resume Score: {score}/100

ATS Score: {ats_score}/100

Candidate Level: {level}
"""

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="resume_report.txt",
        mime="text/plain"
    )
    st.markdown("""
<style>

.footer{
    text-align:center;
    padding:30px;
    margin-top:50px;

    border-top:2px solid #00ffff;

    animation: footerGlow 2s infinite alternate;
}

@keyframes footerGlow{
    from{
        box-shadow:0 0 10px #00ffff;
    }

    to{
        box-shadow:0 0 30px #00ffff;
    }
}

</style>

<div class="footer">

<h2 style="color:#00ffff;">
👨‍💻 Vishal Saini
</h2>

<p>
AI Resume Analyzer Project
</p>

<p>
Built with Python • Streamlit • HTML • CSS
</p>

<p>
🚀 Future Software Engineer
</p>

</div>
""", unsafe_allow_html=True)
st.markdown("""
<div style="
text-align:center;
margin-top:40px;
padding:20px;
border-top:1px solid #00ffff;
color:white;
">
👨‍💻 Developed by <span style="color:#00ffff;font-weight:bold;">
Vishal Saini
</span>
</div>
""", unsafe_allow_html=True)
