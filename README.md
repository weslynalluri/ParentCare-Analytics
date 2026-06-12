# 🧒 ParentCare Analytics
### Data-Driven Digital Wellness Assessment & Parent Intervention Framework

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Deployed-green)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
---

## 📌 Project Overview

**Parent_Care Analytics** is an end-to-end digital wellness assessment framework that analyzes children's screen-time behavior, identifies health risks, calculates a **Digital Wellness Score**, and generates personalized parental recommendations.

The project combines **data analytics**, **feature engineering**, **REST API development**, and **business intelligence dashboarding** to create a complete analytics solution addressing a real-world social problem.

> 💡 **Live API:** [https://parentcare-analytics-2.onrender.com](https://parentcare-analytics-2.onrender.com)  
> 📖 **API Docs (Swagger):** [https://parentcare-analytics-2.onrender.com/docs](https://parentcare-analytics-2.onrender.com/docs)

---

## ❗ Problem Statement

Children increasingly spend excessive time on digital devices, often exceeding recommended screen-time limits. This leads to poor sleep, eye strain, anxiety, and obesity risk. Parents and educators lack a structured method to assess digital wellness and identify at-risk children.

**ParentCare Analytics** solves this by providing a data-driven framework that evaluates screen-time behavior, measures wellness levels, and delivers actionable recommendations.

---

## 🎯 Objectives

- Analyze children's screen-time behavior across age groups and device types
- Identify health risks associated with excessive screen exposure
- Develop a **Digital Wellness Scoring Framework**
- Classify children into wellness categories with intervention priorities
- Generate **personalized parental recommendations** via a rule-based engine
- Expose analytics through **REST APIs** for real-world integration

---

## 🏗️ Project Architecture

```
Children Screen Time Dataset
           ↓
   Data Cleaning & EDA
           ↓
   Feature Engineering
           ↓
  Screen Risk Classification
           ↓
   Digital Wellness Scoring
           ↓
   Wellness Categorization
           ↓
  Rule-Based Recommendation Engine
           ↓
     FastAPI REST APIs
           ↓
    Power BI Dashboard
```

---

## 📊 Dataset

| Property | Details |
|---|---|
| Records | 9,668+ children |
| Source | Children's Screen Time Dataset |
| Type | Synthetic (Research-grade) |

**Key Columns:**
- `Age`, `Gender`, `Urban_or_Rural`
- `Daily_Screen_Time_Hours`
- `Primary_Device`
- `Educational_Screen_Time`, `Recreational_Screen_Time`
- `Health_Impacts` (Poor Sleep, Eye Strain, Anxiety, Obesity Risk)

---

## ⚙️ Feature Engineering

New columns created during analysis (not present in original dataset):

| Feature | Description |
|---|---|
| `Screen_Risk` | Low / Moderate / High based on screen time |
| `Risk_Points` | 100 / 70 / 40 based on risk level |
| `Health_Penalty` | Penalty points per health concern |
| `Digital_Wellness_Score` | Risk Points − Health Penalty |
| `Wellness_Category` | Healthy / Moderate / High Risk / Critical |
| `Concern_Count` | Number of health concerns (0–4) |
| `Intervention_Level` | Healthy Monitoring → Immediate Attention |

---

## 🧮 Digital Wellness Score Logic

```
Screen Risk Assignment:
  Screen Time ≥ 6 hrs  → High Risk  → 40 points
  Screen Time ≥ 3 hrs  → Moderate   → 70 points
  Screen Time < 3 hrs  → Low Risk   → 100 points

Health Penalty (−10 per concern):
  Poor Sleep    → −10
  Eye Strain    → −10
  Anxiety       → −10
  Obesity Risk  → −10

Digital Wellness Score = Risk Points − Health Penalty
```

**Wellness Categories:**

| Score | Category | Intervention |
|---|---|---|
| 90–100 | Healthy | Healthy Monitoring |
| 70–89 | Moderate | Preventive Action |
| 50–69 | High Risk | Monitor Closely |
| Below 50 | Critical | Immediate Attention |

---

## 🤖 Recommendation Engine

Rule-based engine generating personalized parental recommendations:

| Health Concern | Recommendation |
|---|---|
| Poor Sleep | Avoid device usage before bedtime |
| Eye Strain | Follow 20-20-20 eye care rule |
| Anxiety | Encourage outdoor activities and social interaction |
| Obesity Risk | Increase physical activity and reduce sedentary behavior |

Multiple concerns generate combined recommendations automatically.

---

## 🚀 FastAPI REST Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API health check |
| POST | `/assess-child` | Assess wellness for a child |
| GET | `/dashboard-summary` | Overview KPIs |
| GET | `/risk-distribution` | Screen risk breakdown |
| GET | `/age-group-analysis` | Risk by age group |
| GET | `/wellness-distribution` | Wellness category breakdown |
| GET | `/health-concerns` | Health concern statistics |

**Example Request — POST /assess-child:**
```json
{
  "child_name": "Rahul",
  "age": 14,
  "daily_screen_time_hours": 7.5,
  "health_impacts": ["Poor Sleep", "Eye Strain", "Anxiety"]
}
```

**Example Response:**
```json
{
  "child_name": "Rahul",
  "age": 14,
  "screen_risk": "High",
  "wellness_score": 10,
  "wellness_category": "Critical",
  "intervention_level": "Immediate Attention",
  "recommendations": [
    "Avoid device usage before bedtime",
    "Follow 20-20-20 eye care rule",
    "Encourage outdoor activities and social interaction"
  ]
}
```

---

## 📈 Power BI Dashboard

4-page interactive dashboard:

| Page | Content |
|---|---|
| Page 1 | Executive Overview — KPIs, Risk Distribution, Device Analysis |
| Page 2 | Screen Behavior & Risk Analysis — Age, Gender, Urban/Rural |
| Page 3 | Health & Wellness Assessment — Health Impacts, Concern Count |
| Page 4 | Recommendation & Parent Action Center |

---

## 🔍 Key Findings

- **85.77%** of children exceed recommended screen-time limits
- **Smartphones** are associated with the highest concentration of high-risk users
- **Poor Sleep** is the most frequently reported health concern
- **Urban children** show higher screen-risk exposure than rural children
- Children with **multiple health concerns** show significantly lower wellness scores

---

## 🛠️ Tech Stack

| Area | Tools |
|---|---|
| Data Processing | Python, Pandas, NumPy |
| API Development | FastAPI, Pydantic, Uvicorn |
| Visualization | Power BI, DAX |
| Deployment | Render |
| Version Control | GitHub |

---

## 📁 Project Structure

```
ParentCare-Analytics/
│
├── main.py                        # FastAPI application
├── models.py                      # Pydantic request/response models
├── wellness_engine.py             # Wellness scoring logic
├── recommendation_engine.py       # Rule-based recommendation logic
├── dashboard_service.py           # Dashboard analytics functions
│
├── data/
│   └── ParentCare_Final_Dataset.csv
│
├── Dashboard_On_Parent_Care.pbix  # Power BI Dashboard
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ParentCare-Analytics.git

# Navigate to project
cd ParentCare-Analytics

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --reload

# Open Swagger UI
http://127.0.0.1:8000/docs
```

---

## 🌐 Live Deployment

| Resource | Link |
|---|---|
| Live API | https://parentcare-analytics-2.onrender.com |
| API Documentation | https://parentcare-analytics-2.onrender.com/docs |

---

## 🔮 Future Scope

- Add sleep pattern and nutrition datasets for broader wellness analysis
- Integrate WHO/UNICEF research benchmarks into scoring
- Build a parent-facing web interface using Streamlit or React
- Add machine learning model for predictive wellness forecasting
- Expand recommendation engine with age-specific guidance

---


[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/YOUR_USERNAME)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/YOUR_PROFILE)

---

> *This project demonstrates the application of data analytics in addressing modern digital wellness challenges among children.*
