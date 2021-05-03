#Traiter les informations du graphe, en supposant que celui-ci est représenté comme un fichier (voir exemple)

def recup_fichier(liste):
    graphe = str(liste[-1])
    return graphe



def nbr_noeud(graphe):
    with open(graphe,'r') as fichier:
        N =  fichier.readline()
        N = int(N)
    return N

def analyser_graphe(graphe,N):
    L = {}
    with open(graphe,'r') as fichier:
        for i in range(N):
            L[i] = set()
        n_ligne = 0
        for ligne in fichier:
            ligne1 = ligne.split()
            n_ligne += 1
            if len(ligne1) == 2:  # Ajouter chaque valeur à part la première, qui est N la dimension du graphe
                couple1 = int(ligne1[0])
                couple2 = int(ligne1[1])
                if 0 <= couple1 <= N and 0 <= couple2 <= N:
                    L[couple1].add(couple2)

            elif len(ligne1) == 0:  # Ne pas considérer les lignes vides
                pass

    return L

def liste_ordre_dico(dico):
    #creer une liste dans laquelle est noté l'ordre des noeuds par nb d'arêtes décroissant
    nb_arete = []
    for i in dico.values():
        nb_arete.append(len(i))

    tri(dico,nb_arete)

def tri(dico,liste):
    k = len(liste)
    liste_indice = []
    for i in range(k):
        maximum = max(liste)
        element = liste.index(maximum)
        liste_indice.append(element)
        liste[element] = -1


    return liste_indice
