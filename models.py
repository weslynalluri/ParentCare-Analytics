# from pydantic import BaseModel


# class ChildAssessmentRequest(BaseModel):

#     age: int

#     screen_time: float

#     poor_sleep: bool

#     eye_strain: bool

#     anxiety: bool

#     obesity_risk: bool

from pydantic import BaseModel, Field


class ChildAssessmentRequest(BaseModel):

    age: int = Field(
        ...,
        ge=8,
        le=18,
        description="Age must be between 8 and 18"
    )

    screen_time: float = Field(
        ...,
        ge=0,
        le=12,
        description="Daily screen time in hours"
    )

    poor_sleep: bool

    eye_strain: bool

    anxiety: bool

    obesity_risk: bool

class AssessmentResponse(BaseModel):

    age_group: str

    screen_risk: str

    risk_points: int

    health_penalty: int

    wellness_score: int

    wellness_category: str

    priority_level: str

    concern_count: int

    intervention_level: str

    recommendations: list[str]
