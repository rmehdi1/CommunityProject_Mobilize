import pandas as pd
import pickle
import streamlit as st

@st.cache_data
def load_model_artifacts():
    """Load all model artifacts with caching"""
    artifacts = {}

    try:
        # Load trained model
        with open('models/best_model.pkl', 'rb') as f:
            artifacts['model'] = pickle.load(f)

        # Load feature names
        with open('models/model_features.pkl', 'rb') as f:
            artifacts['features'] = pickle.load(f)

        # Load categorical encoders
        with open('models/categorical_encoders.pkl', 'rb') as f:
            artifacts['encoders'] = pickle.load(f)

        # Try to load reference data
        try:
            artifacts['reference_data'] = pd.read_excel('data/processed_petition_data.xlsx')
        except FileNotFoundError:
            artifacts['reference_data'] = None

        return artifacts

    except FileNotFoundError as e:
        return None