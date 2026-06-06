import random

title = 'D&D Character Generator'
races = [
    {'name': 'Hill Dwarf', 'languages': ['Common', 'Dwarvish'], 'speed': 25, 'bonus_str': 0, 'bonus_dex': 0, 'bonus_con': 2, 'bonus_int': 0, 'bonus_wis': 1, 'bonus_cha': 0},
    {'name': 'Tiefling', 'languages': ['Common', 'Infernal'], 'speed': 30, 'bonus_str': 0, 'bonus_dex': 0, 'bonus_con': 0, 'bonus_int': 1, 'bonus_wis': 0, 'bonus_cha': 2},
    {'name': 'Vedalken', 'languages': ['Common', 'Vedalken'], 'speed': 30, 'bonus_str': 0, 'bonus_dex': 0, 'bonus_con': 0, 'bonus_int': 2, 'bonus_wis': 1, 'bonus_cha': 0}
]
chosen_race = random.choice(races)
player_level = 1
player_gold = 10.6
player_conscious = True
stat_str = 9
stat_con = 12
final_con = stat_con + chosen_race['bonus_con']
# Converting the stat to a modifier, (stat-10)//2
mod_str = (stat_str - 10) // 2
print(f'{chosen_race['name']} | CON base: {stat_con} | Racial Bonus: +{chosen_race['bonus_con']} | Final CON: {final_con}')
print(f'They are known to commonly speak {chosen_race['languages'][0]} and {chosen_race['languages'][1]}')