import pandas as pd

# Step 1: Create sample data and save as CSV
data = {
    "Age": [18, 19, 20, 21, 22, 23, 24],
    "Score": [75, 88, 90, 65, 82, 95, 70],
    "Label": ["Pass", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("CSV file created\n")

# Step 2: Load dataset
df = pd.read_csv("data.csv")
print("Dataset Loaded\n")

# First 5 rows
print("First 5 rows:")
print(df.head())

# Last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Structure information
print("\nDataset Info:")
df.info()

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Select single column
score = df["Score"]
print("\nSingle Column (Score):")
print(score)

# Select multiple columns
subset = df[["Age", "Score"]]
print("\nMultiple Columns (Age and Score):")
print(subset)

# Filter rows
filtered = df[df["Score"] > 80]
print("\nFiltered Rows (Score > 80):")
print(filtered)