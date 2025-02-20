import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # For better visualization

# Set random seed for reproducibility
np.random.seed(42)

# Number of cities
num_cities = 20

# Generate a symmetric distance matrix with values between 1 and 5
distance_matrix = np.random.randint(1, 6, size=(num_cities, num_cities))

# Set diagonal elements to 0 (distance from a city to itself)
np.fill_diagonal(distance_matrix, 0)

# Ensure symmetry
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        distance_matrix[j, i] = distance_matrix[i, j]

# Convert to a DataFrame for better visualization
df_distance = pd.DataFrame(distance_matrix, index=[f"{i+1}" for i in range(num_cities)], 
                           columns=[f"{i+1}" for i in range(num_cities)])




# Plot heatmap using Matplotlib and Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(df_distance, annot=True, cmap="coolwarm", fmt="d", linewidths=0.5)
plt.title("TSP Distance Matrix")
plt.xlabel("Cities")
plt.ylabel("Cities")
plt.show()
