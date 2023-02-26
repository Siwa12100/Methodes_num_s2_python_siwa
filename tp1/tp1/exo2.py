import matplotlib.pyplot as plt 
import numpy as np

def interm( t, A, B ) :
    C = ( 1 - t ) * A + t * B 
    return C

def bezier1( t, A, B) :
    C = ( 1 - t ) * A + t * B 
    return C

A = np.array( [ 0, 0 ] )
B = np.array( [ 6, 8 ] )
C = np.array( [ 10,0 ] ) 

plt.figure()
t = 1

F = []
E = []
D = []
#Z = []

T = np.linspace( 0, t, 90)
plt.axis('equal')

def bezier2( t, A, B, C ) :
    D = interm( t, A, B )
    E = interm( t, B, C )
    return bezier1( t, D, E )

#===========================================

# for i in T :
#     F.append( bezier1( i, A, B) )


# for i in T :
#     F.append( bezier1( i, B, C) )


# D = interm( t, A, B )
# E = interm( t, B, C )

# for i in T :
#     Z.append( bezier1( i, E, D) )


for i in T :
    F.append( bezier2( i, A, B, C ) )

F = np.array(F)
# D = np.array(D)
# E = np.array(E)
# Z = np.array(Z)

plt.plot( A[0], A[1], "g*")
# plt.plot( E[0], E[1], "g*")
# plt.plot( D[0], D[1], "g*")
plt.plot( B[0], B[1], "g*")
plt.plot( C[0], C[1], "g*")
plt.plot( F[:,0], F[:,1], "r.")
# plt.plot( Z[:,0], Z[:,1], "r.")
""" plt.show() """