import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Portfolio | Vibinraj D", layout="wide")

# ------------------------------
# Custom CSS – clean, readable, modern
# ------------------------------
st.markdown("""
<style>

body {
    font-family: 'Inter', sans-serif;
}

h1, h2, h3 {
    font-weight: 700;
    color: #111111;
}

p, li {
    font-size: 0.95rem;
    color: #333333;
}

.card {
    background: #ffffff;
    padding: 1.4rem 1.6rem;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.05);
    margin-bottom: 1.4rem;
}

.section-title {
    font-size: 1.45rem;
    margin-bottom: 0.3rem;
    font-weight: 800;
    color: #111111;
}

.section-line {
    width: 70px;
    height: 3px;
    background: #2563eb;
    border-radius: 50px;
    margin-bottom: 1.2rem;
}

a {
    color: #2563eb;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

.container {
    max-width: 1000px;
    margin: auto;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# Load Resume PDF (you must place it locally: files/Vibinraj.pdf)
# ------------------------------
resume_path = Path("files/Vibinraj D Resume.pdf")

# ------------------------------
# Title
# ------------------------------
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<h1>Vibinraj D</h1>", unsafe_allow_html=True)
st.markdown("<p>Senior Business Analyst</p>", unsafe_allow_html=True)

# ------------------------------
# Section: Overview
# ------------------------------
st.markdown("<div class='section-title'>Profile Summary</div><div class='section-line'></div>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
Tech-driven Senior Business Analyst with 1+ year of experience in data analytics, automation and business intelligence. 
Experienced in building automated data pipelines, dashboards, reporting systems and workflow automation using Power BI, BigQuery, SQL, Python and AppScript. Skilled in transforming large datasets into actionable insights for marketing, finance and operations teams.
</div>
""", unsafe_allow_html=True)

# ------------------------------
# Section: Experience
# ------------------------------
st.markdown("<div class='section-title'>Experience</div><div class='section-line'></div>", unsafe_allow_html=True)

experience_data = [
    {
        "role": "Senior Business Analyst",
        "company": "Analytics Avenue",
        "period": "Jul 2025 – Present",
        "items": [
            "Designed and deployed automated BI systems using Power BI, GCP BigQuery, SQL and AppScript.",
            "Built ETL pipelines to automate data ingestion for marketing and finance analytics.",
            "Developed audit, churn and financial reporting dashboards.",
            "Managed data governance and workflow orchestration using Jira and automation scripts."
        ]
    },
    {
        "role": "Business Analyst",
        "company": "Analytics Avenue",
        "period": "Aug 2024 – Jul 2025",
        "items": [
            "Created API-based marketing dashboards for ad performance analytics.",
            "Automated CRM workflows improving lead tracking accuracy by 25%.",
            "Built reporting pipelines using BigQuery and AppScript.",
            "Linked campaign metrics with revenue impact frameworks."
        ]
    },
    {
        "role": "Data Analyst Intern",
        "company": "Analytics Avenue",
        "period": "Sep 2023 – Aug 2024",
        "items": [
            "Worked on SQL, Power BI, Python and Excel automation.",
            "Developed prototype dashboards improving decision visibility by 20%.",
            "Built automation scripts and EDA models for internal teams."
        ]
    }
]

for exp in experience_data:
    st.markdown(f"""
    <div class='card'>
        <h3>{exp['role']} – {exp['company']}</h3>
        <p><b>{exp['period']}</b></p>
        <ul>
            {''.join([f"<li>{item}</li>" for item in exp['items']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------
# Section: Projects
# ------------------------------
st.markdown("<div class='section-title'>Projects</div><div class='section-line'></div>", unsafe_allow_html=True)

projects = [
    {
        "name": "Marketing Performance Automation Dashboard",
        "desc": "Automated dashboards for ad spend, ROI and conversion tracking.",
        "highlights": [
            "Meta & Google Ads API integration",
            "23% faster decision-making via automated refresh"
        ]
    },
    {
        "name": "Churn Prediction & Sales Automation",
        "desc": "Churn prediction system using Python & BigQuery.",
        "highlights": [
            "80% manual reporting reduction",
            "Improved retention forecasting accuracy"
        ]
    },
    {
        "name": "Automated Audit & Financial Reporting",
        "desc": "Power BI + BigQuery based audit tracking with automated ETL.",
        "highlights": [
            "Daily automated updates",
            "Enhanced leadership financial visibility"
        ]
    }
]

for p in projects:
    st.markdown(f"""
    <div class='card'>
        <h3>{p['name']}</h3>
        <p>{p['desc']}</p>
        <ul>
            {''.join([f"<li>{h}</li>" for h in p['highlights']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------
# Section: Skills
# ------------------------------
st.markdown("<div class='section-title'>Skills</div><div class='section-line'></div>", unsafe_allow_html=True)

skills = {
    "Tools": ["Power BI", "Excel", "GCP BigQuery", "Google AppScript"],
    "Programming": ["SQL", "Python (Pandas, NumPy, Matplotlib, Seaborn)"],
    "Analytics": ["Marketing Analytics", "Financial Analytics", "Churn Analysis", "Market Basket Analysis", "Time Series", "EDA"],
    "Automation": ["API Integration", "AppScript Automation", "Workflow Automation"],
    "Project": ["Jira", "Reporting Management", "Cross-Functional Collaboration"]
}

st.markdown("<div class='card'>", unsafe_allow_html=True)
for category, items in skills.items():
    st.markdown(f"**{category}:** " + ", ".join(items))
st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# Section: Resume
# ------------------------------
st.markdown("<div class='section-title'>Resume</div><div class='section-line'></div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

if resume_path.exists():
    with open(resume_path, "rb") as f:
        st.download_button("Download Resume (PDF)", f, "Vibinraj_D_Resume.pdf", mime="application/pdf")
else:
    st.warning("Resume file not found. Place it inside files/Vibinraj D Resume.pdf")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
