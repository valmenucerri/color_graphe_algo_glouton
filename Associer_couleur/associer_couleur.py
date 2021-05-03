from Creer_resultat import creer_fichier
def assigner_couleur(dico,N):
    '''Assigner une couleur, representee par un reel, à chaque noeud, en utilisant le minimum de couleur
    :param: dico, le dictionnaire représentant le graphe. type : dict
    :param : N le nombre de noeuds du graphe; type : int

    :return : couleur, la liste des couleurs utilisees. type : list
    :return: dico, le dictionnaire representant le graphe, avec les couleurs de chaque noeud indiquees. type : dict
    '''
    couleur = []
    c_appli = 0
    traite = []
    for noeud in dico:
        if noeud not in traite:
            c_appli += 1
            dico[noeud].add(str(c_appli))
            traite.append(noeud)
            traite_partiel = []
            traite_partiel.append(noeud)
            for noeuds in dico:
                if noeuds not in traite:
                    if non_adja_liste(noeuds,traite_partiel,dico):
                        dico[noeuds].add(str(c_appli))
                        traite.append(noeuds)
                        traite_partiel.append(noeuds)
            couleur.append(str(c_appli))
    creer_fichier(couleur,dico)



def non_adja_liste(element,liste,dico):
    '''Vérifier si un élément est adjacent à d'autres éléments particuliers, stockés dans une liste
    :param : element, l'element dont on veut vérifier le caractère adjacent. type : int
    :param : liste, la liste contenant les noeuds que l'on veut comparer à element. type : list
    :param : dico, le dictionnaire représentant le graphe. type : dict

    :return : True , l'element n'est adjacent à aucun element de la liste. type : bool
    :return: False , l'element est adjacent à au moins un élément de la liste. type : bool
    '''
    i = 0
    continu = True

    taille = 0
    for i in liste:
        if i not in dico[element]:
            taille += 1



    if taille == len(liste):
        return True
    else:
        return False

