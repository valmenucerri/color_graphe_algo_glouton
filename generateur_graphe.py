'''
Créer un fichier .net qui contient des données aléatoires, conforme à la forme des fichiers .net fournis pour tester nos programmes. Le fichier créé possède le nombre de sites que l'on désire, ce qui permet de créer beaucoup de fichiers .net de tailles différentes, pour tester les codes.
'''

import random as r

N = 10  # A changer comme désiré

# créer un fichier try.net contenant N lignes contenant des couples aléatoires
with open('exemple{}.net'.format(N), 'w') as t:
    t.write(str(N) + '\n')
    for a in range(N - 1):
        for b in range(int(r.randint(0, N - 1) ** 1 / 2)):
            j = str(r.randint(0, N - 1))
            t.write(str(a) + " " + j + "\n")
            t.write(j + " " + str(a) + "\n")
