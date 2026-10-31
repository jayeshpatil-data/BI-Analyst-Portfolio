import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Jayesh", "Rahul", "Sneha"],
    "Exp": [0, 1, 2, 4, 7],
    "Skills": [3, 5, 5, 3, 8]
}

df = pd.DataFrame(data)

def cal_sal(row):
    exp = row["Exp"]
    skill = row["Skills"]
    total = 6 + exp*2.5 + skill*1.2
    if total > 18:
        total = 18 + (total - 18) * 0.5
    return round(total, 1)

df["package"] = df.apply(cal_sal, axis=1)

print(df)
print(f"\nAvg Package: {df['package'].mean():.1f} LPA")
print(f"Your Row (Jayesh): {df.iloc[2]['package']} LPA")