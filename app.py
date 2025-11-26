import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Vibinraj D | Portfolio", layout="wide")

# ============================================================
# Apple-Style Minimal Luxury CSS
# ============================================================
st.markdown("""
<style>

:root {
    --bg: #f5f5f7;
    --surface: #ffffff;
    --border: #e5e5e5;
    --text-dark: #111111;
    --text-medium: #444444;
    --accent: #0071e3;
}

/* Page background */
.stApp {
    background: var(--bg);
}

/* Container */
.container {
    max-width: 900px;
    margin: auto;
    padding-top: 2rem;
    animation: fadeIn 1s ease-out;
}

/* Fade animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
}

/* HEADER */
h1 {
    font-size: 3rem;
    font-weight: 800;
    color: var(--text-dark);
    letter-spacing: -1px;
    margin-bottom: 0.2rem;
}

.subtitle {
    font-size: 1.2rem;
    color: var(--text-medium);
    margin-bottom: 2.5rem;
}

/* Section titles */
.section-title {
    font-size: 1.7rem;
    font-weight: 700;
    color: var(--text-dark);
    margin-top: 2.8rem;
    margin-bottom: 0.4rem;
}

.section-line {
    height: 2px;
    width: 70px;
    background: var(--text-dark);
    opacity: 0.15;
}

/* CARDS - Apple style */
.card {
    background: var(--surface);
    padding: 2rem 2.2rem;
    border-radius: 20px;
    border: 1px solid var(--border);
    box-shadow:
        0 4px 12px rgba(0,0,0,0.04),
        0 0 0 1px rgba(255,255,255,0.9) inset;
    
    margin-top: 1.4rem;
    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow:
        0 8px 22px rgba(0,0,0,0.06),
        0 0 0 1px rgba(255,255,255,1) inset;
}

/* Typography */
h3 {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--text-dark);
    margin-bottom: 0.3rem;
}

p, li {
    font-size: 1rem;
    color: var(--text-medium);
    line-height: 1.55rem;
}

/* Lists */
ul {
    margin-top: 0.6rem;
}
ul li {
    margin-bottom: 6px;
    padding-left: 14px;
    position: relative;
}
ul li::before {
    content: "";
    position: absolute;
    left: 0;
    top: 9px;
    width: 5px;
    height: 5px;
    background: var(--accent);
    border-radius: 50%;
}

/* Buttons */
.stButton > button {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 0.5rem 1.1rem;
    font-weight: 600;
    color: var(--text-dark);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    border-color: var(--accent);
    color: var(--accent);
    box-shadow: 0 8px 16px rgba(0,0,0,0.06);
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# Load Resume
# ============================================================
resume_path = Path("files/Vibinraj D Resume.pdf")

# ============================================================
# Content Starts
# ============================================================
st.markdown("<div class='container'>", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("<h1>Vibinraj D</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Senior Business Analyst</p>", unsafe_allow_html=True)


# ------------------ SUMMARY ------------------
st.markdown("<div class='section-title'>Profile Summary</div><div class='section-line'></div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
Tech-driven Senior Business Analyst with strong experience in data analytics, workflow automation and 
business intelligence. Specialized in building automated reporting ecosystems using Power BI, SQL, BigQuery, 
Python and AppScript. Skilled in transforming large datasets into business decisions for marketing, finance 
and operations.
</div>
""", unsafe_allow_html=True)


# ------------------ EXPERIENCE ------------------
st.markdown("<div class='section-title'>Experience</div><div class='section-line'></div>", unsafe_allow_html=True)

experience = [
    {
        "role": "Senior Business Analyst",
        "company": "Analytics Avenue",
        "period": "Jul 2025 – Present",
        "items": [
            "Designed and deployed automated BI platforms using Power BI, SQL and BigQuery.",
            "Created ETL pipelines for marketing and finance reporting automation.",
            "Developed churn, audit and revenue dashboards.",
            "Implemented data governance and workflow orchestration using Jira."
        ]
    },
    {
        "role": "Business Analyst",
        "company": "Analytics Avenue",
        "period": "Aug 2024 – Jul 2025",
        "items": [
            "Built API-integrated dashboards for marketing analytics.",
            "Automated CRM tracking workflows improving accuracy by 25%.",
            "Developed reporting systems using BigQuery and AppScript.",
            "Linked campaign metrics with revenue intelligence."
        ]
    },
    {
        "role": "Data Analyst Intern",
        "company": "Analytics Avenue",
        "period": "Sep 2023 – Aug 2024",
        "items": [
            "Worked with SQL, Power BI, Python automation and Excel reporting.",
            "Developed prototype dashboards enhancing strategic visibility.",
            "Built EDA and automation scripts for internal analytics."
        ]
    }
]

for e in experience:
    st.markdown(f"""
    <div class='card'>
        <h3>{e['role']} – {e['company']}</h3>
        <p><b>{e['period']}</b></p>
        <ul>
            {''.join([f"<li>{i}</li>" for i in e['items']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)


# ------------------ PROJECTS ------------------
st.markdown("<div class='section-title'>Projects</div><div class='section-line'></div>", unsafe_allow_html=True)

projects = [
    {
        "name": "Marketing Performance Automation Dashboard",
        "desc": "Automated dashboard ecosystem for ad spend, ROI, CAC and conversion trends.",
        "highlights": [
            "Integrated Meta & Google Ads API data",
            "23% faster decision-making via automated refresh cycles"
        ]
    },
    {
        "name": "Churn Prediction & Sales Automation",
        "desc": "Python + BigQuery based predictive churn model with automated reporting.",
        "highlights": [
            "Reduced manual reporting by 80%",
            "Improved retention forecasting visibility"
        ]
    },
    {
        "name": "Audit & Financial Reporting Automation",
        "desc": "End-to-end automated audit + finance dashboards with ETL triggers.",
        "highlights": [
            "Daily scheduled automation",
            "Enhanced leadership reporting clarity"
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


# ------------------ SKILLS ------------------
st.markdown("<div class='section-title'>Skills</div><div class='section-line'></div>", unsafe_allow_html=True)

skills = {
    "Tools": ["Power BI", "Excel", "BigQuery", "AppScript"],
    "Programming": ["SQL", "Python"],
    "Analytics": ["Marketing Analytics", "Financial Analytics", "Churn Models", "Time Series", "EDA"],
    "Automation": ["API Integration", "ETL Automation"],
    "Operations": ["Jira", "Reporting Frameworks"]
}

st.markdown("<div class='card'>", unsafe_allow_html=True)
for cat, items in skills.items():
    st.markdown(f"**{cat}:** " + ", ".join(items))
st.markdown("</div>", unsafe_allow_html=True)


# ------------------ RESUME ------------------
st.markdown("<div class='section-title'>Resume</div><div class='section-line'></div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

if resume_path.exists():
    with open(resume_path, "rb") as f:
        st.download_button("Download Resume (PDF)", f, "Vibinraj_D_Resume.pdf", mime="application/pdf")
else:
    st.write("Resume file not found. Place it in files/Vibinraj D Resume.pdf")

st.markdown("</div>", unsafe_allow_html=True)

# End container
st.markdown("</div>", unsafe_allow_html=True)
