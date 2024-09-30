import matplotlib.pyplot as plt
import numpy as np

# Function to read the vectors from output.txt
def read_vectors(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Extract the normal vector
        normal_line = lines[0].strip().split("<")[1].split(">")[0].split(", ")
        normal_vector = [int(normal_line[0]), int(normal_line[1])]
        # Extract the direction vector
        direction_line = lines[1].strip().split("<")[1].split(">")[0].split(", ")
        direction_vector = [int(direction_line[0]), int(direction_line[1])]
    return normal_vector, direction_vector

# Function to plot the line and vectors
def plot_line_and_vectors(normal_vector, direction_vector):
    # Define the line equation 2x + 5y = 0
    def line_equation(x):
        return -(2/5) * x

    # Create a range of x values
    x_vals = np.linspace(-10, 10, 400)
    y_vals = line_equation(x_vals)

    # Create a plot
    plt.figure(figsize=(8, 8))
    
    # Plot the line
    plt.plot(x_vals, y_vals, 'b', label="Line: 2x + 5y = 0")
    
    # Plot the normal vector from the origin
    plt.quiver(0, 0, normal_vector[0], normal_vector[1], angles='xy', scale_units='xy', scale=1, color='r', label='Normal Vector')
    
    # Plot the direction vector from the origin
    plt.quiver(0, 0, direction_vector[0], direction_vector[1], angles='xy', scale_units='xy', scale=1, color='g', label='Direction Vector')
    
    # Set plot limits
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    
    # Add labels and grid
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line and Vectors Plot')
    
    # Show legend
    plt.legend()

    # Display the plot
    plt.show()
    

# Read vectors from the file
normal_vec, direction_vec = read_vectors("output.txt")

# Plot the line and vectors
plot_line_and_vectors(normal_vec, direction_vec)
plt.savefig('fig.png')
