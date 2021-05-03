import traiter_graphr as gr
import sys
import associer_couleur as ac
import associer as ac2

if __name__ == "__main__":
    graphe = gr.recup_fichier(sys.argv)
    N = gr.nbr_noeud(graphe)
    dico = gr.analyser_graphe(graphe,N)
    ordre = gr.liste_ordre_dico(dico)
    print(ac2.assigner_couleur_triee(dico_trie,N,ordre))