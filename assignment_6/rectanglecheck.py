import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


A =np.array([2,-2])
B =np.array([8,4])
C =np.array([5,7])
D =np.array([-1,1])

# method 1
E=np.linalg.norm(A-B)
F=np.linalg.norm(C-D)
G=np.linalg.norm(A-D)
H=np.linalg.norm(B-C)
I=np.linalg.norm(A-C)
J=np.linalg.norm(B-D)
if E==F:
	if G==H:
		if I==J:
			print("points A, B, C and D are the angular points of a rectangle")

#Generating all lines
x_AB = line_gen(A,B)
x_CD = line_gen(C,D)
x_BC = line_gen(B,C)
x_AD = line_gen(A,D)


plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.02), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.003), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
