# app.py
import streamlit as st
from pathlib import Path

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(
    page_title="Vibinraj D | Portfolio",
    page_icon="💼",
    layout="wide"
)

# ----------------------------------------------------------
# CUSTOM CSS (NEON GLOW + GLASS UI)
# ----------------------------------------------------------
custom_css = """
<style>
.stApp { background: radial-gradient(circle at top, #111827, #020617 70%); color: #e5e7eb; }
main .block-container { padding-top: 2rem; max-width: 1180px; }
section[data-testid="stSidebar"] { background: #020617; border-right: 1px solid rgba(148,163,184,0.3); }
.glow-text { text-shadow: 0 0 12px rgba(56,189,248,0.75); }
.section-title { font-size: 1.6rem; font-weight: 800; }
.section-underline { width: 70px; height: 3px; border-radius: 999px; 
    background: linear-gradient(90deg, #22d3ee, #6366f1, #a855f7);
    box-shadow: 0 0 18px rgba(56,189,248,0.9); margin-bottom: 1rem; }
.glass-card { border-radius: 1.2rem; padding: 1.3rem; background: rgba(15,23,42,0.5);
    border: 1px solid rgba(148,163,184,0.25); backdrop-filter: blur(14px); }
.tech-tag { padding: 0.15rem 0.6rem; margin: 0.15rem; border-radius: 999px;
    border: 1px solid rgba(148,163,184,0.6); font-size: 0.75rem; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ----------------------------------------------------------
# PERSONAL DETAILS (FROM RESUME)
# ----------------------------------------------------------
NAME = "V I B I N R A J  D"
ROLE_TITLE = "Senior Business Analyst"
LOCATION = "Chennai, Tamil Nadu"
EMAIL = "vibinrajd2002@gmail.com"
PHONE = "+91 9943906596"
LINKEDIN = "https://www.linkedin.com/in/vibinraj-d98"
GITHUB = "https://github.com/vibinrajd"

SUMMARY = (
    "Tech-driven Senior Business Analyst with experience in Data Analytics, Process Automation, "
    "and Business Intelligence. Skilled in developing automated data pipelines, "
    "interactive dashboards, and scalable reporting systems using Power BI, SQL, Python, "
    "GCP BigQuery, and AppScript."
)

RESUME_PATH = Path("/mnt/data/Vibinraj D Resume.pdf")

# ----------------------------------------------------------
# EXPERIENCE (DIRECT FROM RESUME)
# ----------------------------------------------------------
experience = [
    {
        "company": "Analytics Avenue",
        "role": "Senior Business Analyst",
        "period": "Jul 2025 – Present",
        "points": [
            "Designed and deployed automated BI systems using Power BI, GCP BigQuery, SQL, and AppScript, reducing reporting time by 70%.",
            "Built ETL pipelines to automate marketing and finance datasets with API integrations.",
            "Developed company-wide audit, churn, and financial dashboards for strategic planning.",
            "Managed data governance and workflow intelligence using Jira + automation tools."
        ]
    },
    {
        "company": "Analytics Avenue",
        "role": "Business Analyst",
        "period": "Aug 2024 – Jul 2025",
        "points": [
            "Built self-refreshing marketing dashboards integrated with APIs for ad performance.",
            "Automated CRM workflows improving lead tracking accuracy by 25%.",
            "Developed automated reporting pipelines using BigQuery + AppScript.",
            "Connected campaign analytics with revenue intelligence frameworks."
        ]
    },
    {
        "company": "Analytics Avenue",
        "role": "Data Analyst Intern",
        "period": "Sep 2023 – Aug 2024",
        "points": [
            "Worked with SQL, Power BI, Excel, and Python automation.",
            "Created prototype dashboards and EDA models improving decision visibility by 20%.",
            "Developed automation scripts and early-stage analytics workflows."
        ]
    }
]

# ----------------------------------------------------------
# PROJECTS (FROM RESUME)
# ----------------------------------------------------------
projects = [
    {
        "title": "Marketing Performance Automation Dashboard",
        "summary": "Automated ad-side and client-side performance dashboards using Meta & Google APIs.",
        "highlights": [
            "Real-time automated Power BI dashboards.",
            "Faster campaign optimization by 23%."
        ],
        "tech": ["Power BI", "AppScript", "BigQuery", "API Integration"]
    },
    {
        "title": "Churn Prediction & Sales Automation",
        "summary": "BigQuery + Python based churn prediction with automated refresh.",
        "highlights": [
            "Reduced manual reporting by 80%.",
            "Enhanced retention tracking for sales."
        ],
        "tech": ["Python", "BigQuery", "Machine Learning"]
    },
    {
        "title": "Automated Audit & Financial Reporting System",
        "summary": "Real-time financial + audit dashboard with BigQuery ETL automation.",
        "highlights": [
            "Daily automated reporting.",
            "Improved financial visibility for leadership."
        ],
        "tech": ["Power BI", "AppScript", "BigQuery"]
    },
    {
        "title": "Employee Performance Automation",
        "summary": "HR analytics system using Power BI + AppScript automations.",
        "highlights": [
            "Improved HR reporting accuracy by 18%."
        ],
        "tech": ["Power BI", "BigQuery", "AppScript"]
    }
]

# ----------------------------------------------------------
# SKILLS (FROM RESUME)
# ----------------------------------------------------------
skills_primary = [
    "Power BI", "SQL", "Python (Pandas, NumPy, Matplotlib, Seaborn)",
    "GCP BigQuery", "AppScript Automation", "API Integration",
    "Time Series", "Marketing Analytics", "Financial Analytics",
    "Churn Analysis", "Market Basket Analysis", "EDA"
]

skills_secondary = [
    "CRM Optimization", "Workflow Automation", "Jira",
    "Reporting Systems", "Cross-Functional Collaboration"
]

# ----------------------------------------------------------
# EDUCATION (FROM RESUME)
# ----------------------------------------------------------
education = [
    ("B.E. Electrical & Electronics Engineering", "University College of Engineering, BIT Campus", "2019–2023", "CGPA 7.68"),
    ("HSC", "Vidya Mandir Hr. Sec. School", "2019", "77.5%"),
    ("SSLC", "Sri Krishna Hr. Sec. School", "2017", "89.4%")
]

# ----------------------------------------------------------
# CERTIFICATIONS (FROM RESUME)
# ----------------------------------------------------------
certifications = [
    "Data Processing Specialist - Aspiring Minds",
    "Data Analytics - Analytics Avenue",
    "Excel Certification - Great Learning",
    "Electric Vehicle Charging System - Coursera"
]

# ----------------------------------------------------------
# ACHIEVEMENTS (FROM RESUME)
# ----------------------------------------------------------
achievements = [
    "CryptoTracker: Real-time cryptocurrency analytics dashboard (35% better insights).",
    "EV Analytics Dashboard supporting policy and manufacturing insights (30% improvement).",
    "Market Basket Analysis improving inventory insights by 15%.",
    "Retail Sales EDA boosting profit optimization by 10%.",
    "Promoted to Senior Business Analyst within a year for automation leadership.",
    "Conducted Power BI & Marketing Analytics workshops."
]

# ----------------------------------------------------------
# SIDEBAR NAVIGATION
# ----------------------------------------------------------
with st.sidebar:
    st.title("💼 Portfolio")
    page = st.radio("Navigate", ["Home", "Experience", "Projects", "Skills", "Education", "Certifications", "Achievements", "Resume", "Contact"])

# ----------------------------------------------------------
# SECTION HEADER HELPER
# ----------------------------------------------------------
def section_header(txt):
    st.markdown(f"<div class='section-title glow-text'>{txt}</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-underline'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------
# PAGE CONTENT
# ----------------------------------------------------------

# HOME PAGE
if page == "Home":
    section_header("Welcome")
    st.markdown(f"## {NAME}")
    st.markdown(f"### {ROLE_TITLE}")
    st.markdown(SUMMARY)
    st.markdown("---")
    st.metric("Experience", "3+ Years")
    st.metric("Expertise", "Analytics + Automation")

# EXPERIENCE PAGE
elif page == "Experience":
    section_header("Work Experience")
    for exp in experience:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"### {exp['role']} | {exp['company']} ({exp['period']})")
        for p in exp["points"]:
            st.markdown(f"- {p}")
        st.markdown("</div><br>", unsafe_allow_html=True)

# PROJECTS PAGE
elif page == "Projects":
    section_header("Projects")
    for proj in projects:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"### {proj['title']}")
        st.markdown(proj["summary"])
        if proj["highlights"]:
            st.markdown("**Highlights:**")
            for h in proj["highlights"]:
                st.markdown(f"- {h}")
        tech_html = "".join([f"<span class='tech-tag'>{t}</span>" for t in proj["tech"]])
        st.markdown(tech_html, unsafe_allow_html=True)
        st.markdown("</div><br>", unsafe_allow_html=True)

# SKILLS PAGE
elif page == "Skills":
    section_header("Skills")
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### Technical Skills")
    for s in skills_primary:
        st.markdown(f"- {s}")
    st.markdown("</div><br>", unsafe_allow_html=True)

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### Supporting Skills")
    for s in skills_secondary:
        st.markdown(f"- {s}")
    st.markdown("</div>", unsafe_allow_html=True)

# EDUCATION PAGE
elif page == "Education":
    section_header("Education")
    for degree, inst, yr, score in education:
        st.markdown(f"### {degree}")
        st.markdown(f"{inst} ({yr})")
        st.markdown(f"**Score:** {score}")
        st.markdown("---")

# CERTIFICATIONS PAGE
elif page == "Certifications":
    section_header("Certifications")
    for c in certifications:
        st.markdown(f"- {c}")

# ACHIEVEMENTS PAGE
elif page == "Achievements":
    section_header("Achievements")
    for a in achievements:
        st.markdown(f"- {a}")

# RESUME PAGE
elif page == "Resume":
    section_header("Resume")
    if RESUME_PATH.exists():
        with open(RESUME_PATH, "rb") as f:
            st.download_button("📄 Download Resume", f, "Vibinraj_Resume.pdf", "application/pdf")
    st.info("Your resume is embedded from the uploaded file.")

# CONTACT PAGE
elif page == "Contact":
    section_header("Contact")
    st.write(f"📧 Email: {EMAIL}")
    st.write(f"📱 Phone: {PHONE}")
    st.write(f"📍 Location: {LOCATION}")
    st.write(f"🔗 LinkedIn: {LINKEDIN}")
    st.write(f"💻 GitHub: {GITHUB}")
