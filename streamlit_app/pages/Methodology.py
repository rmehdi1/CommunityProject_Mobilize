import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show_methodology():
    """
    Display the comprehensive methodology for the Petition Success Optimization Framework
    """
    
    st.title("🔬 Methodology")
    st.markdown("### Messaging Optimization for Community Campaign Success")
    
    # Project Overview
    with st.expander("📋 Project Overview", expanded=True):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Client:** MobilizeNow (Pseudo-Client)
            
            **Primary Objective:** Develop a data-driven messaging optimization framework 
            to improve the success of community-driven campaigns across digital organizing platforms.
            
            **Dataset:** 24,000+ Change.org petitions analyzed for messaging effectiveness patterns
            """)
        
        with col2:
            # Success metrics visualization
            metrics_data = {
                'Metric': ['Model Accuracy Target', 'Records Analyzed', 'Features Extracted', 'Success Rate'],
                'Target': ['≥70%', '≥20,000', '≥3', '23.2%'],
                'Status': ['✅ Achieved 77%', '✅ 24,000+', '✅ 93 features', '✅ Optimal balance']
            }
            st.dataframe(metrics_data, hide_index=True)
    
    # Methodology Phases
    st.markdown("## 📊 Four-Phase Methodology")
    
    # Phase tabs
    phase1, phase2, phase3, phase4 = st.tabs([
        "Phase 1: Data Analysis", 
        "Phase 2: Feature Engineering", 
        "Phase 3: Target Definition", 
        "Phase 4: Predictive Modeling"
    ])
    
    with phase1:
        st.markdown("### 🔍 Phase 1: Data Analysis & Pattern Discovery")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Data Sources:**
            - 24,000+ Change.org petitions
            - 40+ original data columns
            - Geographic, temporal, and engagement metrics
            
            **Data Quality Process:**
            1. **Duplicate Resolution:** 20,000+ duplicates identified
            2. **Missing Value Strategy:** >95% missing fields removed
            3. **Validation:** Cross-reference with platform metrics
            """)
            
        with col2:
            # Sample data quality metrics
            quality_metrics = {
                'Data Quality Check': ['Original Records', 'After Deduplication', 'Clean Records', 'Missing Data Handled'],
                'Count': [44000, 24000, 3081, '100%'],
                'Status': ['Raw', 'Processed', 'Final', 'Complete']
            }
            st.dataframe(quality_metrics, hide_index=True)
        
        st.markdown("**Key Findings from EDA:**")
        st.info("""
        - Severe class imbalance: Only 3.9% declared victories
        - Strong temporal patterns in campaign momentum  
        - Geographic targeting correlates with success
        - Text length and formatting significantly impact outcomes
        """)
    
    with phase2:
        st.markdown("### ⚙️ Phase 2: Feature Engineering & Text Analytics")
        
        # Feature categories
        feature_categories = {
            'Text Length Features': [
                'title_length', 'description_length', 'letter_body_length',
                'title_word_count', 'description_word_count'
            ],
            'Text Complexity Features': [
                'flesch_reading_ease', 'flesch_kincaid_grade', 'gunning_fog',
                'vocab_diversity', 'avg_sentence_length'
            ],
            'Sentiment Features': [
                'sentiment_compound', 'sentiment_positive', 'sentiment_negative',
                'emotional_intensity'
            ],
            'Strategic Language Features': [
                'urgency_count', 'action_count', 'power_count', 'authority_count',
                'weighted_keyword_score'
            ],
            'Professional Features': [
                'professional_sophistication_score', 'html_formatting_count',
                'strategic_urgency_score'
            ]
        }
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Feature Engineering Pipeline:**")
            for category, features in list(feature_categories.items())[:3]:
                with st.expander(f"{category} ({len(features)} features)"):
                    for feature in features:
                        st.write(f"• {feature}")
        
        with col2:
            st.markdown("**Advanced Features:**")
            for category, features in list(feature_categories.items())[3:]:
                with st.expander(f"{category} ({len(features)} features)"):
                    for feature in features:
                        st.write(f"• {feature}")
        
        st.markdown("**Strategic Composite Features:**")
        composite_features = {
            'Professional Sophistication': 'Language complexity + formatting + credibility markers',
            'Strategic Urgency': 'Time pressure + action language + sentiment alignment',
            'Content Comprehensiveness': 'Total content depth across all petition components',
            'Authority Targeting': 'Specificity of decision-maker targeting',
            'Message Coherence': 'Consistency across title, description, and letter',
            'Emotional Resonance': 'Emotional appeal intensity and distribution'
        }
        
        for feature, description in composite_features.items():
            st.write(f"**{feature}:** {description}")
    
    with phase3:
        st.markdown("### 🎯 Phase 3: Target Definition & Success Metrics")
        
        st.markdown("#### Problem: Severe Class Imbalance")
        
        # Visualization of class imbalance problem
        col1, col2 = st.columns(2)
        
        with col1:
            # Original victory distribution
            victory_data = {'Category': ['Unsuccessful', 'Victory'], 'Count': [96.1, 3.9]}
            fig_original = px.pie(
                values=victory_data['Count'], 
                names=victory_data['Category'],
                title="Original Victory Classification",
                color_discrete_map={'Unsuccessful': '#ff6b6b', 'Victory': '#4ecdc4'}
            )
            st.plotly_chart(fig_original, use_container_width=True)
            
        with col2:
            # Final multi-pathway success
            success_data = {'Category': ['Unsuccessful', 'Successful'], 'Count': [76.8, 23.2]}
            fig_final = px.pie(
                values=success_data['Count'], 
                names=success_data['Category'],
                title="Multi-Pathway Success Definition",
                color_discrete_map={'Unsuccessful': '#ff6b6b', 'Successful': '#4ecdc4'}
            )
            st.plotly_chart(fig_final, use_container_width=True)
        
        st.markdown("#### Solution: Multi-Pathway Success Framework")
        
        st.latex(r'''
        \text{Success} = \text{Official Victory} \lor \text{High Efficiency} \lor \text{High Scale}
        ''')
        
        success_components = {
            'Component': ['Official Victory', 'High Efficiency', 'High Scale'],
            'Definition': [
                'Change.org platform recognition',
                'Top 20% daily signature rate (≥2.40 sigs/day)',
                'Top 20% total signatures (≥930 signatures)'
            ],
            'Count': ['119 petitions (3.9%)', '615 petitions (20%)', '615 petitions (20%)'],
            'Rationale': [
                'Platform validation',
                'Sustained daily engagement',
                'Broad community reach'
            ]
        }
        
        df_success = pd.DataFrame(success_components)
        st.dataframe(df_success, hide_index=True)
        
        st.success("""
        **Result:** 23.2% success rate with 0.365 correlation to original victories
        - Eliminates severe class imbalance
        - Maintains strong predictive signal
        - Provides multiple pathways to success
        """)
        
        st.markdown("#### Validation Results")
        validation_metrics = {
            'Metric': ['Victory Correlation', 'Training Sample Size', 'Average Daily Signatures (Successful)', 'Average Total Signatures (Successful)'],
            'Value': ['0.365', '715 petitions', '50.89 sigs/day', '26,524 signatures'],
            'Interpretation': ['Sufficient ML signal', 'Adequate positive examples', 'High engagement', 'Broad community reach']
        }
        st.dataframe(validation_metrics, hide_index=True)
    
    with phase4:
        st.markdown("### 🤖 Phase 4: Predictive Modeling & Evaluation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Model Architecture:**")
            st.code("""
            Random Forest Classifier
            ├── 100 estimators
            ├── Max depth: 10
            ├── Min samples split: 5
            ├── Class weight: balanced
            └── 73 engineered features
            """)
            
            st.markdown("**Feature Selection Process:**")
            st.write("1. **Correlation Analysis:** Removed 20 highly correlated features (>0.9)")
            st.write("2. **Variance Filter:** Eliminated low-variance features")
            st.write("3. **Domain Knowledge:** Retained interpretable business features")
            st.write("4. **SHAP Analysis:** Validated feature importance alignment")
        
        with col2:
            # Model performance visualization
            model_performance = {
                'Model': ['Random Forest', 'Logistic Regression', 'Gradient Boosting'],
                'Accuracy': [0.770, 0.669, 0.789],
                'AUC-ROC': [0.684, 0.707, 0.690],
                'Status': ['✅ Deployed', 'Baseline', 'Alternative']
            }
            
            fig_performance = px.bar(
                model_performance, 
                x='Model', 
                y='Accuracy',
                title='Model Performance Comparison',
                color='Status',
                color_discrete_map={'✅ Deployed': '#4ecdc4', 'Baseline': '#ffa726', 'Alternative': '#42a5f5'}
            )
            fig_performance.add_hline(y=0.7, line_dash="dash", line_color="red", 
                                    annotation_text="SOW Target (70%)")
            st.plotly_chart(fig_performance, use_container_width=True)
    
    # Technical Implementation
    st.markdown("## 🔧 Technical Implementation")
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        st.markdown("**Data Processing**")
        st.code("""
        • pandas, numpy
        • NLTK sentiment analysis
        • textstat readability
        • HTML tag processing
        • Regex pattern matching
        """)
    
    with tech_col2:
        st.markdown("**Machine Learning**")
        st.code("""
        • scikit-learn models
        • SHAP interpretability
        • Cross-validation
        • Feature importance
        • Bootstrap confidence
        """)
    
    with tech_col3:
        st.markdown("**Visualization**")
        st.code("""
        • Streamlit interface
        • Plotly interactive charts
        • Model explainability
        • Business dashboards
        • Export capabilities
        """)
    
    # Feature Importance Analysis
    st.markdown("## 📈 Key Findings & Feature Importance")
    
    # Mock feature importance data based on your results
    top_features = {
        'Feature': [
            'content_comprehensiveness_score',
            'description_html_tags',
            'professional_sophistication_score',
            'description_vocab_diversity',
            'letter_body_length',
            'description_action_count',
            'authority_targeting_score',
            'title_automated_readability'
        ],
        'Importance': [0.0594, 0.0490, 0.0374, 0.0369, 0.0348, 0.0339, 0.0261, 0.0258],
        'Category': [
            'Content', 'Structure', 'Professional', 'Complexity', 
            'Structure', 'Language', 'Language', 'Complexity'
        ]
    }
    
    fig_importance = px.bar(
        top_features, 
        x='Importance', 
        y='Feature',
        color='Category',
        orientation='h',
        title='Top 8 Feature Importance Rankings'
    )
    fig_importance.update_layout(height=500)
    st.plotly_chart(fig_importance, use_container_width=True)
    
    # Business Impact
    st.markdown("## 💼 Business Impact & Recommendations")
    
    impact_col1, impact_col2 = st.columns(2)
    
    with impact_col1:
        st.markdown("**Strategic Priorities:**")
        priorities = [
            "**Content Comprehensiveness** - 32.5% improvement potential",
            "**Professional Formatting** - 28.7% improvement with HTML tags", 
            "**Sophisticated Language** - 13.8% improvement with complexity",
            "**Strategic Targeting** - Authority-specific messaging"
        ]
        for priority in priorities:
            st.write(f"• {priority}")
    
    with impact_col2:
        st.markdown("**Implementation Roadmap:**")
        roadmap = [
            "**Phase 1 (0-30 days):** Deploy 77% accurate prediction model",
            "**Phase 2 (30-90 days):** Integrate into petition creation workflow",
            "**Phase 3 (90+ days):** Scale across MobilizeNow platforms"
        ]
        for phase in roadmap:
            st.write(f"• {phase}")
    
    # Methodology Validation
    st.markdown("## ✅ Methodology Validation")
    
    validation_col1, validation_col2 = st.columns(2)
    
    with validation_col1:
        st.markdown("**Technical Validation:**")
        st.success("✅ 77% accuracy (exceeds 70% SOW target)")
        st.success("✅ 93 pre-launch features engineered")
        st.success("✅ 0.365 correlation with platform victories")
        st.success("✅ Balanced 23.2% success rate")
    
    with validation_col2:
        st.markdown("**Business Validation:**")
        st.success("✅ 100% pre-launch optimization capability")
        st.success("✅ Interpretable strategic recommendations")
        st.success("✅ Transferable across organizing platforms")
        st.success("✅ Evidence-based messaging guidelines")
    
    # Configuration Framework
    st.markdown("## ⚙️ User Configuration Framework")
    
    with st.expander("Advanced: Keyword Weighting System"):
        st.markdown("""
        The system allows domain experts to customize keyword importance based on campaign context:
        
        **Default Configuration (Equal Weighting):**
        - Urgency: 1.0 (time pressure language)
        - Emotional: 1.0 (emotional appeals)
        - Social Proof: 1.0 (community momentum)
        - Power: 1.0 (justice/rights language)
        - Action: 1.0 (calls to action)
        - Authority: 1.0 (institutional targeting)
        - Specificity: 1.0 (data/evidence language)
        
        **Customization Examples:**
        - Environmental campaigns: Increase urgency weighting
        - Policy petitions: Emphasize authority and specificity
        - Social justice: Boost power and emotional language
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("**Methodology developed for MobilizeNow's Messaging Optimization Framework**")
    st.caption("Based on analysis of 24,000+ Change.org petitions with 77% prediction accuracy")

# Example usage in your main Streamlit app:
if __name__ == "__main__":
    show_methodology()