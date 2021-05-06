'''Appeler les modules et sous-programmes nécessaires pour l'exécution du programme
'''
import traiter_graphr as gr
import sys

import Associer_couleur.associer_couleur_triee as ac2
import Associer_couleur.associer_couleur as ac
if __name__ == "__main__":
    graphe = gr.recup_fichier(sys.argv)
    N = gr.nbr_noeud(graphe)
    dico = gr.analyser_graphe(graphe,N)
    print(dico)
    nb_arete = gr.liste_ordre_dico(dico)
    ordre = gr.tri(dico,nb_arete)
    ac2.assigner_couleur_triee(dico,N,ordre)
    #ac.assigner_couleur(dico,N)
