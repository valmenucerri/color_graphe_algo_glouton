'''Creer un fichier texte contenant le dictionnaire final, avec en ses sets d
es chiffres convertis en str correspondant à une couleur'''
import sys

def creer_fichier(couleur,dico):
    with open("resultat_fichier_{}".format(str(sys.argv[-1])),'w') as fichier:
        fichier.write("La liste des couleurs : "+" "+str(couleur)+"\n")
        fichier.write("Le dictionnaire rempli avec les couleurs :"+" "+str(dico)+"\n")
