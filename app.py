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
# LIGHT MODE + NEON GLOW ADVANCED CSS
# ----------------------------------------------------------
custom_css = """
<style>
/* Light clean background */
.stApp {
    background: linear-gradient(180deg, #ffffff 0%, #f7f9fc 100%);
    color: #1f2937;
    font-family: 'Inter', sans-serif;
}

/* Main container spacing */
main .block-container {
    padding-top: 2.5rem;
    max-width: 1180px;
}

/* Sidebar light mode */
section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid rgba(0,0,0,0.07);
}
section[data-testid="stSidebar"] * {
    color: #111827 !important;
}

/* Neon glowing title */
.glow-text {
    color: #0f172a;
    text-shadow: 0 0 10px rgba(0, 153, 255, 0.35);
}

/* Section underline */
.section-underline {
    width: 70px;
    height: 3px;
    border-radius: 999px;
    background: linear-gradient(90deg, #00baff, #6366f1, #b43cff);
    box-shadow: 0 0 10px rgba(0,153,255,0.5);
    margin-bottom: 1rem;
}

/* Glassmorphism card */
.glass-card {
    padding: 1.2rem 1.4rem;
    border-radius: 1.3rem;
    background: rgba(255, 255, 255, 0.75);
    border: 1px solid rgba(0,0,0,0.08);
    backdrop-filter: blur(14px);
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    transition: all 0.25s ease-out;
}

/* CARD hover glow */
.glass-card:hover {
    transform: translateY(-4px);
    border-color: rgba(0,153,255,0.3);
    box-shadow: 0 8px 24px rgba(0,153,255,0.25), 
                0 0 16px rgba(99,102,241,0.25);
}

/* Tags */
.tech-tag {
    display: inline-block;
    padding: 0.22rem 0.65rem;
    margin: 0.15rem;
    font-size: 0.75rem;
    border-radius: 999px;
    background: rgba(255,255,255,0.85);
    border: 1px solid rgba(0,0,0,0.2);
    transition: all 0.2s ease-out;
}

/* Tag hover neon */
.tech-tag:hover {
    border-color: #00baff;
    transform: translateY(-2px);
    box-shadow: 0 0 12px rgba(0,183,255,0.45);
}

/* Buttons */
.stButton > button {
    background: rgba(255,255,255,0.9);
    border: 1px solid rgba(0,0,0,0.1);
    padding: 0.55rem 1.2rem;
    border-radius: 999px;
    color: #111827;
    font-weight: 600;
    transition: all 0.25s ease-out;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
}

/* Button hover glow */
.stButton > button:hover {
    border-color: #009dff;
    color: #007fff;
    box-shadow: 0 0 15px rgba(0,153,255,0.45),
                0 6px 20px rgba(0,153,255,0.15);
    transform: translateY(-3px);
}

/* Clean link hover glow */
a {
    color: #0066cc;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.22s ease-out;
}
a:hover {
    color: #009dff;
    text-shadow: 0 0 12px rgba(0,153,255,0.4);
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ----------------------------------------------------------
# PERSONAL INFORMATION (FROM RESUME)
# ----------------------------------------------------------
NAME = "V I B I N R A J  D"
ROLE_TITLE = "Senior Business Analyst"
LOCATION = "Chennai, Tamil Nadu"
EMAIL = "vibinrajd2002@gmail.com"
PHONE = "+91 9943906596"
LINKEDIN = "https://www.linkedin.com/in/vibinraj-d98"
GITHUB = "https://github.com/vibinrajd"

SUMMARY = (
    "Tech-driven Senior Business Analyst with expertise in Data Analytics, Automation, "
    "and Business Intelligence. Skilled in ETL pipelines, API automation, reporting engines, "
    "Power BI systems, SQL workflows, Python automations, and GCP BigQuery data engineering."
)

# Resume PDF from upload
RESUME_PATH = Path("/mnt/data/Vibinraj D Resume.pdf")

# ----------------------------------------------------------
# RESUME → EXPERIENCE
# ----------------------------------------------------------
experience = [
    {
        "company": "Analytics Avenue",
        "role": "Senior Business Analyst",
        "period": "Jul 2025 – Present",
        "points": [
            "Designed & deployed automated BI systems using Power BI, BigQuery, SQL & AppScript (70% faster reporting).",
            "Developed ETL pipelines for automated marketing and finance ingestion.",
            "Built audit, churn, and financial analytics dashboards for strategic decisions.",
            "Owned data governance & workflow operations using Jira + automation tools."
        ]
    },
    {
        "company": "Analytics Avenue",
        "role": "Business Analyst",
        "period": "Aug 2024 – Jul 2025",
        "points": [
            "Developed self-refreshing dashboards using APIs for ad and client analytics.",
            "Automated CRM workflows improving lead accuracy by 25%.",
            "Built automated reporting pipelines via BigQuery + AppScript.",
            "Connected campaign insights to revenue intelligence frameworks."
        ]
    },
    {
        "company": "Analytics Avenue",
        "role": "Data Analyst Intern",
        "period": "Sep 2023 – Aug 2024",
        "points": [
            "Hands-on experience with SQL, Power BI, Python & automation.",
            "Built dashboards and EDA models improving visibility by 20%.",
            "Created automation scripts & prototype BI solutions."
        ]
    }
]

# ----------------------------------------------------------
# PROJECTS FROM RESUME
# ----------------------------------------------------------
projects = [
    {
        "title": "Marketing Performance Automation Dashboard",
        "summary": "Dual dashboards (Ad & Client side) automated using Meta + Google APIs.",
        "highlights": [
            "Real-time API automated ingestion.",
            "23% faster campaign optimization."
        ],
        "tech": ["Power BI", "AppScript", "BigQuery", "API Integration"]
    },
    {
        "title": "Churn Prediction & Sales Automation System",
        "summary": "Churn prediction using Python + BigQuery with automated tracking.",
        "highlights": [
            "80% reduction in manual retention reporting.",
            "Improved churn tracking accuracy."
        ],
        "tech": ["Python", "BigQuery", "Machine Learning"]
    },
    {
        "title": "Automated Audit & Financial Reporting System",
        "summary": "End-to-end Power BI reporting with ETL refresh automation.",
        "highlights": [
            "Real-time audit visibility.",
            "Improved financial insights for leadership."
        ],
        "tech": ["Power BI", "BigQuery", "AppScript"]
    },
    {
        "title": "Employee Performance Automation",
        "summary": "Automated HR performance analytics.",
        "highlights": [
            "18% improvement in reporting accuracy."
        ],
        "tech": ["Power BI", "BigQuery", "AppScript"]
    }
]

# ----------------------------------------------------------
# SKILLS
# ----------------------------------------------------------
skills_primary = [
    "Power BI", "SQL", "Python (Pandas, NumPy, Matplotlib, Seaborn)",
    "BigQuery", "AppScript Automation", "API Integration",
    "Time Series Analysis", "EDA", "Marketing Analytics",
    "Financial Analytics", "Churn Prediction", "Market Basket Analysis"
]

skills_secondary = [
    "CRM Automation", "Workflow Automation", "Jira",
    "Reporting Management", "Cross-Functional Collaboration"
]

# ----------------------------------------------------------
# EDUCATION
# ----------------------------------------------------------
education = [
    ("B.E. Electrical & Electronics Engineering", "UCE - BIT Campus", "2019–2023", "CGPA: 7.68"),
    ("HSC", "Vidya Mandir Hr Sec School", "2019", "77.5%"),
    ("SSLC", "Sri Krishna Hr Sec School", "2017", "89.4%")
]

# ----------------------------------------------------------
# CERTIFICATIONS
# ----------------------------------------------------------
certifications = [
    "Data Processing Specialist – Aspiring Minds",
    "Data Analytics – Analytics Avenue",
    "Excel Certification – Great Learning",
    "EV Charging System – Coursera"
]

# ----------------------------------------------------------
# ACHIEVEMENTS
# ----------------------------------------------------------
achievements = [
    "CryptoTracker: Real-time crypto dashboard (35% improved analysis).",
    "EV Analytics Dashboard for adoption + manufacturing insights (30% boost).",
    "Market Basket Analysis improving inventory visibility by 15%.",
    "Retail Sales EDA improving profit optimization by 10%.",
    "Promoted to Senior Analyst within 1 year.",
    "Conducted Power BI & Marketing Analytics workshops."
]

# ----------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------
with st.sidebar:
    st.title("💼 Portfolio")
    page = st.radio("Navigate", ["Home", "Experience", "Projects", "Skills", "Education", "Certifications", "Achievements", "Resume", "Contact"])

# ----------------------------------------------------------
# HELPER
# ----------------------------------------------------------
def section_header(txt):
    st.markdown(f"<div class='glow-text' style='font-size:1.7rem;font-weight:900'>{txt}</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-underline'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------
# PAGES
# ----------------------------------------------------------
if page == "Home":
    section_header("Welcome")
    st.markdown(f"## {NAME}")
    st.markdown(f"### {ROLE_TITLE}")
    st.markdown(SUMMARY)
    st.markdown("---")
    st.metric("Experience", "3+ Years")
    st.metric("Expertise", "Analytics + Automation")

elif page == "Experience":
    section_header("Work Experience")
    for exp in experience:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"### {exp['role']} • {exp['company']}")
        st.markdown(f"**{exp['period']}**")
        for p in exp["points"]:
            st.markdown(f"- {p}")
        st.markdown("</div><br>", unsafe_allow_html=True)

elif page == "Projects":
    section_header("Projects")
    for proj in projects:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"### {proj['title']}")
        st.markdown(proj["summary"])
        st.markdown("**Highlights:**")
        for h in proj["highlights"]:
            st.markdown(f"- {h}")
        st.markdown("<br>", unsafe_allow_html=True)
        tech_html = "".join([f"<span class='tech-tag'>{t}</span>" for t in proj["tech"]])
        st.markdown(tech_html, unsafe_allow_html=True)
        st.markdown("</div><br>", unsafe_allow_html=True)

elif page == "Skills":
    section_header("Skills")
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### Technical Skills")
    for s in skills_primary: st.markdown(f"- {s}")
    st.markdown("</div><br>", unsafe_allow_html=True)

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### Soft & Supporting Skills")
    for s in skills_secondary: st.markdown(f"- {s}")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Education":
    section_header("Education")
    for degree, inst, yr, score in education:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"### {degree}")
        st.markdown(f"{inst} ({yr})")
        st.markdown(f"**{score}**")
        st.markdown("</div><br>", unsafe_allow_html=True)

elif page == "Certifications":
    section_header("Certifications")
    for c in certifications:
        st.markdown(f"- {c}")

elif page == "Achievements":
    section_header("Achievements")
    for a in achievements:
        st.markdown(f"- {a}")

elif page == "Resume":
    section_header("Resume")
    if RESUME_PATH.exists():
        with open(RESUME_PATH, "rb") as f:
            st.download_button("📄 Download Resume", f, "Vibinraj_Resume.pdf", "application/pdf")
    st.info("Your resume has been embedded from the uploaded file.")

elif page == "Contact":
    section_header("Contact")
    st.write(f"📧 Email: {EMAIL}")
    st.write(f"📱 Phone: {PHONE}")
    st.write(f"📍 Location: {LOCATION}")
    st.write(f"🔗 LinkedIn: {LINKEDIN}")
    st.write(f"💻 GitHub: {GITHUB}")
