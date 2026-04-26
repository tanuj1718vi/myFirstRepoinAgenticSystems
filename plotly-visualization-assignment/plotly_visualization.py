import pandas as pd
import plotly.express as px

# Create dataset
data = {
    "Epoch": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Training Loss": [0.95, 0.82, 0.70, 0.58, 0.50, 0.45, 0.43, 0.42, 0.42, 0.41]
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Create interactive line chart
fig = px.line(
    df,
    x="Epoch",
    y="Training Loss",
    title="Training Loss Over Epochs",
    markers=True,
    labels={"Epoch": "Epoch", "Training Loss": "Loss"}
)

# Add annotation where loss stabilizes
fig.add_annotation(
    x=8,
    y=0.42,
    text="Loss starts stabilizing here",
    showarrow=True,
    arrowhead=2
)

# Display chart
fig.show()