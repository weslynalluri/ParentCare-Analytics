from pydantic import BaseModel


class ChildAssessmentRequest(BaseModel):

    age: int

    screen_time: float

    poor_sleep: bool

    eye_strain: bool

    anxiety: bool

    obesity_risk: bool