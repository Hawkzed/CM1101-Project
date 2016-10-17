#This contains the map information
import random
from player import *

room_1 = {
    "name": "Room 1",

    "description":
    """
    You enter the space station.
    There is an enemy here.""",

    "exits": {"north": "Room 4", "east": "Room 2"}
}

room_2 = {
    "name": "Room 2",

    "description":"There is an enemy here",

    "exits": {"north": "Room 3", "west": "Room 1"}
}
room_3 = {
    "name": "Room 3",

    "description":"There is an enemy here",

    "exits": {"south": "Room 2", "west": "Room 4"}
}
room_4 = {
    "name": "Room 4",

    "description":"There is an enemy here",

    "exits": {"south": "Room 1", "east": "Room 3"}
}



rooms = {
    "Room 1": room_1,
    "Room 2": room_2,
    "Room 3": room_3,    
    "Room 4": room_4,
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