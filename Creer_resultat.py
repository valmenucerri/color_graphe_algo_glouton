'''Creer un fichier texte contenant le dictionnaire final, avec en ses sets d
es chiffres convertis en str correspondant à une couleur'''
import sys
import matplotlib
import matplotlib.pyplot as plt
import random as r
def creer_fichier(couleur,dico):
    '''
    Creer un fichier texte contenant les résultats obtenus avec le graphe choisi.

    :param couleur: la liste des couleurs utilisées type : list
    :param dico: le graphe, avec les couleurs ajoutées dedans. type : dict

    :return: un fichier .net contenant les résultats. type : file
    '''
    with open("Résultats/resultat_fichier_{}".format(str(sys.argv[-1])),'w') as fichier:
        fichier.write("La liste des couleurs : "+" "+str(couleur)+"\n")
        fichier.write("Il y a "+str(len(couleur))+" couleurs utilisées"+"\n")
        fichier.write("Le graphe rempli avec les couleurs :"+" "+str(dico)+"\n")


def tracer_graphe(L,couleur):
    liste_couleur = creer_liste_couleur()
    N = len(L)
    x = [r.randrange(0, N * 4, 3) for i in range(N)]  # créer un nuage de points aléatoires représentant chaque noeud, x absisse et y ordonnée
    y = [r.randrange(0, N * 4, 3) for y in range(N)]
    plt.subplot(1, 2, 1)  # séparer le graphe en deux partiesn écrire sur la premier
    plt.xlim(-3, N * 4)
    plt.ylim(-3, N * 4)
    tracer_graphe_init(L, x, y)
    plt.subplot(1,2,2)
    plt.xlim(-3, N * 4)
    plt.ylim(-3, N * 4)
    tracer_graph_final(L, x, y, liste_couleur)
    plt.title(str(len(couleur))+" couleurs",color='red')

    plt.savefig("Résultats/exemple{}figure.pdf".format(N))


def tracer_graphe_init(L,x,y):
    N = len(L)
    for pt in range(N):
        plt.scatter(x[pt], y[pt], s=N * 15, color='black')
        plt.text(x[pt] -1, y[pt]+1 , str(pt))
    for noeud1,noeud2_set in L.items():
        for noeud2 in noeud2_set:
            if isinstance(noeud2,int):
                plt.plot([x[noeud1],x[noeud2]],[y[noeud1],y[noeud2]],color='0.6',linestyle = "solid")

def creer_liste_couleur():
    dico_couleur = matplotlib.colors.cnames
    liste_couleur = []

    for couleur in dico_couleur:
        liste_couleur.append(couleur)
    r.shuffle(liste_couleur)
    return liste_couleur

def tracer_graph_final(L,x,y,liste_couleur):
    N = len(L)
    for pt in range(N):
        plt.scatter(x[pt], y[pt], s=N * 15, color='black')
        plt.text(x[pt] -1, y[pt]+1 , str(pt))
    for noeud1,noeud2_set in L.items():
        for noeud2 in noeud2_set:
            if isinstance(noeud2,int):
                plt.plot([x[noeud1],x[noeud2]],[y[noeud1],y[noeud2]],color='0.6',linestyle = "solid")
            else:
                plt.scatter(x[noeud1],y[noeud1],s=N*15,color=liste_couleur[int(noeud2)])
