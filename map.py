#This contains the map information
import random
from player import *

room_1 = {
    "name": "Room 1",
	
	"description":"There is an enemy here.",

    "exits": {"north": "Room 5"}
}

room_2 = {
    "name": "Room 2",

	"description":
    """
    You enter the space station.
    There is a chill in thr air.""",

    "exits": {"east": "Room 3"}
}
room_3 = {
    "name": "Room 3",

    "description":"There is an enemy here.",

    "exits": {"west": "Room 2", "north": "Room 7"}
}
room_4 = {
    "name": "Room 4",

    "description":"There is treasure here.",

    "exits": {"north": "Room 8"}
}

room_5 = {
    "name": "Room 5",

    "description":"There is an enemy here.",

    "exits": {"north": "Room 10", "east": "Room 6", "south": "Room 1"}
}

room_6 = {
    "name": "Room 6",

    "description":"There is an enemy here.",

    "exits": {"west": "Room 5"}
}
room_7 = {
    "name": "Room 7",

    "description":"There is treasure here.",

    "exits": {"north": "Room 12", "south": "Room 3"}
}
room_8 = {
    "name": "Room 8",

    "description":"There is an enemy here.",

    "exits": {"north": "Room 13", "east": "Room 9", "south": "Room 4"}
}

room_9 = {
    "name": "Room 9",

    "description":"There is an enemy here.",

    "exits": {"east": "Room 10", "west": "Room 8"}
}

room_10 = {
    "name": "Room 10",

    "description":"There is an enemy here.",

    "exits": {"north": "Room 14", "west": "Room 9", "east": "Room 11", "south": "Room 5"}
}
room_11 = {
    "name": "Room 11",

    "description":"There is an enemy here.",

    "exits": {"north": "Room 15", "west": "Room 10", "east": "Room 12"}
}
room_12 = {
    "name": "Room 12",

    "description":"There is an enemy here.",

    "exits": {"south": "Room 7", "west": "Room 11", "north": "Room 16"}
}

room_13 = {
    "name": "Room 13",

    "description":"There are some survivors here.",

    "exits": {"south": "Room 8"}
}
room_14 = {
    "name": "Room 14",

    "description":"There is treasure here.",

    "exits": {"south": "Room 10"}
}

room_15 = {
    "name": "Room 15",

    "description":"There is an enemy here.",

    "exits": {"north": "Room 17", "east": "Room 16", "south": "Room 11"}
}

room_16 = {
    "name": "Room 15",

    "description":"There is an enemy here.",

    "exits": {"south": "Room 12", "west": "Room 15"}
}

room_17 = {
    "name": "Room 17",

    "description":"There is an enemy here.",

    "exits": {"north": "Room 18", "south": "Room 15"}
}

room_18 = {
    "name": "Room 18",

    "description":"There is despair here.",

    "exits": {"south": "Room 17"}
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
    A shadow moves..."""
}