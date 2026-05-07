# SmartShip AI
AI-powered shipment delay predictor for supply chain operations

> Predict it. Prevent it. Deliver it.

---

## Problem Statement

54.8% of supply chain orders in our dataset arrived late. Logistics managers only find out after the damage is done — angry customers, SLA breaches, lost revenue.

SmartShip AI predicts shipment delay risk at the moment of order placement, giving operations teams time to act before delays happen.

---

## Live Demo

Live App: https://smartship-ai-supplychain.streamlit.app/


---

## What It Does

| Feature | Description |
|---|---|
| Delay Prediction | Predicts delay risk with 73.96% accuracy |
| Recommended Actions | Tells you exactly what to do about high-risk shipments |
| What-If Simulator | Compare delay risk across all shipping modes instantly |
| Delay Analytics | Visual patterns from 180,519 real supply chain orders |
| Ask AI | Claude-powered Q&A about shipment risk — coming soon |

---

## Tech Stack

- Python 3.13
- Pandas and NumPy — data manipulation
- Scikit-learn — model training and evaluation
- XGBoost — gradient boosting model
- SHAP — explainability layer
- Streamlit — interactive web dashboard
- Matplotlib — data visualisation
- Pickle — model serialisation

---

---

## ML Pipeline

1. Data Loading — 180,519 real supply chain orders
2. EDA — delay patterns by shipping mode, region, time
3. Feature Engineering — date extraction, label encoding, leakage removal
4. Model Training — Logistic Regression, Random Forest, XGBoost
5. Evaluation — Accuracy, Precision, Recall, F1 Score
6. SHAP Explainability — feature importance and direction of impact
7. Deployment — Streamlit web app

---

## Model Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| Logistic Regression | 68.99% | 78.78% | 59.46% | 67.77% |
| XGBoost | 72.02% | 82.47% | 62.19% | 70.91% |
| Random Forest | 73.96% | 80.98% | 68.63% | 74.29% |

Random Forest selected as the best model based on F1 Score.

---

## Key Insights from SHAP Analysis

- Scheduled delivery days is the number one predictor — unrealistic promises cause most delays
- Shipping mode is second — Standard Class carries significantly higher delay risk
- Order timing matters — late night orders miss warehouse cut-off times
- Payment type affects delivery — COD orders have higher failure rates

---

## Run Locally

```bash
git clone https://github.com/siddhipawar-projects/smartship-ai.git
cd smartship-ai

conda create -p venv python==3.13
conda activate venv/

pip install -r requirements.txt

streamlit run app/app.py
```

---

## Dataset

Source: DataCo Smart Supply Chain Dataset
Repository: Mendeley Data — academic research repository
Citation: Constante, F., Silva, F., and Pereira, A. (2019). DataCo Smart Supply Chain Dataset. Mendeley Data.
Size: 180,519 orders across 53 features

---

## About

Built by Siddhi Pawar
Supply Chain Domain Expert | Python | ML | PLM
Mumbai to Dubai

This project combines 4 years of supply chain domain expertise from working with Dassault Systemes clients on PLM implementations with machine learning to solve real logistics problems.

---

## Roadmap

- Claude AI chatbot integration for supply chain Q&A
- Batch prediction — upload CSV of orders
- User authentication and prediction history
- UAE-specific delay pattern analysis
- Real-time data integration via API