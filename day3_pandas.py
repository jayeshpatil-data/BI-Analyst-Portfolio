import pandas as pd

# Create a mini dataset - like real company data
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
df["package"]= df.apply(cal_sal, axis =1)


print(df)
print("\n Your Row: ")
print(df[df["Name"]=="Jayesh"])