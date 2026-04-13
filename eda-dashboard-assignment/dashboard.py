import streamlit as st
import matplotlib.pyplot as plt
from fetch_data import get_clean_data

st.title("Simple Data Dashboard")

# Load data
df = get_clean_data()

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Exploratory analysis
posts_per_user = df.groupby("user_id").size()

# Observation:
# This shows how many posts each user created.

# Bar chart
st.subheader("Posts per User")
fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.bar(posts_per_user.index, posts_per_user.values)
ax1.set_title("Number of Posts per User")
ax1.set_xlabel("User ID")
ax1.set_ylabel("Post Count")
st.pyplot(fig1)

# Observation:
# The bar chart compares post counts for each user.

# Histogram
st.subheader("Post Length Distribution")
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.hist(df["post_length"], edgecolor="black")
ax2.set_title("Distribution of Post Length")
ax2.set_xlabel("Post Length")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

# Observation:
# The histogram shows how post lengths are distributed.