import matplotlib.pyplot as plt 
import numpy as np


def bezier1( t, A, B) :
    C = ( 1 - t ) * A + t * B 
    return C


A = np.array( [ -1, 3] )
B = np.array( [ 4, 2 ] )


plt.figure()
t = 1

F = []

T = np.linspace( 0, t, 200)
#plt.axis('equal')

for i in T :
    F.append( bezier1( i, A, B) )

F = np.array(F)
plt.plot( A[0], A[1], "g*")
plt.plot( B[0], B[1], "g*")
plt.plot( F[:,0], F[:,1], "r.")
plt.show()






