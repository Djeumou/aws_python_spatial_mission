def charger_json_securise(chemin):
    import json

    try:
        with open(chemin, 'r', encoding = "utf-8") as fichier:
            data = json.load(fichier)
            return data
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{chemin}' n'existe pas.")
    except json.JSONDecodeError:
        print(f"Erreur : Le fichier '{chemin}' est mal formé.") 
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")   

# charger_json_securise('mission_data/fantome.json')
with open("mission_data/corrompu.json", "w") as f:
    f.write("{nom: valeur_sans_guillemets}")
data = charger_json_securise("mission_data/corrompu.json")