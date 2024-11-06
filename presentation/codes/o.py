import sys  # for path to external scripts
sys.path.insert(0, '/home/jsr/Desktop/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import matplotlib.pyplot as plt

# Local imports (assuming these scripts exist and are correct)
from line.funcs import *
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

# Labeling the coordinates
tri_coords = np.block([[A, B, P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # Point to label
                 textcoords="offset points", # Position of text
                 xytext=(20,-10), # Offset from point
                 ha='center') # Horizontal alignment

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

