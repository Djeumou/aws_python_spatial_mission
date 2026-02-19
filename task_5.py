import os
from datetime import date
import shutil

shutil.copy('mission_data/journal_bord.txt', f'mission_data/archives/journal_bord_{date.today()}.txt')

# Création du fichier `mission_data/rapports/rapport_systeme.txt` avec le résultat de os.getcwd()
with open('mission_data/rapports/rapport_systeme.txt', 'w', encoding='utf-8') as rapport_file:
    rapport_file.write(f"Répertoire de travail actuel : {os.getcwd()}\n")
    for element in os.environ.keys():
        if "python" in element.lower() or "path" in element.lower():
            rapport_file.write(f"{element} : {os.environ[element]}\n")

    #Espace de disque disponible
    total, used, free = shutil.disk_usage(os.getcwd())
    # print(f"Espace disque disponible : {free / (1024 * 1024 * 1024):.2f} Go")
    rapport_file.write(f"Espace disque disponible : {free / (1024 * 1024 * 1024):.2f} Go\n")