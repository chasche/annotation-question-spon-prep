import os

# le chemin du dossier contenant les fichiers .txt
dossier_source = "/home/charlotte/Documents/M2/S1/projet_qinliang/corpus_converti"

# le chemin du fichier de sortie
fichier_de_sortie = "/home/charlotte/Documents/M2/S1/projet_qinliang/corpus_3rd.txt"

# Ouvrir le fichier de sortie en mode écriture
with open(fichier_de_sortie, 'w') as fusion:

    # Parcourir les fichiers .txt dans le dossier source
    for fichier in os.listdir(dossier_source):
        if fichier.endswith(".txt"):
            chemin_complet = os.path.join(dossier_source, fichier)
            
            
            with open(chemin_complet, 'r') as f:
                contenu = f.read()
                
                
                fusion.write(contenu)
                fusion.write('\n')  # Ajouter un saut de ligne entre les fichiers

print("Tous les fichiers .txt ont été combinés avec succès en", fichier_de_sortie)

