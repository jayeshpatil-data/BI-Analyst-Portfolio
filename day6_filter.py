import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit","Priya","Jayesh","Rahul","Sneha"],
    "Exp": [0,1,2,4,7],
    "Skills": [3,5,5,3,8],
    "package": [9.6,14.5,17.0,18.8,25.6]
})

# Who crossed 18 LPA?
top_talent = df[df["package"] >= 18]

print("All Data:")
print(df)
print("\n--- Top Talent >= 18 LPA ---")
print(top_talent)

avg_package = df["package"].mean()
your_gap = 18 - 17.0
print(f"\nAvg: {avg_package:.1f} LPA")
print(f"Your package: 17.0 LPA")
print(f"Gap to 18: {your_gap:.1f} LPA")
print(f"\nInsight: To cross 18, you need Exp >=4 OR Skills >=8")