import datetime
from zoneinfo import ZoneInfo
from typing import Dict, List, Tuple, Any
from google.adk.agents import Agent

def calculate_bmi(weight_kg: float, height_cm: float) -> Dict[str, Any]:
    """Calculate BMI (Body Mass Index) and provide a health assessment.

    Args:
        weight_kg (float): Weight in kilograms
        height_cm (float): Height in centimeters

    Returns:
        Dict[str, Any]: status and result or error message
    """
    try:
        # Convert height from cm to meters
        height_m = height_cm / 100
        
        # Calculate BMI
        bmi = weight_kg / (height_m * height_m)
        
        # Determine BMI category
        if bmi < 18.5:
            category = "underweight"
        elif 18.5 <= bmi < 25:
            category = "normal weight"
        elif 25 <= bmi < 30:
            category = "overweight"
        else:
            category = "obese"
        
        report = (
            f"Your BMI is {bmi:.1f}, which is classified as '{category}'. "
            f"A healthy BMI range is between 18.5 and 24.9."
        )
        return {"status": "success", "report": report}
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error calculating BMI: {str(e)}"
        }


def calculate_calories_burned(activity: str, duration_min: int, weight_kg: float) -> Dict[str, Any]:
    """Calculate estimated calories burned for a specific activity.

    Args:
        activity (str): Type of activity (e.g., running, swimming, cycling)
        duration_min (int): Duration in minutes
        weight_kg (float): Weight in kilograms

    Returns:
        Dict[str, Any]: status and result or error message
    """
    # MET values (Metabolic Equivalent of Task) for different activities
    met_values = {
        "walking": 3.5,
        "jogging": 7.0,
        "running": 10.0,
        "cycling": 8.0,
        "swimming": 6.0,
        "weight lifting": 3.5,
        "yoga": 2.5,
        "hiit": 8.0,
        "dancing": 4.5,
        "hiking": 5.3,
    }
    
    activity = activity.lower()
    
    if activity not in met_values:
        return {
            "status": "error",
            "error_message": f"Activity '{activity}' is not supported. Supported activities are: {', '.join(met_values.keys())}"
        }
    
    try:
        # Calculate calories burned using MET formula
        # Calories = MET × weight (kg) × duration (hours)
        met = met_values[activity]
        duration_hours = duration_min / 60
        calories = met * weight_kg * duration_hours
        
        report = (
            f"For {duration_min} minutes of {activity}, a person weighing {weight_kg} kg "
            f"would burn approximately {calories:.0f} calories."
        )
        return {"status": "success", "report": report}
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error calculating calories burned: {str(e)}"
        }


def create_workout_plan(fitness_level: str, goal: str, days_per_week: int) -> Dict[str, Any]:
    """Create a personalized workout plan based on fitness level and goals.

    Args:
        fitness_level (str): Beginner, intermediate, or advanced
        goal (str): Weight loss, muscle gain, endurance, or general fitness
        days_per_week (int): Number of workout days per week (1-7)

    Returns:
        Dict[str, Any]: status and result or error message
    """
    if fitness_level.lower() not in ["beginner", "intermediate", "advanced"]:
        return {
            "status": "error",
            "error_message": "Fitness level must be beginner, intermediate, or advanced."
        }
    
    if goal.lower() not in ["weight loss", "muscle gain", "endurance", "general fitness"]:
        return {
            "status": "error",
            "error_message": "Goal must be weight loss, muscle gain, endurance, or general fitness."
        }
    
    if not 1 <= days_per_week <= 7:
        return {
            "status": "error",
            "error_message": "Days per week must be between 1 and 7."
        }
    
    fitness_level = fitness_level.lower()
    goal = goal.lower()
    
    # Generate workout plan based on inputs
    workout_plans = {
        "beginner": {
            "weight loss": {
                "focus": "Full body workouts with cardio emphasis",
                "schedule": "2-3 full body workouts, 2-3 cardio sessions"
            },
            "muscle gain": {
                "focus": "Full body resistance training",
                "schedule": "3 full body strength workouts, 1 active recovery day"
            },
            "endurance": {
                "focus": "Cardio progression",
                "schedule": "2-3 cardio sessions, 1-2 light strength workouts" 
            },
            "general fitness": {
                "focus": "Balanced approach to fitness fundamentals",
                "schedule": "2 strength workouts, 2 cardio sessions, 1 flexibility day"
            }
        },
        "intermediate": {
            "weight loss": {
                "focus": "HIIT and circuit training",
                "schedule": "2-3 HIIT sessions, 2 strength circuits, 1 steady-state cardio" 
            },
            "muscle gain": {
                "focus": "Upper/lower or push/pull/legs split",
                "schedule": "4-5 strength workouts following a split routine, 1 active recovery"
            },
            "endurance": {
                "focus": "Mixed cardio and endurance strength training",
                "schedule": "3-4 varied cardio sessions, 2 endurance-focused strength workouts"
            },
            "general fitness": {
                "focus": "Varied training methods",
                "schedule": "2-3 strength sessions, 2 cardio workouts, 1 flexibility/mobility day"
            }
        },
        "advanced": {
            "weight loss": {
                "focus": "Periodized training with caloric deficit",
                "schedule": "3-4 high-intensity workouts, 2 strength sessions, strategic cardio"
            },
            "muscle gain": {
                "focus": "Specialized split routine",
                "schedule": "5-6 targeted strength sessions following a specialized split"
            },
            "endurance": {
                "focus": "Periodized endurance program",
                "schedule": "4-5 structured cardio sessions, 2 complementary strength workouts"
            },
            "general fitness": {
                "focus": "Periodized approach to all fitness components",
                "schedule": "3 strength sessions, 2-3 varied cardio/HIIT, 1 recovery/flexibility"
            }
        }
    }
    
    plan = workout_plans[fitness_level][goal]
    
    # Adjust plan based on available days per week
    if days_per_week < 3:
        adjusted_schedule = "Focus on full-body workouts and combine cardio with strength when possible."
    elif days_per_week < 5:
        adjusted_schedule = plan["schedule"] + " (Combine some workouts to fit your schedule)"
    else:
        adjusted_schedule = plan["schedule"]
    
    report = (
        f"Workout Plan for {fitness_level.capitalize()} Level with {goal.capitalize()} Goal ({days_per_week} days/week):\n"
        f"• Focus: {plan['focus']}\n"
        f"• Recommended Schedule: {adjusted_schedule}\n\n"
        f"For best results, ensure proper nutrition and recovery between workouts."
    )
    
    return {"status": "success", "report": report}


def calculate_compound_interest(principal: float, annual_rate: float, years: int, contributions_per_year: float = 0.0, compound_frequency: str = "annually") -> Dict[str, Any]:
    """Calculate compound interest growth with optional regular contributions.

    Args:
        principal (float): Initial investment amount
        annual_rate (float): Annual interest rate (as percentage, e.g., 7 for 7%)
        years (int): Investment time horizon in years
        contributions_per_year (float, optional): Additional contributions per year. Defaults to 0.0.
        compound_frequency (str, optional): Compounding frequency (annually, quarterly, monthly, daily). Defaults to "annually".

    Returns:
        Dict[str, Any]: status and result or error message
    """
    frequencies = {
        "annually": 1,
        "semi-annually": 2,
        "quarterly": 4,
        "monthly": 12,
        "daily": 365
    }
    
    if compound_frequency.lower() not in frequencies:
        return {
            "status": "error",
            "error_message": f"Invalid compound frequency. Choose from: {', '.join(frequencies.keys())}"
        }
    
    try:
        # Get number of times compounded per year
        n = frequencies[compound_frequency.lower()]
        
        # Convert annual rate to decimal
        r = annual_rate / 100
        
        # Calculate contribution per period
        contribution_per_period = contributions_per_year / n
        
        # Calculate final amount using compound interest formula with regular contributions
        if contribution_per_period == 0:
            # Without additional contributions
            final_amount = principal * (1 + r/n)**(n*years)
        else:
            # With regular contributions (using Future Value of Annuity formula)
            # First calculate growth of principal
            principal_growth = principal * (1 + r/n)**(n*years)
            
            # Then calculate future value of periodic contributions
            contribution_growth = contribution_per_period * (((1 + r/n)**(n*years) - 1) / (r/n))
            
            final_amount = principal_growth + contribution_growth
        
        total_contributions = principal + (contributions_per_year * years)
        interest_earned = final_amount - total_contributions
        
        report = (
            f"Investment Growth Projection:\n"
            f"• Initial investment: ${principal:,.2f}\n"
            f"• Interest rate: {annual_rate}% (compounded {compound_frequency})\n"
            f"• Time period: {years} years\n"
            f"• Additional contributions: ${contributions_per_year:,.2f} per year\n\n"
            f"• Final balance: ${final_amount:,.2f}\n"
            f"• Total contributions: ${total_contributions:,.2f}\n"
            f"• Interest earned: ${interest_earned:,.2f}\n"
            f"• Growth multiple: {final_amount/principal:.2f}x"
        )
        
        return {"status": "success", "report": report}
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error calculating compound interest: {str(e)}"
        }


def analyze_investment_portfolio(allocation: Dict[str, float], risk_tolerance: str) -> Dict[str, Any]:
    """Analyze an investment portfolio allocation and provide feedback based on risk tolerance.

    Args:
        allocation (Dict[str, float]): Portfolio allocation as percentages (e.g., {"stocks": 60, "bonds": 30, "cash": 10})
        risk_tolerance (str): Low, moderate, or high risk tolerance

    Returns:
        Dict[str, Any]: status and result or error message
    """
    valid_asset_classes = ["stocks", "bonds", "cash", "real estate", "commodities", "cryptocurrency"]
    valid_risk_levels = ["low", "moderate", "high"]
    
    risk_tolerance = risk_tolerance.lower()
    if risk_tolerance not in valid_risk_levels:
        return {
            "status": "error",
            "error_message": f"Invalid risk tolerance. Choose from: {', '.join(valid_risk_levels)}"
        }
    
    # Validate asset classes
    for asset in allocation:
        if asset.lower() not in valid_asset_classes:
            return {
                "status": "error",
                "error_message": f"Invalid asset class '{asset}'. Valid classes are: {', '.join(valid_asset_classes)}"
            }
    
    # Check if allocation sums to approximately 100%
    total_allocation = sum(allocation.values())
    if not 99 <= total_allocation <= 101:
        return {
            "status": "error",
            "error_message": f"Portfolio allocation should sum to 100%. Current total: {total_allocation}%"
        }
    
    # Recommended allocations based on risk tolerance
    recommended_allocations = {
        "low": {
            "stocks": (20, 40),
            "bonds": (40, 60),
            "cash": (10, 25),
            "real estate": (0, 10),
            "commodities": (0, 5),
            "cryptocurrency": (0, 0)
        },
        "moderate": {
            "stocks": (40, 60),
            "bonds": (25, 40),
            "cash": (5, 15),
            "real estate": (5, 15),
            "commodities": (0, 10),
            "cryptocurrency": (0, 5)
        },
        "high": {
            "stocks": (60, 80),
            "bonds": (10, 30),
            "cash": (0, 10),
            "real estate": (5, 20),
            "commodities": (0, 15),
            "cryptocurrency": (0, 10)
        }
    }
    
    # Analyze current allocation compared to recommendations
    analysis = []
    for asset in valid_asset_classes:
        current = allocation.get(asset, 0)
        min_recommended, max_recommended = recommended_allocations[risk_tolerance].get(asset, (0, 0))
        
        if current < min_recommended:
            analysis.append(f"• {asset.capitalize()}: {current}% (Consider increasing to {min_recommended}-{max_recommended}%)")
        elif current > max_recommended:
            analysis.append(f"• {asset.capitalize()}: {current}% (Consider decreasing to {min_recommended}-{max_recommended}%)")
        else:
            analysis.append(f"• {asset.capitalize()}: {current}% (Within recommended range of {min_recommended}-{max_recommended}%)")
    
    # General portfolio observations
    observations = []
    stocks_percentage = allocation.get("stocks", 0)
    bonds_percentage = allocation.get("bonds", 0)
    cash_percentage = allocation.get("cash", 0)
    
    if risk_tolerance == "low" and stocks_percentage > 40:
        observations.append("Your stock allocation is high for your risk tolerance.")
    elif risk_tolerance == "high" and stocks_percentage < 50:
        observations.append("Your stock allocation is low for your risk tolerance.")
        
    if cash_percentage > 20:
        observations.append("High cash allocation may result in potential missed growth opportunities.")
    
    if bonds_percentage < 10 and risk_tolerance != "high":
        observations.append("Consider increasing bond allocation for better stability.")
    
    report = (
        f"Portfolio Analysis for {risk_tolerance.capitalize()} Risk Tolerance:\n\n"
        f"Current Allocation vs. Recommended Range:\n"
        f"{chr(10).join(analysis)}\n\n"
        f"Observations:\n"
        f"{chr(10).join(['• ' + obs for obs in observations]) if observations else '• Your allocation generally aligns with your risk tolerance.'}\n\n"
        f"Note: This is a simplified analysis. Consider consulting a financial advisor for personalized advice."
    )
    
    return {"status": "success", "report": report}


# Define the agents
fitness_agent = Agent(
    name="fitness_coach",
    model="gemini-1.5-pro",
    description=(
        "Agent to help with fitness tracking, workout planning, and health metrics calculation. "
        "Provides personalized advice based on user's fitness level and goals."
    ),
    instruction=(
        "I can calculate health metrics like BMI and calories burned, create personalized "
        "workout plans, and provide fitness advice based on your specific needs and goals."
    ),
    tools=[calculate_bmi, calculate_calories_burned, create_workout_plan],
)

wealth_agent = Agent(
    name="wealth_advisor",
    model="gemini-1.5-pro",
    description=(
        "Agent to help with financial planning, investment analysis, and wealth building strategies. "
        "Provides guidance on investment growth and portfolio management."
    ),
    instruction=(
        "I can help you project investment growth using compound interest calculations, "
        "analyze your investment portfolio allocation, and provide guidance on wealth building strategies."
    ),
    tools=[calculate_compound_interest, analyze_investment_portfolio],
)

# Create a root agent that combines both fitness and wealth tools
root_agent = Agent(
    name="wellness_advisor",
    model="gemini-1.5-pro",
    description=(
        "Agent to help with both physical and financial wellness. "
        "Provides guidance on fitness, health metrics, investment planning, and wealth building."
    ),
    instruction=(
        "I can help you with fitness tracking, workout planning, financial projections, "
        "and investment analysis to support both your physical and financial well-being."
    ),
    tools=[
        calculate_bmi, calculate_calories_burned, create_workout_plan,
        calculate_compound_interest, analyze_investment_portfolio
    ],
)