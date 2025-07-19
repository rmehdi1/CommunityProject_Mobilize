import streamlit as st

st.set_page_config(page_title="Resources - MobilizeNow", page_icon="📚")

st.title("📚 Resources & Downloads")
st.markdown("### Access documentation, toolkits, and project files")

# Downloads Section
st.header("📥 Downloads")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Analysis & Reports")
    
    # Check if files exist and provide download buttons
    try:
        with open("assets/docs/eda_report.pdf", "rb") as file:
            st.download_button(
                label="📈 EDA Report",
                data=file,
                file_name="eda_report.pdf",
                mime="application/pdf",
                help="Comprehensive exploratory data analysis"
            )
    except FileNotFoundError:
        st.button("📈 EDA Report", disabled=True, help="File not available")
    
    try:
        with open("assets/docs/feature_engineering_docs.pdf", "rb") as file:
            st.download_button(
                label="🔧 Feature Engineering Docs",
                data=file,
                file_name="feature_engineering_docs.pdf", 
                mime="application/pdf",
                help="Technical documentation of feature extraction"
            )
    except FileNotFoundError:
        st.button("🔧 Feature Engineering Docs", disabled=True, help="File not available")

with col2:
    st.markdown("### 🛠️ Toolkits & Guides")
    
    st.button(
        "📋 Messaging Toolkit", 
        disabled=True, 
        help="Coming soon - practical guide for campaign messaging"
    )
    
    st.button(
        "🗺️ Platform Roadmap", 
        disabled=True, 
        help="Coming soon - implementation strategy for organizations"
    )

# Data Access
st.markdown("---")
st.header("💾 Data & Code Access")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔗 GitHub Repository")
    st.markdown("""
    Access the complete project codebase:
    - Data preprocessing scripts
    - Model training notebooks  
    - Feature engineering code
    - Streamlit application source
    """)
    
    st.markdown("[🔗 View on GitHub](https://github.com/yourusername/mobilize-now)")

with col2:
    st.markdown("### 📊 Sample Data")
    
    # Provide sample data download
    try:
        with open("data/sample_data.csv", "rb") as file:
            st.download_button(
                label="📊 Sample Dataset",
                data=file,
                file_name="sample_petition_data.csv",
                mime="text/csv",
                help="Sample petition data for testing"
            )
    except FileNotFoundError:
        st.button("📊 Sample Dataset", disabled=True, help="File not available")

# Documentation
st.markdown("---")
st.header("📖 Documentation")

tab1, tab2, tab3 = st.tabs(["🔍 Model Info", "🎯 Usage Guide", "🤝 Contributing"])

with tab1:
    st.markdown("""
    ### Model Details
    
    **Algorithm**: Logistic Regression  
    **Training Data**: 24,000+ Change.org petitions  
    **Features**: 3 key messaging indicators  
    **Accuracy**: 70%+ success prediction  
    
    **Key Features**:
    - Text length analysis
    - Content quality metrics  
    - Engagement indicators
    """)

with tab2:
    st.markdown("""
    ### How to Use the Predictor
    
    1. **Navigate** to the Live Predictor page
    2. **Enter** your petition text in the input box
    3. **Review** the success probability and feature breakdown
    4. **Optimize** your content based on the recommendations
    5. **Test** different versions to improve your score
    
    **Tips for Better Results**:
    - Be specific and clear in your messaging
    - Include compelling calls-to-action
    - Mention local relevance when applicable
    """)

with tab3:
    st.markdown("""
    ### Contributing to the Project
    
    We welcome contributions from the community!
    
    **Ways to Contribute**:
    - 🐛 Report bugs or issues
    - 💡 Suggest new features
    - 📊 Contribute additional data
    - 🔧 Submit code improvements
    - 📝 Improve documentation
    
    **Contact**: [Your contact information]
    """)

# Future Development
st.markdown("---")
st.header("🚀 Future Development")

st.markdown("""
### Planned Features

**🔮 Enhanced Predictions**:
- Multi-language support
- Platform-specific optimization
- Real-time trend analysis

**📊 Advanced Analytics**:
- A/B testing framework
- Geographic success patterns
- Temporal trend analysis

**🛠️ Integration Tools**:
- API for direct platform integration
- Browser extension for real-time feedback
- Mobile app for campaign managers
""")

# Support
st.markdown("---")
st.info("""
### 💬 Need Help?

For questions, support, or collaboration opportunities:
- 📧 Email: [your-email@domain.com]
- 💬 GitHub Issues: [Link to issues page]
- 🐦 Twitter: [@your_handle]
""")