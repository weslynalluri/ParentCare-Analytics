# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def home():

#     return {
#         "message": "ParentCare Analytics API Running"
#     }
from fastapi import FastAPI

from dashboard_service import get_dashboard_summary

from models import ChildAssessmentRequest

from wellness_engine import assess_child

from recommendation_engine import generate_recommendations

from dashboard_service import get_risk_distribution

from dashboard_service import get_age_group_analysis

from dashboard_service import get_wellness_distribution

from dashboard_service import get_health_concerns

app = FastAPI(
    title="ParentCare Analytics API",
    description="Digital Wellness Assessment Framework",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "ParentCare Analytics API Running"

    }


@app.post("/assess-child")
def assess(request: ChildAssessmentRequest):

    result = assess_child(
        age=request.age,
        screen_time=request.screen_time,
        poor_sleep=request.poor_sleep,
        eye_strain=request.eye_strain,
        anxiety=request.anxiety,
        obesity_risk=request.obesity_risk
    )

    recommendations = generate_recommendations(
        result["wellness_category"],
        request.poor_sleep,
        request.eye_strain,
        request.anxiety,
        request.obesity_risk
    )

    result["recommendations"] = recommendations

    return result
@app.get("/risk-distribution")
def risk_distribution():

    return get_risk_distribution()

@app.get("/age-group-analysis")
def age_group_analysis():

    return get_age_group_analysis()


@app.get("/wellness-distribution")
def wellness_distribution():

    return get_wellness_distribution()

@app.get("/health-concerns")
def health_concerns():

    return get_health_concerns()

@app.get("/dashboard-summary")
def dashboard_summary():

    return get_dashboard_summary()
