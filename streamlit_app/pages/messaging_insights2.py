import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def show():
    st.title("📝 Messaging Insights & Strategic Framework")
    st.markdown("*Optimize petition success through data-driven messaging strategies*")
    
    # Sidebar for navigation
    page_section = st.sidebar.selectbox(
        "Navigate to:",
        ["Overview", "Content Framework", "Language Patterns", "Formatting Guidelines", "Success Benchmarks", "Optimization Tools"]
    )
    
    if page_section == "Overview":
        show_overview()
    elif page_section == "Content Framework":
        show_content_framework()
    elif page_section == "Language Patterns":
        show_language_patterns()
    elif page_section == "Formatting Guidelines":
        show_formatting_guidelines()
    elif page_section == "Success Benchmarks":
        show_success_benchmarks()
    elif page_section == "Optimization Tools":
        show_optimization_tools()

def show_overview():
    st.header("🎯 Strategic Messaging Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Success Rate Improvement",
            value="392.8%",
            delta="Content Comprehensiveness",
            help="Top vs bottom quartile comparison"
        )
    
    with col2:
        st.metric(
            label="Formatting Advantage",
            value="255.5%",
            delta="HTML Formatting",
            help="Professional formatting impact"
        )
    
    with col3:
        st.metric(
            label="Model Accuracy",
            value="77.8%",
            delta="Predictive Performance",
            help="Gradient Boosting model performance"
        )
    
    st.markdown("---")
    
    # Key Insights
    st.subheader("🔑 Key Strategic Insights")
    
    insights_data = {
        "Priority": ["1st", "2nd", "3rd", "4th"],
        "Strategy": [
            "Content Comprehensiveness",
            "Professional Formatting", 
            "Language Complexity",
            "Strategic Keywords"
        ],
        "Impact": ["33.5%", "28.7%", "13.8%", "8.8%"],
        "Implementation": [
            "Write 1,500+ character descriptions with comprehensive explanations",
            "Use 25+ HTML tags for professional presentation",
            "Target higher readability complexity (12+ grade level)",
            "Include urgency and action words in titles"
        ]
    }
    
    insights_df = pd.DataFrame(insights_data)
    
    # Display as an interactive table
    st.dataframe(
        insights_df,
        use_container_width=True,
        hide_index=True
    )
    
    # Feature importance visualization
    st.subheader("📊 Feature Importance Analysis")
    
    # Sample feature importance data from the notebook
    features = [
        "Content Comprehensiveness Score", "Description HTML Tags", "Letter Body Length",
        "Title Automated Readability", "Message Coherence Score", "Title Length",
        "Description Caps Ratio", "Professional Sophistication Score", "Authority Targeting Score"
    ]
    
    importance_scores = [0.0810, 0.0670, 0.0632, 0.0413, 0.0384, 0.0276, 0.0260, 0.0221, 0.0233]
    
    fig = px.bar(
        x=importance_scores,
        y=features,
        orientation='h',
        title="Top 9 Most Important Features for Petition Success",
        labels={'x': 'Feature Importance Score', 'y': 'Features'},
        color=importance_scores,
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

def show_content_framework():
    st.header("📋 Content Comprehensiveness Framework")
    
    st.info("""
    **Content comprehensiveness is the #1 predictor of petition success**, showing a 392.8% improvement 
    in success rates when comparing top vs bottom quartile petitions.
    """)
    
    # Content length guidelines
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📏 Optimal Content Lengths")
        
        length_data = {
            "Component": ["Title", "Description", "Letter Body", "Targeting Description"],
            "Successful Median (chars)": [83, 1511, 66, 51],
            "Unsuccessful Median (chars)": [70, 914, 48, 35],
            "Advantage Ratio": ["1.19x", "1.65x", "1.38x", "1.46x"]
        }
        
        length_df = pd.DataFrame(length_data)
        st.dataframe(length_df, use_container_width=True, hide_index=True)
        
    with col2:
        st.subheader("📝 Content Quality Guidelines")
        
        st.markdown("""
        **Title Guidelines:**
        - Aim for 80+ characters
        - Use 13+ words on average
        - Include specific details and context
        
        **Description Guidelines:**
        - Target 1,500+ characters minimum
        - Include comprehensive background
        - Provide detailed problem explanation
        - Offer specific solution proposals
        
        **Letter Body Guidelines:**
        - Write 60+ characters minimum
        - Include implementation specifics
        - Address decision-makers directly
        """)
    
    # Content structure recommendations
    st.subheader("🏗️ Content Structure Framework")
    
    tabs = st.tabs(["Problem Definition", "Solution Framework", "Action Plan", "Supporting Evidence"])
    
    with tabs[0]:
        st.markdown("""
        ### Problem Definition (25% of content)
        
        **Essential Elements:**
        - Clear problem statement with specific impacts
        - Quantified consequences (use statistics when available)
        - Urgency indicators and timeline constraints
        - Affected populations and stakeholder impact
        
        **Example Structure:**
        > "Over 2.3 million students lack access to clean drinking water in schools, 
        > leading to documented health issues and 47% higher absenteeism rates in affected districts."
        """)
    
    with tabs[1]:
        st.markdown("""
        ### Solution Framework (35% of content)
        
        **Core Components:**
        - Specific policy or action requests
        - Implementation timeline and methodology
        - Resource requirements and funding sources
        - Expected outcomes and success metrics
        
        **Power Words to Include:**
        - Implement, establish, mandate, require
        - Guarantee, ensure, protect, prevent
        - Justice, equality, rights, accountability
        """)
    
    with tabs[2]:
        st.markdown("""
        ### Action Plan (25% of content)
        
        **Implementation Details:**
        - Step-by-step implementation process
        - Responsible parties and authorities
        - Timeline milestones and deadlines
        - Monitoring and evaluation framework
        
        **Authority Keywords:**
        - Government, ministry, department, commission
        - Director, secretary, administrator, official
        - Congress, parliament, council, board
        """)
    
    with tabs[3]:
        st.markdown("""
        ### Supporting Evidence (15% of content)
        
        **Evidence Types:**
        - Research studies and statistical data
        - Expert testimonials and endorsements
        - Precedent cases and successful examples
        - Legal or policy framework references
        
        **Credibility Indicators:**
        - Peer-reviewed sources
        - Government data and reports
        - Academic institution research
        - Professional organization studies
        """)

def show_language_patterns():
    st.header("🗣️ Strategic Language Patterns")
    
    # Keyword analysis from the notebook
    st.subheader("🔥 High-Impact Keyword Categories")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Urgency Keywords (1.26x advantage)
        **Immediate Action:**
        - urgent, immediate, now, today
        - emergency, crisis, deadline
        - time running out, last chance
        - breaking, critical, asap
        
        **Time Sensitivity:**
        - expires, final notice, closing soon
        - minutes left, hours left
        - act fast, don't wait
        - clock is ticking
        """)
        
        st.markdown("""
        ### Power Words (1.90x advantage)
        **Justice & Rights:**
        - justice, freedom, rights, equality
        - fair, unfair, wrong, illegal
        - violation, abuse, corruption
        - discrimination, injustice
        
        **Impact Words:**
        - devastating, outrageous, unconscionable
        - historic, unprecedented, groundbreaking
        - transformative, accountability
        """)
    
    with col2:
        st.markdown("""
        ### Action Keywords (2.84x advantage)
        **Direct Actions:**
        - stop, save, protect, demand
        - fight, defend, prevent, ban
        - end, cancel, reverse, change
        - fix, solve, help, support
        
        **Implementation:**
        - implement, establish, mandate
        - enforce, require, ensure
        - guarantee, authorize, regulate
        """)
        
        st.markdown("""
        ### Authority Terms (3.56x advantage)
        **Government Bodies:**
        - government, minister, ministry
        - department, authority, official
        - court, judge, police, administration
        
        **Decision Makers:**
        - commissioner, director, secretary
        - president, governor, mayor
        - chairman, CEO, superintendent
        """)
    
    # Sentiment analysis insights
    st.subheader("😊 Sentiment Strategy Guidelines")
    
    sentiment_col1, sentiment_col2 = st.columns(2)
    
    with sentiment_col1:
        st.info("""
        **Optimal Sentiment Balance:**
        - Titles: Slightly negative (-0.012 successful vs -0.022 unsuccessful)
        - Descriptions: Slightly positive (0.013 vs 0.003)
        - Letter Body: Neutral to slightly positive (-0.004 vs -0.036)
        """)
    
    with sentiment_col2:
        st.warning("""
        **Emotional Intensity Guidelines:**
        - Use emotional language strategically
        - Positive emotions: hopeful, inspired, determined
        - Negative emotions: outraged, concerned, urgent
        - Balance emotion with factual content
        """)

def show_formatting_guidelines():
    st.header("🎨 Professional Formatting Guidelines")
    
    st.success("""
    **Professional formatting shows a 255.5% improvement in success rates**
    (28.7% absolute improvement between top and bottom quartiles)
    """)
    
    # HTML formatting guidelines
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📄 HTML Formatting Strategy")
        
        st.markdown("""
        **Target: 25+ HTML tags for optimal results**
        
        **Essential HTML Elements:**
        - `<p>` paragraphs for structure
        - `<strong>` or `<b>` for emphasis
        - `<em>` or `<i>` for important points
        - `<ul>` and `<li>` for lists
        - `<h3>` or `<h4>` for section headers
        
        **Advanced Formatting:**
        - `<blockquote>` for quotes/testimonials
        - `<a>` links to supporting evidence
        - `<br>` for strategic line breaks
        - Proper paragraph spacing
        """)
    
    with col2:
        st.subheader("📐 Structure Guidelines")
        
        st.markdown("""
        **Paragraph Structure:**
        - 3-5 sentences per paragraph
        - Clear topic sentences
        - Logical flow between paragraphs
        - Use subheadings for long content
        
        **Visual Hierarchy:**
        - Bold key statistics and facts
        - Italicize important concepts
        - Use bullet points for action items
        - Create clear sections with headers
        """)
    
    # Readability complexity
    st.subheader("📚 Readability Complexity Strategy")
    
    complexity_col1, complexity_col2 = st.columns(2)
    
    with complexity_col1:
        st.markdown("""
        ### Target Readability Levels
        
        **Title Complexity:**
        - Flesch-Kincaid: 12+ grade level
        - Gunning Fog: 12+ grade level
        - Use technical terminology appropriately
        
        **Description Complexity:**
        - Flesch Reading Ease: 40-60 (difficult)
        - Professional vocabulary
        - Complex sentence structures
        """)
    
    with complexity_col2:
        st.markdown("""
        ### Writing Techniques
        
        **Vocabulary Selection:**
        - Use 6+ character words on average
        - Include domain-specific terminology
        - Balance accessibility with sophistication
        
        **Sentence Structure:**
        - Vary sentence lengths
        - Use subordinate clauses
        - Include detailed explanations
        """)

def show_success_benchmarks():
    st.header("🎯 Success Benchmarks & Performance Targets")
    
    # Performance benchmarks from successful petitions
    st.subheader("📊 Performance Targets by Component")
    
    benchmark_data = {
        "Component": [
            "Title Length", "Title Complexity", "Description Length", 
            "Description HTML Tags", "Letter Body Length", "Authority Keywords",
            "Action Keywords", "Content Comprehensiveness"
        ],
        "Success Benchmark": [
            "83+ characters", "12+ grade level", "1,511+ characters",
            "25+ HTML tags", "66+ characters", "1.1+ per petition",
            "0.26+ per petition", "Top quartile score"
        ],
        "Failure Benchmark": [
            "70 characters", "10 grade level", "914 characters",
            "14 HTML tags", "48 characters", "0.31 per petition",
            "0.14 per petition", "Bottom quartile"
        ],
        "Improvement Ratio": [
            "1.19x", "1.20x", "1.65x", "2.03x", "1.38x", "3.56x", "1.90x", "4.93x"
        ]
    }
    
    benchmark_df = pd.DataFrame(benchmark_data)
    
    # Create an interactive chart
    fig = px.bar(
        benchmark_df,
        x="Component",
        y="Improvement Ratio", 
        title="Success Improvement Ratios by Component",
        text="Improvement Ratio",
        color="Improvement Ratio",
        color_continuous_scale="Greens"
    )
    
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(xaxis_tickangle=-45, height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed benchmarks table
    st.subheader("📋 Detailed Performance Benchmarks")
    st.dataframe(benchmark_df, use_container_width=True, hide_index=True)
    
    # Success rate by length quartiles
    st.subheader("📈 Success Rates by Content Length")
    
    length_success_data = {
        "Length Quartile": ["Very Short", "Short", "Medium", "Long", "Very Long"],
        "Title Success Rate": [18.4, 19.8, 24.2, 23.7, 31.0],
        "Description Success Rate": [9.2, 16.9, 23.3, 24.5, 42.4],
        "Overall Content Success Rate": [7.6, 16.9, 22.3, 24.5, 44.8]
    }
    
    length_df = pd.DataFrame(length_success_data)
    
    fig = px.line(
        length_df,
        x="Length Quartile",
        y=["Title Success Rate", "Description Success Rate", "Overall Content Success Rate"],
        title="Success Rates by Content Length Quartiles",
        markers=True
    )
    
    fig.update_layout(
        yaxis_title="Success Rate (%)",
        legend_title="Component Type"
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_optimization_tools():
    st.header("🛠️ Petition Optimization Tools")
    
    st.markdown("""
    Use these interactive tools to optimize your petition content based on our data-driven insights.
    """)
    
    # Content analyzer tool
    st.subheader("📝 Content Analyzer")
    
    with st.expander("Analyze Your Petition Content"):
        title_input = st.text_input("Petition Title:", placeholder="Enter your petition title here...")
        description_input = st.text_area("Description:", placeholder="Enter your petition description here...", height=150)
        letter_body_input = st.text_area("Letter Body:", placeholder="Enter your letter body here...", height=100)
        
        if st.button("Analyze Content"):
            if title_input and description_input:
                # Simple analysis based on the patterns identified
                analysis_results = analyze_content(title_input, description_input, letter_body_input)
                display_analysis_results(analysis_results)
            else:
                st.warning("Please enter both title and description to analyze.")
    
    # Keyword optimizer
    st.subheader("🔑 Keyword Optimizer")
    
    with st.expander("Optimize Keywords"):
        content_to_analyze = st.text_area("Content to Analyze:", placeholder="Paste your content here to check for strategic keywords...")
        
        if st.button("Check Keywords"):
            if content_to_analyze:
                keyword_analysis = analyze_keywords(content_to_analyze)
                display_keyword_analysis(keyword_analysis)
            else:
                st.warning("Please enter content to analyze.")
    
    # Success predictor
    st.subheader("🎯 Success Predictor")
    
    with st.expander("Predict Success Probability"):
        st.markdown("*Based on content characteristics and our machine learning model*")
        
        pred_title = st.text_input("Title:", key="pred_title")
        pred_desc = st.text_area("Description:", key="pred_desc", height=100)
        pred_letter = st.text_area("Letter Body:", key="pred_letter", height=80)
        
        if st.button("Predict Success"):
            if pred_title and pred_desc:
                prediction = predict_success(pred_title, pred_desc, pred_letter)
                display_prediction_results(prediction)
            else:
                st.warning("Please enter title and description for prediction.")

# Helper functions for the optimization tools
def analyze_content(title, description, letter_body):
    """Analyze content based on identified success patterns"""
    
    results = {
        "title_length": len(title),
        "title_words": len(title.split()),
        "description_length": len(description),
        "description_words": len(description.split()),
        "letter_body_length": len(letter_body) if letter_body else 0,
        "total_content": len(title) + len(description) + (len(letter_body) if letter_body else 0)
    }
    
    # Calculate scores based on benchmarks
    results["title_score"] = "Good" if results["title_length"] >= 83 else "Needs Improvement"
    results["description_score"] = "Good" if results["description_length"] >= 1511 else "Needs Improvement"
    results["overall_score"] = "Good" if results["total_content"] >= 1600 else "Needs Improvement"
    
    return results

def display_analysis_results(results):
    """Display content analysis results"""
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Title Length", f"{results['title_length']} chars", 
                 delta=f"Target: 83+ chars", 
                 delta_color="normal" if results['title_length'] >= 83 else "inverse")
    
    with col2:
        st.metric("Description Length", f"{results['description_length']} chars",
                 delta=f"Target: 1,511+ chars",
                 delta_color="normal" if results['description_length'] >= 1511 else "inverse")
    
    with col3:
        st.metric("Total Content", f"{results['total_content']} chars",
                 delta="Comprehensiveness Score",
                 delta_color="normal" if results['total_content'] >= 1600 else "inverse")
    
    # Recommendations
    st.subheader("📋 Recommendations:")
    
    if results['title_length'] < 83:
        st.warning(f"🔸 **Title:** Add {83 - results['title_length']} more characters. Include more specific details and context.")
    
    if results['description_length'] < 1511:
        st.warning(f"🔸 **Description:** Add {1511 - results['description_length']} more characters. Include comprehensive background, detailed problem explanation, and specific solutions.")
    
    if results['letter_body_length'] < 66:
        st.warning(f"🔸 **Letter Body:** Add more content. Include implementation specifics and direct appeals to decision-makers.")
    
    if all(score == "Good" for score in [results['title_score'], results['description_score']]):
        st.success("✅ **Great job!** Your content meets the optimal length benchmarks for success.")

def analyze_keywords(content):
    """Analyze keywords in content"""
    
    content_lower = content.lower()
    
    # Keyword categories from the analysis
    urgency_keywords = ['urgent', 'immediate', 'now', 'today', 'emergency', 'crisis', 'deadline', 'breaking', 'critical']
    action_keywords = ['stop', 'save', 'protect', 'demand', 'fight', 'defend', 'prevent', 'ban', 'end', 'change']
    power_keywords = ['justice', 'freedom', 'rights', 'equality', 'fair', 'unfair', 'wrong', 'illegal', 'violation']
    authority_keywords = ['government', 'minister', 'ministry', 'department', 'authority', 'official', 'court', 'administration']
    
    # Count keywords
    urgency_count = sum(1 for keyword in urgency_keywords if keyword in content_lower)
    action_count = sum(1 for keyword in action_keywords if keyword in content_lower)
    power_count = sum(1 for keyword in power_keywords if keyword in content_lower)
    authority_count = sum(1 for keyword in authority_keywords if keyword in content_lower)
    
    return {
        'urgency': urgency_count,
        'action': action_count,
        'power': power_count,
        'authority': authority_count,
        'total': urgency_count + action_count + power_count + authority_count
    }

def display_keyword_analysis(keyword_counts):
    """Display keyword analysis results"""
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Urgency Keywords", keyword_counts['urgency'], 
                 delta="Creates time pressure")
    
    with col2:
        st.metric("Action Keywords", keyword_counts['action'],
                 delta="Drives engagement")
    
    with col3:
        st.metric("Power Keywords", keyword_counts['power'],
                 delta="Emotional resonance")
    
    with col4:
        st.metric("Authority Keywords", keyword_counts['authority'],
                 delta="Targets decision makers")
    
    st.markdown("### Keyword Optimization Suggestions:")
    
    if keyword_counts['urgency'] == 0:
        st.info("🔸 Consider adding urgency keywords: 'urgent', 'immediate', 'critical', 'emergency'")
    
    if keyword_counts['action'] == 0:
        st.info("🔸 Consider adding action keywords: 'stop', 'protect', 'demand', 'prevent'")
    
    if keyword_counts['power'] == 0:
        st.info("🔸 Consider adding power keywords: 'justice', 'rights', 'equality', 'freedom'")
    
    if keyword_counts['authority'] == 0:
        st.info("🔸 Consider adding authority keywords: 'government', 'minister', 'department'")
    
    if keyword_counts['total'] >= 5:
        st.success("✅ Good keyword diversity! Your content includes strategic language patterns.")

def predict_success(title, description, letter_body):
    """Simple success prediction based on key factors"""
    
    score = 0
    max_score = 10
    
    # Title analysis
    if len(title) >= 83:
        score += 2
    elif len(title) >= 70:
        score += 1
    
    # Description analysis  
    if len(description) >= 1511:
        score += 3
    elif len(description) >= 1000:
        score += 2
    elif len(description) >= 500:
        score += 1
    
    # Letter body analysis
    if letter_body and len(letter_body) >= 66:
        score += 1
    
    # Keyword analysis
    all_content = f"{title} {description} {letter_body}".lower()
    keyword_analysis = analyze_keywords(all_content)
    
    if keyword_analysis['total'] >= 3:
        score += 2
    elif keyword_analysis['total'] >= 1:
        score += 1
    
    # HTML formatting (simplified check)
    if '<' in description and '>' in description:
        score += 2
    
    probability = (score / max_score) * 100
    
    return {
        'probability': probability,
        'score': score,
        'max_score': max_score,
        'category': 'High' if probability >= 70 else 'Medium' if probability >= 50 else 'Low'
    }

def display_prediction_results(prediction):
    """Display prediction results"""
    
    # Color coding based on probability
    if prediction['probability'] >= 70:
        color = "success"
        icon = "🎯"
    elif prediction['probability'] >= 50:
        color = "warning" 
        icon = "⚠️"
    else:
        color = "error"
        icon = "❌"
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric("Success Probability", f"{prediction['probability']:.1f}%",
                 delta=f"{prediction['category']} Potential")
    
    with col2:
        if color == "success":
            st.success(f"{icon} **High Success Potential** - Your petition has strong characteristics for success!")
        elif color == "warning":
            st.warning(f"{icon} **Medium Success Potential** - Good foundation, but room for improvement.")
        else:
            st.error(f"{icon} **Low Success Potential** - Significant optimization needed.")
    
    # Progress bar
    st.progress(prediction['score'] / prediction['max_score'])
    st.caption(f"Optimization Score: {prediction['score']}/{prediction['max_score']}")
    
    # Improvement suggestions
    if prediction['probability'] < 70:
        st.markdown("### 🚀 Optimization Opportunities:")
        
        if prediction['score'] < 5:
            st.info("🔸 Focus on content comprehensiveness - add more detailed explanations and context")
        
        if prediction['score'] < 7:
            st.info("🔸 Include professional HTML formatting in your description")
            
        if prediction['score'] < 8:
            st.info("🔸 Add more strategic keywords (urgency, action, power, authority terms)")

if __name__ == "__main__":
    show()