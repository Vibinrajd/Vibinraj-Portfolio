import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Portfolio | Vibinraj D", layout="wide")

# ------------------------------
# Advanced Modern CSS (Animated)
# ------------------------------
st.markdown("""
<style>

/* ---------- ROOT VARIABLES ---------- */
:root {
    --bg: #f8fafc;
    --card-bg: #ffffff;
    --text-dark: #111111;
    --text-light: #333333;
    --accent: #2563eb;
    --shadow: rgba(0,0,0,0.08);
}

/* Global */
body {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    animation: fadeIn 0.8s ease-out;
}

/* Fade-in animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px);}
    to { opacity: 1; transform: translateY(0);}
}

/* Slide-in section titles */
.section-title {
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--text-dark);
    animation: slideIn 0.6s ease-out;
}
@keyframes slideIn {
    from { opacity:0; transform: translateX(-25px);}
    to { opacity:1; transform: translateX(0);}
}

.section-line {
    width: 70px;
    height: 3px;
    background: linear-gradient(90deg, #2563eb, #6366f1);
    border-radius: 10px;
    box-shadow: 0 0 8px rgba(99,102,241,0.4);
    animation: grow 0.8s ease-out;
}
@keyframes grow {
    from { width: 0px; }
    to { width: 70px; }
}

/* ---------- CARD STYLING ---------- */
.card {
    background: var(--card-bg);
    padding: 1.6rem 1.8rem;
    border-radius: 18px;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow:
        0 10px 24px var(--shadow),
        0 0 0 1px rgba(255,255,255,0.5) inset;

    transition: all 0.25s ease-out;
    animation: fadeIn 0.7s ease-out;
}

/* Card hover: depth + scale + subtle glow */
.card:hover {
    transform: translateY(-6px);
    box-shadow:
        0 18px 32px rgba(0,0,0,0.12),
        0 0 20px rgba(37,99,235,0.15);
    border-color: rgba(37,99,235,0.35);
}

/* Typography */
h1, h2, h3 {
    font-weight: 700;
    color: var(--text-dark);
}

p, li {
    font-size: 1rem;
    color: var(--text-light);
}

/* Links */
a {
    color: var(--accent);
    font-weight: 500;
    text-decoration: none;
    transition: 0.2s;
}
a:hover {
    color: #1d4ed8;
    text-shadow: 0 0 6px rgba(37,99,235,0.3);
}

/* Container */
.container {
    max-width: 1000px;
    margin: auto;
    animation: fadeIn 0.6s ease-out;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #ffffff, #eef2ff);
    border: 1px solid rgba(0,0,0,0.10);
    border-radius: 14px;
    padding: 0.55rem 1.3rem;
    font-weight: 600;
    transition: all 0.2s ease-out;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.stButton > button:hover {
    transform: translateY(-3px);
    border-color: #2563eb;
    box-shadow:
        0 10px 20px rgba(37,99,235,0.25),
        0 0 14px rgba(99,102,241,0.25);
}

/* List bullets */
ul li {
    margin-bottom: 6px;
    position: relative;
    padding-left: 15px;
}

ul li::before {
    content: "";
    position: absolute;
    left: 0;
    top: 9px;
    width: 6px;
    height: 6px;
    background: var(--accent);
    border-radius: 50%;
}

</style>
""", unsafe_allow_html=True)


# ------------------------------
# Load PDF
# ------------------------------
resume_path = Path("files/Vibinraj D Resume.pdf")

# ------------------------------
# Begin Container
# ------------------------------
st.markdown("<div class='container'>", unsafe_allow_html=True)

# ------------------------------
# Header
# ------------------------------
st.markdown("<h1>Vibinraj D</h1>", unsafe_allow_html=True)
st.markdown("<p>Senior Business Analyst</p>", unsafe_allow_html=True)

# ------------------------------
# Profile Summary
# ------------------------------
st.markdown("<div class='section-title'>Profile Summary</div><div class='section-line'></div>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
Tech-driven Senior Business Analyst with 1+ year of experience in data analytics, automation and business intelligence. 
Experienced in building automated data pipelines, dashboards, reporting systems and workflow automation using Power BI, BigQuery, SQL, Python and AppScript. Skilled in transforming large datasets into actionable insights for marketing, finance and operations teams.
</div>
""", unsafe_allow_html=True)

# ------------------------------
# Experience
# ------------------------------
st.markdown("<div class='section-title'>Experience</div><div class='section-line'></div>", unsafe_allow_html=True)

experience_data = [
    {
        "role": "Senior Business Analyst",
        "company": "Analytics Avenue",
        "period": "Jul 2025 – Present",
        "items": [
            "Designed and deployed automated BI systems using Power BI, GCP BigQuery, SQL and AppScript.",
            "Built ETL pipelines for marketing and finance analytics automation.",
            "Developed audit, churn and financial reporting dashboards.",
            "Managed data governance and workflow orchestration."
        ]
    },
    {
        "role": "Business Analyst",
        "company": "Analytics Avenue",
        "period": "Aug 2024 – Jul 2025",
        "items": [
            "Built API-based marketing dashboards.",
            "Automated CRM workflows improving tracking accuracy by 25%.",
            "Created reporting pipelines using BigQuery and AppScript.",
            "Connected campaign analytics with revenue insights."
        ]
    },
    {
        "role": "Data Analyst Intern",
        "company": "Analytics Avenue",
        "period": "Sep 2023 – Aug 2024",
        "items": [
            "Worked on SQL, Power BI, Python and automation.",
            "Developed prototype dashboards improving visibility by 20%.",
            "Built automation scripts and EDA models."
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
# Projects
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
# Skills
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
# Resume Download
# ------------------------------
st.markdown("<div class='section-title'>Resume</div><div class='section-line'></div>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)

if resume_path.exists():
    with open(resume_path, "rb") as f:
        st.download_button("Download Resume (PDF)", f, "Vibinraj_D_Resume.pdf", mime="application/pdf")
else:
    st.warning("Resume file not found. Place it inside files/Vibinraj D Resume.pdf")

st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# End Container
# ------------------------------
st.markdown("</div>", unsafe_allow_html=True)
