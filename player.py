#This has the player information and stats
from map import rooms
current_room = rooms["Room 1"]
player_stats = {"strength": 5,"defence": 5, "health": 100, "alive": True, "weapon":None, "experience": 0, "level": 1}
weapons = {"stick": (10), None:(0), "knife":(15), "gun":(30)}
inventory = []
credit = 100
