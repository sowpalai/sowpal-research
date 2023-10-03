# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Function to draw the soil layer
def draw_soil_layer(ax, width=30, depth=0.05):
    # Define soil layer dimensions (length is assumed to be 30 for 30 days)
    length = 0.05
    soil_layer = np.array([
        [0, 0, 0],
        [width, 0, 0],
        [width, depth, 0],
        [0, depth, 0],
        [0, 0, length],
        [width, 0, length],
        [width, depth, length],
        [0, depth, length]
    ])
    
    # Create the sides of the soil layer (rectangle)
    faces = [
        [soil_layer[0], soil_layer[1], soil_layer[5], soil_layer[4]],
        [soil_layer[7], soil_layer[6], soil_layer[2], soil_layer[3]],
        [soil_layer[0], soil_layer[4], soil_layer[7], soil_layer[3]],
        [soil_layer[1], soil_layer[5], soil_layer[6], soil_layer[2]],
        [soil_layer[4], soil_layer[5], soil_layer[6], soil_layer[7]],
        [soil_layer[0], soil_layer[1], soil_layer[2], soil_layer[3]]
    ]

    for face in faces:
        ax.add_collection3d(Poly3DCollection([face], color='saddlebrown'))

# Function to draw a single maize plant at a given position and height
def draw_single_maize(ax, x_position, height):
    ax.plot([x_position, x_position], [0, height], [0, 0], color='green')

# Function to visualize maize growth over a specified number of days
def draw_maize_growth(ax, days=30):
    # Assuming a simple linear growth for maize over the 30 days
    # This is just a representation and may not be accurate
    growth_rate = 0.2  # Adjust this value as needed
    for day in range(1, days + 1):
        height = day * growth_rate
        draw_single_maize(ax, day, height)  # Adjust the x and y values as needed

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Draw the soil layer and maize growth
draw_soil_layer(ax)
draw_maize_growth(ax)

# Set axis labels
ax.set_xlabel('Days')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Height')

# Set axis limits
ax.set_xlim(0, 31)
ax.set_ylim(0, 2)
ax.set_zlim(0, 6)

# Display the plot
plt.show()
 
