#Code by GVV Sharma
#November 12, 2019
#released under GNU GPL
import matplotlib.pyplot as plt
import numpy as np
from coeffs import *
import math
#if using termux
import subprocess
import shlex
#end if


A=[5,-2]
B=[6,4]
C=[7,-2]
AB=math.sqrt(((6-5)**2) + ((4+2)**2))
BC=math.sqrt(((7-6)**2) + ((-2-4)**2))
CA=math.sqrt(((5-7)**2) + ((-2+2)**2))

if AB == BC :
	print("isosceles triangle")
elif BC==CA :
	print("isosceles triangle")
elif CA==AB :
	print("isosceles triangle")
else :
	print("not isosceles triangle")
	
	
A = np.array([5,-2]) 
B = np.array([7,-2]) 
C = np.array([6,4]) 
	
#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)


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
plt.show()
