import pandas as pd
import plotly.express as px

# Load dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# 1. View data
print("First 5 rows:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

# 2. Check info and missing values
print("\nDataset info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Observation:
# The dataset has no missing values.

# 3. Distribution of petal length
fig1 = px.histogram(df, x="petal_length", color="species",
                    title="Petal Length Distribution")
fig1.show()

# Observation:
# Setosa has smaller petal length than the other species.

# 4. Check outliers
fig2 = px.box(df, y="petal_length", color="species",
              title="Outliers in Petal Length")
fig2.show()

# Observation:
# There are no major outliers in petal length.

# 5. Relationship between variables
fig3 = px.scatter(df, x="petal_length", y="petal_width", color="species",
                  title="Petal Length vs Petal Width")
fig3.show()

# Insights about species:
# Setosa has very small petals.
# Virginica has the largest petal length and width.
# Versicolor lies between setosa and virginica.
# Petal length and petal width help separate species clearly.

print("\nEDA completed successfully.")