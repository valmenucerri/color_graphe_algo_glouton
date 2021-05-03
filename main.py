import traiter_graphr as gr
import sys
import associer_couleur as ac
import associer_couleur_triee as ac2
if __name__ == "__main__":
    graphe = gr.recup_fichier(sys.argv)
    N = gr.nbr_noeud(graphe)
    dico = gr.analyser_graphe(graphe,N)
    nb_arete = gr.liste_ordre_dico(dico)
    ordre = gr.tri(dico,nb_arete)
    print(ordre)
    print(ac2.assigner_couleur_triee(dico,N,ordre))