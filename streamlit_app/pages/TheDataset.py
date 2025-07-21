import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show():
    st.title("📊 The Dataset: Change.org Petitions")
    
    # Hero section with key stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Petitions", "24,065", help="Original dataset size before cleaning")
    with col2:
        st.metric("Unique Campaigns", "3,081", help="After deduplication and preprocessing")
    with col3:
        st.metric("Success Rate", "23.2%", help="Using our multi-pathway success definition")
    with col4:
        st.metric("Geographic Coverage", "98.2% India", help="Primary limitation for global applicability")
    
    st.markdown("---")
    
    # Dataset Overview Section
    st.header("🎯 Why Change.org?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Change.org is the world's largest online petition platform**, making it an ideal source for studying grassroots campaign messaging effectiveness. Here's why we selected this dataset:
        
        ✅ **Scale & Diversity**: Over 24,000 petitions spanning social, environmental, and political issues  
        ✅ **Rich Success Metrics**: Signature counts, victory status, engagement data, and timing information  
        ✅ **Message Content**: Complete petition text including titles, descriptions, and targeting information  
        ✅ **Platform Relevance**: Directly applicable to MobilizeNow's digital organizing mission  
        ✅ **Measurable Outcomes**: Clear success indicators for developing predictive models  
        """)
        
        st.info("💡 **Platform Impact**: Change.org hosts millions of users globally, providing insights into what makes advocacy messaging effective at scale.")
    
    with col2:
        st.markdown("""
        **📚 Learn More:**
        
        🔗 [Original Dataset (Kaggle)](https://www.kaggle.com/datasets/muhammedabdulazeem/petitions-from-changeorg)
        
        📄 [Detailed EDA & Feature Engineering Report](https://github.com/rmehdi1/CommunityProject_Mobilize/blob/main/docs/EDA_FeatureEngineering.md)
        
        🌐 [About Change.org](https://www.change.org/about)
        
        💼 [Change.org LinkedIn](https://www.linkedin.com/company/change-org/)
        """)
    
    st.markdown("---")
    
    # Dataset Characteristics
    st.header("📋 Dataset Characteristics")
    
    # Create three columns for key dataset info
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📅 Temporal Coverage")
        st.markdown("""
        - **Timespan**: 2010-2021
        - **Peak Activity**: 2020-2021
        - **Campaign Duration**: 1-4 years average
        """)
    
    with col2:
        st.subheader("🌍 Geographic Distribution")
        st.markdown("""
        - **Primary**: India (98.2%)
        - **Secondary**: US, Japan, Canada
        - **Languages**: Predominantly English
        - **Limitation**: Geographic bias
        """)
    
    with col3:
        st.subheader("📊 Data Quality")
        st.markdown("""
        - **Duplicates Removed**: 21,000+
        - **Missing Data**: <10% for key fields
        - **Complete Records**: 3,081 campaigns
        - **Feature Count**: 162 engineered features
        """)
    
    st.markdown("---")
    
    # Key EDA Findings
    st.header("🔍 Key EDA Findings")
    
    # Create expandable sections for different findings
    with st.expander("🎯 Success Patterns", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Multi-Pathway Success Definition:**
            - Official Victory: 3.9% of campaigns
            - High Efficiency: Top 20% daily signature rate (≥2.40 sigs/day)
            - High Scale: Top 20% total signatures (≥930 signatures)
            - **Combined Success Rate: 23.2%**
            """)
        with col2:
            st.markdown("""
            **Success Characteristics:**
            - Successful campaigns average **50.89 signatures/day**
            - **Early momentum critical**: Victory concentrated in first 50 days
            - **Professional content**: 2.03x more HTML formatting
            - **Strategic language**: 2.41x more urgency keywords
            """)
    
    with st.expander("📝 Content & Messaging Insights"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Length Optimization:**
            - Successful titles: 1.19x longer (83 vs 70 characters)
            - Successful descriptions: 1.65x longer (1,511 vs 914 characters)
            - Comprehensive content shows **32.5 percentage point improvement**
            """)
        with col2:
            st.markdown("""
            **Strategic Language Patterns:**
            - **Urgency terms**: "immediate," "crisis," "deadline"
            - **Action words**: "demand," "stop," "implement"
            - **Authority targeting**: Specific officials vs. generic appeals
            - **Clear CTAs**: 2.8 percentage point advantage
            """)
    
    with st.expander("⚡ Engagement Dynamics"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Extreme Engagement Skew:**
            - **Median**: 0.23 signatures/day
            - **95th Percentile**: 37.0 signatures/day
            - **99th Percentile**: 314.3 signatures/day
            - **Skewness**: 18.4 (severe right-skew)
            """)
        with col2:
            st.markdown("""
            **Activity Patterns:**
            - **Daily Activity**: Only 11.7% of campaigns
            - **Weekly Activity**: 28.6% of campaigns
            - **Monthly Activity**: 55.1% of campaigns
            - **Zero-inflation**: High proportion of inactive periods
            """)
    
    with st.expander("⚠️ Limitations & Considerations"):
        st.markdown("""
        **Critical Limitations for MobilizeNow:**
        
        🌏 **Geographic Bias**: 98.2% of campaigns from India - findings may not generalize to North American organizing contexts
        
        📅 **Temporal Bias**: Older campaigns show artificially higher performance due to longer accumulation periods
        
        🏛️ **Platform Dependency**: Victory definitions tied to Change.org's internal processes
        
        📊 **Class Imbalance**: Original 3.9% victory rate required sophisticated success redefinition
        
        **Mitigation Strategies:**
        - Developed platform-agnostic success metrics
        - Created time-normalized performance indicators
        - Multi-pathway success framework for broader applicability
        """)
    
    st.markdown("---")
    
    # Feature Engineering Highlights
    st.header("⚙️ Feature Engineering Highlights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🎯 Performance Metrics")
        st.markdown("""
        - `signatures_per_day`: Time-normalized efficiency
        - `signatures_per_view`: Conversion effectiveness
        - `views_per_signature`: Engagement intensity
        """)
    
    with col2:
        st.subheader("📊 Composite Scores")
        st.markdown("""
        - Professional Sophistication Score
        - Strategic Urgency Score
        - Content Comprehensiveness Score
        - Authority Targeting Score
        """)
    
    with col3:
        st.subheader("🧠 Text Analytics")
        st.markdown("""
        - Sentiment analysis (VADER)
        - Readability metrics (Flesch)
        - Strategic keyword detection
        - HTML formatting analysis
        """)
    
    # Technical Implementation
    with st.expander("🔧 Technical Implementation Details"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Data Processing Pipeline:**
            1. **Deduplication**: Removed 21,000+ duplicate snapshots
            2. **Missing Data**: Strategic imputation and filtering
            3. **Feature Engineering**: 162 → 73 optimized features
            4. **Correlation Analysis**: Removed multicollinear features (r > 0.9)
            """)
        with col2:
            st.markdown("""
            **Quality Assurance:**
            - **Temporal Validation**: Duration calculations with scraping date buffer
            - **Consistency Checks**: Victory date alignment with status
            - **Feature Selection**: VIF analysis and business relevance
            - **Target Definition**: Comprehensive success metric testing
            """)
    
    st.markdown("---")
    
    # Next Steps
    st.header("🚀 Next Steps in Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Upcoming Model Development:**
        - Predictive modeling for campaign success
        - Text analytics for message optimization
        - Feature importance analysis
        - Cross-validation and performance tuning
        """)
    
    with col2:
        st.markdown("""
        **Strategic Applications:**
        - Messaging recommendation engine
        - Campaign optimization toolkit
        - Success probability calculator
        - Platform expansion roadmap
        """)
    
    # Call to action
    st.info("📖 **Want the full technical details?** Check out our [comprehensive EDA report](https://github.com/rmehdi1/CommunityProject_Mobilize/blob/main/docs/EDA_FeatureEngineering.md) for in-depth analysis, methodology, and statistical validation.")
    
    
    st.success("✅ **Dataset Status**: Cleaned, processed, and ready for modeling with 3,081 unique campaigns and 73 engineered features optimized for messaging effectiveness analysis.")

if __name__ == "__main__":
    show()