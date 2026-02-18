with open('mission_data/journal_bord.txt', 'r', encoding="utf-8") as journal_file:
    lines = journal_file.readlines()
    with open('mission_data/alertes.txt', 'w', encoding='utf-8') as alertes_file:
        for line in lines:
            if "alerte" in line.lower():
                print(line.strip())
                alertes_file.write(line.strip() + '\n')  