import pandas as pd
import matplotlib.pyplot as plt

# Same data from Day 3 - so chart matches your 17.1 LPA
data = {
    "Name": ["Amit", "Priya", "Jayesh", "Rahul", "Sneha"],
    "Exp": [0, 1, 2, 4, 7],
    "Skills": [3, 5, 5, 3, 8]
}
df = pd.DataFrame(data)

def cal_sal(row):
    total = 6 + row["Exp"]*2.5 + row["Skills"]*1.2
    if total > 18:
        total = 18 + (total - 18) * 0.5
    return round(total, 1)

df["package"] = df.apply(cal_sal, axis=1)

# --- Day 5 CHART ---
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["package"], color=['#9E9E9E', '#64B5F6', '#1E88E5', '#FFB74D', '#66BB6A'])
plt.axhline(y=18, color='red', linestyle='--', label='18 LPA Target')
plt.axhline(y=df["package"].mean(), color='green', linestyle='-', label=f'Avg {df["package"].mean():.1f} LPA')
plt.title("Project M5 - Salary Analysis (Avg 17.1 LPA)")
plt.ylabel("Package (LPA)")
plt.legend()
plt.tight_layout()
plt.savefig("day5_package_chart.png")
print("Chart saved as day5_package_chart.png")
print(df)
print(f"\nAvg: {df['package'].mean():.1f} LPA - 0.9 LPA to 18 LPA")