import streamlit as st
import pandas as pd

st.set_page_config(page_title="Home - MobilizeNow", page_icon="🏠")

st.title("🏠 MobilizeNow - Petition Success Predictor")
st.markdown("### Messaging Optimization for Community Campaign Success")

# Project Overview
st.markdown("---")
st.header("📋 Project Overview")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    **MobilizeNow** is a data-driven messaging optimization framework designed to improve the success of community-driven campaigns across digital organizing platforms.
    
    Using machine learning analysis of 24,000+ Change.org petitions, we've developed tools to help grassroots organizations craft more effective messaging and optimize their campaign strategies.
    """)

with col2:
    st.info("""
    **🎯 Target Users:**
    - Grassroots organizations
    - Environmental advocates  
    - Housing rights groups
    - Social justice campaigns
    """)

# Key Findings
st.markdown("---")
st.header("🔍 Key Findings")

# Create metrics row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📊 Petitions Analyzed", 
        value="24,000+",
        help="Total petitions from Change.org dataset"
    )

with col2:
    st.metric(
        label="🎯 Model Accuracy", 
        value="70%+",
        help="Success prediction accuracy achieved"
    )

with col3:
    st.metric(
        label="🔤 Features Extracted", 
        value="3+",
        help="Key messaging features identified"
    )

with col4:
    st.metric(
        label="📈 Success Rate", 
        value="~15%",
        help="Average petition success rate in dataset"
    )

# Success Factors
st.markdown("---")
st.header("💡 What Makes Petitions Successful?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **📝 Content Quality:**
    - Clear, specific messaging
    - Optimal description length
    - Compelling call-to-action
    - Local relevance
    """)

with col2:
    st.markdown("""
    **📊 Strategic Factors:**
    - Timing and urgency
    - Geographic targeting  
    - Issue category selection
    - Community engagement
    """)

# How to Use
st.markdown("---")
st.header("🚀 How to Use This Tool")

st.markdown("""
1. **🔮 Test Your Content**: Use our Live Predictor to analyze your petition text and get real-time feedback
2. **📈 Understand the Model**: Explore our model performance and see what features drive success
3. **📚 Access Resources**: Download our comprehensive toolkit and documentation
4. **🎯 Optimize Your Campaign**: Apply insights to improve your messaging strategy
""")

# Call to Action
st.markdown("---")
st.success("👈 **Ready to get started?** Navigate to the Live Predictor in the sidebar to test your petition content!")

# Footer
st.markdown("---")
st.caption("Built for grassroots organizations to amplify their impact through data-driven messaging optimization.")