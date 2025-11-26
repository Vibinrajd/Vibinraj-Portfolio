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
# ADVANCED LIGHT THEME + 3D GLOW CSS
# ----------------------------------------------------------
custom_css = """
<style>
/* Global */
.stApp {
    background: radial-gradient(circle at top, #fdfdfd 0, #f5f7fb 45%, #edf1fa 100%);
    color: #111827;
    font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

main .block-container {
    padding-top: 2.5rem;
    padding-bottom: 2rem;
    max-width: 1180px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid rgba(15,23,42,0.06);
    box-shadow: 4px 0 18px rgba(15,23,42,0.04);
}
section[data-testid="stSidebar"] * {
    color: #0f172a !important;
}

/* Section title + glow */
.glow-text {
    color: #020617;
    text-shadow: 0 0 12px rgba(56,189,248,0.45), 0 0 26px rgba(129,140,248,0.4);
}
.section-underline {
    width: 80px;
    height: 3px;
    border-radius: 999px;
    margin-bottom: 1rem;
    background: linear-gradient(90deg, #06b6d4, #6366f1, #a855f7);
    box-shadow: 0 0 16px rgba(56,189,248,0.7);
}

/* 3D container with perspective */
.card-3d-wrapper {
    perspective: 1200px;
}

/* 3D glass card with gradient border + glow */
.glass-card-3d {
    position: relative;
    border-radius: 1.4rem;
    padding: 1.25rem 1.35rem;
    background: radial-gradient(circle at top left, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
    border: 1px solid rgba(148,163,184,0.55);
    box-shadow:
        0 14px 35px rgba(15,23,42,0.09),
        0 0 0 1px rgba(255,255,255,0.7) inset;
    transform-style: preserve-3d;
    transition: transform 0.25s ease-out, box-shadow 0.25s ease-out, border-color 0.25s ease-out;
    overflow: hidden;
}

/* Gradient glow border as pseudo element */
.glass-card-3d::before {
    content: "";
    position: absolute;
    inset: -1px;
    border-radius: inherit;
    padding: 1px;
    background: radial-gradient(circle at 0% 0%, rgba(56,189,248,0.7), transparent 55%),
                radial-gradient(circle at 100% 0%, rgba(129,140,248,0.6), transparent 60%),
                radial-gradient(circle at 0% 100%, rgba(236,72,153,0.55), transparent 60%);
    -webkit-mask:
        linear-gradient(#000 0 0) content-box,
        linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
            mask-composite: exclude;
    opacity: 0;
    transition: opacity 0.25s ease-out;
}

/* Inner soft highlight layer */
.glass-card-3d::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: radial-gradient(circle at top left, rgba(255,255,255,0.8), transparent 55%);
    mix-blend-mode: screen;
    opacity: 0.0;
    pointer-events: none;
    transition: opacity 0.25s ease-out;
}

/* 3D Hover motion + glow */
.glass-card-3d:hover {
    transform: translateY(-8px) translateZ(16px) rotateX(1deg);
    box-shadow:
        0 18px 45px rgba(15,23,42,0.22),
        0 0 30px rgba(56,189,248,0.35);
    border-color: rgba(59,130,246,0.75);
}
.glass-card-3d:hover::before {
    opacity: 1;
}
.glass-card-3d:hover::after {
    opacity: 0.7;
}

/* Floating tag chips */
.tech-tag {
    display: inline-block;
    padding: 0.18rem 0.7rem;
    margin: 0.16rem;
    font-size: 0.78rem;
    border-radius: 999px;
    border: 1px solid rgba(148,163,184,0.9);
    background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(241,245,249,0.98));
    box-shadow: 0 4px 10px rgba(148,163,184,0.35);
    transform: translateZ(10px);
    transition: transform 0.2s ease-out, box-shadow 0.2s ease-out, border-color 0.2s ease-out;
}
.tech-tag:hover {
    border-color: #0ea5e9;
    box-shadow: 0 7px 18px rgba(56,189,248,0.45);
    transform: translateY(-2px) translateZ(18px);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #ffffff, #e5f4ff);
    border-radius: 999px;
    border: 1px solid rgba(148,163,184,0.8);
    color: #0f172a;
    font-weight: 600;
    padding: 0.5rem 1.2rem;
    box-shadow:
        0 8px 18px rgba(148,163,184,0.65),
        0 0 0 1px rgba(255,255,255,0.8) inset;
    transition: transform 0.18s ease-out, box-shadow 0.18s ease-out, border-color 0.18s ease-out, background 0.18s ease-out;
}
.stButton > button:hover {
    border-color: #0ea5e9;
    background: linear-gradient(135deg, #e0f5ff, #ffffff);
    transform: translateY(-2px);
    box-shadow:
        0 11px 26px rgba(56,189,248,0.55),
        0 0 18px rgba(129,140,248,0.38);
}

/* Links */
a {
    color: #2563eb;
    font-weight: 500;
    text-decoration: none;
    transition: color 0.18s ease-out, text-shadow 0.18s ease-out;
}
a:hover {
    color: #0ea5e9;
    text-shadow: 0 0 9px rgba(56,189,248,0.7);
}

/* Popup overlay */
.popup-overlay {
    position: fixed;
    inset: 0;
    background: radial-gradient(circle at top, rgba(15,23,42,0.25), rgba(15,23,42,0.55));
    backdrop-filter: blur(6px);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Popup card */
.popup-card {
    position: relative;
    width: min(90%, 760px);
    border-radius: 1.4rem;
    padding: 1.6rem 1.7rem 1.3rem 1.7rem;
    background: radial-gradient(circle at top left, #ffffff 0, #f9fafb 45%, #eef2ff 100%);
    border: 1px solid rgba(148,163,184,0.75);
    box-shadow:
        0 20px 55px rgba(15,23,42,0.45),
        0 0 24px rgba(56,189,248,0.65);
    animation: popup-in 0.22s ease-out;
}

/* Popup gradient edge */
.popup-card::before {
    content: "";
    position: absolute;
    inset: -1px;
    border-radius: inherit;
    padding: 1px;
    background: conic-gradient(from 160deg,
        rgba(56,189,248,0.95),
        rgba(129,140,248,0.95),
        rgba(236,72,153,0.95),
        rgba(56,189,248,0.95)
    );
    -webkit-mask:
        linear-gradient(#000 0 0) content-box,
        linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
            mask-composite: exclude;
    opacity: 0.72;
}

/* Popup animation */
@keyframes popup-in {
    from {
        opacity: 0;
        transform: translateY(18px) scale(0.97);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

/* Popup close button container tweak */
.popup-close-row {
    text-align: right;
    margin-top: 0.8rem;
}

/* Sidebar radio hover */
.stRadio > div:hover {
    text-shadow: 0 0 8px rgba(56,189,248,0.45);
}

/* Metrics align nicer on home */
[data-testid="stMetricValue"] {
    font-weight: 700;
}

</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ----------------------------------------------------------
# SESSION STATE (for popups)
# ----------------------------------------------------------
if "show_project_popup" not in st.session_state:
    st.session_state.show_project_popup = False

if "popup_project_index" not in st.session_state:
    st.session_state.popup_project_index = None

# ----------------------------------------------------------
# CORE PERSONAL INFO (FROM YOUR RESUME)
# ----------------------------------------------------------
NAME = "V I B I N R A J  D"
ROLE_TITLE = "Senior Business Analyst"
LOCATION = "Chennai, Tamil Nadu"
EMAIL = "vibinrajd2002@gmail.com"
PHONE = "+91 9943906596"
LINKEDIN = "https://www.linkedin.com/in/vibinraj-d98"
GITHUB = "https://github.com/vibinrajd"

SUMMARY = (
    "Tech-driven Senior Business Analyst with hands-on experience in Data Analytics, "
    "Process Automation, and Business Intelligence. Skilled in building automated data "
    "pipelines, interactive dashboards, and scalable reporting systems using Power BI, SQL, "
    "Python, GCP BigQuery, and AppScript, with a strong focus on ETL automation, API "
    "integration, and CRM optimization across Marketing, Finance, and Operations."
)

RESUME_PATH = Path("files/Vibinraj D Resume.pdf")  # Put the PDF here locally

# ----------------------------------------------------------
# EXPERIENCE
# ----------------------------------------------------------
experience = [
    {
        "company": "Analytics Avenue",
        "role": "Senior Business Analyst",
        "period": "Jul 2025 – Present",
        "points": [
            "Designed and deployed automated BI systems using Power BI, GCP BigQuery, SQL, and AppScript, cutting report preparation time by 70%.",
            "Built ETL pipelines to automate data ingestion from APIs and databases for marketing and finance dashboards.",
            "Led development of company-wide audit, churn, and financial reporting dashboards to support strategic planning.",
            "Managed data governance, performance tracking, and workflows through Jira and automated reporting tools."
        ]
    },
    {
        "company": "Analytics Avenue",
        "role": "Business Analyst",
        "period": "Aug 2024 – Jul 2025",
        "points": [
            "Created self-refreshing marketing dashboards integrated with APIs for ad and client performance analytics.",
            "Automated CRM workflows, increasing lead tracking accuracy and response efficiency by 25%.",
            "Supported automation of reporting operations through BigQuery data pipelines and AppScript triggers.",
            "Contributed to end-to-end reporting frameworks connecting campaign insights with revenue impact."
        ]
    },
    {
        "company": "Analytics Avenue",
        "role": "Data Analyst Intern",
        "period": "Sep 2023 – Aug 2024",
        "points": [
            "Gained practical exposure to SQL, Power BI, Excel, and Python-based automation.",
            "Assisted in building prototype dashboards and EDA models that enhanced decision visibility by 20%.",
            "Developed foundational automation scripts and visual analytics projects across industries."
        ]
    }
]

# ----------------------------------------------------------
# PROJECTS
# ----------------------------------------------------------
projects = [
    {
        "title": "Marketing Performance Automation Dashboard",
        "summary": "Developed dual dashboards (Ad-side & Client-side) to track ad spend, ROI, and conversions.",
        "highlights": [
            "Automated data collection from Meta & Google APIs into Power BI for near real-time insights.",
            "Enhanced campaign optimization efficiency by 23% through automated performance reporting."
        ],
        "tech": ["Power BI", "GCP BigQuery", "Google AppScript", "Meta & Google APIs"]
    },
    {
        "title": "Churn Prediction & Sales Automation Dashboard",
        "summary": "Designed Python + BigQuery-based churn model to monitor and predict customer retention.",
        "highlights": [
            "Automated data refresh using API triggers, reducing manual reporting by 80%.",
            "Improved accuracy of retention tracking and boosted sales insights through predictive analytics."
        ],
        "tech": ["Python", "BigQuery", "Machine Learning", "Automation"]
    },
    {
        "title": "Automated Audit & Financial Reporting System",
        "summary": "Built an end-to-end automated Power BI dashboard integrating audit logs and financial KPIs.",
        "highlights": [
            "Automated daily updates with AppScript & BigQuery ETL scripts, improving reporting accuracy.",
            "Enabled real-time audit tracking and enhanced financial visibility for leadership decisions."
        ],
        "tech": ["Power BI", "BigQuery", "AppScript", "Financial Analytics"]
    },
    {
        "title": "Workflow & Employee Performance Automation",
        "summary": "Created an automated performance tracking system for employees using Power BI + AppScript.",
        "highlights": [
            "Integrated HR datasets via BigQuery for live workforce analytics, improving accuracy by 18%."
        ],
        "tech": ["Power BI", "BigQuery", "HR Analytics", "Automation"]
    }
]

# ----------------------------------------------------------
# SKILLS
# ----------------------------------------------------------
skills_primary = [
    "Power BI",
    "SQL",
    "Python (Pandas, NumPy, Matplotlib, Seaborn)",
    "GCP BigQuery",
    "Google AppScript Automation",
    "API Integration",
    "Time Series Analysis",
    "Exploratory Data Analysis (EDA)",
    "Marketing Analytics",
    "Financial Analytics",
    "Churn Analysis",
    "Market Basket Analysis"
]

skills_secondary = [
    "CRM Implementation & Optimization",
    "Workflow Automation",
    "Dashboard Automation",
    "Jira & Project Tracking",
    "Reporting Management",
    "Cross-Functional Collaboration"
]

# ----------------------------------------------------------
# EDUCATION
# ----------------------------------------------------------
education = [
    ("B.E. - Electrical & Electronics Engineering", "University College of Engineering, BIT Campus, Tiruchirappalli", "2019 – 2023", "CGPA - 7.68"),
    ("HSC", "Vidya Mandir Hr. Sec. School, Ariyalur", "2019", "77.5%"),
    ("SSLC", "Sri Krishna Hr. Sec. School, Cuddalore", "2017", "89.4%")
]

# ----------------------------------------------------------
# CERTIFICATIONS
# ----------------------------------------------------------
certifications = [
    "Data Processing Specialist - Aspiring Minds",
    "Data Analytics - Analytics Avenue",
    "Excel Certification - Great Learning",
    "Electric Vehicle Charging System - Coursera"
]

# ----------------------------------------------------------
# ACHIEVEMENTS
# ----------------------------------------------------------
achievements = [
    "CryptoTracker: Real-Time Market Analysis using Power BI with live APIs, improving analysis efficiency by 35%.",
    "EV Data Insights Dashboard: EV adoption & manufacturing analytics, improving insight accessibility by 30%.",
    "Market Basket Analysis using Python & Mlxtend, helping identify cross-selling opportunities and improving inventory management by 15%.",
    "Retail Sales Analysis & Insights using Python EDA, boosting profit optimization by 10%.",
    "Promoted to Senior Business Analyst within a year for leadership in automation projects.",
    "Built and deployed company-wide Power BI & BigQuery reporting ecosystem.",
    "Conducted Power BI & Marketing Analytics workshops under Analytics Avenue’s learning programs."
]

# ----------------------------------------------------------
# SIDEBAR NAV
# ----------------------------------------------------------
with st.sidebar:
    st.title("💼 Portfolio")
    page = st.radio(
        "Navigate",
        ["Home", "Experience", "Projects", "Skills", "Education", "Certifications", "Achievements", "Resume", "Contact"]
    )

# ----------------------------------------------------------
# SECTION HEADER HELPER
# ----------------------------------------------------------
def section_header(title: str):
    st.markdown(
        f"<div class='glow-text' style='font-size:1.8rem;font-weight:900;margin-bottom:0.3rem;'>{title}</div>",
        unsafe_allow_html=True
    )
    st.markdown("<div class='section-underline'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------
# POPUP RENDER HELPER
# ----------------------------------------------------------
def render_project_popup(idx: int):
    if idx is None or idx < 0 or idx >= len(projects):
        return
    proj = projects[idx]
    st.markdown("<div class='popup-overlay'>", unsafe_allow_html=True)
    st.markdown("<div class='popup-card'>", unsafe_allow_html=True)

    st.markdown(f"### {proj['title']}")
    st.markdown(f"**Overview:** {proj['summary']}")
    st.markdown(" ")
    st.markdown("**Key Contributions:**")
    for h in proj["highlights"]:
        st.markdown(f"- {h}")

    if proj["tech"]:
        st.markdown(" ")
        st.markdown("**Tech Stack:**")
        tech_html = "".join([f"<span class='tech-tag'>{t}</span>" for t in proj["tech"]])
        st.markdown(tech_html, unsafe_allow_html=True)

    st.markdown("<div class='popup-close-row'>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Close", key="close_popup_button"):
            st.session_state.show_project_popup = False
            st.session_state.popup_project_index = None
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

# ----------------------------------------------------------
# PAGES
# ----------------------------------------------------------
if page == "Home":
    section_header("Welcome")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"## {NAME}")
        st.markdown(f"### {ROLE_TITLE}")
        st.markdown(SUMMARY)
        st.markdown(" ")
        mcol1, mcol2, mcol3 = st.columns(3)
        with mcol1:
            st.metric("Experience", "1+ Years")
        with mcol2:
            st.metric("Focus", "Analytics & Automation")
        with mcol3:
            st.metric("Tools", "Power BI • SQL • Python")
    with col2:
        st.markdown("<div class='card-3d-wrapper'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-3d'>", unsafe_allow_html=True)
        st.markdown("#### Quick Snapshot")
        st.markdown(f"- 📍 Based in **{LOCATION}**")
        st.markdown("- 🎯 Focused on automated reporting & scalable BI")
        st.markdown("- 🤖 Experienced in marketing, finance & churn analytics")
        st.markdown("- 🚀 Strong interest in GenAI + advanced analytics")
        st.markdown("</div></div>", unsafe_allow_html=True)

elif page == "Experience":
    section_header("Work Experience")
    for exp in experience:
        st.markdown("<div class='card-3d-wrapper'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-3d'>", unsafe_allow_html=True)
        st.markdown(f"### {exp['role']} | {exp['company']}")
        st.markdown(f"**{exp['period']}**")
        st.markdown(" ")
        for p in exp["points"]:
            st.markdown(f"- {p}")
        st.markdown("</div></div>", unsafe_allow_html=True)
        st.markdown(" ")

elif page == "Projects":
    section_header("Projects")
    for i, proj in enumerate(projects):
        st.markdown("<div class='card-3d-wrapper'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-3d'>", unsafe_allow_html=True)
        cols = st.columns([3, 1])
        with cols[0]:
            st.markdown(f"### {proj['title']}")
            st.markdown(proj["summary"])
            st.markdown(" ")
            tech_html = "".join([f"<span class='tech-tag'>{t}</span>" for t in proj["tech"]])
            st.markdown(tech_html, unsafe_allow_html=True)
        with cols[1]:
            if st.button("View details", key=f"proj_btn_{i}"):
                st.session_state.show_project_popup = True
                st.session_state.popup_project_index = i
        st.markdown("</div></div>", unsafe_allow_html=True)
        st.markdown(" ")

    # Popup overlay if needed
    if st.session_state.show_project_popup:
        render_project_popup(st.session_state.popup_project_index)

elif page == "Skills":
    section_header("Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card-3d-wrapper'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-3d'>", unsafe_allow_html=True)
        st.markdown("### Technical Skills")
        for s in skills_primary:
            st.markdown(f"- {s}")
        st.markdown("</div></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card-3d-wrapper'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-3d'>", unsafe_allow_html=True)
        st.markdown("### Supporting & Functional Skills")
        for s in skills_secondary:
            st.markdown(f"- {s}")
        st.markdown("</div></div>", unsafe_allow_html=True)

elif page == "Education":
    section_header("Education")
    for degree, inst, yr, score in education:
        st.markdown("<div class='card-3d-wrapper'>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card-3d'>", unsafe_allow_html=True)
        st.markdown(f"### {degree}")
        st.markdown(f"{inst}")
        st.markdown(f"**{yr} | {score}**")
        st.markdown("</div></div>", unsafe_allow_html=True)
        st.markdown(" ")

elif page == "Certifications":
    section_header("Certifications")
    st.markdown("<div class='card-3d-wrapper'>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card-3d'>", unsafe_allow_html=True)
    for c in certifications:
        st.markdown(f"- {c}")
    st.markdown("</div></div>", unsafe_allow_html=True)

elif page == "Achievements":
    section_header("Achievements")
    st.markdown("<div class='card-3d-wrapper'>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card-3d'>", unsafe_allow_html=True)
    for a in achievements:
        st.markdown(f"- {a}")
    st.markdown("</div></div>", unsafe_allow_html=True)

elif page == "Resume":
    section_header("Resume")
    st.markdown("<div class='card-3d-wrapper'>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card-3d'>", unsafe_allow_html=True)
    if RESUME_PATH.exists():
        with open(RESUME_PATH, "rb") as f:
            st.download_button(
                "📄 Download Resume (PDF)",
                f,
                file_name="Vibinraj_D_Resume.pdf",
                mime="application/pdf"
            )
        st.markdown(
            "Your resume is embedded from the local `files/Vibinraj D Resume.pdf` path."
        )
    else:
        st.warning(
            "Resume file not found. Create a `files` folder and place your file as `Vibinraj D Resume.pdf` inside it."
        )
    st.markdown("</div></div>", unsafe_allow_html=True)

elif page == "Contact":
    section_header("Contact")
    st.markdown("<div class='card-3d-wrapper'>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card-3d'>", unsafe_allow_html=True)
    st.markdown(f"- **Email:** `{EMAIL}`")
    st.markdown(f"- **Phone:** `{PHONE}`")
    st.markdown(f"- **Location:** {LOCATION}")
    st.markdown(f"- **LinkedIn:** [{LINKEDIN}]({LINKEDIN})")
    st.markdown(f"- **GitHub:** [{GITHUB}]({GITHUB})")
    st.markdown("</div></div>", unsafe_allow_html=True)
