import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple

def create_messaging_insights_app():
    """
    Main function to create the messaging insights framework
    """
    st.title("🎯 Messaging Optimization Framework")
    st.markdown("### *Data-Driven Insights for Campaign Success*")
    
    # Create tabs for different aspects of messaging insights
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Key Insights Overview", 
        "📝 Content Strategy Framework", 
        "💬 Language Patterns & Psychology", 
        "📈 Performance Benchmarks", 
        "🛠️ Implementation Toolkit"
    ])
    
    with tab1:
        create_key_insights_overview()
    
    with tab2:
        create_content_strategy_framework()
    
    with tab3:
        create_language_patterns_psychology()
    
    with tab4:
        create_performance_benchmarks()
    
    with tab5:
        create_implementation_toolkit()

def create_key_insights_overview():
    """Tab 1: Key Insights Overview"""
    st.header("🔍 Key Messaging Insights")
    
    # Executive Summary
    st.subheader("Executive Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Model Accuracy Achieved",
            value="79.1%",
            delta="Exceeds 70% target",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            label="Success Rate Improvement",
            value="393%",
            delta="Top vs Bottom Quartile",
            delta_color="normal"
        )
    
    with col3:
        st.metric(
            label="Key Features Identified",
            value="73",
            delta="Actionable insights",
            delta_color="normal"
        )
    
    st.markdown("---")
    
    # Critical Success Factors
    st.subheader("🎯 Critical Success Factors")
    
    success_factors = {
        "Content Comprehensiveness": {
            "impact": "393% improvement",
            "description": "Detailed, thorough petition content significantly increases success probability",
            "key_metric": "1,500+ character descriptions"
        },
        "Professional Sophistication": {
            "impact": "High correlation",
            "description": "Complex, technical language builds credibility and authority",
            "key_metric": "Graduate-level readability"
        },
        "Strategic HTML Formatting": {
            "impact": "256% improvement", 
            "description": "Professional formatting creates visual impact and organization",
            "key_metric": "25+ HTML tags"
        },
        "Authority Language": {
            "impact": "Strong predictor",
            "description": "References to officials, government, and institutions add legitimacy",
            "key_metric": "Multiple authority terms"
        }
    }
    
    for factor, details in success_factors.items():
        with st.expander(f"📋 {factor}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.write(f"**Impact:** {details['impact']}")
                st.write(f"**Description:** {details['description']}")
            with col2:
                st.info(f"**Target:** {details['key_metric']}")
    
    # Success Pathway Analysis
    st.subheader("🛤️ Multiple Pathways to Success")
    
    # Create visualization for success pathways
    pathway_data = {
        'Pathway': ['Official Victory', 'High Efficiency', 'High Scale', 'Multiple Pathways'],
        'Percentage': [3.9, 20.0, 20.0, 19.3],
        'Description': [
            'Official victory declaration',
            'High signatures per day (top 20%)',
            'High total signatures (top 20%)',
            'Combination of multiple factors'
        ]
    }
    
    fig = px.bar(
        x=pathway_data['Percentage'],
        y=pathway_data['Pathway'],
        orientation='h',
        title="Success Pathways Distribution",
        labels={'x': 'Percentage of Petitions (%)', 'y': 'Success Pathway'}
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Key Finding Alert
    st.warning("🔑 **Key Finding:** Content comprehensiveness is the single most important factor, showing 33.5% absolute improvement in success rates between top and bottom quartiles.")

def create_content_strategy_framework():
    """Tab 2: Content Strategy Framework"""
    st.header("📝 Content Strategy Framework")
    
    # Length Optimization
    st.subheader("📏 Content Length Optimization")
    
    # Create length benchmark visualization
    length_data = {
        'Component': ['Title', 'Description', 'Letter Body', 'Targeting'],
        'Successful_Median': [83, 1511, 66, 51],
        'Unsuccessful_Median': [70, 914, 48, 35],
        'Advantage_Ratio': [1.19, 1.65, 1.38, 1.46]
    }
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Character Length Comparison', 'Success Advantage Ratio'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    # Length comparison
    fig.add_trace(
        go.Bar(name='Successful', x=length_data['Component'], y=length_data['Successful_Median']),
        row=1, col=1
    )
    fig.add_trace(
        go.Bar(name='Unsuccessful', x=length_data['Component'], y=length_data['Unsuccessful_Median']),
        row=1, col=1
    )
    
    # Advantage ratio
    fig.add_trace(
        go.Bar(name='Advantage Ratio', x=length_data['Component'], y=length_data['Advantage_Ratio'], 
               marker_color='gold'),
        row=1, col=2
    )
    
    fig.update_layout(height=400, title_text="Content Length Strategy")
    st.plotly_chart(fig, use_container_width=True)
    
    # Optimal Length Guidelines
    st.subheader("📐 Optimal Length Guidelines")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **📑 Title Optimization**
        - Target: 80+ characters
        - Optimal: "Long" quartile (31% success rate)
        - Include specific details and context
        """)
        
        st.info("""
        **📄 Description Optimization** 
        - Target: 1,500+ characters
        - Very Long descriptions: 42.4% success rate
        - Include comprehensive background and solutions
        """)
    
    with col2:
        st.info("""
        **✉️ Letter Body Optimization**
        - Target: 65+ characters
        - Focus on specific implementation requests
        - Include technical details and requirements
        """)
        
        st.info("""
        **🎯 Targeting Optimization**
        - Target: 50+ characters  
        - Specify exact officials and departments
        - Include titles and proper names
        """)
    
    # Content Structure Framework
    st.subheader("🏗️ Content Structure Framework")
    
    structure_framework = {
        "Title Structure": [
            "Lead with specific action/outcome",
            "Include target authority/institution", 
            "Add urgency or timeline element",
            "Use professional, formal language"
        ],
        "Description Structure": [
            "Problem statement with data/evidence",
            "Background context and impact analysis",
            "Detailed solution with implementation steps",
            "Call-to-action with specific next steps"
        ],
        "Letter Structure": [
            "Formal greeting to specific official",
            "Clear, specific policy request",
            "Supporting evidence and rationale",
            "Timeline for response/action"
        ]
    }
    
    for section, guidelines in structure_framework.items():
        with st.expander(f"📋 {section}"):
            for i, guideline in enumerate(guidelines, 1):
                st.write(f"{i}. {guideline}")

def create_language_patterns_psychology():
    """Tab 3: Language Patterns & Psychology"""
    st.header("💬 Language Patterns & Psychology")
    
    # Keyword Effectiveness Analysis
    st.subheader("🔑 Strategic Keyword Analysis")
    
    # Create keyword effectiveness visualization
    keyword_data = {
        'Category': ['Power Words', 'Authority Terms', 'Call-to-Actions', 'Urgency Language', 'Emotional Terms'],
        'With_Feature': [24.1, 24.0, 25.7, 26.8, 24.5],
        'Without_Feature': [23.1, 22.6, 22.9, 22.2, 23.0],
        'Improvement': [1.1, 1.3, 2.8, 4.6, 1.5]
    }
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Success Rate by Keyword Usage', 'Improvement Percentage Points'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    # Success rates
    fig.add_trace(
        go.Bar(name='With Keywords', x=keyword_data['Category'], y=keyword_data['With_Feature']),
        row=1, col=1
    )
    fig.add_trace(
        go.Bar(name='Without Keywords', x=keyword_data['Category'], y=keyword_data['Without_Feature']),
        row=1, col=1
    )
    
    # Improvement
    fig.add_trace(
        go.Bar(name='Improvement (pp)', x=keyword_data['Category'], y=keyword_data['Improvement'],
               marker_color='green'),
        row=1, col=2
    )
    
    fig.update_layout(height=400, title_text="Keyword Strategy Impact")
    st.plotly_chart(fig, use_container_width=True)
    
    # Psychology-Based Language Framework
    st.subheader("🧠 Psychology-Based Language Framework")
    
    psychology_framework = {
        "Urgency & Scarcity": {
            "keywords": ["urgent", "immediate", "deadline", "crisis", "time running out"],
            "psychology": "Creates motivation through time pressure",
            "usage": "Use sparingly in titles and openings for maximum impact",
            "success_lift": "+4.6 percentage points"
        },
        "Authority & Credibility": {
            "keywords": ["government", "official", "department", "ministry", "court"],
            "psychology": "Leverages respect for institutional authority",
            "usage": "Reference specific officials and institutions",
            "success_lift": "+1.3 percentage points"
        },
        "Power & Justice": {
            "keywords": ["justice", "rights", "equality", "violation", "accountability"],
            "psychology": "Appeals to moral foundations and fairness",
            "usage": "Frame issues in terms of fundamental rights",
            "success_lift": "+1.1 percentage points"
        },
        "Action & Agency": {
            "keywords": ["stop", "demand", "protect", "prevent", "implement"],
            "psychology": "Empowers supporters with clear actions",
            "usage": "Include specific, actionable verbs",
            "success_lift": "+2.8 percentage points"
        }
    }
    
    for category, details in psychology_framework.items():
        with st.expander(f"🎭 {category}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.write(f"**Psychology:** {details['psychology']}")
                st.write(f"**Usage Strategy:** {details['usage']}")
                st.write(f"**Example Keywords:** {', '.join(details['keywords'][:3])}...")
            with col2:
                st.success(f"**Impact:** {details['success_lift']}")
    
    # Sentiment & Emotional Tone
    st.subheader("😊 Sentiment & Emotional Strategy") 
    
    sentiment_insights = {
        "Optimal Sentiment Range": "Neutral to Slightly Positive (0.0 to +0.1)",
        "Emotional Intensity": "Moderate intensity works best",
        "Title Strategy": "Professional, factual tone",
        "Description Strategy": "Balanced emotion with evidence"
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **📊 Sentiment Analysis Results**
        - Positive titles: 24.3% success rate
        - Neutral titles: 22.9% success rate  
        - Negative titles: 22.5% success rate
        
        *Insight: Slight positive tone optimizes without appearing biased*
        """)
    
    with col2:
        st.warning("""
        **⚖️ Emotional Balance Strategy**
        - Lead with facts and evidence
        - Include emotional connection 
        - Maintain professional credibility
        - Avoid excessive emotional language
        """)

def create_performance_benchmarks():
    """Tab 4: Performance Benchmarks"""
    st.header("📈 Performance Benchmarks & Targets")
    
    # Success Rate Benchmarks
    st.subheader("🎯 Success Rate Benchmarks by Feature")
    
    # Create benchmark visualization
    benchmark_data = {
        'Feature': [
            'Content Comprehensiveness',
            'Professional Sophistication', 
            'HTML Formatting',
            'Authority Targeting',
            'Strategic Urgency'
        ],
        'Bottom_Quartile': [8.5, 12.5, 14.2, 13.4, 20.4],
        'Top_Quartile': [41.9, 39.1, 42.8, 36.0, 29.2],
        'Improvement': [33.4, 26.6, 28.6, 22.6, 8.8]
    }
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Bottom Quartile',
        x=benchmark_data['Feature'],
        y=benchmark_data['Bottom_Quartile'],
        marker_color='lightcoral'
    ))
    
    fig.add_trace(go.Bar(
        name='Top Quartile', 
        x=benchmark_data['Feature'],
        y=benchmark_data['Top_Quartile'],
        marker_color='lightgreen'
    ))
    
    fig.update_layout(
        title='Success Rate Benchmarks by Feature Quartile',
        xaxis_title='Feature Category',
        yaxis_title='Success Rate (%)',
        barmode='group',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Specific Targets & Thresholds
    st.subheader("🎯 Specific Performance Targets")
    
    targets = {
        "Content Length Targets": {
            "Title": "83+ characters (successful median)",
            "Description": "1,511+ characters with HTML formatting", 
            "Letter Body": "66+ characters with specific requests",
            "Total Content": "1,660+ characters across all components"
        },
        "Language Complexity Targets": {
            "Readability Level": "Graduate level (Flesch-Kincaid 12+)",
            "Vocabulary Diversity": "High variety of technical terms",
            "Sentence Complexity": "Average 15+ words per sentence",
            "Professional Tone": "Formal, institutional language"
        },
        "Strategic Content Targets": {
            "HTML Tags": "25+ formatting tags for professionalism",
            "Authority References": "3+ specific officials/institutions",
            "Action Keywords": "5+ strategic action terms",
            "Evidence/Data": "Include statistics and citations"
        }
    }
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**📏 Content Length Targets**")
        for metric, target in targets["Content Length Targets"].items():
            st.write(f"• **{metric}:** {target}")
    
    with col2:
        st.info("**🧠 Language Complexity Targets**")
        for metric, target in targets["Language Complexity Targets"].items():
            st.write(f"• **{metric}:** {target}")
    
    with col3:
        st.info("**⚡ Strategic Content Targets**")
        for metric, target in targets["Strategic Content Targets"].items():
            st.write(f"• **{metric}:** {target}")
    
    # ROI Calculator
    st.subheader("💰 Expected Business Impact Calculator")
    
    st.write("**Calculate the potential improvement for your campaigns:**")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        current_success_rate = st.slider(
            "Current Success Rate (%)",
            min_value=5.0,
            max_value=50.0,
            value=23.2,
            step=0.5
        )
        
        improvement_scenario = st.selectbox(
            "Improvement Scenario",
            options=[
                "Conservative (10% improvement)",
                "Moderate (25% improvement)", 
                "Aggressive (35% improvement)",
                "Best Case (Following all recommendations)"
            ]
        )
    
    with col2:
        # Calculate potential improvements
        improvement_multipliers = {
            "Conservative (10% improvement)": 1.10,
            "Moderate (25% improvement)": 1.25,
            "Aggressive (35% improvement)": 1.35,
            "Best Case (Following all recommendations)": 1.65  # Based on description length advantage
        }
        
        multiplier = improvement_multipliers[improvement_scenario]
        new_success_rate = min(current_success_rate * multiplier, 95.0)  # Cap at 95%
        absolute_improvement = new_success_rate - current_success_rate
        
        st.metric(
            label="Projected Success Rate",
            value=f"{new_success_rate:.1f}%",
            delta=f"+{absolute_improvement:.1f} percentage points"
        )
        
        # Calculate campaign impact
        campaigns_per_month = st.number_input("Campaigns per Month", min_value=1, value=10)
        
        additional_successes = (absolute_improvement / 100) * campaigns_per_month
        
        st.success(f"""
        **Monthly Impact Projection:**
        - Additional successful campaigns: {additional_successes:.1f}
        - Success rate improvement: {((new_success_rate/current_success_rate - 1) * 100):.1f}%
        - Implementation ROI: High (content optimization is low-cost)
        """)

def create_implementation_toolkit():
    """Tab 5: Implementation Toolkit"""
    st.header("🛠️ Implementation Toolkit")
    
    # Content Checklist
    st.subheader("✅ Pre-Launch Content Checklist")
    
    checklist_categories = {
        "Title Optimization": [
            "Title is 80+ characters long",
            "Includes specific action/outcome",
            "References target authority/institution",
            "Uses professional, formal language",
            "Contains urgency or timeline element"
        ],
        "Description Excellence": [
            "Description is 1,500+ characters",
            "Includes problem statement with evidence",
            "Provides background context and impact", 
            "Details specific solution with implementation steps",
            "Uses 25+ HTML formatting tags",
            "Contains clear call-to-action"
        ],
        "Strategic Language": [
            "Includes 3+ authority references",
            "Contains 5+ action keywords",
            "Uses power words (justice, rights, equality)",
            "Maintains neutral to slightly positive sentiment",
            "Includes statistics or data evidence"
        ],
        "Professional Presentation": [
            "Graduate-level readability (Flesch-Kincaid 12+)",
            "Professional HTML formatting",
            "Structured paragraphs and sections",
            "Technical vocabulary appropriate to topic",
            "Formal, institutional tone throughout"
        ]
    }
    
    for category, items in checklist_categories.items():
        with st.expander(f"📋 {category} Checklist"):
            for item in items:
                st.checkbox(item, key=f"checklist_{category}_{item}")
    
    # Content Templates
    st.subheader("📝 Content Templates & Examples")
    
    template_type = st.selectbox(
        "Select Template Type",
        options=["High-Impact Title Template", "Description Structure Template", "Letter Body Template"]
    )
    
    if template_type == "High-Impact Title Template":
        st.code("""
HIGH-IMPACT TITLE TEMPLATE:

[Specific Action] + [Target Authority] + [Clear Outcome/Timeline]

Examples:
• "Mandatory Installation of Oxygen Plants in All Hospitals Above 50 Beds: Immediate Implementation Required"
• "Department of Health: Implement 24/7 Emergency Response Protocol for Rural Healthcare Centers"
• "City Council: Establish Comprehensive Public Transportation System by December 2024"

Key Elements:
1. Lead with specific, actionable demand
2. Name exact authority/institution 
3. Include timeline or urgency element
4. Use formal, professional language
5. Target 80+ characters for optimal length
        """, language="text")
    
    elif template_type == "Description Structure Template":
        st.code("""
DESCRIPTION STRUCTURE TEMPLATE (1,500+ characters):

**SECTION 1: Problem Statement (300-400 chars)**
- Clear definition of the issue
- Statistical evidence or data
- Impact on affected communities

**SECTION 2: Background Context (400-500 chars)**  
- Historical context and root causes
- Previous attempts or related initiatives
- Stakeholder analysis and current situation

**SECTION 3: Detailed Solution (500-600 chars)**
- Specific implementation steps
- Timeline and milestones
- Resource requirements and funding
- Success metrics and accountability measures

**SECTION 4: Call-to-Action (200-300 chars)**
- Specific next steps for decision-makers
- Contact information and follow-up process
- Community engagement opportunities

HTML Formatting: Use <p>, <ul>, <li>, <strong>, <em> tags for professional presentation
        """, language="text")
    
    else:  # Letter Body Template
        st.code("""
LETTER BODY TEMPLATE (65+ characters):

**Formal Structure:**

Dear [Specific Title] [Name],

I am writing to formally request [specific action/policy change]. 

[2-3 sentences with supporting evidence and rationale]

We respectfully request implementation by [specific timeline] to ensure [specific outcome].

Thank you for your consideration of this urgent matter.

Sincerely,
[Name and Title]

**Key Requirements:**
- Address specific official by name and title
- Include concrete implementation timeline
- Provide supporting evidence/rationale
- Maintain formal, respectful tone
- Request specific, measurable action
        """, language="text")
    
    # Performance Tracking Dashboard
    st.subheader("📊 Performance Tracking Framework")
    
    st.write("**Key Metrics to Track:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **📈 Success Metrics**
        - Overall success rate (target: 30%+)
        - Average signatures per petition
        - Time to reach milestones
        - Official response rate
        - Media coverage generated
        """)
        
        st.info("""
        **📝 Content Quality Metrics**
        - Average content length
        - HTML formatting usage
        - Keyword density scores
        - Readability levels
        - Authority reference count
        """)
    
    with col2:
        st.info("""
        **🎯 Engagement Metrics**
        - Signature velocity (signatures/day)
        - Social sharing rates
        - Comment engagement
        - Geographic reach
        - Demographic participation
        """)
        
        st.info("""
        **⚡ Optimization Metrics**
        - A/B testing results
        - Template performance
        - Keyword effectiveness
        - Format preference analysis
        - Channel performance comparison
        """)
    
    # Implementation Roadmap
    st.subheader("🗺️ Implementation Roadmap")
    
    roadmap_phases = {
        "Phase 1: Foundation (Days 1-30)": [
            "Train team on messaging framework",
            "Implement content checklist process", 
            "Create template library",
            "Establish baseline metrics"
        ],
        "Phase 2: Optimization (Days 31-90)": [
            "Deploy A/B testing for key elements",
            "Refine templates based on performance",
            "Integrate with existing workflow",
            "Scale successful patterns"
        ],
        "Phase 3: Advanced Analytics (Days 91+)": [
            "Implement predictive scoring",
            "Develop custom optimization tools",
            "Create automated recommendations",
            "Expand to additional platforms"
        ]
    }
    
    for phase, tasks in roadmap_phases.items():
        with st.expander(f"📅 {phase}"):
            for i, task in enumerate(tasks, 1):
                st.write(f"{i}. {task}")
    
    # Final Recommendations
    st.subheader("🎯 Final Strategic Recommendations")
    
    st.success("""
    **🔑 TOP 5 IMMEDIATE ACTIONS:**
    
    1. **Implement Content Length Standards**: Ensure all descriptions exceed 1,500 characters with comprehensive detail
    
    2. **Deploy Professional HTML Formatting**: Use structured formatting with 25+ tags for visual impact
    
    3. **Integrate Authority Language**: Include specific official titles, government departments, and institutional references
    
    4. **Establish Quality Control Process**: Use the provided checklist for every petition before launch
    
    5. **Track and Optimize**: Monitor success rates and iterate based on performance data
    
    **Expected Impact**: 25-65% improvement in success rates with systematic implementation
    """)

# Main execution
if __name__ == "__main__":
    create_messaging_insights_app()