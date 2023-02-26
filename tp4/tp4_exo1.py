import numpy as np
import matplotlib.pyplot as plt
import math


# Exercice 1 :
# ------------


# 1.) Formule explicite pour une courbe de Bézier d'ordre 2 : 

# C(t) = ( 1 - t )(( 1 - t )A + tB ) + t( ( 1 - t )B + tC )


# 2.)
# A = np.array( [ 0, 3 ] )
# B = np.array( [ 1, 1 ] )
# C = np.array( [ 2, 2 ] )


def formuleBezier2( t, A, B, C ) :
    return ( 1 - t )**2*A + 2*t*( 1 - t )*B + t**2*C


A,B,C = np.array([0,1]),np.array([3,3]),np.array([5,0]) # (par exemple)
allt = np.linspace(0,1,100) # toutes les valeurs de t testées

allFt = np.zeros((len(allt),2)) # va stocker le point F(t) en chaque valeur t testée

for i in range(len(allt)):
    allFt[i] = formuleBezier2(allt[i],A,B,C)
plt.figure()

P = np.array( [A, B, C ])
plt.plot( P[:,0], P[:,1] , 'k*')
plt.plot( allFt[:,0], allFt[:,1] , 'r')
plt.show()