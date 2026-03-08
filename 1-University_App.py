import streamlit as st

# ---------- CONSTANTS ----------
PAGE_TITLE = "NILESH Interactive"
INSTITUTE_NAME = "NILESH Institute of Technology"
MENU_OPTIONS = ["Home", "About", "Departments", "Academic", "Administration", "Events", "Gallery", "Admissions", "Contact"]

METRICS = {
    "Students": "2500+",
    "Departments": "6",
    "Placements": "90%",
    "Recruiters": "120+"
}

HIGHLIGHTS = [
    {"title": "Modern Campus", "desc": "Smart classrooms & labs"},
    {"title": "Experienced Faculty", "desc": "Highly qualified professors"},
    {"title": "Placements", "desc": "Top companies visit every year"}
]

DEPARTMENTS = {
    "Computer Science": {
        "desc": "Focus areas: AI, Data Science, Web Development",
        "subjects": ["Data Structures", "Machine Learning", "Cloud Computing"]
    },
    "Mechanical": {
        "desc": "Focus areas: Design, Manufacturing",
        "subjects": []
    },
    "Electronics": {
        "desc": "Focus areas: Embedded Systems, Communication",
        "subjects": []
    },
    "Information Technology": {
        "desc": "Focus areas: Networking, Cyber Security",
        "subjects": []
    }
}

EVENTS = [
    ("AI Workshop", "Jan 2026"),
    ("Tech Fest", "Feb 2026"),
    ("IEEE Conference", "March 2026"),
    ("Hackathon", "April 2026")
]

GALLERY_IMAGES = [
    "https://images.unsplash.com/photo-1503676260728-1c00da094a0b",
    "https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d",
    "https://images.unsplash.com/photo-1523050854058-8df90110c9f1"
]

COURSES = ["B.Tech CSE", "Mechanical", "Electronics", "IT"]

CONTACT_INFO = {
    "address": "BSF Academy, Tekanpur, Gwalior",
    "phone": "07524-274319",
    "email": "info@NILESH.ac.in",
    "lat": 26.2,
    "lon": 78.3
}

# Credentials for login (in production, use proper authentication)
CREDENTIALS = {
    "admin": "admin123",
    "student": "student123",
    "faculty": "faculty123"
}

ABOUT_TEXT = """
## About NILESH Institute of Technology

NILESH Institute of Technology (NIT) is a premier engineering college dedicated to providing world-class education
in various engineering disciplines.

### Our Mission
To impart quality education in engineering and develop competent engineers with a strong ethical foundation,
committed to the services of society.

### Our Vision
To become a leading institute of engineering education in India, recognized for research, innovation, and excellence
in technical education.

### Key Highlights
- **Established**: 1999
- **Accreditation**: AICTE Approved
- **Students**: 2500+
- **Faculty**: Highly experienced and qualified
- **Placement Rate**: 90%+
- **Companies**: 120+ recruiters visit annually

### Our Departments
1. Computer Science Engineering
2. Mechanical Engineering
3. Electronics Engineering
4. Information Technology
5. Civil Engineering
6. Electrical Engineering

### Why Choose NILESH?
- Modern campus infrastructure with smart classrooms
- Hands-on practical training and industry internships
- State-of-the-art laboratories
- Expert faculty with industry experience
- Strong alumni network
- Focus on research and innovation
- Holistic development programs
"""

ADMINISTRATION_DATA = {
    "Principal": {
        "name": "Dr. Rajesh Kumar",
        "qualification": "Ph.D. in Computer Science",
        "experience": "25+ years in academics and administration",
        "email": "principal@nilesh.ac.in"
    },
    "Vice-Principal (Academic)": {
        "name": "Prof. Neha Singh",
        "qualification": "M.Tech in Electronics",
        "experience": "18 years in academic development",
        "email": "vp-academic@nilesh.ac.in"
    },
    "Vice-Principal (Administration)": {
        "name": "Prof. Arun Verma",
        "qualification": "MBA in Administration",
        "experience": "20 years in institute management",
        "email": "vp-admin@nilesh.ac.in"
    },
    "Dean (Academic Affairs)": {
        "name": "Dr. Priya Patel",
        "qualification": "Ph.D. in Mechanical Engineering",
        "experience": "15 years in curriculum development",
        "email": "dean-academics@nilesh.ac.in"
    },
    "Dean (Activities)": {
        "name": "Prof. Vikram Sharma",
        "qualification": "M.Tech in IT",
        "experience": "12 years in student activities",
        "email": "dean-activities@nilesh.ac.in"
    }
}

ACADEMIC_DATA = {
    "Academic Calendar": [
        "Semester I: July - November",
        "Semester II: December - April",
        "Summer Break: April - June",
        "Mid-semester exams: October & March",
        "End-semester exams: November & April"
    ],
    "Academic Programs": [
        "B.Tech (4 years) - 6 Engineering Branches",
        "M.Tech (2 years) - Specialized branches",
        "PhD Programs - Research focused",
        "Diploma (3 years) - Technical education"
    ],
    "Academic Policies": [
        "Minimum CGPA for good standing: 6.0",
        "Attendance requirement: 75%",
        "No backlogs allowed for graduation",
        "Grade appeals within 7 days of result declaration",
        "Makeup exams for medical emergencies"
    ],
    "Learning Resources": [
        "Central Library: 50,000+ books",
        "Digital Library: Access to 10+ e-resources",
        "Computer Labs: Equipped with latest software",
        "Internet: High-speed WiFi across campus",
        "Online courses: Partnership with MOOCs"
    ]
}

CSS_STYLE = """
<style>
.main { background-color: #f5f7fa; }
.navbar { background-color: #002147; padding: 10px; border-radius: 5px; }
.navbar h2 { color: white; text-align: center; }
.card { background-color: white; padding: 20px; border-radius: 10px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); transition: 0.3s; }
.card:hover { transform: scale(1.03); }
.hero { background: linear-gradient(90deg,#002147,#0056b3); padding: 40px; 
        border-radius: 10px; color: white; text-align: center; }
.nav-btn-container { display: flex; gap: 8px; margin: 10px 0; }
.nav-btn { flex: 1; padding: 12px; border-radius: 8px; color: white; font-weight: bold; 
           text-align: center; cursor: pointer; border: none; transition: all 0.3s; }
.nav-btn:hover { transform: scale(1.05); }
.btn-home { background-color: #FF6B6B; }
.btn-dept { background-color: #4ECDC4; }
.btn-events { background-color: #45B7D1; }
.btn-gallery { background-color: #FFA07A; }
.btn-admissions { background-color: #98D8C8; }
.btn-contact { background-color: #6C5CE7; }
</style>
"""

# ---------- HELPER FUNCTIONS ----------
def render_card(title: str, content: str):
    """Render a card with title and content"""
    st.markdown(f'<div class="card"><h4>{title}</h4><p>{content}</p></div>', unsafe_allow_html=True)

def render_hero():
    """Render hero section"""
    st.markdown('<div class="hero"><h1>Welcome to NILESH</h1><p>Excellence in Engineering Education</p></div>', unsafe_allow_html=True)

def render_metrics():
    """Render metrics in columns"""
    cols = st.columns(len(METRICS))
    for col, (label, value) in zip(cols, METRICS.items()):
        col.metric(label, value)

def render_highlights():
    """Render highlights cards"""
    st.write("### Highlights")
    cols = st.columns(3)
    for col, highlight in zip(cols, HIGHLIGHTS):
        with col:
            render_card(highlight["title"], highlight["desc"])

def login_page():
    """Display login page"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="hero" style="padding: 60px 40px;"><h2>NILESH Login</h2></div>', unsafe_allow_html=True)
        st.write("")
        
        username = st.text_input("Username", placeholder="Enter username")
        password = st.text_input("Password", type="password", placeholder="Enter password")
        
        col_btn1, col_btn2 = st.columns([1, 1])
        
        with col_btn1:
            if st.button("Login", use_container_width=True):
                if username in CREDENTIALS and CREDENTIALS[username] == password:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid username or password")
        
        with col_btn2:
            st.write("")  # Spacing
        
        st.write("")
        st.info("Demo Credentials:\n- Username: admin, Password: admin123\n- Username: student, Password: student123\n- Username: faculty, Password: faculty123")

def render_navigation():
    """Render navigation buttons with different colors"""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"
    
    # First row of navigation (5 options)
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    
    if col1.button("🏠 Home", use_container_width=True, key="btn_home"):
        st.session_state.current_page = "Home"
        st.rerun()
    
    if col2.button("ℹ️ About", use_container_width=True, key="btn_about"):
        st.session_state.current_page = "About"
        st.rerun()
    
    if col3.button("🏛️ Departments", use_container_width=True, key="btn_depts"):
        st.session_state.current_page = "Departments"
        st.rerun()
    
    if col4.button("📚 Academic", use_container_width=True, key="btn_academic"):
        st.session_state.current_page = "Academic"
        st.rerun()
    
    if col5.button("👥 Administration", use_container_width=True, key="btn_admin"):
        st.session_state.current_page = "Administration"
        st.rerun()
    
    # Second row of navigation (4 options + logout)
    col6, col7, col8, col9, col10 = st.columns(5, gap="small")
    
    if col6.button("📅 Events", use_container_width=True, key="btn_events"):
        st.session_state.current_page = "Events"
        st.rerun()
    
    if col7.button("🎨 Gallery", use_container_width=True, key="btn_gallery"):
        st.session_state.current_page = "Gallery"
        st.rerun()
    
    if col8.button("📝 Admissions", use_container_width=True, key="btn_admit"):
        st.session_state.current_page = "Admissions"
        st.rerun()
    
    if col9.button("☎️ Contact", use_container_width=True, key="btn_contact"):
        st.session_state.current_page = "Contact"
        st.rerun()
    
    if col10.button("🚪 Logout", use_container_width=True, key="btn_logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
    
    # Add CSS to color the buttons
    st.markdown("""
    <style>
    div[data-testid="column"] button {
        font-weight: bold;
        padding: 12px !important;
        font-size: 14px !important;
        height: auto !important;
        border-radius: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.divider()
    return st.session_state.current_page

# Page config
st.set_page_config(page_title=PAGE_TITLE, layout="wide")

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Custom CSS
st.markdown(CSS_STYLE, unsafe_allow_html=True)

# Check if user is logged in
if not st.session_state.logged_in:
    login_page()
else:
    # Navbar
    st.markdown(f'<div class="navbar"><h2>{INSTITUTE_NAME} - Welcome, {st.session_state.username}!</h2></div>', unsafe_allow_html=True)

    menu = render_navigation()

    # ---------- HOME ----------
    if menu == "Home":
        render_hero()
        st.divider()
        render_metrics()
        render_highlights()

    # ---------- ABOUT ----------
    elif menu == "About":
        st.markdown(ABOUT_TEXT)
        
        st.divider()
        st.write("### Contact the Institute")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"📧 Email\n\n{CONTACT_INFO['email']}")
        with col2:
            st.info(f"📞 Phone\n\n{CONTACT_INFO['phone']}")
        with col3:
            st.info(f"📍 Address\n\n{CONTACT_INFO['address']}")

    # ---------- ACADEMIC ----------
    elif menu == "Academic":
        st.title("📚 Academic Information")
        
        tabs = st.tabs(["Academic Calendar", "Programs", "Policies", "Resources"])
        
        with tabs[0]:
            st.subheader("Academic Calendar")
            for item in ACADEMIC_DATA["Academic Calendar"]:
                st.write(f"• {item}")
        
        with tabs[1]:
            st.subheader("Academic Programs")
            for item in ACADEMIC_DATA["Academic Programs"]:
                st.write(f"• {item}")
        
        with tabs[2]:
            st.subheader("Academic Policies")
            for item in ACADEMIC_DATA["Academic Policies"]:
                st.write(f"• {item}")
        
        with tabs[3]:
            st.subheader("Learning Resources")
            for item in ACADEMIC_DATA["Learning Resources"]:
                st.write(f"• {item}")

    # ---------- ADMINISTRATION ----------
    elif menu == "Administration":
        st.title("👥 Administration & Leadership")
        
        st.write("### Institute Leadership Team")
        
        for position, details in ADMINISTRATION_DATA.items():
            with st.expander(f"📌 {position}: {details['name']}", expanded=False):
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.write(f"**Name:** {details['name']}")
                    st.write(f"**Qualification:** {details['qualification']}")
                    st.write(f"**Experience:** {details['experience']}")
                    st.write(f"**Email:** {details['email']}")
                with col2:
                    st.info(f"✉️ Contact\n\n{details['email']}")

    # ---------- DEPARTMENTS ----------
    elif menu == "Departments":
        st.title("Departments")
        tabs = st.tabs(list(DEPARTMENTS.keys()))
        
        for tab, (dept_name, dept_info) in zip(tabs, DEPARTMENTS.items()):
            with tab:
                st.subheader(f"{dept_name} Engineering")
                st.write(dept_info["desc"])
                if dept_info["subjects"]:
                    with st.expander("View Subjects"):
                        for subject in dept_info["subjects"]:
                            st.write(f"- {subject}")

    # ---------- EVENTS ----------
    elif menu == "Events":
        st.title("Latest Events")
        for name, date in EVENTS:
            render_card(name, f"Date: {date}")
            st.divider()

    # ---------- GALLERY ----------
    elif menu == "Gallery":
        st.title("Campus Gallery")
        cols = st.columns(3)
        for idx, img in enumerate(GALLERY_IMAGES):
            cols[idx % 3].image(img, use_column_width=True)

    # ---------- ADMISSIONS ----------
    elif menu == "Admissions":
        st.title("Admission Enquiry")
        with st.form("admission_form"):
            st.text_input("Student Name")
            st.text_input("Email")
            st.selectbox("Select Course", COURSES)
            if st.form_submit_button("Submit"):
                st.success("Application submitted successfully!")

    # ---------- CONTACT ----------
    elif menu == "Contact":
        st.title("Contact Us")
        st.markdown(f"""
        **Address:** {CONTACT_INFO['address']}  
        **Phone:** {CONTACT_INFO['phone']}  
        **Email:** {CONTACT_INFO['email']}
        """)
        st.map({"lat": [CONTACT_INFO['lat']], "lon": [CONTACT_INFO['lon']]})