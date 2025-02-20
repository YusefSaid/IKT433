import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Define the 5 clusters (based on your task)
clusters = {
    "a": [1, 2, 3, 4],
    "b": [5, 6, 7, 8],
    "c": [9, 10, 11, 12],
    "d": [13, 14, 15, 16],
    "e": [17, 18, 19, 20]
}

# Compute intra-cluster distances
total_distance = 0
cluster_distances = {}

for cluster_name, cluster in clusters.items():
    intra_cluster_sum = 0
    for i in range(len(cluster)):
        for j in range(i + 1, len(cluster)):
            city1 = cluster[i] - 1  # Convert to 0-based index
            city2 = cluster[j] - 1  # Convert to 0-based index
            intra_cluster_sum += distance_matrix[city1, city2]

    cluster_distances[cluster_name] = intra_cluster_sum
    total_distance += intra_cluster_sum


# Plot heatmap using Matplotlib and Seaborn
plt.figure(figsize=(10, 8))
ax = sns.heatmap(df_distance, annot=True, cmap="coolwarm", fmt="d", linewidths=0.5, cbar=True)

# Add cluster boundaries using rectangles
cluster_ranges = [0, 4, 8, 12, 16, 20]  # Define boundaries for clusters
for i in range(len(cluster_ranges) - 1):
    x_start, x_end = cluster_ranges[i], cluster_ranges[i+1]
    y_start, y_end = cluster_ranges[i], cluster_ranges[i+1]
    
    # Draw a rectangle around the cluster
    ax.add_patch(plt.Rectangle((x_start, y_start), x_end-x_start, y_end-y_start,
                               fill=False, edgecolor='black', lw=2))

# Adjust cluster labels above the heatmap (avoid overlap)
for i, cluster_name in enumerate(clusters.keys()):
    plt.text((cluster_ranges[i] + cluster_ranges[i+1]) / 2, -1, cluster_name.lower(),
             fontsize=16, fontweight="bold", color="black", ha='center')

# Set title with computed total intra-cluster distance
# Print total intra-cluster distance
plt.title(f"TSP Distance Matrix (Total Intra-Cluster Distance: {total_distance})", fontsize=14)
plt.xlabel("Cities", fontsize=12)
plt.ylabel("Cities", fontsize=12)

plt.show()

# Display computed total intra-cluster distance
total_distance
