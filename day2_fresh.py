
# Fresh Day 2 - Python for 18 LPA Data Scientist
import sys

print("=== Fresh Day 2 - Python Core ===")

# TASK 1: Function for Salary Logic (Interviewers love this)
def calculate_package(years_exp, skills_count):
    base = 6  # 6 LPA base
    exp_bonus = years_exp * 2.5
    skill_bonus = skills_count * 1.2
    total = base + exp_bonus + skill_bonus
    if total > 18:
        total = 18 + (total - 18) * 0.5  # cap logic
    return round(total, 1)

# Test it
for exp in range(0, 5):
    pkg = calculate_package(exp, 5)
    print(f"Exp {exp} years + 5 skills = {pkg} LPA")

# TASK 2: List & Dict - Real Data Handling
my_skills = ["Python", "SQL", "Pandas", "Azure", "Tableau"]
skill_levels = {"Python": 8, "SQL": 7, "Pandas": 6, "Azure": 5, "Tableau": 7}

print("\nMy Skill Stack:")
for skill in my_skills:
    print(f"- {skill}: Level {skill_levels[skill]}/10")

# TASK 3: Learning Loop Logic
target = 18
current = calculate_package(0, len(my_skills))
print(f"\nCurrent estimated: {current} LPA")
print(f"Target: {target} LPA")
print(f"Gap: {target - current} LPA -> Cover in next 118 days")

# TASK 4: Your Profile Dict
profile = {
    "name": "Jayesh",
    "goal": "18 LPA Data Scientist",
    "laptop": "MacBook Air M5",
    "days_left": 118,
    "status": "On Leave - Power Mode ON"
}
print(f"\nProfile: {profile}")

print("\n=== Day 2 Done -> Ready for Pandas ===")