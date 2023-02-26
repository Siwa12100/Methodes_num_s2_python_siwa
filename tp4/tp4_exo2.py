import numpy as np
import matplotlib.pyplot as plt
import math

# Exercice 2 :
# ------------

# F(t) = ( 1 - t )*( ( 1 - t )**2*A + 2*t*( 1 - t )*B + t**2*C ) + t*( ( 1 - t )**2*B + 2*t*( 1 - t )*C + t**2*D )




def formuleBezier3( t, A, B, C, D ) :
    return ( 1 - t )*( ( 1 - t )**2*A + 2*t*( 1 - t )*B + t**2*C ) + t*( ( 1 - t )**2*B + 2*t*( 1 - t )*C + t**2*D )


A,B,C,D = np.array([0,1]),np.array([3,3]),np.array([5,0]), np.array([4,5]) # (par exemple)
allt = np.linspace(0,1,100) # toutes les valeurs de t testées

allFt = np.zeros((len(allt),2)) # va stocker le point F(t) en chaque valeur t testée

for i in range(len(allt)):
    allFt[i] = formuleBezier3(allt[i],A,B,C,D)
plt.figure()

P = np.array( [A, B, C, D ])
plt.plot( P[:,0], P[:,1] , 'k*')
plt.plot( allFt[:,0], allFt[:,1] , 'r')
plt.show()