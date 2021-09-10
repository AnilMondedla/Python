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
def MyFun(p,q): 
    plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
    plt.plot(A[0], A[1], 'o') 
    plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
    plt.plot(B[0], B[1], 'o')
    plt.text(B[0] * (1 - 0.02), B[1] * (1) , 'B')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.legend(loc='best')
    plt.grid() # minor
    plt.plot(p,q,marker='o')
    plt.show()
    
x=0
y=(x/2)-2
b=y
y=0
x=(2*y)+4
a=x
A = np.array([a,0]) 
B = np.array([0,b]) 
x_AB = line_gen(A,B)

x,y=[int(x) for x in input("Enter the x and y  : example 4 0 :").split()]
if (x-2*y) == 4 :
	print('This is a solution')
	p=x
	q=y
	MyFun(p,q)
	
else :
    print('This is not a solution')
