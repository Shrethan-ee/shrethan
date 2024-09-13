import matplotlib.pyplot as plt

# Example: Simulating the output reading from a file
output_file_path = 'output.txt'

# Reading the ratio from the file
with open("output.txt", 'r') as file:
    output = file.read()

# Parsing the ratio from the output
# Example: "The ratio in which P divides AB is 2:3."
import re
match = re.search(r'The ratio in which P divides AB is (\d+):(\d+)\.', output)
if match:
    m = int(match.group(1))
    n = int(match.group(2))

# Coordinates of points A, B, and P
x2, y2 = 2, 3  # Point A
x3, y3 = 7, 8  # Point B
x1, y1 = 4, 5  # Point P

# Plotting the points and the line segment
plt.plot([x2, x3], [y2, y3], 'bo-', label='Line segment AB')
plt.plot(x1, y1, 'ro', label=f'Point P (Ratio = {m}:{n})')

# Annotating the points
plt.text(x2, y2, '  A(2,3)', verticalalignment='bottom', horizontalalignment='right')
plt.text(x3, y3, '  B(7,8)', verticalalignment='top', horizontalalignment='left')
plt.text(x1, y1, f'  P(4,5)', verticalalignment='top', horizontalalignment='right')

# Setting up the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Division of Line Segment AB by Point P')
plt.grid(True)
plt.legend()
plt.axis('equal')

# Show plot
plt.savefig('fig.png')
plt.show()
