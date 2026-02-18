import json

with open('mission_data/missions.json', 'r', encoding='utf-8') as file:
    missions = json.load(file)

# print(missions['missions'])
for mission in missions['missions']:
    long_string = ""
    keys = mission.keys()
    for key in keys:
        if key == "id":
            long_string = str(long_string) + " " + str([mission[key]]) + " "
        elif key == "nom":
            long_string = " " + str(long_string) + " " + str(mission[key]) + " " + "->" + " "
        elif key == "duree_jours":
            long_string = " " + str(long_string) + " " + str(mission[key]) + " jours" + "|" + " "
        elif key == "equipage":
            long_string = " " + str(long_string) + " " + str(key) + ":" + str(len(mission[key])) + "|" + " "
        else:
            long_string = " " + str(long_string) + " " + str(mission[key]) + "|" + " "
    print(long_string)