import pandas as pd
import numpy as np

# 🔹 Step 1: Create DataFrame
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)


# 🔹 Step 2: Detect missing values
print("\nMissing values:\n", df.isnull().sum())


# 🔹 Step 3: Fill missing Salary with mean
mean_salary = df["Salary"].mean()
df["Salary"].fillna(mean_salary, inplace=True)


# 🔹 Step 4: Drop Temporary_Notes column
df.drop("Temporary_Notes", axis=1, inplace=True)


# 🔹 Step 5: Rename Salary → Annual_Salary
df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)


# 🔹 Step 6: Group by Department
summary = df.groupby("Department").agg({
    "Annual_Salary": ["mean", "count"]
})

print("\nFinal Summary Table:\n", summary)