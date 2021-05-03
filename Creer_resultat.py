'''Creer un fichier texte contenant le dictionnaire final, avec en ses sets d
es chiffres convertis en str correspondant à une couleur'''
import sys

def creer_fichier(couleur,dico):
    '''
    Creer un fichier texte contenant les résultats obtenus avec le graphe choisi.

    :param couleur: la liste des couleurs utilisées type : list
    :param dico: le graphe, avec les couleurs ajoutées dedans. type : dict

    :return: un fichier .net contenant les résultats. type : file
    '''
    with open("Résultats/resultat_fichier_{}".format(str(sys.argv[-1])),'w') as fichier:
        fichier.write("La liste des couleurs : "+" "+str(couleur)+"\n")
        fichier.write("Le graphe rempli avec les couleurs :"+" "+str(dico)+"\n")
