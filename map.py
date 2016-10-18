#This contains the map information
import random
from player import *
from items import *


room_1 = {
    "name": "Room 1",
	"stall":[],
	"description":"There is an enemy here.",
    "enemy": True,
	"items": [],
    "exits": {"north": "Room 5"}

}

room_2 = {
    "name": "Room 2",
    "enemy": True,
	"items": [],
	"description":"There is an enemy here.",
	
	"stall":[],

    "exits": {"east": "Room 3", "south":"Shop"}
}
room_3 = {
    "name": "Room 3",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"west": "Room 2", "north": "Room 7"}
}
room_4 = {
    "name": "Room 4",
    "enemy": False,
	"stall":[],
    "description":"There is treasure here.",
	"items": [],
    "exits": {"north": "Room 8"}
}

room_5 = {
    "name": "Room 5",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"north": "Room 10", "east": "Room 6", "south": "Room 1"}
}

room_6 = {
    "name": "Room 6",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"west": "Room 5"}
}
room_7 = {
    "name": "Room 7",
    "enemy": False,
	"stall":[],
    "description":"There is treasure here.",
	"items": [],
    "exits": {"north": "Room 12", "south": "Room 3"}
}
room_8 = {
    "name": "Room 8",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"north": "Room 13", "east": "Room 9", "south": "Room 4"}
}

room_9 = {
    "name": "Room 9",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"east": "Room 10", "west": "Room 8"}
}

room_10 = {
    "name": "Room 10",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"north": "Room 14", "west": "Room 9", "east": "Room 11", "south": "Room 5"}
}
room_11 = {
    "name": "Room 11",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"north": "Room 15", "west": "Room 10", "east": "Room 12"}
}
room_12 = {
    "name": "Room 12",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"south": "Room 7", "west": "Room 11", "north": "Room 16"}
}

room_13 = {
    "name": "Room 13",
    "enemy": False,
	"stall":[],
    "description":"There are some survivors here.",
	"items": [],
    "exits": {"south": "Room 8"}
}
room_14 = {
    "name": "Room 14",
    "enemy": False,
	"stall":[],
    "description":"There is treasure here.",
	"items": [],
    "exits": {"south": "Room 10"}
}

room_15 = {
    "name": "Room 15",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"north": "Room 17", "east": "Room 16", "south": "Room 11"}
}

room_16 = {
    "name": "Room 15",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"south": "Room 12", "west": "Room 15"}
}

room_17 = {
    "name": "Room 17",
    "enemy": True,
	"stall":[],
    "description":"There is an enemy here.",
	"items": [],
    "exits": {"north": "Room 18", "south": "Room 15"}
}

room_18 = {
    "name": "Room 18",
    "enemy": True,
	"stall":[],
    "description":"There is despair here.",
	"items": [],
    "exits": {"south": "Room 17"}
}

room_shop = {
    "name": "Shop",
	"enemy": False,
    "description": "A small robot stands behind a counter",
    "stall": [item_1, item_2, item_3],
	"items": [],
	"exits": {"north": "Room 2"}
}			  

rooms = {
    "Room 1": room_1,
    "Room 2": room_2,
    "Room 3": room_3,    
    "Room 4": room_4,
	"Room 5": room_5,
    "Room 6": room_6,
    "Room 7": room_7,    
    "Room 8": room_8,
	"Room 9": room_9,
    "Room 10": room_10,
    "Room 11": room_11,    
    "Room 12": room_12,
	"Room 13": room_13,
    "Room 14": room_14,
    "Room 15": room_15,    
    "Room 16": room_16,
	"Room 17": room_17,
    "Room 18": room_18,
	"Shop": room_shop
}

descriptions = {
    1 : """
    The door begrudgingly swings open and you
    walk in, making sure to stay silent.
    It's dark and a shiver runs down your spine
    as you spy someone, or something, standing
    in the middle of the room...
    """,
    2 : """
    You slip in through the slightly ajar door
    A musty, dank order creep into my nose. At first
    it seems as there's nothing there but then,
    you start hearing breathing that is not your own.
    A shadow moves...""",
    3: """
    The gold glint in the corner of your eye instantly
    catches your attention as you enter,
    no lock, yet untouched,
    precious resources may lie inside! """,

    4 :""" Silence in here, 
    all that remains are the screams of those once here,
    just as the blackness of 
    space... nothing is here... nothing.""",

    5 :""" BOOM, BOOM, BOOM, 
    you here the thud of terror aproach you!
    it has awoken, it is fresh, 
    unfortunately it is HUNGRY! """,

    6: """ What approaches you is daunting,
    its objective is cruel.
    if base could see you now,
    they would think you're a fool.""",

    7: """ What happened here is unspeakable,
     limbs hanging from the ovehead wires.
     drip... drip... drip.""",

    8: """ You enter only to find a room untouched,
    this was once the dining room,
    where colleagues would come together to discuss reaserch and to enjoy conversation.
    Food still on the plate, water still in the cups.
    There had been an evacuation here.""",

    9 :""" A light blinks in the corner, you go over to it, 
    only to find it open.
    You look inside... a small fortune awaits you!
    Take it quickly, at least now you will die a rich man.""",

    10 :""" The object in the corner is open,
    inside there are weapons of dubious value.
    Enjoy."""
}
