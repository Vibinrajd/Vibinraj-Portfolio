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

/* Text */
h1, h2, h3 {
    font-weight: 700;
    color: var(--text-dark);
}

p, li {
    font-size: 1rem;
    color: var(--text-light);
}

/* ---------- HYPERLINKS ---------- */
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

/* ---------- CONTAINER ---------- */
.container {
    max-width: 1000px;
    margin: auto;
    animation: fadeIn 0.6s ease-out;
}

/* ---------- BUTTONS ---------- */
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

/* ---------- UL / LI Animation ---------- */
ul li {
    margin-bottom: 6px;
    position: relative;
    padding-left: 15px;
    animation: fadeIn 0.8s ease-out;
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
    box-shadow: 0 0 4px rgba(37,99,235,0.5);
}
