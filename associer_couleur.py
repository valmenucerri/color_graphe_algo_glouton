#traiter le problème en associant une couleur à chaque noeud, de manière à ce que les noeuds adjacents ne soient pas de couleur identique

def assigner_couleur(dico):
    couleur = []
    c_appli = 0
    traite = []
    for noeud in dico:
