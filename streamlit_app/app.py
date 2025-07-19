import streamlit as st

st.set_page_config(
    page_title="MobilizeNow - Petition Success Predictor",
    page_icon="🔮",
    layout="wide"
)

st.write("✅ app.py is rendering!")

st.title("🔮 MobilizeNow - Petition Success Predictor")
st.markdown("### Messaging Optimization for Community Campaign Success")

st.markdown("""
Welcome to the MobilizeNow Petition Success Predictor! 

Navigate using the sidebar to explore:
- 🏠 **Home**: Project overview and key findings
- 🔮 **Live Predictor**: Test your petition content
- 📈 **Model Performance**: See how our model works
- 📚 **Resources**: Downloads and documentation
""")

st.sidebar.success("Select a page above")

import sys
import os
sys.path.append(os.path.dirname(__file__))

# Now import
try:
    from utils.data_processing import load_model_artifacts
    
    # Test loading
    artifacts = load_model_artifacts()
    if artifacts:
        st.success("✅ All model artifacts loaded successfully!")
        st.write(f"Features: {len(artifacts['features'])}")
    else:
        st.error("❌ Failed to load model artifacts")
except ImportError as e:
    st.error(f"Import error: {e}")
    st.info("Model loading will be available once files are properly organized")


artifacts = load_model_artifacts()
if artifacts:
    st.success("✅ All model artifacts loaded successfully!")
    st.write(f"Features: {len(artifacts['features'])}")
else:
    st.error("❌ Failed to load model artifacts")

