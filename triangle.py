#Drawing a triangle given 3 sides
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

x1,y1,x2,y2,x3,y3=[int(x) for x in input("Enter the triangle coordinates : example 1 0 6 0 4 3 :").split()]

#Triangle vertices
A = np.array([x1,y1]) 
B = np.array([x2,y2]) 
C = np.array([x3,y3])

M = np.array([[1,x1,y1], [1, x2, y2], [1,x3,y3]]) 
area = 1/2*np.abs(np.linalg.det(M))
print("Area of the triangle = ", area, "sq.units" )

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.02), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.003), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
