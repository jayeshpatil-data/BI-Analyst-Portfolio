import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit","Priya","Jayesh","Rahul","Sneha"],
    "Exp": [0,1,2,4,7],
    "Skills": [3,5,5,3,8],
    "package": [9.6,14.5,17.0,18.8,25.6]
})

Top_Talent = df[df["package"]>=18]

avg_package = df["package"].mean()

print(Top_Talent)
print(f"{avg_package:.1f}")
print(f"\nAvg: {avg_package:.1f} LPA")