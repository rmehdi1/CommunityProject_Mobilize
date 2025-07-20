# CommunityProject_Mobilize

#  MobilizeNow: Predictive Messaging Framework for Campaign Success

[![Streamlit App](https://img.shields.io/badge/Launch%20App-Streamlit-ff4b4b)](https://communityprojectmobilize-kqpvfren9u8u6qqgdnfjty.streamlit.app/)

MobilizeNow is a data-driven toolkit to help grassroots organizations craft strategic, effective campaign messaging. Based on 24,000+ Change.org petitions, this project analyzes success patterns, builds predictive models, and provides actionable insights for digital advocacy.

---

##  Project Summary

This project aims to bridge the gap between intuition-based messaging and evidence-driven strategy in grassroots campaigns. By analyzing text, engagement metrics, and campaign outcomes, we engineered 162+ features, modeled success pathways, and developed a modular optimization app for community use.

---

##  Repository Structure
COMMUNITYPROJECT_MOBILIZE/
├── docs/
│ ├── EDA_FeatureEngineering.md
│ ├── ImplementationRoadmap.md
│ └── MessagingFramework.md
│
├── notebooks/
│ ├── 01_preprocessing_and_eda.ipynb
│ ├── 02_Analysis_ModelingExperiments.ipynb
│ └── 03_PredictiveModelPipeline.ipynb
│
├── data/
│ ├── inputdata.csv
│ ├── processed_petition_data.csv
│ └── sample_data.csv
│
├── models/
│ ├── best_model.pkl
│ └── categorical_encoders.pkl
│
├── streamlit_app/
│ ├── Home.py
│ ├── pages/
│ │ ├── petition_analyzer.py
│ │ ├── Messaging_Insights.py
│ │ ├── Model_Guide.py
│ │ ├── Roadmap.py
│ │ └── TheDataset.py
│ └── utils/
│ ├── data_processing.py
│ ├── feature_engineering.py
│ ├── messaging_utils.py
│ └── model_performance.py

## 📊 Notebooks Overview

### `01_preprocessing_and_eda.ipynb`
- Data cleaning, quality analysis, and geographic/temporal insights.

### `02_Analysis_ModelingExperiments.ipynb`
- Experimental models and feature testing on Change.org petitions.

### `03_PredictiveModelPipeline.ipynb`
- Clean, production-ready ML pipeline with feature engineering.

---

## 🔍 Key Findings

- **Success Metric**: Combined official victory, daily efficiency, and reach.
- **Feature Engineering**: Over 160 engineered features; final 73 used in modeling.
- **High-Impact Predictors**: Description length, urgency terms, targeting specificity.
- **Geographic Bias**: 98% petitions from India — critical for generalization awareness.

---

## 🛠️ Streamlit App

🔗 **Live Demo:** [MobilizeNow Streamlit App](https://communityprojectmobilize-kqpvfren9u8u6qqgdnfjty.streamlit.app/)

### App Modules
- `Home`: Overview and instructions
- `Petition Analyzer`: Upload your campaign and receive feedback
- `Messaging Insights`: Breakdown of emotional tone, strategic scoring
- `Model Guide`: Understand modeling pipeline and SHAP interpretability
- `Roadmap`: See implementation plans for organizations

---

## 📦 Core Deliverables

- 📄 `EDA_FeatureEngineering.md` — Full data analysis report  
- 🧠 `MessagingFramework.md` — Strategic best practices  
- 🛤️ `ImplementationRoadmap.md` — Step-by-step rollout guide  
- 🧪 `03_PredictiveModelPipeline.ipynb` — End-to-end ML model  
- 📊 `Streamlit App` — App for real-time petition scoring

---

## 📅 Timeline & Scope

**Duration:** June 13 – July 20, 2025  
**SOW Summary:** [SOW_PseudoClient_RajihaMehdi.pdf](./)  
**Client:** MobilizeNow (pseudo-client)

### Project Phases
1. EDA & Pattern Discovery  
2. Feature Engineering  
3. Predictive Modeling  
4. Toolkit & App Deployment

---

## 🌍 Community Impact

- Empowers grassroots organizers with data-backed tools
- Provides success predictors based on actual performance trends
- Enables platform-agnostic strategy development

