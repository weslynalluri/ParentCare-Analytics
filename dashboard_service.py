import pandas as pd


df = pd.read_csv(
        "ParentCare_Final_Dataset.csv"
    )
def get_risk_distribution():

    risk_counts = df["Screen_Risk"].value_counts()

    return risk_counts.to_dict()
def get_dashboard_summary():

    total_children = len(df)

    avg_screen_time = round(
        df["Avg_Daily_Screen_Time_hr"].mean(),
        2
    )

    high_risk_pct = round(
        (
            (df["Screen_Risk"] == "High Risk").mean()
        ) * 100,
        2
    )

    avg_wellness_score = round(
        df["Digital_Wellness_Score"].mean(),
        2
    )

    return {
        "total_children": total_children,
        "average_screen_time": avg_screen_time,
        "high_risk_percentage": high_risk_pct,
        "average_wellness_score": avg_wellness_score
    }
def get_age_group_analysis():

    age_analysis = (
        df.groupby("Age_Group")
        .agg({
            "screen_time_hours":"mean",
            "wellness_score":"mean"
        })
        .round(2)
    )

    return age_analysis.to_dict()

def get_wellness_distribution():

    return (
        df["Wellness_Category"]
        .value_counts()
        .to_dict()
    )

def get_health_concerns():

    return {
        "poor_sleep": int(df["Poor_Sleep"].sum()),
        "eye_strain": int(df["Eye_Strain"].sum()),
        "anxiety": int(df["Anxiety"].sum()),
        "obesity_risk": int(df["Obesity_Risk"].sum())
    }

