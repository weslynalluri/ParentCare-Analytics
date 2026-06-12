# wellness_engine.py

def get_age_group(age):

    if age <= 10:
        return "8-10"

    elif age <= 13:
        return "11-13"

    elif age <= 16:
        return "14-16"

    else:
        return "17-18"


# ----------------------------------

def get_screen_risk(screen_time):

    if screen_time < 2:
        return "Low Risk"

    elif screen_time < 4:
        return "Moderate Risk"

    else:
        return "High Risk"


# ----------------------------------

def get_risk_points(screen_risk):

    if screen_risk == "Low Risk":
        return 100

    elif screen_risk == "Moderate Risk":
        return 70

    else:
        return 40


# ----------------------------------

def calculate_health_penalty(
    poor_sleep,
    eye_strain,
    anxiety,
    obesity_risk
):

    penalty = 0

    if poor_sleep:
        penalty += 15

    if eye_strain:
        penalty += 10

    if anxiety:
        penalty += 10

    if obesity_risk:
        penalty += 5

    return penalty


# ----------------------------------

def get_wellness_category(score):

    if score >= 80:
        return "Healthy"

    elif score >= 60:
        return "Moderate"

    elif score >= 40:
        return "High Risk"

    else:
        return "Critical"


# ----------------------------------

def get_priority_level(category):

    if category == "Critical":
        return "Critical"

    elif category == "High Risk":
        return "High"

    elif category == "Moderate":
        return "Medium"

    else:
        return "Low"


# ----------------------------------

def get_concern_count(
    poor_sleep,
    eye_strain,
    anxiety,
    obesity_risk
):

    count = 0

    if poor_sleep:
        count += 1

    if eye_strain:
        count += 1

    if anxiety:
        count += 1

    if obesity_risk:
        count += 1

    return count


# ----------------------------------

def get_intervention_level(concern_count):

    if concern_count >= 3:
        return "Immediate Attention"

    elif concern_count == 2:
        return "Monitor Closely"

    elif concern_count == 1:
        return "Preventive Action"

    else:
        return "Healthy Monitoring"


# ----------------------------------

def assess_child(
    age,
    screen_time,
    poor_sleep,
    eye_strain,
    anxiety,
    obesity_risk
):

    age_group = get_age_group(age)

    screen_risk = get_screen_risk(screen_time)

    risk_points = get_risk_points(screen_risk)

    health_penalty = calculate_health_penalty(
        poor_sleep,
        eye_strain,
        anxiety,
        obesity_risk
    )

    wellness_score = max(
        0,
        risk_points - health_penalty
    )

    wellness_category = get_wellness_category(
        wellness_score
    )

    priority_level = get_priority_level(
        wellness_category
    )

    concern_count = get_concern_count(
        poor_sleep,
        eye_strain,
        anxiety,
        obesity_risk
    )

    intervention_level = get_intervention_level(
        concern_count
    )

    return {
        "age_group": age_group,
        "screen_risk": screen_risk,
        "risk_points": risk_points,
        "health_penalty": health_penalty,
        "wellness_score": wellness_score,
        "wellness_category": wellness_category,
        "priority_level": priority_level,
        "concern_count": concern_count,
        "intervention_level": intervention_level
    }