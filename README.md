# NutriPlan: Personalised Calorie & Macro Planning Engine

A lightweight, type-safe Python calculation engine that computes Basal Metabolic Rate (BMR), Total Daily Energy Expenditure (TDEE), target daily calories, and tailored macronutrient splits based on user biometrics and fitness goals.

## Features

- **Mifflin-St Jeor BMR Calculation**: Accurate metabolic rate estimation tailored to age, biological sex, weight, and height.
- **Activity-Adjusted TDEE**: Supports five activity tiers (`sedentary`, `light`, `moderate`, `active`, `very_active`).
- **Goal-Driven Calorie & Macro Splits**: Automatically adjusts caloric targets and protein/carb/fat ratios for `lose_weight`, `maintain`, and `gain_muscle`.
- **Strict Data Validation**: Uses [Pydantic](https://docs.pydantic.dev/) models (`UserProfile` and `MacroPlan`) to enforce valid physiological inputs and clean structured outputs.
- **Forgiving CLI Runner**: Interactive command-line interface that normalizes input formatting and reports clear validation feedback.

## Project Structure

```text
nutri-plan/
├── engine.py           # Core BMR, TDEE, and macro calculation logic + Pydantic schemas
├── main.py             # Interactive CLI entry point
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignored local environment and cache files
└── README.md           # Project documentation