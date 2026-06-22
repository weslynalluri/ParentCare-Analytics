# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def home():

#     return {
#         "message": "ParentCare Analytics API Running"
#     }
from fastapi import FastAPI,HTTPException

from dashboard_service import get_dashboard_summary

from models import ChildAssessmentRequest,AssessmentResponse

from wellness_engine import assess_child

from recommendation_engine import generate_recommendations

from dashboard_service import get_risk_distribution

from dashboard_service import get_age_group_analysis

from dashboard_service import get_wellness_distribution

from dashboard_service import get_health_concerns

import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="ParentCare Analytics API",
    description="""
Digital Wellness Assessment Framework

Features:

- Child Wellness Assessment
- Risk Classification
- Health Concern Detection
- Parent Recommendations
- Dashboard Analytics

Built using FastAPI, Pandas and Power BI.
""",
    version="1.1.0",
    contact={
        "name": "Wesly"
    }
)

@app.get(
    "/",
    tags=["System"],
    summary="API Home",
    description="Returns API status information."
)
def home():

    return {
        "message": "ParentCare Analytics API Running"
    }


@app.get(
    "/health",
    tags=["System"],
    summary="Health Check",
    description="Checks whether the API service is running."
)
def health():

    return {
        "status": "healthy",
        "service": "ParentCare Analytics API"
    }



@app.post(
    "/assess-child",
    tags=["Assessment"],
    response_model=AssessmentResponse,
    summary="Assess Child Wellness"
)
def assess(request: ChildAssessmentRequest):

    try:

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

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Assessment failed: {str(e)}"
        )
    


@app.get(
    "/age-group-analysis",
    tags=["Analytics"],
    summary="Age Group Analysis",
    description="Returns average screen time and wellness score by age group."
)
def age_group_analysis():

    result = get_age_group_analysis()
    return result


@app.get(
    "/risk-distribution",
    tags=["Analytics"],
    summary="Risk Distribution",
    description="Returns distribution of Low, Moderate and High Risk children."
)
def risk_distribution():

    return get_risk_distribution()




@app.get(
    "/wellness-distribution",
    tags=["Analytics"],
    summary="Wellness Distribution",
    description="Returns distribution of wellness categories."
)
def wellness_distribution():

    return get_wellness_distribution()



@app.get(
    "/health-concerns",
    tags=["Analytics"],
    summary="Health Concerns",
    description="Returns counts of Poor Sleep, Eye Strain, Anxiety and Obesity Risk."
)
def health_concerns():

    return get_health_concerns()



@app.get(
    "/dashboard-summary",
    tags=["Analytics"],
    summary="Dashboard Summary",
    description="Returns key KPIs used in the ParentCare dashboard."
)
def dashboard_summary():

    return get_dashboard_summary()










