def generate_recommendations(
    wellness_category,
    poor_sleep,
    eye_strain,
    anxiety,
    obesity_risk
):

    recommendations = []

    # Category Recommendation

    if wellness_category == "Critical":
        recommendations.append(
            "Immediate parental monitoring is recommended."
        )

    elif wellness_category == "High Risk":
        recommendations.append(
            "Reduce recreational screen exposure."
        )

    elif wellness_category == "Moderate":
        recommendations.append(
            "Maintain balanced screen habits."
        )

    else:
        recommendations.append(
            "Continue healthy digital practices."
        )

    # Health Impact Recommendations

    if poor_sleep:
        recommendations.append(
            "Avoid device usage at least one hour before bedtime."
        )

    if eye_strain:
        recommendations.append(
            "Follow the 20-20-20 eye care rule."
        )

    if anxiety:
        recommendations.append(
            "Encourage outdoor activities and offline social interaction."
        )

    if obesity_risk:
        recommendations.append(
            "Increase daily physical activity and reduce sedentary behavior."
        )

    return recommendations