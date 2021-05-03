import traiter_graphr as gr
import sys

if __name__ == "__main__":
    graphe = gr.recup_fichier(sys.argv)
    N = gr.nbr_noeud(graphe)
    dico = gr.analyser_graphe(graphe,N)
    print(dico)