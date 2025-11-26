# ============================================================
# Portfolio App | Vibinraj D
# Apple-Style Minimal Luxury + Animations + Loader
# Single-page Streamlit portfolio
# ============================================================

import streamlit as st
from pathlib import Path

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="Vibinraj D | Portfolio",
    layout="wide"
)

# ------------------------------------------------------------
# APPLE-STYLE LOADING OVERLAY (CSS + HTML)
# ------------------------------------------------------------
st.markdown(
    """
<style>
/* ===========================
   Global Loading Overlay
   =========================== */

#loading-overlay {
    position: fixed;
    inset: 0;
    background: #f5f5f7;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    animation: fadeOutLoader 1.2s ease-out forwards;
    animation-delay: 1.3s;
}

/* Circular loader */
.loader {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  border: 3px solid rgba(0,0,0,0.12);
  border-top-color: #0071e3;
  animation: spinLoader 0.9s linear infinite;
}

/* Loader spin */
@keyframes spinLoader {
  to { transform: rotate(360deg); }
}

/* Loader fade-out */
@keyframes fadeOutLoader {
    from { opacity: 1; }
    to { opacity: 0; visibility: hidden; }
}
</style>

<div id="loading-overlay">
    <div class="loader"></div>
</div>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# MAIN GLOBAL CSS (APPLE-STYLE PREMIUM)
# ------------------------------------------------------------
st.markdown(
    """
<style>

/* ===========================================================
   Root theme variables (Apple-style)
   =========================================================== */

:root {
    --bg: #f5f5f7;
    --surface: rgba(255,255,255,0.82);
    --surface-strong: rgba(255,255,255,0.96);
    --border: #dedede;
    --border-soft: #e6e6e7;
    --text-dark: #111111;
    --text-medium: #3a3a3c;
    --accent: #0071e3;
    --radius: 22px;
    --shadow-soft: 0 10px 30px rgba(0,0,0,0.05);
    --shadow-hover: 0 18px 40px rgba(0,0,0,0.08);
}

/* ===========================================================
   Base page styling
   =========================================================== */

.stApp {
    background: var(--bg);
}

/* Remove default padding for a tighter Apple look */
main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* Global text smoothing */
body, p, h1, h2, h3, h4 {
    -webkit-font-smoothing: antialiased;
}

/* ===========================================================
   Container
   =========================================================== */

.container {
    max-width: 960px;
    margin: 0 auto;
    animation: fadeSlow 1.2s ease-out;
}

/* Simple fade */
@keyframes fadeSlow {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* ===========================================================
   Hero section
   =========================================================== */

.hero {
    padding-top: 1rem;
    padding-bottom: 1.5rem;
    animation: fadeUp 1s ease-out;
}

/* Fade-up animation */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(28px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Subtle slide-in animation */
@keyframes slideRight {
    from { opacity: 0; transform: translateX(-25px); }
    to { opacity: 1; transform: translateX(0); }
}

/* ===========================================================
   Headings & Typography
   =========================================================== */

h1 {
    font-size: 3.4rem;
    font-weight: 850;
    color: var(--text-dark);
    letter-spacing: -1.6px;
    margin-bottom: 0.15rem;
}

.hero-subtitle {
    font-size: 1.24rem;
    color: var(--text-medium);
    margin-bottom: 2.6rem;
    animation: slideRight 1.3s ease-out;
}

.section-title {
    font-size: 1.85rem;
    font-weight: 720;
    letter-spacing: -0.4px;
    color: var(--text-dark);
    margin-top: 3rem;
    margin-bottom: 0.35rem;
    animation: fadeUp 0.7s ease-out;
}

/* Section underline/line */
.section-line {
    width: 90px;
    height: 2px;
    background: var(--text-dark);
    opacity: 0.14;
    margin-bottom: 1rem;
    animation: fadeUp 1.1s ease-out;
}

/* Smaller heading in cards */
h3 {
    font-size: 1.24rem;
    font-weight: 700;
    margin-bottom: 0.32rem;
    color: var(--text-dark);
}

/* Body text */
p {
    font-size: 1.04rem;
    color: var(--text-medium);
    line-height: 1.65rem;
}

/* ===========================================================
   Cards – glassy Apple-like surfaces
   =========================================================== */

.card {
    position: relative;
    background: var(--surface);
    padding: 2rem 2.3rem;
    border-radius: var(--radius);
    border: 1px solid var(--border-soft);
    backdrop-filter: blur(22px);
    margin-top: 1.5rem;

    box-shadow:
        var(--shadow-soft),
        0 0 0 1px rgba(255,255,255,0.8) inset;

    animation: fadeUp 1s ease-out;
    transition:
        transform 0.38s ease,
        box-shadow 0.38s ease,
        filter 0.35s ease;
}

/* Card hover: micro tilt + brightness */
.card:hover {
    transform: translateY(-7px) scale(1.015) rotateX(0.8deg);
    box-shadow:
        var(--shadow-hover),
        0 0 0 1px rgba(255,255,255,1) inset;
    filter: brightness(1.03);
}

/* Shimmer on hover */
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

/* ===========================================================
   Lists – pure controlled bullets (avoid double bullets)
   =========================================================== */

ul {
    margin-top: 0.7rem;
    padding-left: 0;
    list-style: none;
}

ul li {
    list-style: none !important;
    margin-bottom: 7px;
    padding-left: 16px;
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

/* ===========================================================
   Links
   =========================================================== */

a {
    color: var(--accent);
    text-decoration: none;
    font-weight: 600;
    transition: opacity 0.2s ease;
}

a:hover {
    text-decoration: underline;
    opacity: 0.85;
}

/* ===========================================================
   Buttons – Apple-ish CTA
   =========================================================== */

.stButton > button {
    background: var(--surface-strong);
    padding: 0.55rem 1.2rem;
    border-radius: 12px;
    border: 1px solid var(--border-soft);
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

/* ===========================================================
   Horizontal Rule – minimal divider
   =========================================================== */

hr {
    border: none;
    height: 1px;
    background: #d2d2d3;
    opacity: 0.4;
    margin: 2.3rem 0;
}

/* ===========================================================
   Small label styles
   =========================================================== */

.meta-label {
    font-size: 0.88rem;
    color: #6c6c70;
    margin-bottom: 0.5rem;
}

/* Contact line style */
.contact-line {
    font-size: 0.98rem;
    color: var(--text-medium);
    line-height: 1.5rem;
}

</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# DATA: EXPERIENCE, PROJECTS, SKILLS, EDUCATION, ETC.
# ------------------------------------------------------------

# Experience entries
experience_data = [
    {
        "role": "Senior Business Analyst",
        "company": "Analytics Avenue",
        "period": "Jul 2025 – Present",
        "items": [
            "Designed and deployed automated BI systems using Power BI, BigQuery, SQL and AppScript.",
            "Built ETL pipelines for automated marketing and finance reporting.",
            "Developed churn, audit and revenue dashboards for leadership visibility.",
            "Implemented data governance standards and workflow automation at scale.",
        ],
    },
    {
        "role": "Business Analyst",
        "company": "Analytics Avenue",
        "period": "Aug 2024 – Jul 2025",
        "items": [
            "Developed API-driven dashboards for marketing and campaign performance analytics.",
            "Automated CRM tracking workflows, improving lead tracking accuracy by 25%.",
            "Built reporting automation with BigQuery and AppScript for cross-functional teams.",
            "Linked campaign KPIs with revenue impact frameworks.",
        ],
    },
    {
        "role": "Data Analyst Intern",
        "company": "Analytics Avenue",
        "period": "Sep 2023 – Aug 2024",
        "items": [
            "Worked with SQL, Python, Power BI and Excel on analytics and automation projects.",
            "Developed prototype dashboards improving decision visibility by 20%.",
            "Built EDA scripts and internal automation utilities for reporting.",
        ],
    },
]

# Project entries
projects_data = [
    {
        "name": "Marketing Performance Automation Dashboard",
        "desc": "Automated analytics for advertising performance, including ROI, CAC, spend and conversion trends.",
        "highlights": [
            "Integrated Meta and Google Ads APIs to centralize performance data.",
            "Reduced reporting time by approximately 23% through automated refresh cycles.",
        ],
    },
    {
        "name": "Churn Prediction & Sales Automation",
        "desc": "Predictive churn analytics and automated reporting using Python and BigQuery.",
        "highlights": [
            "Reduced manual effort for churn reporting by nearly 80%.",
            "Improved retention forecasting visibility for sales and account teams.",
        ],
    },
    {
        "name": "Audit & Financial Reporting Automation",
        "desc": "End-to-end automated dashboards for audit logs and financial KPIs.",
        "highlights": [
            "Implemented daily scheduled ETL refresh for audit and finance data.",
            "Enhanced leadership decision clarity with real-time financial views.",
        ],
    },
]

# Skills dictionary
skills_data = {
    "Tools": ["Power BI", "Excel", "BigQuery", "Google AppScript"],
    "Programming": ["SQL", "Python"],
    "Analytics": [
        "Marketing Analytics",
        "Financial Analytics",
        "Churn Models",
        "Time Series",
        "Exploratory Data Analysis",
    ],
    "Automation": ["API Integration", "ETL Automation"],
    "Operations": ["Jira", "Reporting Frameworks", "Cross-Functional Collaboration"],
}

# Education entries
education_data = [
    {
        "degree": "B.E. - Electrical & Electronics Engineering",
        "institution": "University College of Engineering, BIT Campus, Tiruchirappalli",
        "years": "2019 – 2023",
        "detail": "CGPA: 7.68",
    },
    {
        "degree": "Higher Secondary (HSC)",
        "institution": "Vidya Mandir Hr. Sec. School, Ariyalur",
        "years": "2019",
        "detail": "Percentage: 77.5%",
    },
    {
        "degree": "SSLC",
        "institution": "Sri Krishna Hr. Sec. School, Cuddalore",
        "years": "2017",
        "detail": "Percentage: 89.4%",
    },
]

# Certifications
certifications_data = [
    "Data Processing Specialist – Aspiring Minds",
    "Data Analytics – Analytics Avenue",
    "Excel Certification – Great Learning",
    "Electric Vehicle Charging System – Coursera",
]

# Achievements
achievements_data = [
    "Developed a real-time crypto analytics dashboard (CryptoTracker) in Power BI, improving analysis efficiency.",
    "Built EV adoption and manufacturing analytics dashboards supporting strategic decision making.",
    "Implemented market basket analysis using Python to identify cross-selling patterns.",
    "Conducted retail sales analysis with EDA to optimize discounts and highlight high-margin products.",
    "Promoted to Senior Business Analyst within one year for leadership in automation projects.",
]

# Contact info
contact_data = {
    "location": "Chennai, Tamil Nadu, India",
    "email": "vibinrajd2002@gmail.com",
    "phone": "+91 9943906596",
    "linkedin": "https://www.linkedin.com/in/vibinraj-d98",
    "github": "https://github.com/vibinrajd",
}

# Resume path (local)
resume_path = Path("files/Vibinraj D Resume.pdf")

# ------------------------------------------------------------
# HELPER FUNCTIONS
# ------------------------------------------------------------

def render_section_header(title: str) -> None:
    """Render a section title and underline."""
    st.markdown(
        f"<div class='section-title'>{title}</div><div class='section-line'></div>",
        unsafe_allow_html=True,
    )


def render_experience_section(experience_list) -> None:
    """Render the Experience section using card layout."""
    for experience in experience_list:
        role = experience["role"]
        company = experience["company"]
        period = experience["period"]
        items_html = "".join(f"<li>{i}</li>" for i in experience["items"])

        st.markdown(
            f"""
<div class='card'>
    <h3>{role} – {company}</h3>
    <p><b>{period}</b></p>
    <ul>
        {items_html}
    </ul>
</div>
""",
            unsafe_allow_html=True,
        )


def render_projects_section(projects_list) -> None:
    """Render the Projects section with highlights under each project."""
    for project in projects_list:
        name = project["name"]
        desc = project["desc"]
        highlights_html = "".join(f"<li>{h}</li>" for h in project["highlights"])

        st.markdown(
            f"""
<div class='card'>
    <h3>{name}</h3>
    <p>{desc}</p>
    <ul>
        {highlights_html}
    </ul>
</div>
""",
            unsafe_allow_html=True,
        )


def render_skills_section(skills_dict) -> None:
    """Render skills as labeled rows inside a single card."""
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    for category, items in skills_dict.items():
        label = f"**{category}:** "
        values = ", ".join(items)
        st.markdown(label + values)
    st.markdown("</div>", unsafe_allow_html=True)


def render_education_section(education_list) -> None:
    """Render the Education section."""
    for edu in education_list:
        degree = edu["degree"]
        institution = edu["institution"]
        years = edu["years"]
        detail = edu["detail"]

        st.markdown(
            f"""
<div class='card'>
    <h3>{degree}</h3>
    <p>{institution}</p>
    <p><b>{years}</b> | {detail}</p>
</div>
""",
            unsafe_allow_html=True,
        )


def render_certifications_section(certifications_list) -> None:
    """Render the Certifications section."""
    cert_items_html = "".join(f"<li>{c}</li>" for c in certifications_list)

    st.markdown(
        f"""
<div class='card'>
    <h3>Certifications</h3>
    <ul>
        {cert_items_html}
    </ul>
</div>
""",
        unsafe_allow_html=True,
    )


def render_achievements_section(achievements_list) -> None:
    """Render the Achievements section."""
    items_html = "".join(f"<li>{a}</li>" for a in achievements_list)

    st.markdown(
        f"""
<div class='card'>
    <h3>Key Achievements</h3>
    <ul>
        {items_html}
    </ul>
</div>
""",
        unsafe_allow_html=True,
    )


def render_resume_section(path: Path) -> None:
    """Render the resume download section."""
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h3>Resume</h3>", unsafe_allow_html=True)

    if path.exists():
        with open(path, "rb") as f:
            st.download_button(
                "Download Resume (PDF)",
                f,
                "Vibinraj_D_Resume.pdf",
                mime="application/pdf",
            )
    else:
        st.write(
            "Resume file not found. Place it under: files/Vibinraj D Resume.pdf"
        )

    st.markdown("</div>", unsafe_allow_html=True)


def render_contact_section(contact_dict) -> None:
    """Render the contact details section."""
    location = contact_dict["location"]
    email = contact_dict["email"]
    phone = contact_dict["phone"]
    linkedin = contact_dict["linkedin"]
    github = contact_dict["github"]

    st.markdown(
        f"""
<div class='card'>
    <h3>Contact</h3>
    <p class="contact-line"><b>Location:</b> {location}</p>
    <p class="contact-line"><b>Email:</b> {email}</p>
    <p class="contact-line"><b>Phone:</b> {phone}</p>
    <p class="contact-line"><b>LinkedIn:</b> <a href="{linkedin}" target="_blank">{linkedin}</a></p>
    <p class="contact-line"><b>GitHub:</b> <a href="{github}" target="_blank">{github}</a></p>
</div>
""",
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------
# PAGE CONTENT RENDERING
# ------------------------------------------------------------

# Wrap everything in container
st.markdown("<div class='container'>", unsafe_allow_html=True)

# HERO SECTION
st.markdown("<div class='hero'>", unsafe_allow_html=True)
st.markdown("<h1>Vibinraj D</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-subtitle'>Senior Business Analyst</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# PROFILE SUMMARY
render_section_header("Profile Summary")
st.markdown(
    """
<div class='card'>
Tech-driven Senior Business Analyst with experience in data analytics, automation and 
business intelligence. Skilled in building automated reporting systems, ETL pipelines, dashboards 
and workflow automation using Power BI, SQL, Python, BigQuery and AppScript. Focused on converting 
raw datasets into practical insights that support decisions across marketing, finance and operations.
</div>
""",
    unsafe_allow_html=True,
)

# EXPERIENCE
render_section_header("Experience")
render_experience_section(experience_data)

# PROJECTS
render_section_header("Projects")
render_projects_section(projects_data)

# SKILLS
render_section_header("Skills")
render_skills_section(skills_data)

# EDUCATION
render_section_header("Education")
render_education_section(education_data)

# CERTIFICATIONS
render_section_header("Certifications")
render_certifications_section(certifications_data)

# ACHIEVEMENTS
render_section_header("Achievements")
render_achievements_section(achievements_data)

# RESUME
render_section_header("Resume")
render_resume_section(resume_path)

# CONTACT
render_section_header("Contact")
render_contact_section(contact_data)

# Close container
st.markdown("</div>", unsafe_allow_html=True)
