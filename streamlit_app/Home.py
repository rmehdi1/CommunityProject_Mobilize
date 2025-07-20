import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="MobilizeNow - Petition Success Framework",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"  # Changed to expanded to make sidebar more visible
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .key-metrics {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    
    .deliverable-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #4ecdc4;
    }
    
    .insight-box {
        background: #e8f5e8;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #4caf50;
    }
    
    .prediction-button {
        background: linear-gradient(45deg, #ff6b6b, #ffa726);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 2rem 0;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
        transition: transform 0.3s ease;
    }
    
    .prediction-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
    }
    
    .tab-content {
        padding: 1rem 0;
    }
    
    .highlight-stat {
        background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem;
    }
    
    /* Enhanced tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        padding: 0px 24px;
        background-color: white;
        border-radius: 8px;
        color: #1f2937;
        font-weight: 600;
        font-size: 16px;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #667eea !important;
        color: white !important;
        border: 2px solid #4f46e5;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    

    
    .navigation-helper {
    background: linear-gradient(135deg, #f0f0f0 0%, #e0e0e0 100%);
    padding: 0.8rem 1.2rem;
    border-radius: 10px;
    margin: 1rem 0;
    color: #102a13;
    border-left: 4px solid #2e7d32;
    text-align: center;
    font-size: 1rem;
    }
    
    .sidebar-reminder {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation reminder


# Main header
st.markdown("""
<div class="main-header">
    <h1> MobilizeNow Petition Success Framework</h1>
    <h3>Data-Driven Messaging Optimization for Community Campaigns</h3>
    <p><strong>Delivered by:</strong> Rajiha Mehdi |  Summer, 2025</p>
</div>
""", unsafe_allow_html=True)





# Key metrics row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="highlight-stat">
        <h2>77%</h2>
        <p>Model Accuracy<br><small>Exceeds 70% SOW Target</small></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-stat">
        <h2>24,000+</h2>
        <p>Petitions Analyzed<br><small>Change.org Dataset</small></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="highlight-stat">
        <h2>93</h2>
        <p>Predictive Features<br><small>Pre-launch Optimization</small></p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="highlight-stat">
        <h2>32%</h2>
        <p>Success Improvement<br><small>Top vs Bottom Quartile</small></p>
    </div>
    """, unsafe_allow_html=True)

# Mini navigation helper (moved below metrics)
st.markdown("""
<div class="navigation-helper" style="padding: 0.5rem 1rem; font-size: 0.95rem;">
    👇 Click a tab to explore: <strong>Project Objective → Key Steps → Key Insights → Deliverables</strong>
</div>
""", unsafe_allow_html=True)

# Main content tabs with enhanced visibility
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Project Objective", 
    "🔬 Key Steps", 
    "💡 Key Insights", 
    "📋 Deliverables"
])

with tab1:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    
    st.header("Project Objective")
    
    st.markdown("""
    <div class="key-metrics">
    <h4>Primary Goal</h4>
    <p>Develop a data-driven messaging optimization framework for MobilizeNow to <strong>increase success rates of community-driven campaigns</strong> across digital organizing platforms.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Strategic Focus")
        st.markdown("""
        - **Grassroots Empowerment**: Provide evidence-based messaging guidelines
        - **Predictive Analytics**: Enable pre-launch campaign optimization  
        - **Platform Scalability**: Framework transferable across fundraising and advocacy
        - **Data-Driven Insights**: Challenge conventional wisdom with statistical evidence
        """)
        
    with col2:
        st.subheader("📊 Proof of Concept")
        st.markdown("""
        - **Dataset**: 24,065 Change.org petitions with 41 features
        - **Success Metrics**: Victory status, signature counts, engagement data
        - **Methodology**: Machine learning with statistical validation
        - **Transferability**: Principles applicable to MobilizeNow's platform ecosystem
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    
    st.header("Key Steps & Methodology")
    
    # Process flow
    steps = [
        ("Phase 1: Data Analysis & Pattern Discovery", "Comprehensive Change.org dataset analysis with 24,000+ petitions", "🔍"),
        ("Phase 2: Feature Engineering & Text Analytics", "Advanced NLP techniques and strategic messaging features", "⚙️"),
        ("Phase 3: Predictive Modeling & Success Analysis", "Machine learning models with 77% accuracy achievement", "🤖"),
        ("Phase 4: Strategic Framework Development", "Actionable guidelines and implementation roadmap", "🎯")
    ]
    
    for i, (title, description, icon) in enumerate(steps, 1):
        st.markdown(f"""
        <div class="deliverable-card">
            <h4>{icon} {title}</h4>
            <p><strong>Deliverable:</strong> {description}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("🛠️ Technical Implementation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Data Processing:**
        - Text cleaning and HTML parsing
        - Sentiment analysis with VADER
        - Readability scoring (Flesch-Kincaid, Gunning Fog)
        - Strategic keyword extraction
        """)
        
    with col2:
        st.markdown("""
        **Machine Learning:**
        - Random Forest (77% accuracy)
        - Feature importance analysis
        - SHAP interpretability
        - Cross-validation with 95% confidence intervals
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    
    st.header("Key Insights & Findings")
    
    st.subheader("🏆 Top Success Factors")
    
    insights = [
        ("Content Comprehensiveness", "32.5% improvement potential", "Longer, detailed descriptions with comprehensive explanations drive 2.5x higher success rates"),
        ("Professional Sophistication", "25.3% improvement potential", "Sophisticated language and technical terminology build credibility and trust"),
        ("HTML Formatting", "28.7% improvement potential", "Professional formatting with 25+ HTML tags signals legitimacy"),
        ("Strategic Language", "59% advantage", "Urgency and action keywords create measurable psychological impact")
    ]
    
    for factor, improvement, detail in insights:
        st.markdown(f"""
        <div class="insight-box">
            <h5>✅ {factor}</h5>
            <p><strong>{improvement}</strong> - {detail}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("📈 Evidence-Based Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Surprising Discoveries:**
        - Complex language outperforms simple messaging
        - Longer titles (83+ characters) have 19% higher success
        - HTML formatting provides 2x advantage  
        - Negative emotional framing more effective than positive
        """)
        
    with col2:
        st.markdown("""
        **Optimal Benchmarks:**
        - Description: 1,500+ characters
        - Title: 83+ characters with urgency language
        - HTML Tags: 25+ for professional presentation
        - Strategic Keywords: 8+ action words per description
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    
    st.header("Key Deliverables & Resources")
    
    # Main deliverables
    st.subheader("🎯 Primary Deliverables")
    
    main_deliverables = [
        ("Messaging Best Practices Toolkit", "messaging_insights", "Evidence-based guidelines for effective petition messaging", "📝"),
        ("Petition Success Predictor", "petition_analyzer", "Interactive tool for real-time petition optimization", "🔮")
    ]
    
    for title, page_name, description, icon in main_deliverables:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
            <div class="deliverable-card">
                <h4>{icon} {title}</h4>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(f"Access {title.split()[0]}", key=f"btn_{page_name}"):
                st.switch_page(f"pages/{page_name}.py")
    
    st.subheader("📚 Supporting Documentation")
    
    # Updated sub_deliverables with proper linking
    sub_deliverables = [
        ("EDA & Feature Engineering Report", "TheDataset", "Comprehensive analysis of petition patterns and text features", "📊"),
        ("Model Performance & Interpretation Guide", "Model Guide", "Detailed model validation and business interpretation", "🤖"), 
        ("Platform Expansion Roadmap", "Roadmap", "Strategic plan for scaling across MobilizeNow platforms", "🗺️")
    ]
    
    for title, page_name, description, icon in sub_deliverables:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
            <div class="deliverable-card">
                <h5>{icon} {title}</h5>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(f"View {icon}", key=f"btn_{page_name.lower().replace(' ', '_')}"):
                st.switch_page(f"pages/{page_name}.py")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Large prediction tool button
st.markdown("<br><br>", unsafe_allow_html=True)

# Create a prominent call-to-action
st.markdown("""
<div style="text-align: center; margin: 3rem 0;">
    <h2>🚀 Ready to Optimize Your Petition?</h2>
    <p style="font-size: 1.1rem; color: #666;">Use our AI-powered prediction tool to analyze and improve your campaign messaging</p>
</div>
""", unsafe_allow_html=True)

# Large button with columns for centering
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🔮 **LAUNCH PETITION ANALYZER**", type="primary", use_container_width=True):
        st.switch_page("pages/petition_analyzer.py")
    
    st.markdown("""
    <div style="text-align: center; margin-top: 1rem; color: #666;">
        <p><strong>77% Accuracy</strong> • <strong>Pre-launch Optimization</strong> • <strong>Instant Results</strong></p>
    </div>
    """, unsafe_allow_html=True)

# Reminder about sidebar navigation
st.markdown("""
<div class="navigation-helper">
    <h4>🧭 Don't forget to check the sidebar for more sections!</h4>
    <p><strong>Available sections:</strong> Dataset Analysis • Model Guide • Messaging Insights • Petition Analyzer • Roadmap</p>
</div>
""", unsafe_allow_html=True)

# Footer with project summary
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **🎯 Project Impact**
    - Enables predictable petition optimization
    - Provides evidence-based strategic guidance
    - Challenges conventional messaging wisdom
    """)

with col2:
    st.markdown("""
    **📊 Technical Achievement**
    - 77% prediction accuracy (exceeds SOW target)
    - 93 pre-launch optimization features
    - Comprehensive statistical validation
    """)

with col3:
    st.markdown("""
    **🚀 Implementation Ready**
    - Complete framework for deployment
    - Transferable given reusable pipeline
    """)

# Contact/Credits
st.markdown("""
---
<div style="text-align: center; color: #666; padding: 1rem;">
    <p><strong>MobilizeNow Petition Success Framework</strong><br>
    Delivered by Rajiha Mehdi | Project Duration: June 13 - July 20, 2025<br>
    <em>Empowering grassroots organizations with data-driven messaging strategies</em></p>
</div>
""", unsafe_allow_html=True)