import pandas as pd

monster_manuel = pd.read_csv('CSV_files/Random_encounter_monsters.csv')
monster_manuel = monster_manuel.sort_values('Monster')
monster_manuel = monster_manuel.rename(columns={'Legendary?': 'Legendary', 'Lair?': 'Lair'})
monster_manuel = monster_manuel[monster_manuel.Legendary == 'N']
xp_threshold = pd.read_csv('CSV_files/xp_threshold.csv', index_col='Level')

party_size = int(input("How many members in your party? "))
party_level = int(input("What level is your party? "))
environment = (input("""What environment are you traveling through? (Artic,
Coastal, Desert, Forest, Grassland, Hill, Mountain, Swamp, Underdark,
Underwater, Urban) """))
