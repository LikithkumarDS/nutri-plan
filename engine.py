from typing import Literal
from pydantic import BaseModel, Field


class UserProfile(BaseModel):
    age: int = Field(..., gt=0, lt=120)
    gender: Literal["male", "female"]
    weight_kg: float = Field(..., gt=20)
    height_cm: float = Field(..., gt=50)
    activity_level: Literal["sedentary", "light", "moderate", "active", "very_active"]
    goal: Literal["lose_weight", "maintain", "gain_muscle"]


class MacroPlan(BaseModel):
    bmr: float
    tdee: float
    target_calories: float
    protein_g: float
    carbs_g: float
    fats_g: float


ACTIVITY_MULTIPLIERS = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "active": 1.725,
    "very_active": 1.9,
}

GOAL_CALORIE_ADJUSTMENTS = {
    "lose_weight": -500,
    "maintain": 0,
    "gain_muscle": 300,
}

# Macro ratios: (Protein %, Carbs %, Fats %)
GOAL_MACRO_SPLITS = {
    "lose_weight": (0.40, 0.30, 0.30),
    "maintain": (0.30, 0.40, 0.30),
    "gain_muscle": (0.30, 0.45, 0.25),
}


def calculate_nutriplan(profile: UserProfile) -> MacroPlan:
    # 1. Calculate BMR (Mifflin-St Jeor)
    if profile.gender == "male":
        bmr = (10 * profile.weight_kg) + (6.25 * profile.height_cm) - (5 * profile.age) + 5
    else:
        bmr = (10 * profile.weight_kg) + (6.25 * profile.height_cm) - (5 * profile.age) - 161

    # 2. Calculate TDEE
    tdee = bmr * ACTIVITY_MULTIPLIERS[profile.activity_level]

    # 3. Adjust for Goal
    target_calories = max(1200.0, tdee + GOAL_CALORIE_ADJUSTMENTS[profile.goal])

    # 4. Calculate Macros (Protein = 4 kcal/g, Carbs = 4 kcal/g, Fats = 9 kcal/g)
    p_ratio, c_ratio, f_ratio = GOAL_MACRO_SPLITS[profile.goal]
    protein_g = (target_calories * p_ratio) / 4
    carbs_g = (target_calories * c_ratio) / 4
    fats_g = (target_calories * f_ratio) / 9

    return MacroPlan(
        bmr=round(bmr, 1),
        tdee=round(tdee, 1),
        target_calories=round(target_calories, 1),
        protein_g=round(protein_g, 1),
        carbs_g=round(carbs_g, 1),
        fats_g=round(fats_g, 1),
    )