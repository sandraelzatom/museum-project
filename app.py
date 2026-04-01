import streamlit as st

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Signal & Script Museum", layout="wide")

# 2. SWISS DESIGN STYLE (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #f0f0f0; font-family: 'Helvetica', sans-serif; }
    .hero { 
        background-color: #E63946; /* Swiss Red */
        color: white; 
        padding: 60px; 
        border: 10px solid black;
        text-transform: uppercase;
        font-weight: 900;
        font-size: 80px;
        line-height: 0.8;
        margin-bottom: 40px;
    }
    .artifact-card {
        background-color: white;
        border-left: 20px solid #FFB703; /* Swiss Yellow */
        padding: 30px;
        margin-bottom: 30px;
        border-bottom: 5px solid black;
    }
    .year { font-size: 50px; font-weight: bold; color: black; }
    </style>
    """, unsafe_allow_html=True)

# 3. HERO SECTION
st.markdown('<div class="hero">SIGNAL<br>& SCRIPT</div>', unsafe_allow_html=True)

# 4. THE EXHIBIT CONTENT (The Narrative Flow)
st.write("### A History of Communication / Vol. 01")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        <div class="artifact-card">
            <div class="year">1837</div>
            <h2>THE TELEGRAPH</h2>
            <p>The first time human thought traveled faster than a horse. 
            The world began to shrink as the speed of a message reached the speed of light.</p>
        </div>
        <div class="artifact-card">
            <div class="year">1989</div>
            <h2>THE WORLD WIDE WEB</h2>
            <p>The global nervous system is connected. Information becomes democratic, 
            instant, and accessible to the entire human race at once.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.sidebar.title("Curator's Review")
    st.sidebar.info("**Design Style:** Swiss")
    st.sidebar.warning("**Principle:** Cialdini Authority")
    st.sidebar.success("**Archetype:** The Sage")
    st.sidebar.write("This exhibit transitions from physical signal to digital pulse.")
