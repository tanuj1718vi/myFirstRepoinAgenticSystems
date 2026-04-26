import numpy as np
import matplotlib.pyplot as plt

# Create epochs list from 1 to 10
epochs = list(range(1, 11))

# Generate synthetic training loss values using NumPy
np.random.seed(42)
loss = np.linspace(1.0, 0.2, 10) + np.random.uniform(-0.05, 0.05, 10)

# Model accuracy data
models = ["Model A", "Model B", "Model C"]
accuracy = [0.85, 0.90, 0.88]

# 1. Line Plot: Loss vs Epoch
plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker='o')
plt.title("Training Loss vs Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 2. Scatter Plot: Epoch vs Loss
plt.figure(figsize=(8, 5))
plt.scatter(epochs, loss)
plt.title("Scatter Plot of Epoch vs Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 3. Bar Chart: Model Accuracy Comparison
plt.figure(figsize=(8, 5))
plt.bar(models, accuracy)
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.grid(axis='y')
plt.show()