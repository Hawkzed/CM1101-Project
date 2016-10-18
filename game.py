#This is the main game engine
from normalise_input import normalise_inputs
from player import *
from map import *
from enemy import *
from items import *
import time
import random




# prints current room (example : print_room(rooms["Room1"])
def print_room(room):
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()


# takes a dictionary of exits and a direction returns the name of the exit it leads to
# example ( exit_leads_to(rooms["Room1"]["exits"], "south"))
def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


# prints a line of a menu of exits. arguments are the name of the exit and the
# name of the room it leads to. example ("east","Room2")
def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")


# prints actions available to the player (add actions)
def print_menu(exits):
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction)
	for item in inventory:
		print("DROP " + str(item["id"]).upper() + " to drop " + str(item["name"]) + ".")
    for item in room_stall:
		print("BUY " + str(item["id"].upper()) + " for " + str(item["cost"]) + " credits.")
    if len(current_room["stall"]) > 0:
		for item in inventory:
			print("SELL " + str(item["id"]).upper() + " to sell and receive " + str(0.5*int(item["cost"])) " credits."
	    
		   
	
    print("What do you want to do?")


# checks if the exit is valid returns True if valid else False
# example: is_valid_exit(rooms["room1"]["exits"], "north") == True
def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


# updates the current room based on the direction (example execut_go("east"))
def execute_go(direction):
    global current_room
    if direction in current_room["exits"].keys():
        new_position = current_room["exits"][direction]
        current_room = rooms[new_position]

        i = random.randrange(1,3)
        current_room["description"] = descriptions[1]
    else:
        print("You cannot go there.")


#  prints the menu of actions using print_menu() function.
#It then prompts the player to type an action. (add actions)
def menu(exits):
    print_menu(exits)
    user_input = input("> ")
    normalised_user_input = normalise_inputs(user_input)
    return normalised_user_input


# returns the room the player will move in.
#example (move(rooms["Room1"]["exits"], "north")---> rooms["Room4"])
def move(exits, direction):
    return rooms[exits[direction]]

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")


def main():
    # Main game loop
	while True:
	    # Display game status (room description, inventory etc.)
	    print_room(current_room)
	    input("continue...\n")

	    # Show the menu with possible actions and ask the player
	    command = menu(current_room["exits"])

		# Execute the player's command
	    execute_command(command)


if __name__ == "__main__":
	main()
