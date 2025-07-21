
import os 
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import re
from pathlib import Path
import warnings


warnings.filterwarnings('ignore')
# Text processing imports
try:
    import nltk
    from nltk.sentiment import SentimentIntensityAnalyzer
    from nltk.tokenize import word_tokenize, sent_tokenize
    # Download required NLTK data
    try:
        nltk.data.find('vader_lexicon')
    except LookupError:
        nltk.download('vader_lexicon', quiet=True)
    try:
        nltk.data.find('punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    try:
        nltk.data.find('stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)
except ImportError:
    st.error("NLTK not installed. Please install with: pip install nltk")
try:
    from textstat import flesch_reading_ease, flesch_kincaid_grade, gunning_fog, automated_readability_index
except ImportError:
    st.error("Textstat not installed. Please install with: pip install textstat")
# ============================================================================
# PAGE CONFIGURATION & STYLING
# ============================================================================
st.set_page_config(
    page_title="Petition Success Predictor",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Custom CSS for beautiful styling
st.markdown("""
<style>
    /* Main container styling */
    .main-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .sub-header {
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    /* Results container */
    .results-container {
        background: rgba(255, 255, 255, 0.98);
        color: #2c3e50;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #3b82f6;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
    
    /* Success indicators */
    .success-excellent { border-left-color: #10b981; background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%); }
    .success-good { border-left-color: #3b82f6; background: linear-gradient(135deg, #dbeafe 0%, #93c5fd 100%); }
    .success-moderate { border-left-color: #f59e0b; background: linear-gradient(135deg, #fef3c7 0%, #fcd34d 100%); }
    .success-poor { border-left-color: #ef4444; background: linear-gradient(135deg, #fee2e2 0%, #fca5a5 100%); }
    
    /* Recommendation cards */
    .recommendation {
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
        padding: 1rem;
        margin: 0.8rem 0;
        border-radius: 10px;
        border-left: 3px solid #10b981;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .improvement {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        padding: 1rem;
        margin: 0.8rem 0;
        border-radius: 10px;
        border-left: 3px solid #f59e0b;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Form styling */
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        transition: border-color 0.3s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(59, 130, 246, 0.4);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom progress bars */
    .progress-container {
        background: #e2e8f0;
        border-radius: 10px;
        height: 8px;
        margin: 0.5rem 0;
    }
    
    .progress-bar {
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }
    
    .progress-excellent { background: linear-gradient(90deg, #10b981, #059669); }
    .progress-good { background: linear-gradient(90deg, #3b82f6, #1d4ed8); }
    .progress-moderate { background: linear-gradient(90deg, #f59e0b, #d97706); }
    .progress-poor { background: linear-gradient(90deg, #ef4444, #dc2626); }
    
    /* Expandable sections */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border-radius: 10px;
        border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)
# ============================================================================
# PETITION PROCESSING PIPELINE
# ============================================================================
class StreamlitPetitionPipeline:
    """Streamlit-optimized petition processing pipeline"""
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer() if 'nltk' in globals() else None
        self.setup_keywords()
    def setup_keywords(self):
        """Define keyword categories for analysis"""
        self.urgency_keywords = [
            'urgent', 'immediate', 'immediately', 'now', 'today', 'emergency', 'crisis',
            'deadline', 'time running out', "before it's too late", 'last chance',
            'act now', 'breaking', 'critical', 'asap', 'quickly', 'rapidly', 'soon'
        ]
        self.action_keywords = [
            'stop', 'save', 'protect', 'demand', 'fight', 'defend', 'prevent',
            'ban', 'end', 'cancel', 'reverse', 'change', 'fix', 'solve',
            'help', 'support', 'join', 'sign', 'act', 'take action', 'make',
            'force', 'require', 'ensure', 'guarantee', 'implement', 'establish'
        ]
        self.power_words = [
            'justice', 'freedom', 'rights', 'equality', 'fair', 'unfair', 'wrong',
            'illegal', 'violation', 'abuse', 'corruption', 'scandal', 'outrage',
            'discrimination', 'injustice', 'betrayal', 'exploitation', 'oppression'
        ]
        self.authority_keywords = [
            'government', 'minister', 'ministry', 'department', 'authority', 'official',
            'court', 'judge', 'police', 'administration', 'commissioner', 'director',
            'secretary', 'chief', 'president', 'prime minister', 'governor', 'congress'
        ]
        self.cta_patterns = [
            r'\bsign\s+this\b', r'\bsign\s+now\b', r'\bjoin\s+us\b', r'\bhelp\s+us\b',
            r'\btake\s+action\b', r'\bact\s+now\b', r'\bmake\s+a\s+difference\b',
            r'\bdemand\s+action\b', r'\bstop\s+this\b', r'\bforce\s+them\b'
        ]
    def clean_html(self, text):
        """Remove HTML tags and clean text"""
        if pd.isna(text) or text is None:
            return ""
        clean = re.sub('<.*?>', '', str(text))
        return ' '.join(clean.split())
    def count_html_tags(self, text):
        """Count HTML tags in text"""
        if pd.isna(text) or text is None:
            return 0
        return len(re.findall('<.*?>', str(text)))
    def count_keywords(self, text, keywords):
        """Count keyword occurrences"""
        if pd.isna(text) or text is None:
            return 0
        clean_text = self.clean_html(text).lower()
        count = 0
        for keyword in keywords:
            count += clean_text.count(keyword.lower())
        return count
    def get_sentiment_scores(self, text):
        """Get sentiment scores"""
        if pd.isna(text) or text is None or not self.sia:
            return {'compound': 0, 'pos': 0, 'neg': 0, 'neu': 0}
        clean_text = self.clean_html(text)
        return self.sia.polarity_scores(clean_text)
    def calculate_readability(self, text):
        """Calculate readability metrics"""
        if pd.isna(text) or len(str(text).strip()) < 10:
            return {
                'flesch_ease': 0, 'flesch_kincaid': 0, 'gunning_fog': 0,
                'automated_readability': 0, 'avg_sentence_length': 0,
                'avg_word_length': 0, 'vocab_diversity': 0, 'caps_ratio': 0
            }
        clean_text = self.clean_html(text)
        try:
            if 'textstat' in globals():
                flesch_ease = flesch_reading_ease(clean_text)
                flesch_kincaid = flesch_kincaid_grade(clean_text)
                gunning_fog_score = gunning_fog(clean_text)
                automated_readability = automated_readability_index(clean_text)
            else:
                flesch_ease = flesch_kincaid = gunning_fog_score = automated_readability = 0
        except:
            flesch_ease = flesch_kincaid = gunning_fog_score = automated_readability = 0
        # Additional metrics
        try:
            if 'nltk' in globals():
                sentences = sent_tokenize(clean_text)
                words = word_tokenize(clean_text)
            else:
                sentences = clean_text.split('.')
                words = clean_text.split()
            
            avg_sentence_length = len(words) / len(sentences) if sentences else 0
            avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
            unique_words = set(word.lower() for word in words if word.isalpha())
            vocab_diversity = len(unique_words) / len(words) if words else 0
            caps_words = sum(1 for word in words if word.isupper() and len(word) > 1)
            caps_ratio = caps_words / len(words) if words else 0
        except:
            avg_sentence_length = avg_word_length = vocab_diversity = caps_ratio = 0
        return {
            'flesch_ease': flesch_ease,
            'flesch_kincaid': flesch_kincaid,
            'gunning_fog': gunning_fog_score,
            'automated_readability': automated_readability,
            'avg_sentence_length': avg_sentence_length,
            'avg_word_length': avg_word_length,
            'vocab_diversity': vocab_diversity,
            'caps_ratio': caps_ratio
        }
    def extract_features(self, petition_data):
        """Extract all features from petition data"""
        features = {}
        text_columns = ['title', 'description', 'letter_body', 'targeting_description']
        # Process each text column
        for col in text_columns:
            if col in petition_data:
                text = petition_data[col]
                # Basic text features
                features[f'{col}_length'] = len(str(text)) if pd.notna(text) else 0
                features[f'{col}_clean_length'] = len(self.clean_html(text))
                features[f'{col}_word_count'] = len(self.clean_html(text).split()) if self.clean_html(text) else 0
                # HTML features
                if col == 'description':
                    features[f'{col}_html_tags'] = self.count_html_tags(text)
                # Keyword counts
                features[f'{col}_urgency_count'] = self.count_keywords(text, self.urgency_keywords)
                features[f'{col}_action_count'] = self.count_keywords(text, self.action_keywords)
                features[f'{col}_power_count'] = self.count_keywords(text, self.power_words)
                features[f'{col}_authority_count'] = self.count_keywords(text, self.authority_keywords)
                # Boolean keyword features
                features[f'{col}_has_urgency'] = int(features[f'{col}_urgency_count'] > 0)
                features[f'{col}_has_action'] = int(features[f'{col}_action_count'] > 0)
                # CTA detection
                cta_count = sum(len(re.findall(pattern, str(text).lower())) for pattern in self.cta_patterns) if pd.notna(text) else 0
                features[f'{col}_cta_count'] = cta_count
                features[f'{col}_has_cta'] = int(cta_count > 0)
                # Numbers and statistics
                features[f'{col}_numbers_count'] = len(re.findall(r'\d+', str(text))) if pd.notna(text) else 0
                features[f'{col}_has_statistics'] = int(bool(re.search(r'\d+%|\d+\s*(percent|million|thousand|billion)', str(text), re.IGNORECASE)) if pd.notna(text) else False)
                # Text structure
                features[f'{col}_paragraph_count'] = len([p for p in str(text).split('\n') if p.strip()]) if pd.notna(text) else 0
                features[f'{col}_question_count'] = str(text).count('?') if pd.notna(text) else 0
                # Sentiment features
                sentiment = self.get_sentiment_scores(text)
                features[f'{col}_sentiment_compound'] = sentiment['compound']
                features[f'{col}_sentiment_positive'] = sentiment['pos']
                features[f'{col}_sentiment_negative'] = sentiment['neg']
                features[f'{col}_emotional_intensity'] = sentiment['pos'] + sentiment['neg']
                # Readability features
                readability = self.calculate_readability(text)
                for metric, value in readability.items():
                    features[f'{col}_{metric}'] = value
        # Strategic composite features
        features['content_comprehensiveness_score'] = (
            features.get('title_clean_length', 0) +
            features.get('description_clean_length', 0) +
            features.get('letter_body_clean_length', 0)
        )
        # Professional sophistication score
        desc_complexity = features.get('description_flesch_kincaid', 0)
        desc_length = features.get('description_clean_length', 0)
        html_formatting = features.get('description_html_tags', 0)
        title_complexity_norm = min(features.get('title_flesch_kincaid', 0) / 20, 1)
        desc_length_norm = min(desc_length / 2000, 1)
        html_tags_norm = min(html_formatting / 25, 1)
        features['professional_sophistication_score'] = (
            title_complexity_norm * 0.4 + desc_length_norm * 0.3 + html_tags_norm * 0.3
        )
        # Strategic urgency score
        urgency_total = features.get('title_urgency_count', 0) + features.get('description_urgency_count', 0)
        action_total = features.get('title_action_count', 0) + features.get('description_action_count', 0)
        sentiment_score = max(0, features.get('title_sentiment_compound', 0) + 1) / 2
        features['strategic_urgency_score'] = min((urgency_total + action_total) / 10 * 0.7 + sentiment_score * 0.3, 1)
        # Authority targeting score
        features['authority_targeting_score'] = (
            features.get('title_authority_count', 0) +
            features.get('description_authority_count', 0) +
            features.get('targeting_description_word_count', 0) / 10
        )
        # Message coherence score (simplified)
        features['message_coherence_score'] = 0.5
        return features
# ============================================================================
# MODEL LOADING FUNCTIONS
# ============================================================================
@st.cache_data
def load_model_artifacts():
    """Load all model artifacts with caching"""
    artifacts = {}
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        st.write(f"🔍 Script directory: {script_dir}")
        st.write(f"🔍 Current working directory: {os.getcwd()}")
        st.write(f"🔍 Files in script directory: {os.listdir(script_dir)}")
        
        # Check if models and data directories exist
        models_dir = os.path.join(script_dir, 'models')
        data_dir = os.path.join(script_dir, 'data')
        
        st.write(f"🔍 Models directory exists: {os.path.exists(models_dir)}")
        st.write(f"🔍 Data directory exists: {os.path.exists(data_dir)}")
        
        if os.path.exists(models_dir):
            st.write(f"🔍 Files in models directory: {os.listdir(models_dir)}")
        if os.path.exists(data_dir):
            st.write(f"🔍 Files in data directory: {os.listdir(data_dir)}")
        
        # Load trained model
        model_path = os.path.join(script_dir, 'models', 'best_model.pkl')
        st.write(f"🔍 Looking for model at: {model_path}")
        
        with open(model_path, 'rb') as f:
            artifacts['model'] = pickle.load(f)
        
        # Load feature names
        features_path = os.path.join(script_dir, 'models', 'model_features.pkl')
        with open(features_path, 'rb') as f:
            artifacts['features'] = pickle.load(f)
        
        # Load categorical encoders
        encoders_path = os.path.join(script_dir, 'models', 'categorical_encoders.pkl')
        with open(encoders_path, 'rb') as f:
            artifacts['encoders'] = pickle.load(f)
        
        # Try to load reference data
        try:
            data_path = os.path.join(script_dir, 'data', 'processed_petition_data.xlsx')
            artifacts['reference_data'] = pd.read_excel(data_path)
        except FileNotFoundError:
            # Try CSV as fallback
            try:
                data_path = os.path.join(script_dir, 'data', 'processed_petition_data.csv')
                artifacts['reference_data'] = pd.read_csv(data_path)
            except FileNotFoundError:
                artifacts['reference_data'] = None
        
        st.success("✅ All model artifacts loaded successfully!")
        return artifacts
        
    except FileNotFoundError as e:
        st.error(f"Model files not found: {e}")
        return None
    except Exception as e:
        st.error(f"Error loading model artifacts: {e}")
        return None
    
    
def predict_success(petition_data, model_artifacts, pipeline):
    """Predict petition success probability"""
    if not model_artifacts:
        return demo_prediction(petition_data, pipeline)
    try:
        features = pipeline.extract_features(petition_data)
        
        # Create feature vector
        feature_vector = []
        for feature_name in model_artifacts['features']:
            feature_vector.append(features.get(feature_name, 0))
        # Make prediction
        feature_array = np.array(feature_vector).reshape(1, -1)
        probability = model_artifacts['model'].predict_proba(feature_array)[0, 1]
        prediction = model_artifacts['model'].predict(feature_array)[0]
        return probability, prediction, features
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        return demo_prediction(petition_data, pipeline)
def demo_prediction(petition_data, pipeline):
    """Demo prediction when model is not available"""
    features = pipeline.extract_features(petition_data)
    # Simple scoring system
    score = 0.0
    # Content length (40% weight)
    content_score = features.get('content_comprehensiveness_score', 0)
    if content_score >= 2000:
        score += 0.4
    elif content_score >= 1000:
        score += 0.25
    elif content_score >= 500:
        score += 0.15
    # HTML formatting (20% weight)
    html_tags = features.get('description_html_tags', 0)
    score += min(html_tags / 25, 1) * 0.20
    # Strategic language (25% weight)
    urgency_count = features.get('title_urgency_count', 0) + features.get('description_urgency_count', 0)
    action_count = features.get('title_action_count', 0) + features.get('description_action_count', 0)
    strategic_score = min((urgency_count + action_count) / 8, 1)
    score += strategic_score * 0.25
    # Professional sophistication (15% weight)
    prof_score = features.get('professional_sophistication_score', 0)
    score += prof_score * 0.15
    probability = min(score, 0.95)
    prediction = 1 if probability >= 0.5 else 0
    return probability, prediction, features
# ============================================================================
# FEEDBACK GENERATION
# ============================================================================
def generate_detailed_feedback(petition_data, features, probability, prediction):
    """Generate comprehensive feedback and recommendations"""
    
    feedback = {
        'probability': probability,
        'prediction': prediction,
        'grade': '',
        'strengths': [],
        'improvements': [],
        'specific_recommendations': [],
        'metrics': {}
    }
    # Overall grade and styling
    if probability >= 0.8:
        feedback['grade'] = "🏆 EXCELLENT"
        feedback['grade_class'] = "success-excellent"
        feedback['overall'] = "Your petition has exceptional success potential!"
    elif probability >= 0.7:
        feedback['grade'] = "🎯 VERY GOOD"
        feedback['grade_class'] = "success-good"
        feedback['overall'] = "Your petition has strong success potential with minor optimizations."
    elif probability >= 0.6:
        feedback['grade'] = "✅ GOOD"
        feedback['grade_class'] = "success-good"
        feedback['overall'] = "Your petition shows good potential with some improvements needed."
    elif probability >= 0.5:
        feedback['grade'] = "📈 MODERATE"
        feedback['grade_class'] = "success-moderate"
        feedback['overall'] = "Your petition has moderate potential - several improvements recommended."
    elif probability >= 0.4:
        feedback['grade'] = "⚠️ NEEDS WORK"
        feedback['grade_class'] = "success-moderate"
        feedback['overall'] = "Your petition needs significant improvements to succeed."
    else:
        feedback['grade'] = "🔧 MAJOR REVISION NEEDED"
        feedback['grade_class'] = "success-poor"
        feedback['overall'] = "Your petition requires major restructuring for success."
    # Analyze specific metrics
    content_score = features.get('content_comprehensiveness_score', 0)
    html_tags = features.get('description_html_tags', 0)
    urgency_count = features.get('title_urgency_count', 0) + features.get('description_urgency_count', 0)
    action_count = features.get('title_action_count', 0) + features.get('description_action_count', 0)
    prof_score = features.get('professional_sophistication_score', 0)
    # Content analysis
    if content_score >= 2000:
        feedback['strengths'].append("✅ Excellent content comprehensiveness")
    elif content_score >= 1000:
        feedback['strengths'].append("✅ Good content length")
    else:
        feedback['improvements'].append("📝 Increase content comprehensiveness")
        feedback['specific_recommendations'].append(
            f"Expand total content to 2000+ characters (current: {content_score:.0f})"
        )
    # HTML formatting
    if html_tags >= 15:
        feedback['strengths'].append("✅ Professional HTML formatting")
    else:
        feedback['improvements'].append("🎨 Improve formatting and structure")
        feedback['specific_recommendations'].append(
            f"Add HTML formatting: <b>bold</b>, <strong>emphasis</strong>, <h3>headers</h3> (current: {html_tags} tags)"
        )
    # Strategic language
    if urgency_count >= 2:
        feedback['strengths'].append("✅ Strong urgency language")
    else:
        feedback['specific_recommendations'].append(
            "Add urgency keywords: 'immediate', 'urgent', 'critical', 'emergency'"
        )
    if action_count >= 3:
        feedback['strengths'].append("✅ Strong action-oriented language")
    else:
        feedback['specific_recommendations'].append(
            "Include more action words: 'demand', 'stop', 'implement', 'enforce'"
        )
    # Store metrics for display
    feedback['metrics'] = {
        'Content Length': f"{content_score:.0f} characters",
        'HTML Tags': f"{html_tags}",
        'Urgency Words': f"{urgency_count}",
        'Action Words': f"{action_count}",
        'Professional Score': f"{prof_score:.2f}",
        'Success Probability': f"{probability:.1%}"
    }
    return feedback
# ============================================================================
# STREAMLIT UI COMPONENTS
# ============================================================================
def display_header():
    """Display the main header"""
    st.markdown("""
    <div class="main-container">
        <div class="main-header">Petition Success Predictor</div>
        <div class="sub-header">
            Get instant feedback on your petition's success potential using advanced machine learning
        </div>
    </div>
    """, unsafe_allow_html=True)
def display_results(feedback, features):
    """Display comprehensive analysis results"""
    
    # Main results
    st.markdown(f"""
    <div class="results-container">
        <div style="text-align: center; margin-bottom: 2rem;">
            <div class="metric-card {feedback['grade_class']}" style="font-size: 1.5rem; font-weight: bold;">
                {feedback['grade']}
            </div>
            <div style="font-size: 2rem; font-weight: bold; color: #2563eb; margin: 1rem 0;">
                Success Probability: {feedback['probability']:.1%}
            </div>
            <div class="progress-container">
                <div class="progress-bar progress-{feedback['grade_class'].split('-')[1]}" style="width: {feedback['probability']*100}%;"></div>
            </div>
            <p style="font-size: 1.2rem; color: #64748b; margin-top: 1rem;">{feedback['overall']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    # Metrics grid
    col1, col2, col3 = st.columns(3)
    metrics_items = list(feedback['metrics'].items())
    
    for i, (metric, value) in enumerate(metrics_items):
        col = [col1, col2, col3][i % 3]
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 0.9rem; color: #64748b; font-weight: 500;">{metric}</div>
                <div style="font-size: 1.4rem; font-weight: bold; color: #1e293b;">{value}</div>
            </div>
            """, unsafe_allow_html=True)
    # Strengths
    if feedback['strengths']:
        st.markdown("### 🌟 Strengths")
        for strength in feedback['strengths']:
            st.markdown(f'''
            <div style="background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); 
                        padding: 1rem; margin: 0.8rem 0; border-radius: 10px; 
                        border-left: 3px solid #10b981; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                        color: #065f46; font-weight: 500;">
                {strength}
            </div>
            ''', unsafe_allow_html=True)
    # Improvements
    if feedback['improvements']:
        st.markdown("### 🔧 Areas for Improvement")
        for improvement in feedback['improvements']:
            st.markdown(f'''
            <div style="background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); 
                        padding: 1rem; margin: 0.8rem 0; border-radius: 10px; 
                        border-left: 3px solid #f59e0b; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                        color: #92400e; font-weight: 500;">
                {improvement}
            </div>
            ''', unsafe_allow_html=True)
    # Specific recommendations
    if feedback['specific_recommendations']:
        st.markdown("### 📋 Specific Recommendations")
        for i, rec in enumerate(feedback['specific_recommendations'], 1):
            st.markdown(f'''
            <div style="background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); 
                        padding: 1rem; margin: 0.8rem 0; border-radius: 10px; 
                        border-left: 3px solid #10b981; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                        color: #065f46; font-weight: 500;">
                {i}. {rec}
            </div>
            ''', unsafe_allow_html=True)
    # Next steps
    st.markdown("### 🎯 Next Steps")
    next_steps = [
        "Implement the recommendations above",
        "Re-analyze your petition to track improvements",
        "Consider A/B testing different versions",
        "Launch when you achieve 70%+ success probability"
    ]
    
    for i, step in enumerate(next_steps, 1):
        st.markdown(f'''
        <div style="background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); 
                    padding: 1rem; margin: 0.8rem 0; border-radius: 10px; 
                    border-left: 3px solid #10b981; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                    color: #065f46; font-weight: 500;">
            {i}. {step}
        </div>
        ''', unsafe_allow_html=True)
def create_sample_petition():
    """Return sample petition data"""
    return {
        'title': "Mandatory Installation of Oxygen Plants in All Hospitals Above 50 Beds to Save Lives During Medical Emergencies",
        'description': """<h3><strong>URGENT: Critical Oxygen Crisis in Indian Hospitals</strong></h3>
<p>The <strong>COVID-19 pandemic</strong> has exposed a devastating gap in our healthcare infrastructure: <strong>over 85% of hospitals</strong> lack adequate oxygen generation facilities.</p>
<h3><strong>The Problem:</strong></h3>
<ul>
<li><strong>Oxygen shortage</strong> affects 2,847 hospitals nationwide</li>
<li><strong>Supply chain disruptions</strong> lead to critical delays</li>
<li><strong>Rural hospitals</strong> are disproportionately affected</li>
<li><strong>Emergency patients</strong> face life-threatening delays</li>
</ul>
<h3><strong>Our Solution:</strong></h3>
<p>We demand the <strong>Ministry of Health and Family Welfare</strong> implement immediate regulations requiring:</p>
<ul>
<li><strong>Mandatory oxygen plants</strong> in all hospitals with 50+ beds</li>
<li><strong>24-month implementation timeline</strong> with government support</li>
<li><strong>Regular audits</strong> and compliance monitoring</li>
<li><strong>Financial assistance</strong> for rural and government hospitals</li>
</ul>
<p>This initiative will <strong>save over 50,000 lives annually</strong> and ensure that no patient dies due to oxygen shortage.</p>""",
        'letter_body': """Dear Honorable Minister of Health and Family Welfare,
We urgently request your immediate intervention to address the critical oxygen shortage crisis in Indian hospitals that has claimed thousands of lives.
As healthcare facilities nationwide struggle with inadequate oxygen infrastructure, patients continue to die from preventable causes. We demand mandatory installation of oxygen generation plants in all hospitals above 50 beds capacity.
This life-saving measure requires immediate policy implementation with a 24-month compliance timeline, government financial support, and regular monitoring.
We trust in your leadership to implement this critical healthcare reform that will save countless lives and strengthen our medical infrastructure.
Sincerely,
Concerned Citizens of India""",
        'targeting_description': "Ministry of Health and Family Welfare, Government of India; State Health Ministers; Hospital Administration Boards; Medical Council of India",
        'original_locale': 'en-IN',
        'has_location': True
    }
def display_usage_tips():
    """Display usage tips and best practices"""
    with st.expander("📚 How to Use This Tool", expanded=False):
        st.markdown("""
        #### Getting Started:
        1. **Fill in the form:** Enter your petition title, description, letter body, and target audience
        2. **Use HTML formatting:** Include tags like `<strong>`, `<h3>`, `<ul><li>` in your description
        3. **Be strategic:** Use urgency language, action words, and specific targets
        4. **Click "Analyze":** Get instant AI-powered predictions and recommendations
        5. **Iterate:** Improve based on feedback and re-analyze
        #### Tips for High Success Probability:
        - **Content Length:** Aim for 2000+ total characters across all fields
        - **HTML Formatting:** Use professional formatting with 15+ HTML tags
        - **Strategic Language:** Include urgency words like "immediate", "urgent", "critical"
        - **Action Words:** Use "demand", "stop", "implement", "enforce"
        - **Authority Targeting:** Mention specific officials, departments, or institutions
        - **Statistics:** Include numbers, percentages, and data when possible
        #### Success Benchmarks:
        - 📝 **Content:** 2000+ total characters
        - 🎨 **Formatting:** 15+ HTML tags
        - ⚡ **Language:** 5+ urgency/action keywords
        - 🏛️ **Authority:** Specific targets mentioned
        """)
# ============================================================================
# MAIN APPLICATION
# ============================================================================
def main():
    """Main Streamlit application"""
    
    # Initialize session state for sample data
    if 'sample_data' not in st.session_state:
        st.session_state.sample_data = None
    
    # Display header
    display_header()
    
    # Initialize pipeline
    pipeline = StreamlitPetitionPipeline()
    
    # Try to load model artifacts
    model_artifacts = load_model_artifacts()
    
    # Status indicator
    if model_artifacts:
        st.success("✅ Model loaded successfully! Full analysis available.")
    else:
        st.warning("⚠️ Demo Mode")
        st.info("💡 Ensure Right Model usage.")
    # Usage tips
    display_usage_tips()
    

    # Sample loader buttons outside the form
    st.markdown("## 🚀 Quick Start")
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])

    with col1:
        if st.button("📘 Sample Petition 1"):
            st.session_state.sample_data = {
            'title': "Help Needed in Delhi Schools",
            'description': "Please sign",
            'letter_body': "to whom it may concern",
            'targeting_description': "everyone",
            'original_locale': 'en-IN',
            'has_location': True
        }
            st.success("✅ Sample Petition 1 loaded!")

    with col2:
        if st.button("📗 Sample Petition 2"):
            st.session_state.sample_data = create_sample_petition()
            st.success("✅ Sample Petition 2 loaded!")

    with col3:
        if st.session_state.sample_data:
            st.info("📋 Sample loaded! The form below is pre-filled.")
        else:
            st.info("💡 Load a sample petition to see an example.")

    
    # Create form
    st.markdown("## 📝 Petition Analysis Form")
    
    # Get sample data if loaded
    sample_data = st.session_state.sample_data or {}
    
    with st.form("petition_form"):
        # Title input
        title = st.text_area(
            "📋 Petition Title",
            value=sample_data.get('title', ''),
            placeholder="Enter your petition title (e.g., 'Mandatory Installation of Oxygen Plants in All Hospitals to Save Lives')",
            height=100,
            help="A compelling title that clearly states your petition's goal"
        )
        
        # Description input
        description = st.text_area(
            "📄 Petition Description",
            value=sample_data.get('description', ''),
            placeholder="Enter detailed petition description with background, problem statement, and proposed solution. Use HTML formatting for better results.",
            height=300,
            help="Use HTML tags like <strong>, <h3>, <ul><li> for professional formatting"
        )
        
        # Letter body input
        letter_body = st.text_area(
            "✉️ Letter to Decision Makers",
            value=sample_data.get('letter_body', ''),
            placeholder="Enter the letter body that will be sent to decision makers. Be specific about your demands.",
            height=200,
            help="The formal letter that will be sent to the petition targets"
        )
        
        # Targeting input
        targeting_description = st.text_area(
            "🎯 Target Audience",
            value=sample_data.get('targeting_description', ''),
            placeholder="Who is this petition targeting? (e.g., 'Ministry of Health, State Governments, Hospital Administrators')",
            height=100,
            help="Specify the decision makers who can implement your requested changes"
        )
        
        # Advanced options in columns
        col1, col2 = st.columns(2)
        
        with col1:
            original_locale = st.selectbox(
                "🌍 Locale",
                options=[('India (en-IN)', 'en-IN'), ('United States (en-US)', 'en-US'),
                        ('United Kingdom (en-GB)', 'en-GB'), ('Canada (en-CA)', 'en-CA')],
                index=0 if not sample_data else next((i for i, (_, code) in enumerate([('India (en-IN)', 'en-IN'), ('United States (en-US)', 'en-US'), ('United Kingdom (en-GB)', 'en-GB'), ('Canada (en-CA)', 'en-CA')]) if code == sample_data.get('original_locale', 'en-IN')), 0),
                format_func=lambda x: x[0],
                help="Select the primary geographic region for your petition"
            )
        
        with col2:
            has_location = st.checkbox(
                "📍 Has Geographic Location",
                value=sample_data.get('has_location', True),
                help="Check if your petition targets a specific geographic area"
            )
        
        # Submit button
        submitted = st.form_submit_button("🔍 Analyze Petition", type="primary")
    
    if submitted:
        # Validate inputs
        if not title.strip() or not description.strip():
            st.error("❌ Please fill in at least the title and description fields.")
            return
        
        # Create petition data
        petition_data = {
            'title': title.strip(),
            'description': description.strip(),
            'letter_body': letter_body.strip(),
            'targeting_description': targeting_description.strip(),
            'original_locale': original_locale[1],
            'has_location': has_location
        }
        
        # Show processing message
        with st.spinner("🔄 Analyzing your petition... Please wait."):
            try:
                # Make prediction
                probability, prediction, features = predict_success(petition_data, model_artifacts, pipeline)
                
                # Generate feedback
                feedback = generate_detailed_feedback(petition_data, features, probability, prediction)
                
                # Display results
                st.markdown("## 📊 Analysis Results")
                display_results(feedback, features)
                
                # Advanced metrics
                with st.expander("🔍 Advanced Metrics", expanded=False):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("#### Content Analysis")
                        content_metrics = {
                            'Total Content Length': f"{features.get('content_comprehensiveness_score', 0):.0f} characters",
                            'Title Length': f"{features.get('title_clean_length', 0)} characters",
                            'Description Length': f"{features.get('description_clean_length', 0)} characters",
                            'HTML Tags': f"{features.get('description_html_tags', 0)} tags"
                        }
                        
                        for metric, value in content_metrics.items():
                            st.markdown(f"**{metric}:** {value}")
                    
                    with col2:
                        st.markdown("#### Language Analysis")
                        language_metrics = {
                            'Urgency Keywords': f"{features.get('title_urgency_count', 0) + features.get('description_urgency_count', 0)}",
                            'Action Keywords': f"{features.get('title_action_count', 0) + features.get('description_action_count', 0)}",
                            'Authority References': f"{features.get('targeting_description_authority_count', 0)}",
                            'Professional Score': f"{features.get('professional_sophistication_score', 0):.3f}"
                        }
                        
                        for metric, value in language_metrics.items():
                            st.markdown(f"**{metric}:** {value}")
                
            except Exception as e:
                st.error(f"❌ Analysis error: {str(e)}")
                st.error("Please check your inputs and try again.")
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #64748b; padding: 1rem;">
        <p>🤖 Powered by Advanced Machine Learning | Built with Streamlit</p>
        <p>💡 Tip: Aim for 70%+ success probability before launching your petition</p>
    </div>
    """, unsafe_allow_html=True)
if __name__ == "__main__":
    main()
