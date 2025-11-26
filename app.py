import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Vibinraj D | Portfolio", layout="wide")

# ============================================
# ADVANCED UI CSS (Glass + Depth + Motion)
# ============================================
st.markdown("""
<style>

:root {
    --bg: #eef2f7;
    --card: rgba(255,255,255,0.78);
    --border: rgba(0,0,0,0.08);
    --shadow: rgba(0,0,0,0.12);
    --accent: #3066ff;
    --font-dark: #0f0f0f;
    --font-light: #333333;
}

/* Page background */
.stApp {
    background: var(--bg);
}

/* Center container */
.container {
    max-width: 900px;
    margin: auto;
    animation: fadeIn 0.9s ease-out;
}

/* Fade-in animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px);}
    to { opacity: 1; transform: translateY(0);}
}

/* Section titles */
.section-title {
    font-size: 1.9rem;
    font-weight: 800;
    color: var(--font-dark);
    letter-spacing: -0.5px;
    margin-top: 2.5rem;
    margin-bottom: 0.4rem;
    animation: slideIn 0.55s ease-out;
}

@keyframes slideIn {
    from { opacity:0; transform: translateX(-18px); }
    to { opacity:1; transform: translateX(0); }
}

.section-line {
    width: 85px;
    height: 4px;
    border-radius: 8px;
    background: linear-gradient(90deg, var(--accent), #7b5dfc);
    animation: grow 0.7s ease-out;
}
@keyframes grow {
    from { width: 0px; }
    to { width: 85px; }
}

/* Premium glass-card */
.card {
    background: var(--card);
    padding: 1.8rem 2rem;
    border-radius: 20px;
    border: 1px solid var(--border);
    backdrop-filter: blur(14px);
    box-shadow:
        0 12px 30px var(--shadow),
        0 0 0 1px rgba(255,255,255,0.4) inset;
    margin-top: 1.2rem;

    transform: translateY(0px) scale(1);
    transition: all 0.28s ease;
    animation: fadeIn 0.9s ease-out;
}

.card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow:
        0 18px 38px rgba(0,0,0,0.18),
        0 0 14px rgba(48,102,255,0.18);
    border-color: rgba(48,102,255,0.4);
}

/* Typography */
h1 {
    font-size: 3rem;
    font-weight: 900;
    color: var(--font-dark);
    letter-spacing: -1.5px;
    margin-top: 1rem;
    margin-bottom: -0.8rem;
}

h3 {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--font-dark);
}

p, li {
    font-size: 1rem;
    color: var(--font-light);
    line-height: 1.55rem;
}

/* Bullet enhancement */
ul li {
    margin-bottom: 6px;
    position: relative;
    padding-left: 14px;
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

/* Clean links */
a {
    color: var(--accent);
    text-decoration: none;
    font-weight: 600;
}
a:hover {
    text-decoration: underline;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #ffffff, #eef1ff);
    border: 1px solid rgba(0,0,0,0.15);
    border-radius: 12px;
    padding: 0.5rem 1.1rem;
    font-weight: 600;
    transition: 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    border-color: var(--accent);
    box-shadow:
        0 10px 20px rgba(48,102,255,0.25),
        0 0 12px rgba(48,102,255,0.25);
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------
# Begin Content
# ---------------------------------------
st.markdown("<div class='container'>", unsafe_allow_html=True)

# Header
st.markdown("<h1>Vibinraj D</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:1.2rem;color:#444;'>Senior Business Analyst</p>", unsafe_allow_html=True)


# ================================
# Profile Summary
# ================================
st.markdown("<div class='section-title'>Profile Summary</div><div class='section-line'></div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
Tech-driven Senior Business Analyst with hands-on expertise in data analytics, automation, 
and business intelligence. Experienced in developing automated data pipelines, dashboards, 
reporting frameworks, and workflow automation using Power BI, BigQuery, SQL, Python and AppScript. 
Focused on transforming raw datasets into insights that drive marketing, finance and operational decisions.
</div>
""", unsafe_allow_html=True)


# ================================
# Experience
# ================================
st.markdown("<div class='section-title'>Experience</div><div class='section-line'></div>", unsafe_allow_html=True)

experience = [
    {
        "role": "Senior Business Analyst",
        "company": "Analytics Avenue",
        "period": "Jul 2025 – Present",
        "items": [
            "Designed and deployed automated BI systems using Power BI, BigQuery, SQL and AppScript.",
            "Built ETL automation pipelines for marketing and finance analytics.",
            "Developed audit, churn and financial dashboards improving decision visibility.",
            "Managed data governance, automated reporting workflows and Jira-based tracking."
        ]
    },
    {
        "role": "Business Analyst",
        "company": "Analytics Avenue",
        "period": "Aug 2024 – Jul 2025",
        "items": [
            "Created API-based dashboards for ad and client performance analytics.",
            "Automated CRM workflows enhancing lead accuracy by 25%.",
            "Built reporting pipelines using BigQuery + AppScript automation.",
            "Linked campaign insights with revenue impact layers."
        ]
    },
    {
        "role": "Data Analyst Intern",
        "company": "Analytics Avenue",
        "period": "Sep 2023 – Aug 2024",
        "items": [
            "Worked on SQL, Power BI, Python automation and Excel enhancements.",
            "Developed prototype dashboards improving decision visibility by 20%.",
            "Built automation scripts and EDA-based insights for internal teams."
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


# ================================
# Projects
# ================================
st.markdown("<div class='section-title'>Projects</div><div class='section-line'></div>", unsafe_allow_html=True)

projects = [
    {
        "name": "Marketing Performance Automation Dashboard",
        "desc": "Automated reporting for ad spend, ROI, CAC and conversion performance.",
        "highlights": [
            "Meta and Google Ads API integration",
            "23% faster decision-making through live refresh cycles"
        ]
    },
    {
        "name": "Churn Prediction & Sales Automation",
        "desc": "Predictive churn model with automated reporting layers.",
        "highlights": [
            "80% manual reporting reduction",
            "Higher retention forecasting accuracy"
        ]
    },
    {
        "name": "Automated Audit & Financial Reporting",
        "desc": "Real-time audit and finance analytics with automated ETL runs.",
        "highlights": [
            "Daily automated updates",
            "Improved leadership reporting clarity"
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


# ================================
# Skills
# ================================
st.markdown("<div class='section-title'>Skills</div><div class='section-line'></div>", unsafe_allow_html=True)

skills = {
    "Tools": ["Power BI", "Excel", "GCP BigQuery", "Google AppScript"],
    "Programming": ["SQL", "Python (Pandas, NumPy, Matplotlib, Seaborn)"],
    "Analytics": ["Marketing Analytics", "Financial Analytics", "Churn Models", "Market Basket Analysis", "Time Series", "EDA"],
    "Automation": ["API Integration", "AppScript Automation", "Workflow Automation"],
    "Operational": ["Jira", "Reporting Management", "Cross-Functional Collaboration"]
}

st.markdown("<div class='card'>", unsafe_allow_html=True)
for cat, items in skills.items():
    st.markdown(f"**{cat}:** " + ", ".join(items))
st.markdown("</div>", unsafe_allow_html=True)


# ================================
# Resume Download
# ================================
st.markdown("<div class='section-title'>Resume</div><div class='section-line'></div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

resume_path = Path("files/Vibinraj D Resume.pdf")
if resume_path.exists():
    with open(resume_path, "rb") as pdf:
        st.download_button("Download Resume (PDF)", pdf, "Vibinraj_D_Resume.pdf", mime="application/pdf")
else:
    st.write("Resume file not found. Place it in files/Vibinraj D Resume.pdf")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
