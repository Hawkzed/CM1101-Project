#This has the player information and stats
from map import rooms
current_room = rooms["Room 2"]
player_stats = {"strength": 5,"defence": 5, "health": 100, "alive": True, "weapon":None, "credits": 50, "level": 1}
weapons = {"stick": (10), None:(0), "knife":(15), "gun":(30)}
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
