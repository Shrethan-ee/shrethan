import matplotlib.pyplot as plt
import numpy as np

output_file_path = 'output.txt'

with open("output.txt", 'r') as file:
    output = file.read()

import re
match = re.search(r'(\d+):(\d+)\.', output)
if match:
    m1 = int(match.group(1))
    m2 = int(match.group(2))
#Given points
A = np.array(([2,3])).reshape(-1,1)
B = np.array(([7,8])).reshape(-1,1)

n=m2/m1

#Point
P= (B+n*A)/(1+n) # calculating the coordinate points of R which divides the join between the two points
#print(R)

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
  
  #Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$',color='blue')

#Labeling the coordinates
tri_coords = np.block([[A,B,P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:],color='red')

vert_labels = ['A','B','P']
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,-10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
                 
# use set_position
ax = plt.gca()
#ax.spines['top'].set_color('red')
#ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
ax.spines['bottom'].set_visible(True)
plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(['ratio=2:3'],loc="upper left")
plt.grid() # minor
plt.axis('equal')


plt.savefig('fig.png')
plt.show()
