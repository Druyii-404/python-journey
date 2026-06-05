import random

title = 'D&D Character Generator'
races = ['Bugbear', 'Half-Orc', 'Tiefling', 'Dragonborn', 'Gnome']
chosen_race = random.choice(races)
player_level = 1
player_gold = 10.6
player_conscious = True
stat_str = 9
# Converting the stat to a modifier, (stat-10)//2
mod_str = (stat_str - 10) // 2
print(title)
print(f'Character Level: {player_level}')
print(f'Gold: {player_gold}')
print(f'Conscious: {player_conscious}')
print(f'Strength: {stat_str} Modifier: {mod_str}')
print(f'You got the {chosen_race} race out of a possible {len(races)}!')