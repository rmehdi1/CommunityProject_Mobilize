import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pickle
import os

def load_data():
    """Load processed data and model artifacts"""
    try:
        # Load processed data
        data_path = os.path.join("streamlit_app", "data", "processed_petition_data.csv")
        df = pd.read_csv(data_path)
        
        # Load model artifacts
        model_path = os.path.join("streamlit_app", "models", "best_model.pkl")
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
            
        features_path = os.path.join("streamlit_app", "models", "model_features.pkl")
        with open(features_path, 'rb') as f:
            feature_names = pickle.load(f)
            
        return df, model, feature_names
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None

def create_success_metrics_viz(df):
    """Create visualization showing success rate improvements"""
    
    # Key metrics from your analysis
    metrics_data = {
        'Metric': ['Content Length', 'Professional Formatting', 'Title Complexity', 'Strategic Language'],
        'Success_Multiplier': [1.65, 2.03, 1.19, 1.18],
        'Improvement_Percentage': [65, 103, 19, 18],
        'Category': ['Content', 'Structure', 'Complexity', 'Language']
    }
    
    metrics_df = pd.DataFrame(metrics_data)
    
    fig = px.bar(
        metrics_df, 
        x='Metric', 
        y='Improvement_Percentage',
        color='Category',
        title="📈 Success Rate Improvements by Strategic Element",
        labels={'Improvement_Percentage': 'Improvement (%)', 'Metric': 'Strategic Element'},
        color_discrete_map={
            'Content': '#1f77b4',
            'Structure': '#ff7f0e', 
            'Complexity': '#2ca02c',
            'Language': '#d62728'
        }
    )
    
    fig.update_layout(
        height=400,
        showlegend=True,
        title_x=0.5,
        title_font_size=16
    )
    
    # Add annotations showing multipliers
    for i, row in metrics_df.iterrows():
        fig.add_annotation(
            x=row['Metric'],
            y=row['Improvement_Percentage'] + 5,
            text=f"{row['Success_Multiplier']}x",
            showarrow=False,
            font=dict(size=12, color="black", family="Arial Black")
        )
    
    return fig

def create_length_analysis_viz(df):
    """Create visualization showing optimal content lengths"""
    
    # Sample data based on your analysis
    length_data = {
        'Content_Type': ['Title', 'Description', 'Letter Body', 'Target Description'],
        'Successful_Median': [83, 1511, 66, 51],
        'Unsuccessful_Median': [70, 914, 48, 35],
        'Optimal_Range': ['80+ chars', '1500+ chars', '60+ chars', '50+ chars']
    }
    
    length_df = pd.DataFrame(length_data)
    
    fig = go.Figure()
    
    # Add bars for successful petitions
    fig.add_trace(go.Bar(
        x=length_df['Content_Type'],
        y=length_df['Successful_Median'],
        name='Successful Petitions',
        marker_color='#2ca02c',
        text=length_df['Optimal_Range'],
        textposition='outside'
    ))
    
    # Add bars for unsuccessful petitions
    fig.add_trace(go.Bar(
        x=length_df['Content_Type'],
        y=length_df['Unsuccessful_Median'],
        name='Unsuccessful Petitions',
        marker_color='#d62728'
    ))
    
    fig.update_layout(
        title="📏 Optimal Content Lengths for Success",
        xaxis_title="Content Type",
        yaxis_title="Character Count",
        barmode='group',
        height=400,
        title_x=0.5,
        title_font_size=16
    )
    
    return fig

def create_feature_importance_viz(model, feature_names):
    """Create feature importance visualization"""
    try:
        if hasattr(model, 'feature_importances_'):
            importance_df = pd.DataFrame({
                'Feature': feature_names,
                'Importance': model.feature_importances_
            }).sort_values('Importance', ascending=False).head(15)
            
            # Categorize features
            def categorize_feature(feature):
                if any(x in feature.lower() for x in ['length', 'word_count', 'comprehensiveness']):
                    return 'Content Length'
                elif any(x in feature.lower() for x in ['html', 'formatting', 'professional']):
                    return 'Formatting'
                elif any(x in feature.lower() for x in ['sentiment', 'urgency', 'action']):
                    return 'Strategic Language'
                elif any(x in feature.lower() for x in ['complexity', 'readability', 'flesch']):
                    return 'Complexity'
                else:
                    return 'Other'
            
            importance_df['Category'] = importance_df['Feature'].apply(categorize_feature)
            
            fig = px.bar(
                importance_df,
                x='Importance',
                y='Feature',
                color='Category',
                orientation='h',
                title=" Top 15 Most Important Features for Petition Success",
                labels={'Importance': 'Feature Importance', 'Feature': 'Feature Name'}
            )
            
            fig.update_layout(
                height=600,
                title_x=0.5,
                title_font_size=16,
                yaxis={'categoryorder': 'total ascending'}
            )
            
            return fig
        else:
            return None
    except Exception as e:
        st.error(f"Error creating feature importance viz: {e}")
        return None

def show_messaging_insights():
    """Main function to display messaging insights"""
    
    st.title("🎯 Messaging Insights & Best Practices")
    st.markdown("*Evidence-based recommendations from analysis of 3,081 Change.org petitions*")
    
    # Load data
    df, model, feature_names = load_data()
    
    if df is None:
        st.error("Unable to load data. Please check your data files.")
        return
    
    # Key Findings Summary
    st.header(" Key Findings")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Overall Success Boost", 
            "352%", 
            "vs simplified messaging"
        )
    
    with col2:
        st.metric(
            "Content Length Advantage", 
            "1.65x", 
            "longer descriptions"
        )
    
    with col3:
        st.metric(
            "Formatting Advantage", 
            "2.03x", 
            "more HTML tags"
        )
    
    with col4:
        st.metric(
            "Model Accuracy", 
            "77%", 
            "prediction success"
        )
    
    # Success Rate Improvements
    st.header(" Success Rate Improvements")
    st.markdown("**Professional sophistication outperforms simplified messaging across all categories:**")
    
    fig1 = create_success_metrics_viz(df)
    st.plotly_chart(fig1, use_container_width=True)
    
    # Content Length Analysis
    st.header("📏 Optimal Content Lengths")
    st.markdown("**Successful petitions consistently use longer, more detailed content:**")
    
    fig2 = create_length_analysis_viz(df)
    st.plotly_chart(fig2, use_container_width=True)
    
    # Feature Importance
    if model and feature_names:
        st.header(" Most Important Success Factors")
        st.markdown("**Top features that predict petition success:**")
        
        fig3 = create_feature_importance_viz(model, feature_names)
        if fig3:
            st.plotly_chart(fig3, use_container_width=True)

                        # 🔍 Add brief footnotes for key features
            with st.expander("🧾 What do these features mean?"):
                st.markdown("""
                - **flesch_ease**: A readability score (higher = easier to read).
                - **html_tags**: Count of HTML tags used for formatting (like `<h3>`, `<ul>`).
                - **sentiment_positive**: Measures how positively the text is written.
                - **action_count**: Number of action-oriented words (e.g. "demand", "implement").
                - **caps_ratio**: Ratio of capitalized words (overuse can hurt credibility).
                - **comprehensiveness_score**: Overall depth of explanation across sections.
                - **readability**: How easy the text is to read (influenced by sentence complexity and vocabulary).
                """)
    
    # Strategic Framework
    st.header(" The Four Pillars of Campaign Success")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1.  Content Comprehensiveness")
        st.markdown("""
        **Impact:** +32.5 percentage points
        - Target 2,000+ total characters
        - Include background, problem, solution
        - Provide detailed implementation timeline
        - Use evidence and specific examples
        """)
        
        st.subheader("2.  Professional Formatting")
        st.markdown("""
        **Impact:** +28.7 percentage points
        - Use 25+ HTML tags for structure
        - Include headers: <h3>, <strong>
        - Create lists: <ul>, <li>
        - Format like a policy brief
        """)
    
    with col2:
        st.subheader("3.  Professional Sophistication")
        st.markdown("""
        **Impact:** +25.3 percentage points
        - Target college-level readability (Grade 10.7+)
        - Use technical terminology
        - Complex sentence structures
        - Professional tone throughout
        """)
        
        st.subheader("4.  Strategic Language")
        st.markdown("""
        **Impact:** Varied by category
        - **Urgency:** "immediate", "crisis", "deadline"
        - **Action:** "demand", "stop", "implement"
        - **Authority:** Specific officials/departments
        """)
    
    # Practical Recommendations
    st.header("💡 Practical Recommendations")
    
    tab1, tab2, tab3 = st.tabs(["✅ Do This", "❌ Avoid This", "🎯 Optimization Checklist"])
    
    with tab1:
        st.markdown("""
        ### ✅ Best Practices for High Success
        
        **Content Strategy:**
        - Write descriptions 1,500+ characters with comprehensive explanations
        - Include detailed background context and proposed solutions
        - Use specific statistics and evidence when available
        - Target specific decision-makers by name and title
        
        **Language Strategy:**
        - Use sophisticated vocabulary and technical terms
        - Include urgency keywords: "immediate", "urgent", "critical"
        - Add action words: "demand", "implement", "enforce"
        - Reference authority figures and institutions
        
        **Formatting Strategy:**
        - Use HTML formatting: <strong>bold</strong>, <h3>headers</h3>
        - Create structured lists and bullet points
        - Include emphasis and visual hierarchy
        - Present content like a professional document
        """)
    
    with tab2:
        st.markdown("""
        ### ❌ Common Mistakes to Avoid
        
        **Content Anti-Patterns:**
        - Descriptions under 500 characters
        - Generic, vague language
        - No specific targets or timeline
        - Missing background context
        
        **Language Anti-Patterns:**
        - Overly casual or informal tone
        - All caps or excessive emotion
        - No urgency or call-to-action
        - Vague, non-specific demands
        
        **Formatting Anti-Patterns:**
        - Plain text with no structure
        - Wall-of-text paragraphs
        - No visual hierarchy or emphasis
        - Missing headers or organization
        """)
    
    with tab3:
        st.markdown("""
        ### 🎯 Pre-Launch Optimization Checklist
        
        **Content Quality (Target: 70%+ success probability):**
        - [ ] 2,000+ total characters across all fields
        - [ ] College-level readability (Grade 10+)
        - [ ] 25+ HTML formatting tags
        - [ ] 5+ urgency/action keywords
        - [ ] 3+ specific officials targeted
        
        **Structure Requirements:**
        - [ ] Clear problem statement
        - [ ] Specific, actionable solution
        - [ ] Implementation timeline
        - [ ] Expected impact/outcomes
        - [ ] Strong call-to-action
        
        **Strategic Language:**
        - [ ] Authority-targeting language
        - [ ] Urgency and time-pressure words
        - [ ] Specific action demands
        - [ ] Professional tone throughout
        - [ ] Evidence-based arguments
        """)
    
    # Success Benchmarks
    st.header("🎯 Success Benchmarks")
    
    benchmark_data = {
        'Element': ['Title Length', 'Description Length', 'HTML Tags', 'Readability Level', 'Urgency Keywords'],
        'Successful Benchmark': ['83+ characters', '1,511+ characters', '25+ tags', 'Grade 10.7+', '2+ keywords'],
        'Impact': ['1.19x advantage', '1.65x advantage', '2.03x advantage', 'Higher credibility', 'Higher engagement']
    }
    
    benchmark_df = pd.DataFrame(benchmark_data)
    st.table(benchmark_df)
    
    # Call to Action
    st.header("🚀 Ready to Optimize Your Campaign?")
    st.markdown("""
    **Use these insights to transform your petition strategy:**
    
    1. **Audit your current petition** against these benchmarks
    2. **Implement the four pillars** systematically
    3. **Test and iterate** based on performance
    4. **Scale successful patterns** across your campaigns
    
    Remember: **Professional sophistication beats simplification** in grassroots organizing!
    """)

    # 📘 Add Messaging Framework View
    with st.expander("📘 View Full Messaging Framework"):
        st.markdown("""
<div style="background: #f0f8ff; padding: 20px; border-radius: 10px;">
    <p style="font-size: 1.1em;">The complete strategic messaging framework is available on GitHub:</p>
    <a href="https://github.com/rmehdi1/CommunityProject_Mobilize/blob/main/docs/MessagingFramework.md" target="_blank" style="font-weight: bold; font-size: 1.05em; color: #1a73e8;">
        🔗 Open MessagingFramework.md on GitHub
    </a>
</div>
""", unsafe_allow_html=True)


    # Footer
    st.markdown("---")
    st.caption("📊 Analysis based on 3,081 Change.org petitions | 🎯 77% prediction accuracy | 📈 Up to 352% success improvement")




if __name__ == "__main__":
    show_messaging_insights()
