# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define points for the cube
points = np.array([
    [-1, -1, -1],
    [-1, -1, 1],
    [-1, 1, -1],
    [-1, 1, 1],
    [1, -1, -1],
    [1, -1, 1],
    [1, 1, -1],
    [1, 1, 1]
])

# Define edges of the cube
edges = [
    [0, 1], [1, 3], [3, 2], [2, 0],
    [4, 5], [5, 7], [7, 6], [6, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

# Plot the edges of the cube
for edge in edges:
    ax.plot3D(*zip(*points[edge]), color="b")

# Create and scatter points for different soil layers
# Horizon B (Subsoil)
middle_layer_z = np.random.uniform(0, 1/3, 30000)
middle_layer_x = np.random.uniform(-1, 1, 30000)
middle_layer_y = np.random.uniform(-1, 1, 30000)
ax.scatter(middle_layer_x, middle_layer_y, middle_layer_z, c='burlywood', label='Horizon B (Subsoil)')

# Horizon A (Top soil)
top_layer_z = np.random.uniform(1/3, 1, 10000)
top_layer_x = np.random.uniform(-1, 1, 10000)
top_layer_y = np.random.uniform(-1, 1, 10000)
ax.scatter(top_layer_x, top_layer_y, top_layer_z, c='saddlebrown', label='Horizon A (Top soil)')

# Horizon C (Parent Material)
bottom_layer_z = np.random.uniform(-1, 1, 3000)
bottom_layer_x = np.random.uniform(-1, 1, 3000)
bottom_layer_y = np.random.uniform(-1, 1, 3000)
ax.scatter(bottom_layer_x, bottom_layer_y, bottom_layer_z, c='grey', label='Horizon C (Parent Material)')

# Set axis labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.show()
