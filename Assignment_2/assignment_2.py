import numpy as np
import matplotlib.pyplot as plt
import math
from math import sin

#if using termux
import subprocess
import shlex
#end if

#Given
angA = 60
angB = 50
b=7


#To find angle P
angC = 180 - (angA + angB) 



#To find a
a = (math.sin(math.radians(angA))/math.sin(math.radians(angB)))*7


#To find coordinate of B(p,q)
p = (math.cos(math.radians(70)))*a
q = (math.sin(math.radians(70)))*a


#Triangle vertices
A= np.array([b,0])

B = np.array([p,q])
C = np.array([0,0])


#Generating lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_AC = line_gen(A,C)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 ), P[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1), Q[1 ] * (1+0.3) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), R[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
