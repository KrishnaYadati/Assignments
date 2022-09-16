
#Code by GVV Sharma (works on termux)
#February 16, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To verify basic proportionality theorem


#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/home/krishna/Krishna/Assignments/Matrix-lineassignment/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters
k = 1
c = 8
a = 12
p2 =4
theta = np.pi/3
A = c*np.array(([np.cos(theta),np.sin(theta)]))
C = np.array(([0,0]))
e1 = np.array(([1,0]))
e2 = np.array(([0,1]))
P =(p2*e1)+A
R = (a*e1)
B = (k*A+C)/(k+1)
Q = (k*P+R)/(k+1)

v1=A-C
v2=A-Q
ar_t1=0.5*np.linalg.norm((np.cross(v1,v2)))

v3=R-P
v4=R-B
ar_t2=0.5*np.linalg.norm((np.cross(v3,v4)))

print("Ar(AQC)=",ar_t1)
print("Ar(PBR)=",ar_t2)


##Generating all lines
x_AC = line_gen(A,C)
x_CR = line_gen(C,R)
x_RP = line_gen(R,P)
x_PA = line_gen(P,A)
x_BQ = line_gen(B,Q)
x_PB = line_gen(P,B)
x_BR = line_gen(B,R)
x_AQ = line_gen(A,Q)
x_QC = line_gen(Q,C)


#Plotting all lines
plt.plot(x_AC[0,:],x_AC[1,:])#,label='$Diameter$')
plt.plot(x_CR[0,:],x_CR[1,:])#,label='$Diameter$')
plt.plot(x_RP[0,:],x_RP[1,:])#,label='$Diameter$')
plt.plot(x_PA[0,:],x_PA[1,:])#,label='$Diameter$')
plt.plot(x_BQ[0,:],x_BQ[1,:])#,label='$Diameter$')
plt.plot(x_PB[0,:],x_PB[1,:])#,label='$Diameter$')
plt.plot(x_BR[0,:],x_BR[1,:])#,label='$Diameter$')
plt.plot(x_AQ[0,:],x_AQ[1,:])#,label='$Diameter$')
plt.plot(x_QC[0,:],x_QC[1,:])#,label='$Diameter$')


#Labeling the coordinates
tri_coords = np.vstack((A,B,C,P,Q,R)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','P','Q','R']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/home/krishna/Krishna/python/figs/matrix-10-10.pdf')
#subprocess.run(shlex.split("termux-open /home/krishna/Krishna/pytho/figs/matrix-10-10.pdf"))
#else
#plt.show()
