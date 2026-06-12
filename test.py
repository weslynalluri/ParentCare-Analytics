# from app.wellness_engine import assess_child

# result = assess_child(
#     age=15,
#     screen_time=5.5,
#     poor_sleep=True,
#     eye_strain=True,
#     anxiety=False,
#     obesity_risk=False
# )

# print(result)


from app.wellness_engine import assess_child
from app.recommendation_engine import generate_recommendations

result = assess_child(
    age=15,
    screen_time=5.5,
    poor_sleep=True,
    eye_strain=True,
    anxiety=False,
    obesity_risk=False
)

recommendations = generate_recommendations(
    result["wellness_category"],
    poor_sleep=True,
    eye_strain=True,
    anxiety=False,
    obesity_risk=False
)

print(result)
print()
print(recommendations)