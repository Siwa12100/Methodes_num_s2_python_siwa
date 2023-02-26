
import numpy as np
import matplotlib.pyplot as plt
import math


#################################################################################################
###
### EXERCICE 2 : Définir une nouvelle police de caractères sous Python
###
#################################################################################################


# On active le "mode interactif" de pyplot. Ainsi, les plt.show() ne sont plus nécessaires.
plt.ion()						

# --------------------------------------------------------------------------------------
# Fonction de "fin temporaire" pendant l'avancée du TP. Attend une frappe Entrée, puis quitte le script.

def stop_ici():
	plt.pause(0.1)	# nécessaire pour que matplotlib ait le temps d'afficher les figures
	input()
	exit()

# --------------------------------------------------------------------------------------
# Tous les passages indiqués "TODO()" sont à remplacer par vos soins

def TODO():
	print("à vous!")
	stop_ici()


######################################################################
### Fonctions de tracé de courbes de Bézier : reprises du TP2
######################################################################

# --------------------------------------------------------------------------------------
# Calcul d'un point d'une courbe de Bézier
#
# - t = paramètre du point de la courbe à calculer [nombre réel entre 0 et 1]
# - P = points de contrôle [au même format qu'au TP2 : np.array de taille (N+1,2)]

def bezierCasteljau(t,P):
    while(P.shape[0]>1):
        P = (1-t)*P[:-1] + t*P[1:]
    return P[0]

# --------------------------------------------------------------------------------------
# Traçage d'une courbe dans sa totalité
#
# - P = points de contrôle [au même format qu'au TP2 : np.array de taille (N+1,2)]
# - trace_controle = True pour tracer également le polygone de controle
# - kwargs permet de passer tous les arguments habituels de la commande plt.plot (couleur, markers, etc.)

def traceBezier(P, trace_controle=False, **kwargs):
    if trace_controle:
        plt.plot( P[:,0], P[:,1], linestyle='--', color='black')
    Nt = 100
    Ft = np.array( [ bezierCasteljau(t,P) for t in np.linspace(0,1,Nt) ] )
    plt.plot( Ft[:,0], Ft[:,1], **kwargs)

# --------------------------------------------------------------------------------------
# Traçage d'un carré de coté 1
#
# - offset = coordonnées du coin en bas à gauche du carré ([0,0] par défaut)
# - kwargs permet de passer tous les arguments habituels de la commande plt.plot (couleur, markers, etc.)

def traceCarre(offset=[0,0], **kwargs):
    Carre = np.array( [ [0,0], [1,0], [1,1], [0,1], [0,0] ] )
    Carre = Carre + np.array(offset)
    plt.plot( Carre[:,0], Carre[:,1],  **kwargs)


# print("-"*80)
# print(''' QUESTION 1 : Prise en main des fonctions.''')
# print()
# print()

# Dans une première figure, tracez :
# - En VERT: un carré de coté 1 (et tel que son coin en bas à gauche soit aux coordonnées [0,0])
# - En BLEU: la courbe de Bézier associée aux points de contrôle
# P0=[0,0], P1=[2,2], P2=[2,-2], P3=[0,2], P4=[0,0]
# ''')

def exo1() :
    plt.figure()
    traceCarre(color = 'green' )
    P0 = np.array( [ 0, 0 ] )
    P1 = np.array( [ 2, 2 ] )
    P2 = np.array( [ 2,-2 ] )
    P3 = np.array( [ 0, 2 ] )
    P4 = np.array( [ 0, 0 ] )
    P = np.array([ P4, P3, P2, P1, P0 ])
    traceBezier(P, True) 
    plt.axis('equal')

# exo1()
# stop_ici()

print("-"*80)
# print(''' QUESTION 2.
# Complétez le code de tracé de la fonction traceLettre ci-dessous [le TODO() à la fin de la fonction].

# Pour ce faire, réfléchissez bien aux points suivants :
# - Sous quel format la fonction traceBezier doit-elle recevoir les points de contrôle ?
# - Comment 'transmettre' à la fonction traceBezier le fait qu'on veut ou non tracer le polygone de contrôle ?
# - Comment 'transmettre' à la fonction traceBezier les options de traçage (couleur, etc.) passées à la fonction traceLettres ?

# Vérification : une fois le TODO() complété, le code de test suivant devra tracer la lettre "a" en bleu (et ses points de controle)
# ''')
print()
print()

###################################################################
# Fonction de tracé d'une lettre quelconque.
# C'est la fonction principale de cet exercice.
# On vous donne un squelette, que vous allez compléter progressivement.
###################################################################
#
# - char : caractère qu'on souhaite tracer ("a", "b", etc., ainsi que l'espace " ")
# - offset = coordonnées du point auquel on souhaite tracer la lettre ([0,0] si on ne précise pas)
# - trace_controle, kwargs : même signification que pour la fonction traceBezier

def traceLettre(char, offset=[0,0], trace_controle=False, **kwargs):
    
    # Définition de la liste des points de contrôle pour cette lettre
    # ( strokes[0]=points de contrôle pour le 1er trait, strokes[1]=points de contrôle pour le 2è trait, etc. )
    strokes = []    

    if char =="a":
        strokes.append( np.array([ [.8,.05], [.8,1] , [.75,1.1], [.1,.85] ]) * 200 )  # premier trait du 'a'
        strokes.append( np.array( [ [.78,.1], [-.25,-.3], [-.3,.7], [.8, .5] ] ) * 200 )  # deuxième trait du 'a'

    elif char==" ":
        pass  
    
    elif char=="z":
        strokes.append([ [59,60], [97,61] ])
        strokes.append([ [98,104], [59,60] ]) 
        strokes.append([ [57,105], [98,104] ])                                                        # pour 'tracer' le caractère espace... on ne trace rien ! ^^
    
    else:
        raise("character '"+char+"' is not implemented yet")

    ### Le tracé proprement dit
    for lst in strokes:
        #print(lst)      # pour que vous compreniez ce que contient la variable lst (vous pouvez ensuite supprimer cette ligne)
        # Tracer la courbe de Bézier définie par la liste de points lst
        traceBezier(np.array(lst), trace_controle, **kwargs )


print("-"*80)
# print(''' QUESTION 3 : trois nouvelles lettres.

# À ce stade, la fonction traceLettre sait uniquement tracer un "a". Rajoutez le code (=les 'strokes') permettant de tracer les lettres "g", "t" et "c".

# Méthode conseillée : construisez la lettre sous inkscape (exo 1), puis relevez la position des points de contrôle et rentrez-les sous Python.

# Attention : chaque lettre doit "tenir" dans un carré unité (le "g" pouvant dépasser un peu vers le bas, et le "t" un peu vers le haut)
# ''')

### Teste le "g":
plt.figure()
traceLettre("z", trace_controle=True, color="blue", linewidth=3)
traceCarre(color="green")
plt.axis("equal")


### Teste le "t":
plt.figure()
traceLettre("a", trace_controle=True, color="blue", linewidth=3)
traceCarre(color="green")
plt.axis("equal")

stop_ici() # -------------- Supprimez cette ligne pour passer à la suite --------------

### Teste le "c":
plt.figure()
traceLettre("c", trace_controle=True, color="blue", linewidth=3)
traceCarre(color="green")
plt.axis("equal")

stop_ici() # -------------- Supprimez cette ligne pour passer à la suite --------------


print("-"*80)
print(''' QUESTION 4 : Gestion de l'offset.

Modifiez votre fonction traceLettre afin de pouvoir passer en option l'OFFSET (=décalage) auquel on souhaite tracer la lettre.
Inspirez-vous de la fonction traceCarre, pour laquelle cette fonctionnalité est déjà implémentée.

Vérification : une fois votre code écrit, le code ci-dessous représentera les 4 lettres a,c,g,t dans la disposition suivante:
 ac
 gt
''')

### Vérification:
plt.figure()
traceLettre("a", offset = [0,0],  color="blue", linewidth=3)
traceCarre(color="green", offset=[0,0] )
traceLettre("c", offset = [2,0], color="blue", linewidth=3)
traceCarre(color="green", offset=[2,0] )
traceLettre("g", offset = [0,-2], color="blue", linewidth=3)
traceCarre(color="green", offset=[0,-2] )
traceLettre("t", offset = [2,-2], color="blue", linewidth=3)
traceCarre(color="green", offset=[2,-2] )
plt.axis("equal")

stop_ici() # -------------- Supprimez cette ligne pour passer à la suite --------------


print("-"*80)
print(''' QUESTION 5.
Répartissez-vous le travail dans le groupe TP afin de coder TOUTES les lettres de l'alphabet !
(Il faudra donc vous "passer" le code de chaque lettre les uns aux autres, au fur et à mesure que vous les écrivez.)

Attention : chaque lettre doit toujours tenir dans un carré unité (en dépassant un peu vers le haut ou le bas pour certaines lettres comme le "l", le "j", etc.).
''')

### Vérification (par exemple, pour vérifier le code du "b" une fois qu'il est défini):
plt.figure()
traceLettre("b", trace_controle=True, color="blue", linewidth=3)
traceCarre(color="green")
plt.axis("equal")

stop_ici() # -------------- Supprimez cette ligne pour passer à la suite --------------


print("-"*80)
print(''' QUESTION 6 : tracé d'une phrase quelconque.

Écrivez une fonction traceStr, avec le prototype défini ci-dessous, qui trace une chaîne de caractères quelconque (sans ponctuation) dans votre police.

Consigne pour le OFFSET (décalage) : chaque caractère de la chaîne doit être tracé avec un décalage de +1 vers la droite par rapport au caractère précédent.
''')

# --------------------------------------------------------------------------------------
# Fonction de tracé d'une chaîne de caractères quelconque (sans ponctuation)
#
# - chaine = chaîne de caractères qu'on souhaite tracer
# - trace_controle et kwargs : même signification que pour la fonction traceBezier

def traceStr(chaine, trace_controle=False, **kwargs):
    TODO()    


### Vérification:

phrase = "gattaca taca tagata"                                   # version basique avec uniquement les lettre a,c,g,t
# phrase = "portez ce vieux whisky au juge blond qui fume"       # pangramme (phrase avec les 26 lettres de l'alphabet)

plt.figure()
traceStr(phrase, color="blue", linewidth=3)
plt.axis("equal")



stop_ici() # FINI !
