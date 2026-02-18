import os
from datetime import date
import shutil

shutil.copy('mission_data/journal_bord.txt', f'mission_data/archives/journal_bord_{date.today()}.txt')

os.