import os
import subprocess

# Chemin du dossier contenant les fichiers PDF d'origine
dossier_pdf = '/home/charlotte/Documents/M2/S1/projet_qinliang/corpus'

# Chemin du dossier où vous souhaitez enregistrer les fichiers texte convertis
dossier_txt = '/home/charlotte/Documents/M2/S1/projet_qinliang/corpus_converti'

# Vérifiez si le dossier de sortie existe, sinon, créez-le
if not os.path.exists(dossier_txt):
    os.makedirs(dossier_txt)

# Parcourez tous les fichiers PDF du dossier d'origine
for fichier_pdf in os.listdir(dossier_pdf):
    if fichier_pdf.endswith('.pdf'):
        nom_pdf = os.path.splitext(fichier_pdf)[0]
        fichier_txt = os.path.join(dossier_txt, f"{nom_pdf}.txt")
        chemin_pdf = os.path.join(dossier_pdf, fichier_pdf)

        # Utilisez pdftotext pour convertir le fichier PDF en texte
        subprocess.run(['pdftotext', chemin_pdf, fichier_txt])

        print(f'Converti {fichier_pdf} en {nom_pdf}.txt')

print('Conversion terminée.')
