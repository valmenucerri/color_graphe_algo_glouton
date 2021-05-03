import traiter_graphr as gr
import sys
import associer_couleur as ac

if __name__ == "__main__":
    graphe = gr.recup_fichier(sys.argv)
    N = gr.nbr_noeud(graphe)
    dico = gr.analyser_graphe(graphe,N)
    print(ac.assigner_couleur(dico,N))