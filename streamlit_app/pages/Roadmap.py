import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import pandas as pd
import os
def show_roadmap():
    """
    Display the Implementation Roadmap with interactive timeline and enhanced aesthetics
    """
    
    # Page header with styling
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 30px;">
        <h1 style="color: white; margin: 0; font-size: 2.5em;">🚀 Implementation Roadmap</h1>
        <p style="color: white; margin: 10px 0 0 0; font-size: 1.2em;">Strategic Transformation for MobilizeNow Messaging Optimization</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for better organization
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Timeline Overview", "📋 Detailed Phases", "📈 Success Metrics", "📄 Full Documentation"])
    
    with tab1:
        st.markdown("### 🗓️ Interactive Project Timeline")
        
        # Create timeline data
        timeline_data = create_timeline_data()
        
        # Create interactive Gantt chart
        fig = create_gantt_chart(timeline_data)
        st.plotly_chart(fig, use_container_width=True)
        
        # Phase overview cards
        create_phase_cards()
        
    with tab2:
        st.markdown("### 📋 Detailed Phase Breakdown")
        
        # Phase 1
        create_phase_detail("Phase 1: Foundation and Proof of Concept", 
                          "🏗️", 
                          "Build baseline model and establish messaging effectiveness principles",
                          ["Organizational Setup", "Training & Skill Development", 
                           "Content Standards Implementation", "Template Development", 
                           "Initial Testing & Quality Control"])
        
        # Phase 2  
        create_phase_detail("Phase 2: Data Expansion and Advanced Optimization",
                          "📊",
                          "Broaden dataset and refine predictive capabilities",
                          ["Data Expansion", "Feature Engineering & Analytics",
                           "Predictive Model Refinement", "Advanced Testing",
                           "Skill Enhancement"])
        
        # Phase 3
        create_phase_detail("Phase 3: Integration and Organizational Transformation",
                          "🔄",
                          "Institutionalize best practices and develop proprietary tools",
                          ["Platform Development", "Cross-Platform Expansion",
                           "Staff Specialization", "Innovation & Knowledge Sharing"])
    
    with tab3:
        st.markdown("### 📈 Success Indicators & Risk Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 🎯 Success Indicators
            """)
            
            success_metrics = [
                ("Campaign Quality", "Campaigns consistently meet content standards", "✅"),
                ("Performance Improvement", "+40-60% success rate increase", "📈"),
                ("Staff Efficiency", "Increased confidence and productivity", "👥"),
                ("Thought Leadership", "Recognition in advocacy messaging", "🏆")
            ]
            
            for metric, description, icon in success_metrics:
                st.markdown(f"""
                <div style="background: #f0f8ff; padding: 15px; border-radius: 10px; margin: 10px 0; border-left: 4px solid #4CAF50;">
                    <strong>{icon} {metric}</strong><br>
                    <small>{description}</small>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            #### ⚠️ Risk Management
            """)
            
            risks = [
                ("Staff Resistance", "Phased rollout and comprehensive training", "👥"),
                ("Resource Constraints", "Prioritization of high-impact tasks", "💰"),
                ("Data Applicability", "Cross-platform validation", "📊"),
                ("Implementation Gaps", "Adaptable and modular tools", "🔧")
            ]
            
            for risk, mitigation, icon in risks:
                st.markdown(f"""
                <div style="background: #fff3cd; padding: 15px; border-radius: 10px; margin: 10px 0; border-left: 4px solid #ffc107;">
                    <strong>{icon} {risk}</strong><br>
                    <small>Mitigation: {mitigation}</small>
                </div>
                """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### 📄 Complete Implementation Roadmap")
        
        # Add download button for the roadmap
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📥 View Full Roadmap Document", use_container_width=True):
                display_full_roadmap()

def create_timeline_data():
    """Create timeline data for the Gantt chart"""
    
    # Calculate dates (assuming project starts now)
    start_date = datetime.now().date()
    
    phases = [
        {
            'Phase': 'Phase 1: Foundation & POC',
            'Start': start_date,
            'End': start_date + timedelta(days=180),  # 6 months
            'Color': '#FF6B6B',
            'Duration': '6 months'
        },
        {
            'Phase': 'Phase 2: Data Expansion',
            'Start': start_date + timedelta(days=150),  # Slight overlap
            'End': start_date + timedelta(days=330),  # 6 months duration
            'Color': '#4ECDC4',
            'Duration': '6 months'
        },
        {
            'Phase': 'Phase 3: Integration',
            'Start': start_date + timedelta(days=300),  # Slight overlap
            'End': start_date + timedelta(days=540),  # 8 months duration
            'Color': '#45B7D1',
            'Duration': '8 months'
        }
    ]
    
    return phases

def create_gantt_chart(timeline_data):
    """Create an interactive Gantt chart"""
    
    # Convert to DataFrame for easier handling
    df_data = []
    for phase in timeline_data:
        df_data.append({
            'Task': phase['Phase'],
            'Start': phase['Start'],
            'Finish': phase['End'],
            'Resource': phase['Phase'].split(':')[0]  # Phase 1, Phase 2, Phase 3
        })
    
    df = pd.DataFrame(df_data)
    
    # Create Gantt chart using plotly express
    fig = px.timeline(df, 
                     x_start="Start", 
                     x_end="Finish", 
                     y="Task",
                     title="Project Timeline - Messaging Optimization Implementation",
                     color="Resource",
                     color_discrete_map={
                         "Phase 1": "#FF6B6B",
                         "Phase 2": "#4ECDC4", 
                         "Phase 3": "#45B7D1"
                     })
    
    # Update layout for better appearance
    fig.update_layout(
        height=400,
        showlegend=True,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12),
        margin=dict(l=20, r=20, t=60, b=40),
        xaxis_title="Timeline",
        yaxis_title="Project Phases"
    )
    
    # Customize hover information
    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>" +
                     "Start: %{x}<br>" +
                     "End: %{x}<br>" +
                     "<extra></extra>"
    )
    
    return fig

def create_phase_cards():
    """Create overview cards for each phase"""
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF6B6B, #FF8E8E); padding: 20px; border-radius: 15px; color: white; text-align: center; margin: 10px 0;">
            <h3 style="margin: 0;">🏗️ Phase 1</h3>
            <h4 style="margin: 10px 0;">Foundation & POC</h4>
            <p style="margin: 0; font-size: 0.9em;">Build baseline model and establish messaging principles</p>
            <div style="margin-top: 15px; font-size: 1.5em; font-weight: bold;">6 months</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4ECDC4, #44A08D); padding: 20px; border-radius: 15px; color: white; text-align: center; margin: 10px 0;">
            <h3 style="margin: 0;">📊 Phase 2</h3>
            <h4 style="margin: 10px 0;">Data Expansion</h4>
            <p style="margin: 0; font-size: 0.9em;">Broaden dataset and refine predictive capabilities</p>
            <div style="margin-top: 15px; font-size: 1.5em; font-weight: bold;">6 months</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #45B7D1, #2E86AB); padding: 20px; border-radius: 15px; color: white; text-align: center; margin: 10px 0;">
            <h3 style="margin: 0;">🔄 Phase 3</h3>
            <h4 style="margin: 10px 0;">Integration</h4>
            <p style="margin: 0; font-size: 0.9em;">Institutionalize practices and develop tools</p>
            <div style="margin-top: 15px; font-size: 1.5em; font-weight: bold;">8 months</div>
        </div>
        """, unsafe_allow_html=True)

def create_phase_detail(title, icon, description, activities):
    """Create detailed phase information"""
    
    st.markdown(f"""
    <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #007bff;">
        <h3>{icon} {title}</h3>
        <p style="font-style: italic; color: #6c757d;">{description}</p>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(min(len(activities), 3))
    
    for i, activity in enumerate(activities):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background: white; padding: 15px; border-radius: 8px; margin: 5px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <strong>• {activity}</strong>
            </div>
            """, unsafe_allow_html=True)

def display_full_roadmap():
    """Redirect user to the GitHub-hosted roadmap markdown file"""

    st.markdown("""
    <div style="background: #f0f8ff; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <h2>📋 Implementation Roadmap for Messaging Optimization Framework</h2>
        <p>View the complete roadmap on GitHub:</p>
        <a href="https://github.com/rmehdi1/CommunityProject_Mobilize/blob/main/docs/ImplementationRoadmap.md" target="_blank" style="font-size: 1.1em; font-weight: bold; color: #1a73e8;">🔗 Open Roadmap on GitHub</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🔗 Related Documentation")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 View Messaging Insights", use_container_width=True):
            st.switch_page("pages/Messaging_Insights.py")
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.switch_page("streamlit_app.py")


# CSS for better styling
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
    }
    .element-container {
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    show_roadmap()