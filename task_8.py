import json
import math

def distance_interplanetaire(corps1, corps2, donnees_corps):
    """
    Calcule la distance approximative entre deux corps célestes
    basée sur leur distance au Soleil (en millions de km).
    Retourne la valeur absolue de la différence.
    """
    for corps in donnees_corps['corps_celestes']:
        if corps['nom'] == corps1:
            distance_soleil_mkm_1 = corps['distance_soleil_mkm']
        if corps['nom'] == corps2:
            distance_soleil_mkm_2 = corps['distance_soleil_mkm']

    return math.fabs(math.sqrt(math.pow(distance_soleil_mkm_1, 2) + math.pow(distance_soleil_mkm_2, 2) - 2 * distance_soleil_mkm_1 * distance_soleil_mkm_2 * math.cos(math.radians(0))))  # Angle de 0° pour simplification

def temps_trajet(distance_mkm, vitesse_km_s):
    """
    Calcule le temps de trajet en jours.
    distance en millions de km, vitesse en km/s.
    """
    return (distance_mkm * 1e6) / (vitesse_km_s * 86400)  # Convertir distance en km et temps en jours

def delta_v(gravite_depart, gravite_arrivee, altitude_orbite_km):
    """
    Estimation simplifiée du delta-v nécessaire (en km/s).
    Formule simplifiée : sqrt(2 * g_depart * alt) + sqrt(2 * g_arrivee * alt)
    (les altitudes sont converties en mètres)
    """
    return math.sqrt(2 * gravite_depart * altitude_orbite_km * 1000) + math.sqrt(2 * gravite_arrivee * altitude_orbite_km * 1000)

def poids_sur_corps(masse_kg, gravite_m_s2):
    """Calcule le poids (en Newtons) sur un corps céleste."""
    return masse_kg * gravite_m_s2

def charger_corps_celestes(chemin="mission_data/corps_celestes.json"):
    """Charge le fichier des corps célestes avec gestion d'erreur."""
    with open (chemin, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
    
if __name__ == "__main__":
    corps = charger_corps_celestes()
    # print (corps['corps_celestes'][0])
    d = distance_interplanetaire("Terre", "Mars", corps)
    print(f"Distance Terre-Mars : {d} millions km")
    
    t = temps_trajet(d, 11.0)
    print(f"Temps de trajet à 11 km/s : {t:.0f} jours")
    
    print(f"Poids d'un astronaute (80 kg) sur Mars : {poids_sur_corps(80, 3.72):.1f} N")