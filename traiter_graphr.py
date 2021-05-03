'''Traiter les informations du graphe, en supposant que celui-ci est représenté comme un fichier (voir exemple)
'''
def recup_fichier(liste):
    '''
    Récupérer le nom du fichier dans la ligne de commande

    :param liste: la liste cotenant les informations de la ligne de commande. type : list

    :return: graphe : le nom du fichier. type : str
    '''
    graphe = str(liste[-1])
    return graphe



def nbr_noeud(graphe):
    '''
    Récupérer le nombre total de noeuds, c'est à dire la dimension du graphe

    :param graphe: le nom du fichier du graphe. type : str
    :return: N : le nombre total de noeuds. type : int
    '''
    with open("exemple_graphe/"+graphe,'r') as fichier:
        N = fichier.readline()
        N = int(N)
    return N

def analyser_graphe(graphe,N):
    '''
    Créer le dictionnaire associé au graphe, de la forme {noeud : {noeud(s) adjacent(s)}}
    :param graphe: le nom du fichier. type : str
    :param N: le nombre total de noeuds. type : int
    :return: L : le dictionnaire associé au graphe. type : dict
    '''
    L = {}
    with open("exemple_graphe/"+graphe,'r') as fichier:
        for i in range(N):
            L[i] = set()
        n_ligne = 0
        for ligne in fichier:
            ligne1 = ligne.split()
            n_ligne += 1
            if len(ligne1) == 2:  # Traiter chaque valeur sauf la première, qui est N la dimension du graphe
                couple1 = int(ligne1[0])
                couple2 = int(ligne1[1])
                if 0 <= couple1 <= N and 0 <= couple2 <= N:
                    L[couple1].add(couple2)

            elif len(ligne1) == 0:  # Ne pas considérer les lignes vides
                pass

    return L

def liste_ordre_dico(dico):
    '''
    Récupérer le nombre d'arêtes; donc le nombre de noeuds adjacents, de chaque noeud
    :param dico: le dictionnaire du graphe. type : dict
    :return: nb_arete: la liste contenant le nb d'arêtes pour chaque noeud (representés par les indices de la liste). type : list
    '''
    #creer une liste dans laquelle est noté l'ordre des noeuds par nb d'arêtes décroissant
    nb_arete = []
    for i in dico.values():
        nb_arete.append(len(i))

    return nb_arete

def tri(dico,liste):
    '''
    Déterminer le rangemment décroissant des noeuds, en fonction de leur nombre d'arêtes
    :param dico: le dictionnaire du graphe. type : dict
    :param liste: le nb d'arêtes de chaque noeud. type : list
    :return: liste_indice : l'ordre des noeuds décroissant (en fonction de leur nb d'arêtes). type : list
    '''
    k = len(liste)
    liste_indice = []
    for i in range(k):
        maximum = max(liste)
        element = liste.index(maximum)
        liste_indice.append(element)
        liste[element] = -1  #Remplacer les éléments traités par des -1, pour éviter de kes traiter une seconde fois
    return liste_indice
