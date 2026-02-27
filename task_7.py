import json

with open("mission_data/telemetrie.json", 'r', encoding="utf-8") as f:
    telemetrie = json.load(f)
# print(telemetrie)
print("Phase \t \t ", " | Altitude \t \t ", " | Vitesse \t \t ", " | Carburant \t \t ", "-| Alertes \t \t ")
print("--------------------------------------------------------------------------------")
for alli in telemetrie['releves']:
    print(alli['phase'], "\t \t | ", alli['altitude_km'], " km \t \t | ", alli['vitesse_km_s'], " km/s \t \t | ", alli['carburant_pct'], "% \t \t | ", list(alli['systemes'].keys())[0])
# print(telemetrie['releves'][0]["Altitude"])