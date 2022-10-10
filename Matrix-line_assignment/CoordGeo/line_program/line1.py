#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math

import sys                                          #for path to external scripts
sys.path.insert(0,'/home/krishna/Krishna/python/codes/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters
A1 = np.array(([2,5]))
A2=np.array(([1,3.466]))
A3=np.array(([1,5.21]))
o=np.array(([5.663,1.37]))
o1=np.array(([0.34,6.65]))
P=np.array(([2,3]))
n1=np.array(([1,-1]))
n2=np.array(([2.21,-1]))
n3=np.array(([1,-2.21]))
#n1 = A[0,:]
#n2 = A[1,:]
#c1 = b[0]
#c2 = b[1]


#Solution vector
#x = LA.solve(A,b)



#Generating all lines
k1 = -10
k2 = 7
AB = line_dir_pt(n1,A1,k1,k2)
CD = line_dir_pt(n2,A2,k1,k2)
EF = line_dir_pt(n3,A3,k1,k2)

#intersection of two lines


#o = line_intersect(n2,A1,n1,A2)
#o1=line_intersect(n3,A3,n1,A1)
v1=o-P
N1=np.linalg.norm(v1)
print(math.trunc(N1))
v2=o1-P
N2=np.linalg.norm(v2)
print(math.trunc(N2))


#Plotting all lines
plt.plot(AB[0,:],AB[1,:],label='$line1$')
plt.plot(CD[0,:],CD[1,:],label='$line2$')
plt.plot(EF[0,:],EF[1,:],label='$line3$')
#Labeling the coordinates
tri_coords = np.vstack((P,o,o1)).T
#tri_coords = P.T
#plt.scatter(tri_coords[0,:])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','o','o1']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,3), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/home/krishna/Krishna/python/figs/line1.pdf')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-7.pdf"))
#else
plt.show()

