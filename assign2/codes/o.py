import matplotlib.pyplot as plt

output_file_path = 'output.txt'

with open("output.txt", 'r') as file:
    output = file.read()

import re
match = re.search(r'(\d+):(\d+)\.', output)
if match:
    m = int(match.group(1))
    n = int(match.group(2))

x2, y2 = 2, 3  
x3, y3 = 7, 8  
x1, y1 = 4, 5  

plt.plot([x2, x3], [y2, y3], 'bo-', label='Line segment AB')
plt.plot(x1, y1, 'ro', label=f'Point P (Ratio = {m}:{n})')

plt.text(x2, y2, '  A(2,3)', verticalalignment='bottom', horizontalalignment='right')
plt.text(x3, y3, '  B(7,8)', verticalalignment='top', horizontalalignment='left')
plt.text(x1, y1, f'  P(4,5)', verticalalignment='top', horizontalalignment='right')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Division of Line Segment AB by Point P')
plt.grid(True)
plt.legend()
plt.axis('equal')

plt.savefig('fig.png')
plt.show()
