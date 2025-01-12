import sys  # for path to external scripts
sys.path.insert(0, '/home/jsr/Desktop/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import matplotlib.pyplot as plt

# Local imports (assuming these scripts exist and are correct)
from line.funcs import line_gen
from triangle.funcs import *
from conics.funcs import circ_gen

def read_ratio_from_file(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()  # Read the first line and remove any whitespace
        a_str, b_str = line.split(':')  # Split the line by ':'
        a, b = int(a_str), int(b_str)   # Convert each part to an integer
    return a / b  # Calculate the ratio as b/a

# Load ratio from file
filename = 'output.txt'
n = read_ratio_from_file(filename)

# Given points
A = np.array(([2,3])).reshape(-1,1)
B = np.array(([7,8])).reshape(-1,1)

# Point
P = (A + n * B) / (1 + n)  # calculating the coordinate points of P

# Generating line AB
x_AB = line_gen(A, B)

# Plotting line AB
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')

# Scatter plot of points A, B, and P
plt.scatter([A[0, 0], B[0, 0], P[0, 0]], [A[1, 0], B[1, 0], P[1, 0]])

# Manually label points A, B, and P without a loop
plt.annotate('A\n(2, 3)', (A[0, 0], A[1, 0]), textcoords="offset points", xytext=(20, -10), ha='center')
plt.annotate('B\n(7, 8)', (B[0, 0], B[1, 0]), textcoords="offset points", xytext=(20, -10), ha='center')
plt.annotate(f'P\n({P[0, 0]:.1f}, {P[1, 0]:.1f})', (P[0, 0], P[1, 0]), textcoords="offset points", xytext=(20, -10), ha='center')

# Modify axes visibility
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

# Save and display plot
plt.savefig('/home/jsr/Desktop/shrethan/presentation/fig/fig.png')
plt.show()

