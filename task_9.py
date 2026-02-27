class NavigationError(Exception):
    from datetime import datetime
    """Classe de base pour les erreurs de navigation spatiale."""

def valider_mission(mission):
    """Valide les données d'une mission spatiale."""
    
    # Vérification des champs obligatoires
    champs_obligatoires = ["id", "nom", "destination", "date_lancement", "statut", "equipage", "duree_jours", "budget_millions_usd"]
    for champ in champs_obligatoires:
        if champ not in mission.keys():
            raise NavigationError(f"Le champ '{champ}' est manquant.") 
    
    # Vérification du format de la date    from datetime import datetime
    try:        
        datetime.strptime(mission["date_lancement"], "%Y-%m-%d")
    except ValueError:        
        raise NavigationError("Le champ 'date_lancement' doit être au format 'YYYY-MM-DD'.")
    
    # Vérification du statut
    statuts_valides = ["planifiée", "en cours", "terminée", "annulée", "théorique"]
    if mission["statut"] not in statuts_valides:
        raise NavigationError(f"Le champ 'statut' doit être l'un des suivants : {', '.join(statuts_valides)}.")
    
    # Vérification de la durée
    if not isinstance(mission["duree_jours"], int) or mission["duree_jours"] < 0:
        raise NavigationError("Le champ 'duree_jours' doit être un entier positif.")
    
    # Vérification du budget
    if not isinstance(mission["budget_millions_usd"], (int, float)) or mission["budget_millions_usd"] < 0:
        raise NavigationError("Le champ 'budget_millions_usd' doit être un nombre positif.")