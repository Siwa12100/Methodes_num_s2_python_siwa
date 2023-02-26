import numpy as np
import matplotlib.pyplot as plt
C


# =-=-=-=-=- Exercice 1 =-=-=-=-=-=-=

# Question 1 :
# ------------

a0 = np.array( [ -1, 3 ] )
a1 = np.array( [ 2, 6 ] )
a2 = np.array( [ 7, 8 ] )
a3 = np.array( [ 4, 1 ] )

P = np.array([ a0, a1, a2, a3 ])
# P[0, 0] correspond à la première valeur du premier point.
# P[0, :] correspond à toutes les valeurs de la première ligne.
assert isinstance( P, np.ndarray ) and P.shape == ( 4,2 ), " P n'a pas le bon format ! "





# Question 2 :
# ------------

def valeur( tab, lig, col ) :
    return tab[ lig, col ]

nombre = valeur( P, 2, 0 )
#print(nombre)
assert nombre == 7, " Pas la bonne valeur !"




# Question 3 :
# ------------

def valeur2( tab, a ) :
    return tab[ a, : ]

P1 = valeur2(P, 1)
#print(P1)
assert np.array_equal(P1, np.array([2,6])), " mauvais format pour  P1 ! "





# Question 4 :
# ------------

taille = len(P)
Psaufdernier = P[ 0 : taille - 1 ,: ]
#print( Psaufdernier )
assert Psaufdernier.shape == (3,2), " taille (N,2) attendue pour Psaufdernier ! "





# Question 5 :
# ------------

P_x = P[:,0]
#print(P_x)





# Question 6 :
# ------------

plt.figure()
plt.plot(P[ : , 0 ] , P[ : , 1 ])
#plt.show()




# =-=-=-=-=-= Exercice 2 =-=-=-=-=-=-=

def bezier1( t, A, B) :
    C = ( 1 - t ) * A + t * B 
    return C

# Question 1 :
# ------------
t = 0.5

# p0 = np.array([])
# p1 = np.array([])

# A = bezier1( t, p0, p1 )

plt.figure()
plt.plot(A)
plt.show()



def CasteljauEtape(t,P) :
    nv_P = [len(P) - 1 ]
    for e in range(len(P) - 1 ) :
        nv_P[e] = bezier1(t, P[e, 0], P[e, 1])
    
    return nv_P



def bezierCasteljau(t,P) :
    nv_P_bis = len(nv_P)
    for e in range (t) :
        nv_P_bis[e] = CasteljauEtape( t, P[e, 0], P[e, 1] )







