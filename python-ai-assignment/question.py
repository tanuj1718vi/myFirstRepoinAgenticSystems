import pandas as pd

# Create dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Score": [90, 75, 88, 60, 95],
    "Passed": [True, True, True, False, True],
    "Category": ["A", "B", "A", "C", "A"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 1. Select single column
print("\nName column:")
print(df["Name"])

# 2. Select multiple columns
new_df = df[["Name", "Score"]]
print("\nName and Score columns:")
print(new_df)

# 3. First three rows using iloc
print("\nFirst 3 rows using iloc:")
print(df.iloc[:3])

# 4. Use loc after setting index
df2 = df.set_index("Name")
print("\nUsing loc with index:")
print(df2.loc["Alice"])

# 5. Filter Score > 85
print("\nScore > 85:")
print(df[df["Score"] > 85])

# 6. Filter Score > 85 and Passed True
print("\nScore > 85 and Passed True:")
print(df[(df["Score"] > 85) & (df["Passed"] == True)])

# 7. Sort by Score descending
sorted_df = df[df["Score"] > 85].sort_values(by="Score", ascending=False)
print("\nSorted by Score (Descending):")
print(sorted_df)

# 8. Chaining filter and sort
print("\nFilter and Sort together:")
print(df[(df["Score"] > 85) & (df["Passed"] == True)].sort_values(by="Score", ascending=False))