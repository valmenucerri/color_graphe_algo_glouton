
from traiter_graphr import liste_ordre_dico
dico ={0: {1, 2}, 1: set(), 2: {0, 1, 4}, 3: {4, 5}, 4: {3, 5}, 5: {3}}

liste = liste_ordre_dico(dico)
def tri(dico,liste):
    k = len(liste)
    liste_indice = []
    for i in range(k):
        maximum = max(liste)
        element = liste.index(maximum)
        liste_indice.append(element)
        liste[element] = -1


    return liste_indice

print(tri(dico,liste))