import pandas as pd

monster_manuel = pd.read_csv('CSV_files/random_encounter_monsters.csv')
monster_manuel = monster_manuel.sort_values('monster')
monster_manuel = monster_manuel[monster_manuel.legendary == 'N']
monster_manuel = monster_manuel[monster_manuel.xp > 0]
xp_threshold = pd.read_csv('CSV_files/xp_threshold.csv', index_col='level')

def encounter_difficulty(difficulty, party_level, party_size):
    threshold = xp_threshold[difficulty]
    threshold = threshold[party_level]
    threshold *= party_size
    return threshold

def choosing_monsters(party_threshold, terrain):
    monster_choices = monster_manuel[monster_manuel.xp <= party_xp_threshold]
    monster_choices = monster_choices[monster_choices[terrain] == 1]
    monster_names = list(monster_choices.monster)
    return monster_choices
    #for item in monster_names:
        #current_monster = monster_choices[monster_choices.monster == item]
        #print(item, int(party_xp_threshold/current_monster.xp))

party_size = int(input("How many members in your party? "))
party_level = int(input("What level is your party? "))
environment = input("""What environment are you traveling through? (Artic, Coastal, Desert, Forest, Grassland, Hill,
Mountain, Swamp, Underdark, Underwater, Urban) """).lower()
difficulty = input("How hard of an encounter? (Easy, Medium, Hard, Deadly)").lower()

party_xp_threshold = encounter_difficulty(difficulty, party_level, party_size)

print(choosing_monsters(party_xp_threshold, environment))
