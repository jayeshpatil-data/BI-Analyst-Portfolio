import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Jayesh", "Rahul", "Sneha"],
    "Exp": [0, 1, 2, 4, 7],
    "Skills": [3, 5, 5, 3, 8]
}

df = pd.DataFrame(data)

def cal_sal(row):
    total = 6+ row["Exp"]*2.5 + row["Skills"]*1.2
    if total>18:
        total = 18+(total-18)*0.5
    return round(total,1)

df["package"] = df.apply(cal_sal, axis=1)

# DAY 4 KPI
avg_package = df["package"].mean()
max_package = df["package"].max()

def get_performance(pkg):
    if pkg >= 18:
        return "Top Talent"
    elif pkg >= 14:
        return "High"
    elif pkg >= 10:
        return "Medium"
    else:
        return "Low"

df["Performance"] = df["package"].apply(get_performance)

print(df)
print(f"\nAvg: {round(avg_package,1)} LPA, Max: {max_package} LPA")