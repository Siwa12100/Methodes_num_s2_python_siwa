import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import binom
from time import time

# Fonctions vues dans le différents TP : 
# --------------------------------------


# algorithme de Casteljau calculant F_P(t) pour UNE valeur de t
def CasteljauUnPoint(t,P):
    P = P.copy() # (nécessaire afin de ne pas écraser le P en dehors de la fonction )
    N = P.shape[0]-1
    for i in range(N):
        for j in range(N-i):
            P[j] = (1-t)*P[j] + t*P[j+1]
    return P[0]



# Calcul et traçage de F_P(t) en K valeurs différentes de t
def traceBezierCasteljau(P,K):
    allt = np.linspace(0,1,K)
    allFt = np.array( [CasteljauUnPoint(t,P) for t in allt] )
    plt.plot(allFt[:,0],allFt[:,1])




# Formule explicite calculant F_P(t) pour UNE valeur de t

def BezierFormuleUnPoint(t,P):
    N = P.shape[0]-1
    Ft = np.zeros(2)

    for i in range(N+1):
        Ft += binom(N,i) * t**i * (1-t)**(N-i) * P[i]
    return Ft




# Calcul et traçage de F_P(t) en K valeurs différentes de t
def traceBezierFormule(P,K):
    allt = np.linspace(0,1,K)
    allFt = np.array( [BezierFormuleUnPoint(t,P) for t in allt] )
    plt.plot(allFt[:,0],allFt[:,1])


#T=np.append(T,18)      # Ajoute l’élément 18 à la fin du tableau T.

# Exercice 2 : 
# ------------

debut = time()

P = np.array( [ 0, 0 ])


# A = np.array( [ 1, 1 ] )
# B = np.array( [ 2, 2 ] )
# C = np.array( [ 3, 3 ] )

#P = np.array( [ A, B, C ] )

# for i in range( N ) :
#     A = np.array( [ 2+i, 4+i ])
#     P.append(P, A)
N = 4
P = np.random.rand( N, 2 )

traceBezierCasteljau( P, 100 )

fin = time()
duree = fin-debut

print( " Duree : ", duree )
plt.show()