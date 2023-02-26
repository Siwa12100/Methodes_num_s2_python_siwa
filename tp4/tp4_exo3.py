import numpy as np
import matplotlib.pyplot as plt
import math


# Exercice 3 :
# ------------


def binom( N, k ) :
    a = 1
    for i in range(k) :
        a = a * ( N - i ) / ( k - i )
    return a 


def formuleBezierGenerale( t, P ) :
    Ft = np.zeros(2)

    N = len(P) - 1
    for k in range ( N + 1 ) :
        
        Ft = Ft + binom( N,k ) * t**k *( 1 - t ) ** ( N - k ) * P[k]

    return Ft
    
# A,B,C = np.array([0,1]),np.array([3,3]),np.array([5,0]) # (par exemple)
# allt = np.linspace(0,1,100) # toutes les valeurs de t testées

# P = np.array( [A, B, C ])

# allFt = np.zeros((len(allt),2)) # va stocker le point F(t) en chaque valeur t testée

# for i in range(len(allt)):
#     allFt[i] = formuleBezierGenerale(allt[i],P)
# plt.figure()

# plt.plot( P[:,0], P[:,1] , 'k*')
# plt.plot( allFt[:,0], allFt[:,1] , 'r')
# plt.show()  


A,B,C,D = np.array([0,1]),np.array([3,3]),np.array([5,0]), np.array([4,5]) # (par exemple)
allt = np.linspace(0,1,100) # toutes les valeurs de t testées
P = np.array( [A, B, C, D ])
allFt = np.zeros((len(allt),2)) # va stocker le point F(t) en chaque valeur t testée

for i in range(len(allt)):
    allFt[i] = formuleBezierGenerale(allt[i],P)
plt.figure()


plt.plot( P[:,0], P[:,1] , 'k*')
plt.plot( allFt[:,0], allFt[:,1] , 'r')
plt.show()

