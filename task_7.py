import json

with open("mission_data/telemetrie.json", 'r', encoding="utf-8") as f:
    telemetrie = json.load(f)

print(telemetrie['releves'][0]["phase"])