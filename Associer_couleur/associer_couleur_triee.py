'''Associer une couleur à chaque noeud d'un graphe, en commençant par le noeud ayant le plus d'arêtes'''
from Creer_resultat import creer_fichier
from Associer_couleur.associer_couleur import non_adja_liste

def assigner_couleur_triee(dico,N,ordre):
    '''Assigner une couleur, representee par un reel, à chaque noeud, en utilisant le minimum de couleur, et en considerant les noeuds par ordre décroissant de nb d'arêtes
    Entree : dico, le dictionnaire représentant le graphe
    Entree : N le nombre de noeuds du graphe
    Entree : ordre, la liste contenant les indices de noeud dans l'ordre décroissant du nombre d'arêtes

    Sortie : couleur, la liste des couleurs utilisees
    Sortie : dico, le dictionnaire representant le graphe, avec les couleurs de chaque noeud indiquees
    '''
    couleur = []
    c_appli = 0
    traite = []
    for noeud in ordre:
        if noeud not in traite:
            c_appli += 1
            dico[noeud].add(str(c_appli))
            traite.append(noeud)
            traite_partiel = []
            traite_partiel.append(noeud)
            for noeuds in ordre:
                if noeuds not in traite:
                    if non_adja_liste(noeuds,traite_partiel,dico):
                        dico[noeuds].add(str(c_appli))
                        traite.append(noeuds)
                        traite_partiel.append(noeuds)
            couleur.append(str(c_appli))
    creer_fichier(couleur,dico)