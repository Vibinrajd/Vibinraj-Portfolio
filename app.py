import streamlit as st
from pathlib import Path

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(
    page_title="Vibinraj D | Portfolio",
    layout="wide"
)

# ----------------------------------------------------------
# PROFESSIONAL CLEAN LIGHT CSS
# ----------------------------------------------------------
clean_css = """
<style>

.stApp {
    background: #fafafb;
    color: #1a1a1a;
    font-family: 'Inter', sans-serif;
}

/* Center container */
main .block-container {
    padding: 2.2rem 2rem 3rem 2rem;
    max-width: 1100px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e6e6e6;
}

/* Section title */
.section-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: #111;
    margin-bottom: 0.4rem;
}

.section-line {
    width: 70px;
    height: 3px;
    background: #3a7afe;
    border-radius: 6px;
    margin-bottom: 1.2rem;
}

/* Clean card */
.card {
    background: #ffffff;
    padding: 1.6rem;
    border-radius: 12px;
    border: 1px solid #e2e2e2;
    box-shadow: 0 3px 10px rgba(0,0,0,0.04);
    transition: 0.15s ease;
}

.card:hover {
    border-color: #3a7afe;
    box-shadow: 0 4px 18px rgba(58,122,254,0.15);
}

/* Subheading */
.card h3 {
    font-size: 1.2rem;
    margin-bottom: 0.4rem;
}

/* Text adjustments */
p, li {
    font-size: 0.96rem;
    line-height: 1.55;
}

/* Skills tag */
.tag {
    display: inline-block;
    padding: 0.22rem 0.6rem;
    margin: 0.14rem;
    font-size: 0.78rem;
    border: 1px solid #d6d6d6;
    border-radius: 8px;
    background: #fefefe;
}

</style>
"""

st.markdown(clean_css, unsafe_allow_html=True)

# ----------------------------------------------------------
# YOUR DATA
# ----------------------------------------------------------

NAME = "Vibinraj D"
ROLE = "Senior Business Analyst"
LOCATION = "Chennai, Tamil Nadu"
EMAIL = "vibinrajd2002@gmail.com"
PHONE = "+91 9943906596"
LINKEDIN = "https://www.linkedin.com/in/vibinraj-d98"
GITHUB = "https://github.com/vibinrajd"

SUMMARY = """
Data-driven Senior Business Analyst with expertise in analytics, automation, reporting, 
and workflow engineering. Experienced in building scalable BI systems using Power BI, 
BigQuery, AppScript, SQL, and Python. Focused on automation, accuracy, and enabling 
business teams to make faster decisions.
"""

RESUME_PATH = Path("files/Vibinraj D Resume.pdf")

experience = [
    {
        "title": "Senior Business Analyst",
        "company": "Analytics Avenue",
        "years": "Jul 2025 – Present",
        "points": [
            "Designed and deployed automated BI systems using Power BI, BigQuery, SQL, and AppScript.",
            "Improved reporting speed by 70% through ETL automation and API integrations.",
            "Built company-wide audit, churn, and financial dashboards for leadership reporting.",
            "Managed data governance, Jira-based workflows, and automated pipelines."
        ]
    },
    {
        "title": "Business Analyst",
        "company": "Analytics Avenue",
        "years": "Aug 2024 – Jul 2025",
        "points": [
            "Created automated marketing dashboards with API-driven refresh for ad performance.",
            "Automated CRM workflows improving accuracy and reducing manual touchpoints.",
            "Developed BigQuery + AppScript pipelines for daily reporting operations.",
            "Linked marketing analytics to revenue attribution frameworks."
        ]
    },
    {
        "title": "Data Analyst Intern",
        "company": "Analytics Avenue",
        "years": "Sep 2023 – Aug 2024",
        "points": [
            "Executed EDA, dashboards, and automation scripts across domains.",
            "Improved leadership decision visibility with structured reporting formats.",
            "Gained hands-on expertise in SQL, Power BI, and Python automation."
        ]
    }
]

projects = [
    ("Marketing Performance Automation Dashboard",
     "Automated ad and client-side marketing dashboards using Meta & Google APIs.",
     ["23% faster optimization decisions", "Automated ingestion to Power BI"],
     ["Power BI", "BigQuery", "AppScript", "APIs"]),

    ("Churn Prediction & Sales Automation",
     "Predictive churn model integrated with automated refresh cycles.",
     ["80% reduction in manual reporting", "Improved retention intelligence"],
     ["Python", "BigQuery", "ML"]),

    ("Audit & Financial Reporting System",
     "Automated Power BI financial audit dashboard with ETL triggers.",
     ["Daily automated refresh", "Clear leadership KPIs"],
     ["Power BI", "AppScript", "BigQuery"]),

    ("Performance Automation for HR",
     "Live workforce analytics dashboards using AppScript + BigQuery ETL.",
     ["18% accuracy improvement", "Unified reporting workflow"],
     ["Power BI", "BigQuery"])
]

skills_primary = [
    "Power BI", "SQL", "Python", "BigQuery", "AppScript", 
    "Automation", "Reporting Systems", "APIs", 
    "EDA", "Time Series", "Churn Analytics", "Marketing Analytics"
]

education = [
    ("B.E. Electrical & Electronics Engineering", "UCE-BIT Campus", "2019–2023"),
    ("HSC", "Vidya Mandir Hr Sec School", "2019"),
    ("SSLC", "Sri Krishna Hr Sec School", "2017"),
]

# ----------------------------------------------------------
# SIDEBAR NAVIGATION
# ----------------------------------------------------------
with st.sidebar:
    st.header("Portfolio")
    page = st.radio(
        "Navigate",
        ["Home", "Experience", "Projects", "Skills", "Education", "Resume", "Contact"]
    )

# ----------------------------------------------------------
# HEADER FUNCTION
# ----------------------------------------------------------
def header(title):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-line'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------
# PAGES
# ----------------------------------------------------------

if page == "Home":
    header("Profile")
    st.markdown(f"## {NAME}")
    st.markdown(f"### {ROLE}")
    st.write(SUMMARY)

elif page == "Experience":
    header("Experience")
    for job in experience:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"**{job['title']} — {job['company']} ({job['years']})**")
        st.write("")
        for p in job["points"]:
            st.write(f"- {p}")
        st.markdown("</div><br>", unsafe_allow_html=True)

elif page == "Projects":
    header("Projects")
    for title, desc, highlights, tags in projects:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {title}")
        st.write(desc)
        st.write("**Key Outcomes:**")
        for h in highlights:
            st.write(f"- {h}")
        st.write("")
        tag_html = "".join([f"<span class='tag'>{t}</span>" for t in tags])
        st.markdown(tag_html, unsafe_allow_html=True)
        st.markdown("</div><br>", unsafe_allow_html=True)

elif page == "Skills":
    header("Skills")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("### Technical Skills")
    st.write(", ".join(skills_primary))
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Education":
    header("Education")
    for degree, school, year in education:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"**{degree}**")
        st.markdown(f"{school} • {year}")
        st.markdown("</div><br>", unsafe_allow_html=True)

elif page == "Resume":
    header("Resume")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    if RESUME_PATH.exists():
        with open(RESUME_PATH, "rb") as f:
            st.download_button(
                "Download Resume (PDF)",
                f,
                file_name="Vibinraj_D_Resume.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Resume not found. Add it under files/Vibinraj D Resume.pdf")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Contact":
    header("Contact")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write(f"Email: {EMAIL}")
    st.write(f"Phone: {PHONE}")
    st.write(f"Location: {LOCATION}")
    st.write(f"LinkedIn: {LINKEDIN}")
    st.write(f"GitHub: {GITHUB}")
    st.markdown("</div>", unsafe_allow_html=True)
