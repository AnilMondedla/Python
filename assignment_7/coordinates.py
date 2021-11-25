import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
A = np.array([-6,8])
B=np.array([8,-6])

T1=(3*A+B)/4
T2=(A+B)/4
T3=(A+3*B)/4

x_AB = line_gen(A,B)
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 - 0.02) , 'A({}, {})'.format(A[0], A[1]))
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.04), B[1] * (1- 0.02) , 'B({}, {})'.format(B[0], B[1]))
plt.plot(T1[0], T1[1], 'o')
plt.text(T1[0] * (1 - 0.1), T1[1] , 'T1({}, {})'.format(round(T1[0],2),T1[1]))
plt.plot(T2[0], T2[1], 'o')
plt.text(T2[0] * (1- 0.1), T2[1], 'T2({}, {})'.format(round(T2[0],2),T2[1]))
plt.plot(T3[0], T3[1], 'o')
plt.text(T3[0] * (1- 0.1), T3[1], 'T3({}, {})'.format(round(T3[0],2),T3[1]))
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
# plt.axis('equal')

plt.show()
