import os

if 'mission_data' in os.listdir():
    print("Le dossier 'mission_data' existe déjà.")
else:
    print("Le dossier 'mission_data' n'existe pas. Vous pouvez le créer.")

print("mission_data/")
for item in os.listdir('mission_data'):
    item_path = os.path.join('mission_data', item)
    print(f"{item} \t {os.path.getsize(item_path)/1024:.2f} Ko")

os.makedirs('mission_data/archives', exist_ok=True)
os.makedirs('mission_data/rapports', exist_ok=True)
