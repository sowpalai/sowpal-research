# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Function to draw soil at a specified position
def draw_soil(ax, position=0):
    """Draw a rectangle representing soil at a specified position."""
    width = 1
    depth = 0.5
    length = 3
    soil_layer = np.array([
        [position, 0, 0],
        [position + width, 0, 0],
        [position + width, depth, 0],
        [position, depth, 0],
        [position, 0, length],
        [position + width, 0, length],
        [position + width, depth, length],
        [position, depth, length]
    ])
    faces = [
        [soil_layer[0], soil_layer[1], soil_layer[5], soil_layer[4]],
        [soil_layer[7], soil_layer[6], soil_layer[2], soil_layer[3]],
        [soil_layer[0], soil_layer[4], soil_layer[7], soil_layer[3]],
        [soil_layer[1], soil_layer[5], soil_layer[6], soil_layer[2]]
    ]
    for face in faces:
        ax.add_collection3d(Poly3DCollection([face], color='saddlebrown'))

# Function to map input to climatic condition
def climatic_condition(condition):
    """Map a given input to a climatic condition."""
    conditions = {
        1: 'Raining',
        2: 'Sunny Day',
        3: 'Night',
        4: 'Snow',
        5: 'Dew'
    }
    return conditions.get(condition, 'Unknown')

# Main function
def main():
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Render 5 different plots with 5 climatic conditions
    for i in range(5):
        real_time_data = np.random.randint(1, 6)  # Simulating real-time data
        condition = climatic_condition(real_time_data)
        draw_soil(ax, position=i*2)  # Draw soil with a gap
        ax.text(i*2 + 0.5, 0.5, 2, condition, color='red')  # Label the condition

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2)
    ax.set_zlim(0, 3)

    ax.set_xlabel('X - Different Plots')
    ax.set_ylabel('Y - Depth')
    ax.set_zlabel('Z - Height/Length')

    plt.show()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
