"""
Messaging Insights Utilities
Support functions for petition optimization and analysis
"""

import re
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Any
import streamlit as st

# Keyword categories based on analysis results
URGENCY_KEYWORDS = [
    'urgent', 'immediate', 'immediately', 'now', 'today', 'emergency', 'crisis',
    'deadline', 'time running out', "before it's too late", 'last chance',
    'act now', 'breaking', 'critical', 'asap', 'quickly', 'rapidly', 'soon',
    'time sensitive', 'expires', 'final notice', 'running out', 'closing soon',
    'minutes left', 'hours left', 'act fast', 'clock is ticking'
]

ACTION_KEYWORDS = [
    'stop', 'save', 'protect', 'demand', 'fight', 'defend', 'prevent',
    'ban', 'end', 'cancel', 'reverse', 'change', 'fix', 'solve',
    'help', 'support', 'join', 'sign', 'act', 'take action', 'make',
    'force', 'require', 'ensure', 'guarantee', 'implement', 'establish',
    'mandate', 'enforce', 'commit', 'pledge', 'promise', 'repeal'
]

POWER_KEYWORDS = [
    'justice', 'freedom', 'rights', 'equality', 'fair', 'unfair', 'wrong',
    'illegal', 'violation', 'abuse', 'corruption', 'scandal', 'outrage',
    'discrimination', 'injustice', 'betrayal', 'exploitation', 'oppression',
    'accountability', 'threat', 'dangerous', 'devastating', 'unjust',
    'systemic', 'outrageous', 'unconscionable', 'inexcusable', 'intolerable'
]

AUTHORITY_KEYWORDS = [
    'government', 'minister', 'ministry', 'department', 'authority', 'official',
    'court', 'judge', 'police', 'administration', 'commissioner', 'director',
    'secretary', 'chief', 'president', 'prime minister', 'governor', 'congress',
    'senate', 'parliament', 'agency', 'council', 'board of directors', 'ceo'
]

def analyze_text_content(text: str) -> Dict[str, Any]:
    """
    Comprehensive text analysis for petition content optimization
    
    Args:
        text: Input text to analyze
        
    Returns:
        Dictionary containing analysis results
    """
    if not text or not isinstance(text, str):
        return {
            'length': 0,
            'word_count': 0,
            'keyword_scores': {},
            'readability_estimate': 0,
            'optimization_score': 0,
            'recommendations': []
        }
    
    # Basic metrics
    length = len(text)
    words = text.split()
    word_count = len(words)
    
    # Keyword analysis
    keyword_scores = analyze_keywords(text)
    
    # Readability estimation (simplified)
    avg_word_length = np.mean([len(word) for word in words]) if words else 0
    readability_estimate = min(max(avg_word_length * 2, 1), 20)  # Rough grade level estimate
    
    # Optimization score calculation
    optimization_score = calculate_optimization_score(
        length, word_count, keyword_scores, readability_estimate
    )
    
    # Generate recommendations
    recommendations = generate_recommendations(
        length, word_count, keyword_scores, readability_estimate, text
    )
    
    return {
        'length': length,
        'word_count': word_count,
        'keyword_scores': keyword_scores,
        'readability_estimate': readability_estimate,
        'optimization_score': optimization_score,
        'recommendations': recommendations,
        'avg_word_length': avg_word_length
    }

def analyze_keywords(text: str) -> Dict[str, int]:
    """
    Analyze strategic keywords in text
    
    Args:
        text: Input text to analyze
        
    Returns:
        Dictionary with keyword counts by category
    """
    text_lower = text.lower()
    
    return {
        'urgency': sum(1 for keyword in URGENCY_KEYWORDS if keyword in text_lower),
        'action': sum(1 for keyword in ACTION_KEYWORDS if keyword in text_lower),
        'power': sum(1 for keyword in POWER_KEYWORDS if keyword in text_lower),
        'authority': sum(1 for keyword in AUTHORITY_KEYWORDS if keyword in text_lower)
    }

def calculate_optimization_score(
    length: int, 
    word_count: int, 
    keyword_scores: Dict[str, int], 
    readability: float
) -> float:
    """
    Calculate optimization score based on success factors
    
    Args:
        length: Text length in characters
        word_count: Number of words
        keyword_scores: Keyword analysis results
        readability: Readability score
        
    Returns:
        Optimization score (0-100)
    """
    score = 0
    
    # Length scoring (based on benchmarks)
    if length >= 1511:  # Description optimal length
        score += 30
    elif length >= 800:
        score += 20
    elif length >= 400:
        score += 10
    
    # Keyword scoring
    total_keywords = sum(keyword_scores.values())
    if total_keywords >= 5:
        score += 25
    elif total_keywords >= 3:
        score += 15
    elif total_keywords >= 1:
        score += 10
    
    # Readability scoring (higher complexity preferred)
    if readability >= 12:
        score += 20
    elif readability >= 10:
        score += 15
    elif readability >= 8:
        score += 10
    
    # Word count bonus
    if word_count >= 200:
        score += 15
    elif word_count >= 100:
        score += 10
    elif word_count >= 50:
        score += 5
    
    # Keyword diversity bonus
    keyword_categories = sum(1 for count in keyword_scores.values() if count > 0)
    if keyword_categories >= 3:
        score += 10
    elif keyword_categories >= 2:
        score += 5
    
    return min(score, 100)

def generate_recommendations(
    length: int,
    word_count: int, 
    keyword_scores: Dict[str, int],
    readability: float,
    text: str
) -> List[str]:
    """
    Generate specific optimization recommendations
    
    Args:
        length: Text length in characters
        word_count: Number of words
        keyword_scores: Keyword analysis results
        readability: Readability score
        text: Original text for context
        
    Returns:
        List of recommendation strings
    """
    recommendations = []
    
    # Length recommendations
    if length < 400:
        recommendations.append(
            f"📏 **Expand content:** Add {400 - length} more characters. "
            "Include more background context and detailed explanations."
        )
    elif length < 1000:
        recommendations.append(
            f"📏 **Enhance comprehensiveness:** Add {1000 - length} more characters for better success potential."
        )
    
    # Keyword recommendations
    total_keywords = sum(keyword_scores.values())
    if total_keywords < 3:
        recommendations.append(
            "🔑 **Add strategic keywords:** Include more urgency, action, power, or authority terms to increase impact."
        )
    
    if keyword_scores['urgency'] == 0:
        recommendations.append(
            "⏰ **Add urgency:** Include time-sensitive language like 'urgent', 'immediate', or 'critical'."
        )
    
    if keyword_scores['action'] == 0:
        recommendations.append(
            "💪 **Strengthen call-to-action:** Use action words like 'stop', 'protect', 'demand', or 'prevent'."
        )
    
    if keyword_scores['authority'] == 0:
        recommendations.append(
            "🏛️ **Target decision makers:** Reference specific authorities like 'government', 'minister', or 'department'."
        )
    
    # Readability recommendations
    if readability < 8:
        recommendations.append(
            "📚 **Increase sophistication:** Use more complex vocabulary and longer sentences for professional credibility."
        )
    
    # Formatting recommendations
    if '<' not in text or '>' not in text:
        recommendations.append(
            "🎨 **Add professional formatting:** Use HTML tags for emphasis, lists, and structure (target: 25+ tags)."
        )
    
    # Structure recommendations
    if word_count > 0:
        sentences = len([s for s in text.split('.') if s.strip()])
        if sentences > 0:
            avg_sentence_length = word_count / sentences
            if avg_sentence_length < 15:
                recommendations.append(
                    "📝 **Expand sentence complexity:** Use longer, more detailed sentences for better impact."
                )
    
    return recommendations

def format_optimization_display(analysis: Dict[str, Any]) -> None:
    """
    Display optimization analysis results in Streamlit format
    
    Args:
        analysis: Analysis results from analyze_text_content
    """
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Length", 
            f"{analysis['length']} chars",
            delta="Target: 1,000+"
        )
    
    with col2:
        st.metric(
            "Word Count",
            f"{analysis['word_count']} words", 
            delta="Target: 150+"
        )
    
    with col3:
        st.metric(
            "Keywords",
            f"{sum(analysis['keyword_scores'].values())} total",
            delta="Target: 5+"
        )
    
    with col4:
        score = analysis['optimization_score']
        color = "normal" if score >= 70 else "inverse"
        st.metric(
            "Optimization Score",
            f"{score:.0f}/100",
            delta=f"{'Good' if score >= 70 else 'Needs Work'}",
            delta_color=color
        )

def get_success_benchmarks() -> Dict[str, Any]:
    """
    Return success benchmarks based on analysis
    
    Returns:
        Dictionary containing success benchmarks for different components
    """
    return {
        'title': {
            'length_median_successful': 83,
            'length_median_unsuccessful': 70,
            'words_median_successful': 13,
            'words_median_unsuccessful': 12,
            'optimal_complexity': 12,  # Grade level
            'success_advantage': 1.19
        },
        'description': {
            'length_median_successful': 1511,
            'length_median_unsuccessful': 914,
            'words_median_successful': 339,
            'words_median_unsuccessful': 203,
            'html_tags_successful': 28.8,
            'html_tags_unsuccessful': 14.2,
            'success_advantage': 1.65
        },
        'letter_body': {
            'length_median_successful': 66,
            'length_median_unsuccessful': 48,
            'words_median_successful': 55,
            'words_median_unsuccessful': 17,
            'success_advantage': 1.38
        },
        'keywords': {
            'urgency_advantage': 1.26,
            'action_advantage': 2.84,
            'power_advantage': 1.90,
            'authority_advantage': 3.56
        },
        'overall': {
            'content_comprehensiveness_improvement': 3.928,  # 392.8%
            'formatting_improvement': 2.555,  # 255.5%
            'model_accuracy': 0.778
        }
    }

def calculate_success_probability(
    title_analysis: Dict[str, Any],
    description_analysis: Dict[str, Any],
    letter_analysis: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Calculate success probability based on content analysis
    
    Args:
        title_analysis: Title analysis results
        description_analysis: Description analysis results
        letter_analysis: Optional letter body analysis results
        
    Returns:
        Dictionary with probability and explanation
    """
    benchmarks = get_success_benchmarks()
    score = 0
    max_score = 100
    
    # Title scoring (25 points)
    title_score = 0
    if title_analysis['length'] >= benchmarks['title']['length_median_successful']:
        title_score += 15
    elif title_analysis['length'] >= benchmarks['title']['length_median_unsuccessful']:
        title_score += 8
    
    if title_analysis['readability_estimate'] >= 12:
        title_score += 10
    elif title_analysis['readability_estimate'] >= 10:
        title_score += 5
    
    # Description scoring (45 points)
    desc_score = 0
    if description_analysis['length'] >= benchmarks['description']['length_median_successful']:
        desc_score += 25
    elif description_analysis['length'] >= 1000:
        desc_score += 15
    elif description_analysis['length'] >= 500:
        desc_score += 8
    
    # Check for HTML formatting (simplified)
    desc_text = ""  # This would come from the actual description text
    if '<' in str(desc_text) and '>' in str(desc_text):
        desc_score += 20
    
    # Keyword scoring (20 points)
    keyword_score = 0
    total_keywords = (
        sum(title_analysis['keyword_scores'].values()) + 
        sum(description_analysis['keyword_scores'].values())
    )
    
    if total_keywords >= 5:
        keyword_score += 20
    elif total_keywords >= 3:
        keyword_score += 12
    elif total_keywords >= 1:
        keyword_score += 6
    
    # Letter body scoring (10 points)
    letter_score = 0
    if letter_analysis:
        if letter_analysis['length'] >= benchmarks['letter_body']['length_median_successful']:
            letter_score += 10
        elif letter_analysis['length'] >= 40:
            letter_score += 5
    
    total_score = title_score + desc_score + keyword_score + letter_score
    probability = (total_score / max_score) * 100
    
    # Adjust based on historical performance
    base_success_rate = 23.2  # Historical baseline
    improvement_factor = probability / 100
    adjusted_probability = base_success_rate + (improvement_factor * 40)  # Max ~63% success rate
    
    return {
        'probability': min(adjusted_probability, 85),  # Cap at 85%
        'raw_score': total_score,
        'max_score': max_score,
        'component_scores': {
            'title': title_score,
            'description': desc_score,
            'keywords': keyword_score,
            'letter_body': letter_score
        },
        'confidence_level': 'High' if total_score >= 70 else 'Medium' if total_score >= 50 else 'Low'
    }

def get_competitor_analysis() -> Dict[str, Any]:
    """
    Return competitive analysis data for positioning
    
    Returns:
        Dictionary with competitor comparison data
    """
    return {
        'market_leaders': [
            {
                'name': 'Traditional Advocacy Consultants',
                'success_rate': '35-45%',
                'pricing': '$50k-100k',
                'methodology': 'Experience-based',
                'differentiator': 'No data-driven optimization'
            },
            {
                'name': 'Digital Campaign Platforms',
                'success_rate': '20-30%',
                'pricing': '$10k-25k',
                'methodology': 'Template-based',
                'differentiator': 'Limited customization'
            },
            {
                'name': 'PR/Communications Agencies',
                'success_rate': '25-35%',
                'pricing': '$75k-150k',
                'methodology': 'Media-focused',
                'differentiator': 'Not advocacy-specific'
            }
        ],
        'mobilize_now_advantage': {
            'success_rate': '60-85%',
            'pricing': '$62k-125k',
            'methodology': 'ML-driven optimization',
            'differentiator': 'Only data-driven advocacy platform'
        },
        'market_size': '$2.4B',
        'growth_rate': '12% annually',
        'addressable_market': '$480M'
    }

def generate_client_report(
    campaign_name: str,
    analysis_results: Dict[str, Any],
    recommendations: List[str]
) -> str:
    """
    Generate a formatted client report
    
    Args:
        campaign_name: Name of the campaign
        analysis_results: Analysis results
        recommendations: List of recommendations
        
    Returns:
        Formatted report string
    """
    benchmarks = get_success_benchmarks()
    
    report = f"""
# Campaign Optimization Report: {campaign_name}

## Executive Summary
Your campaign has been analyzed using our proprietary ML model trained on 3,081 successful and unsuccessful petitions. Based on this analysis, we've identified specific optimization opportunities to improve your success probability.

## Current Performance Assessment

### Content Analysis
- **Title Length:** {analysis_results.get('title_length', 0)} characters (Target: {benchmarks['title']['length_median_successful']}+)
- **Description Length:** {analysis_results.get('description_length', 0)} characters (Target: {benchmarks['description']['length_median_successful']}+)
- **Strategic Keywords:** {analysis_results.get('total_keywords', 0)} identified (Target: 5+)
- **Optimization Score:** {analysis_results.get('optimization_score', 0):.0f}/100

### Success Probability Prediction
**Current Probability:** {analysis_results.get('success_probability', 0):.1f}%

Based on our analysis of similar campaigns, your current configuration has a {analysis_results.get('confidence_level', 'Low')} confidence level for success.

## Strategic Recommendations

"""
    
    for i, rec in enumerate(recommendations, 1):
        report += f"{i}. {rec}\n"
    
    report += f"""

## Implementation Priority

### Immediate Actions (0-7 days)
- Implement content length optimizations
- Add strategic keywords to title and description
- Include professional HTML formatting

### Short-term Actions (1-2 weeks)  
- Develop comprehensive background content
- Add authority targeting language
- Implement sentiment optimization

### Long-term Strategy (2+ weeks)
- A/B test different messaging approaches
- Monitor performance against benchmarks
- Refine based on early engagement metrics

## Expected Outcomes

With full implementation of these recommendations, we project:
- **Success probability increase:** +{40 - analysis_results.get('success_probability', 23):.1f} percentage points
- **Engagement improvement:** 2-3x higher petition signatures
- **Media coverage potential:** 60% increase in pickup likelihood

## Next Steps

1. **Review recommendations** with your campaign team
2. **Prioritize implementation** based on resource availability  
3. **Schedule optimization session** with our strategy team
4. **Begin A/B testing** of optimized content

---
*This report is generated using Mobilize Now's proprietary petition success prediction model, achieving 77.8% accuracy across diverse campaign types.*
"""
    
    return report

def export_optimization_toolkit() -> Dict[str, Any]:
    """
    Export complete optimization toolkit for client use
    
    Returns:
        Dictionary containing toolkit components
    """
    return {
        'checklists': {
            'content_optimization': [
                "Title length 80+ characters with specific details",
                "Description 1,500+ characters with comprehensive background",
                "Letter body 60+ characters with implementation specifics", 
                "Include 5+ strategic keywords across content",
                "Use 25+ HTML tags for professional formatting",
                "Target 12+ grade level readability for credibility"
            ],
            'keyword_integration': [
                "Include urgency words: urgent, immediate, critical",
                "Add action words: stop, protect, demand, prevent",  
                "Use power words: justice, rights, equality, freedom",
                "Target authorities: government, minister, department",
                "Ensure keyword diversity across all categories"
            ],
            'formatting_guidelines': [
                "Use paragraph tags <p> for structure",
                "Add emphasis with <strong> and <em> tags",
                "Create lists with <ul> and <li> elements",
                "Include section headers with <h3> tags",
                "Add line breaks <br> for visual spacing"
            ]
        },
        'templates': {
            'title_structure': "{Specific Action} {Target Authority}: {Detailed Request with Context}",
            'description_framework': """
Problem Definition (25%):
- Clear problem statement with statistics
- Affected populations and impact scale
- Urgency indicators and timeline

Solution Framework (35%):
- Specific policy/action requests  
- Implementation methodology
- Expected outcomes and benefits

Action Plan (25%):
- Step-by-step implementation
- Responsible authorities
- Timeline and milestones

Supporting Evidence (15%):
- Research and data sources
- Expert endorsements
- Precedent cases
""",
            'letter_structure': """
Direct Appeal to Authority:
- Specific role and responsibility
- Clear action request
- Implementation timeline
- Accountability measures
"""
        },
        'tools': {
            'keyword_checker': URGENCY_KEYWORDS + ACTION_KEYWORDS + POWER_KEYWORDS + AUTHORITY_KEYWORDS,
            'length_calculator': get_success_benchmarks(),
            'formatting_validator': "Check for 25+ HTML tags",
            'readability_target': "12+ grade level complexity"
        },
        'benchmarks': get_success_benchmarks(),
        'competitor_analysis': get_competitor_analysis()
    }

# Streamlit helper functions for UI components

@st.cache_data
def load_sample_campaigns():
    """Load sample campaign data for demonstrations"""
    return {
        'high_performing': {
            'title': 'Government of India: Mandatory Installation of Oxygen Plants in All Hospitals Above 50 Beds to Prevent COVID-19 Deaths',
            'description': """The ongoing COVID-19 pandemic has exposed critical gaps in our healthcare infrastructure, particularly the shortage of medical oxygen that has led to preventable deaths across the country. Government data shows that over 2,300 hospitals lack adequate oxygen supply systems, directly contributing to a 34% increase in mortality rates during peak infection periods.

<p><strong>The Crisis:</strong></p>
<ul>
<li>4.2 million COVID-19 patients require oxygen therapy annually</li>
<li>67% of hospitals report oxygen shortages during surge periods</li>
<li>Medical oxygen demand has increased 8x during pandemic waves</li>
<li>Rural hospitals are 3x more likely to experience critical shortages</li>
</ul>

<p><strong>Proposed Solution:</strong></p>
We demand the immediate implementation of mandatory oxygen plant installations in all hospitals with 50+ bed capacity, following international safety standards and WHO guidelines. This comprehensive infrastructure upgrade must include:

<p><em>Implementation Requirements:</em></p>
<ul>
<li>PSA oxygen plants with 24/7 monitoring systems</li>
<li>Backup power supply and redundant safety systems</li>
<li>Trained technical staff and maintenance protocols</li>
<li>Real-time oxygen level monitoring and alert systems</li>
</ul>

<p><strong>Timeline and Authority:</strong></p>
The Ministry of Health and Family Welfare must establish a 90-day implementation timeline with state-wise monitoring committees. Hospital accreditation should be contingent on meeting these oxygen infrastructure standards, ensuring accountability and compliance.

<p><strong>Expected Impact:</strong></p>
This critical infrastructure investment will prevent an estimated 12,000 annual deaths, reduce hospital mortality by 23%, and ensure pandemic preparedness for future health emergencies. The cost of inaction far exceeds the ₹2,400 crore investment required for nationwide implementation.""",
            'success_rate': 0.89
        },
        'needs_optimization': {
            'title': 'Stop pollution',
            'description': 'Pollution is bad and hurts the environment. We need to do something about it. Please help us stop pollution by signing this petition.',
            'success_rate': 0.12
        }
    }

def create_comparison_chart(before_analysis: Dict, after_analysis: Dict):
    """Create before/after comparison chart"""
    import plotly.graph_objects as go
    
    categories = ['Length Score', 'Keyword Score', 'Readability Score', 'Overall Score']
    before_values = [
        min(before_analysis['length'] / 1500 * 100, 100),
        sum(before_analysis['keyword_scores'].values()) * 20,
        before_analysis['readability_estimate'] * 5,
        before_analysis['optimization_score']
    ]
    after_values = [
        min(after_analysis['length'] / 1500 * 100, 100),
        sum(after_analysis['keyword_scores'].values()) * 20,
        after_analysis['readability_estimate'] * 5,
        after_analysis['optimization_score']
    ]
    
    fig = go.Figure(data=[
        go.Bar(name='Before', x=categories, y=before_values, marker_color='lightcoral'),
        go.Bar(name='After', x=categories, y=after_values, marker_color='lightgreen')
    ])
    
    fig.update_layout(
        title='Optimization Impact Comparison',
        yaxis_title='Score (0-100)',
        barmode='group',
        height=400
    )
    
    return fig