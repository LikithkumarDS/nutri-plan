from pydantic import ValidationError
from engine import UserProfile, calculate_nutriplan


def run():
    print("=== NutriPlan: Personalised Calorie & Macro Engine ===")
    try:
        age = int(input("Age: "))
        gender = input("Gender (male/female): ").strip().lower()
        weight_kg = float(input("Weight (kg): "))
        height_cm = float(input("Height (cm): "))
        activity_level = (
            input("Activity (sedentary/light/moderate/active/very_active): ")
            .strip()
            .lower()
            .replace(" ", "_")
        )
        goal = (
            input("Goal (lose_weight/maintain/gain_muscle): ")
            .strip()
            .lower()
            .replace(" ", "_")
        )

        profile = UserProfile(
            age=age,
            gender=gender,
            weight_kg=weight_kg,
            height_cm=height_cm,
            activity_level=activity_level,
            goal=goal,
        )

        plan = calculate_nutriplan(profile)

        print("\n--- Your Daily Plan ---")
        print(f"BMR:             {plan.bmr} kcal")
        print(f"TDEE:            {plan.tdee} kcal")
        print(f"Target Calories: {plan.target_calories} kcal")
        print(f"Protein:         {plan.protein_g} g")
        print(f"Carbs:           {plan.carbs_g} g")
        print(f"Fats:            {plan.fats_g} g")

    except ValidationError as e:
        print("\nValidation Error:")
        for err in e.errors():
            field = err["loc"][0]
            print(f" - {field}: {err['msg']}")
    except ValueError:
        print("\nInput Error: Please enter valid numbers for Age, Weight, and Height.")


if __name__ == "__main__":
    run()