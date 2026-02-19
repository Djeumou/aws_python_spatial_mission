def ajouter_mission (chemin_json, nouvelle_mission):
    import json

    with open(chemin_json, 'r', encoding='utf-8') as f:
        exist_missions = json.load(f)

    if nouvelle_mission['id'] in exist_missions:
            print(f"Erreur : La mission avec l'ID {nouvelle_mission['id']} existe déjà.")
    else:
        exist_missions["missions"].append(nouvelle_mission)
        try:
            with open(chemin_json, 'w', encoding='utf-8') as f:
                json.dump(exist_missions, f, ensure_ascii=False, indent=4)
            # print(f"Élément ajouté : {cle} = {valeur}")
        except Exception as e:
            print(f"Erreur lors de l'écriture : {e}")

def supprimer_mission(chemin_json, mission_id):
     import json
     with open(chemin_json, 'r', encoding='utf-8') as f:
        exist_missions = json.load(f)

        for element in exist_missions["missions"]:
            if element["id"] == mission_id:
                exist_missions["missions"].remove(element)
                try:
                    with open(chemin_json, 'w', encoding='utf-8') as f:
                        json.dump(exist_missions, f, ensure_ascii=False, indent=4)
                    print(f"Mission avec l'ID {mission_id} supprimée.")
                except Exception as e:
                    print(f"Erreur lors de l'écriture : {e}")
                break      

nouvelle = {
    "id": "MSN-006",
    "nom": "Proxima Relay",
    "destination": "Alpha Centauri (sonde)",
    "date_lancement": "2035-06-01",
    "statut": "théorique",
    "equipage": [],
    "duree_jours": 29200,
    "budget_millions_usd": 125000
}

# ajouter_mission("mission_data/missions.json", nouvelle)
# supprimer_mission("mission_data/missions.json", "MSN-006")

#Exercise Okay !!!