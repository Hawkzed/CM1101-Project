#This has the player information and stats
from map import rooms
current_room = rooms["Room 2"]
player_stats = {"strength": 5,"defence": 5, "health": 100, "weapon":None, "credits": 50}
weapons = {"stick": (15), None:(10), "knife":(20), "gun":(30)}
inventory = []

for key,value in inventory:
	if value["id"] == "1":
		player_stats["strength"] += 5
	elif value["id"] == "2":
		player_stats["defence"] += 5
	elif value["id"] == "3":
		player_stats["health"] += 5
	elif value["id"] == "4":
		player_stats["strength"] += 5
		player_stats["defence"] += 5
		player_stats["health"] += 5
