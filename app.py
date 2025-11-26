import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Vibinraj D | Portfolio", layout="wide")

# ============================================================
# APPLE-STYLE MINIMAL LUXURY + ADVANCED ANIMATIONS
# ============================================================
st.markdown("""
<style>

:root {
    --bg: #f5f5f7;
    --surface: rgba(255,255,255,0.82);
    --surface-strong: rgba(255,255,255,0.9);
    --border: #e6e6e7;
    --text-dark: #111111;
    --text-medium: #3a3a3c;
    --accent: #0071e3;
    --radius: 22px;
}

/* Page background */
.stApp {
    background: var(--bg);
}

/* Fade animations */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeSlow {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideRight {
    from { opacity: 0; transform: translateX(-25px); }
    to { opacity: 1; transform: translateX(0); }
}

/* Container */
.container {
    max-width: 900px;
    margin: auto;
    padding-top: 2.4rem;
    animation: fadeSlow 1.2s ease-out;
}

/* Hero Section */
.hero {
    text-align: left;
    padding-top: 1rem;
    padding-bottom: 1rem;
    animation: fadeUp 1s ease-out;
}

/* Header text */
h1 {
    font-size: 3.4rem;
    font-weight: 850;
    color: var(--text-dark);
    letter-spacing: -1.6px;
    margin-bottom: 0.3rem;
}

.subtitle {
    color: var(--text-medium);
    font-size: 1.22rem;
    margin-bottom: 2.7rem;
    animation: slideRight 1.3s ease-out;
}

/* Section titles */
.section-title {
    font-size: 1.85rem;
    font-weight: 700;
    letter-spacing: -0.4px;
    color: var(--text-dark);
    margin-top: 3rem;
    margin-bottom: 0.3rem;
    animation: fadeUp 0.7s ease-out;
}

.section-line {
    width: 90px;
    height: 2px;
    background: var(--text-dark);
    opacity: 0.14;
    margin-bottom: 1rem;
    animation: fadeUp 1.1s ease-out;
}

/* Card container */
.card {
    position: relative;
    background: var(--surface);
    padding: 2rem 2.3rem;
    border-radius: var(--radius);
    border: 1px solid var(--border);
    backdrop-filter: blur(22px);
    margin-top: 1.5rem;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.05),
        0 0 0 1px rgba(255,255,255,0.8) inset;

    animation: fadeUp 1s ease-out;
    transition:
        transform 0.38s ease,
        box-shadow 0.38s ease,
        filter 0.35s ease;
}

/* Card hover animations */
.card:hover {
    transform: translateY(-7px) scale(1.015) rotateX(1deg);
    box-shadow:
        0 18px 40px rgba(0,0,0,0.08),
        0 0 0 1px rgba(255,255,255,1) inset;
    filter: brightness(1.03);
}

/* Shimmer effect */
.card::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: var(--radius);
    opacity: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.35), transparent 70%);
    mix-blend-mode: overlay;
    transition: opacity 0.35s ease;
}

.card:hover::after {
    opacity: 1;
}

/* Typography */
h3 {
    font-size: 1.23rem;
    font-weight: 700;
    margin-bottom: 0.35rem;
    color: var(--text-dark);
}

p, li {
    font-size: 1.05rem;
    color: var(--text-medium);
    line-height: 1.62rem;
}

/* Lists */
ul {
    margin-top: 0.7rem;
}
ul li {
    padding-left: 15px;
    margin-bottom: 7px;
    position: relative;
}
ul li::before {
    content: "";
    position: absolute;
    left: 0;
    top: 10px;
    width: 5px;
    height: 5px;
    background: var(--accent);
    border-radius: 50%;
}

/* Apple-style button */
.stButton > button {
    background: var(--surface-strong);
    padding: 0.55rem 1.2rem;
    border-radius: 12px;
    border: 1px solid var(--border);
    color: var(--text-dark);
    font-weight: 600;
    transition: 0.3s ease;
    box-shadow: 0 6px 16px rgba(0,0,0,0.05);
}

.stButton > button:hover {
    transform: translateY(-3px);
    border-color: var(--accent);
    color: var(--accent);
    box-shadow: 0 10px 24px rgba(0,0,0,0.08);
}

/* Separators */
hr {
    border: none;
    height: 1px;
    background: #d2d2d3;
    opacity: 0.4;
    margin: 2.3rem 0;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# Load resume
# ============================================================
resume_path = Path("files/Vibinraj D Resume.pdf")

# ============================================================
# Start Content
# ============================================================
st.markdown("<div class='container'>", unsafe_allow_html=True)

# HERO HEADER
st.markdown("<div class='hero'>", unsafe_allow_html=True)
st.markdown("<h1>Vibinraj D</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Senior Business Analyst</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# PROFILE SUMMARY
# ============================================================
st.markdown("<div class='section-title'>Profile Summary</div><div class='section-line'></div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
Tech-driven Senior Business Analyst with expertise in data analytics, automation, and business 
intelligence. Skilled in designing automated reporting systems, ETL pipelines, dashboards, 
and workflow automation using Power BI, SQL, Python, BigQuery, and AppScript. Focused on 
transforming data into actionable insights across marketing, finance, and operations.
</div>
""", unsafe_allow_html=True)

# ============================================================
# EXPERIENCE
# ============================================================
st.markdown("<div class='section-title'>Experience</div><div class='section-line'></div>", unsafe_allow_html=True)

experience = [
    {
        "role": "Senior Business Analyst",
        "company": "Analytics Avenue",
        "period": "Jul 2025 – Present",
        "items": [
            "Designed and deployed automated BI systems using Power BI, BigQuery, SQL and AppScript.",
            "Built ETL pipelines for automated marketing and finance reporting.",
            "Developed churn, audit and revenue dashboards.",
            "Implemented company-wide data governance and workflow automation."
        ]
    },
    {
        "role": "Business Analyst",
        "company": "Analytics Avenue",
        "period": "Aug 2024 – Jul 2025",
        "items": [
            "Developed API-driven dashboards for marketing analytics.",
            "Automated CRM tracking workflows improving accuracy by 25%.",
            "Built BigQuery + AppScript reporting automation systems.",
            "Connected campaign KPIs with revenue intelligence insights."
        ]
    },
    {
        "role": "Data Analyst Intern",
        "company": "Analytics Avenue",
        "period": "Sep 2023 – Aug 2024",
        "items": [
            "Worked with SQL, Python and Power BI for analytics and automation.",
            "Developed prototype dashboards improving decision visibility by 20%.",
            "Built EDA and internal automation scripts."
        ]
    }
]

for e in experience:
    st.markdown(f"""
    <div class='card'>
        <h3>{e['role']} – {e['company']}</h3>
        <p><b>{e['period']}</b></p>
        <ul>
            {''.join(f'<li>{i}</li>' for i in e['items'])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# PROJECTS
# ============================================================
st.markdown("<div class='section-title'>Projects</div><div class='section-line'></div>", unsafe_allow_html=True)

projects = [
    {
        "name": "Marketing Performance Automation Dashboard",
        "desc": "Automated reporting ecosystem for advertising metrics: ROI, CAC, spend and conversion trends.",
        "highlights": [
            "Integrated Meta & Google Ads APIs",
            "Reduced reporting time by 23%"
        ]
    },
    {
        "name": "Churn Prediction & Sales Automation",
        "desc": "Predictive churn model with automated reporting layers in Python and BigQuery.",
        "highlights": [
            "80% manual reporting reduction",
            "Improved retention forecasting accuracy"
        ]
    },
    {
        "name": "Audit & Financial Reporting Automation",
        "desc": "Real-time audit + finance analytics with scheduled ETL refresh.",
        "highlights": [
            "Daily automated updates",
            "Enhanced leadership decision visibility"
        ]
    }
]

for p in projects:
    st.markdown(f"""
    <div class='card'>
        <h3>{p['name']}</h3>
        <p>{p['desc']}</p>
        <ul>
            {''.join(f'<li>{h}</li>' for h in p['highlights'])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# SKILLS SECTION
# ============================================================
st.markdown("<div class='section-title'>Skills</div><div class='section-line'></div>", unsafe_allow_html=True)

skills = {
    "Tools": ["Power BI", "Excel", "BigQuery", "AppScript"],
    "Programming": ["SQL", "Python"],
    "Analytics": ["Marketing Analytics", "Financial Analytics", "Churn Models", "EDA", "Time Series"],
    "Automation": ["API Integration", "ETL Automation"],
    "Operations": ["Jira", "Reporting Frameworks"]
}

st.markdown("<div class='card'>", unsafe_allow_html=True)
for cat, items in skills.items():
    st.markdown(f"**{cat}:** " + ", ".join(items))
st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# RESUME DOWNLOAD
# ============================================================
st.markdown("<div class='section-title'>Resume</div><div class='section-line'></div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

if resume_path.exists():
    with open(resume_path, "rb") as f:
        st.download_button("Download Resume (PDF)", f, "Vibinraj_D_Resume.pdf", mime="application/pdf")
else:
    st.write("Resume not found. Place it under files/Vibinraj D Resume.pdf")

st.markdown("</div>", unsafe_allow_html=True)

# End container
st.markdown("</div>", unsafe_allow_html=True)
