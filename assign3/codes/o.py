import sys  # for path to external scripts
sys.path.insert(0, '/home/jsr/Desktop/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# Local imports (assuming these scripts exist and are correct)
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

def read_data_from_file(filename):
    """Reads data from a file and returns it as a NumPy array."""
    data = np.loadtxt(filename, delimiter=',')
    return data

# Load data from file
filename = 'output.txt'
data = read_data_from_file(filename)

# Define points N and O
N = data[0]
M = data[1]
O = np.array([0, 0])  # O is the origin

# Calculate NO and MO vectors and their magnitudes
NO_vector = N - O
NO_magnitude = np.linalg.norm(NO_vector)
MO_vector = M - O
MO_magnitude = np.linalg.norm(MO_vector)

# Generate line between points N and O, and M and O
x_NO = line_gen(N.reshape(-1, 1), O.reshape(-1, 1))  # Ensure N and O are column vectors
x_MO = line_gen(M.reshape(-1, 1), O.reshape(-1, 1))

# Create figure and axis
fig, ax = plt.subplots()

# Plot dotted lines for NO and MO
ax.plot([O[0], N[0]], [O[1], N[1]], linestyle='--', color='green')
ax.plot([O[0], M[0]], [O[1], M[1]], linestyle='--', color='purple')

# Plot the arrows for NO and MO vectors
ax.quiver(O[0], O[1], NO_vector[0], NO_vector[1], angles='xy', scale_units='xy', 
          scale=NO_magnitude, color='green', label='Normal vector', width=0.005)

ax.quiver(O[0], O[1], MO_vector[0], MO_vector[1], angles='xy', scale_units='xy', 
          scale=MO_magnitude, color='purple', label='Direction vector', width=0.005)

# Identity matrix and standard basis vectors
I = np.eye(2)
e1 = I[:, [0]]
e2 = I[:, [1]]

# Line parameters (line in normal form)
n1 = np.array([2, 5]).reshape(-1, 1)  # Normal vector
c1 = 0

k1 = -4  # Lower bound
k2 = 5   # Upper bound

# Generate line with normal form
x_A = line_norm(n1, c1, k1, k2)

# Plot the generated line
ax.plot(x_A[0, :], x_A[1, :], label='$(2~~~~~5)\mathbf{x}=0,s=-0.4$')

# Customize the plot appearance
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Show grid, legend, and equal axis scaling
plt.legend(loc='best')
plt.grid()  # Display grid
plt.axis('equal')  # Equal scaling on both axes

# Show the plot
plt.show()
#plt.savefig('/home/jsr/Desktop/shrethan/assign3/fig/fig.png')


