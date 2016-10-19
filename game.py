#This is the main game engine#This is the main game engine
from normalise_input import normalise_inputs
from combat import *
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


def item_list(items):
	return ",".join(item["name"] for item in items)
# returns the items as a a string

	
def print_room_items(room):
	# tells the user which items are present in the room
	if len(room["items"]) != 0:
		print("There is " + str(item_list(room["items"])) + " here.")
		print('')
			

def print_inv_items(items):
	# Displays the player inventory
	print("You have " + str(item_list(room["items"])) + ".")


# takes a dictionary of exits and a direction returns the name of the exit it leads to
# example ( exit_leads_to(rooms["Room1"]["exits"], "south"))
def exit_leads_to(exits, direction):
	return rooms[exits[direction]]["name"]


# prints a line of a menu of exits. arguments are the name of the exit and the
# name of the room it leads to. example ("east","Room2")
def print_exit(direction, leads_to):
	print("GO " + direction.upper() + " to " + leads_to + ".")


# prints actions available to the player (add actions)
def print_menu(exits, room_items, inventory, room_stall):
	print("You can:")
	for direction in exits:
		print_exit(direction, exit_leads_to(exits, direction))
	if len(current_room["stall"]) > 0:
		for item in room_stall:
			print("BUY " + str(item["id"].upper()) + " to buy" + str(item["name"]) + " for " + str(item["cost"])
                  + " credits.")
		print("BUY RETIRE to retire from the game!")
		print("You have " + str(player_stats["credits"]) + " credits available.")
	for item in room_items:
		print("TAKE " + str(item["id"].upper() + " to take " + str(item["name"])))
	print("What do you want to do?")


# checks if the exit is valid returns True if valid else False
# example: is_valid_exit(rooms["room1"]["exits"], "north") == True
def is_valid_exit(exits, chosen_exit):
	return chosen_exit in exits


# updates the current room based on the direction (example execute_go("east"))
def execute_go(direction):
	global current_room
	if direction in current_room["exits"].keys():
		new_position = current_room["exits"][direction]
		current_room = rooms[new_position]

		#This checks the type of the room and randomises the description
		#Check end of map.py file for all the decriptions in use along with their numbers

		if current_room["name"] != "Shop":
			if current_room["type"] == "enemy":
				i = random.randrange(1,4)
			elif current_room["type"] == "empty":
				i = random.randrange(5,7)
			elif current_room["type"] == "loot":
				i = random.randrange(8,10)
			elif current_room["type"] == "boss":
				i = 11
			elif current_room["type"] == "civil":
				i = random.randrange(12,14)

			current_room["description"] = descriptions[i]
	else:
		print("You cannot go there.")

	for line in inventory:
		if line["id"] == "1":
			player_stats["strength"] += 5
			inventory.remove(line)
		elif value["id"] == "2":
			player_stats["defence"] += 5
			inventory.remove(line)
		elif value["id"] == "3":
			player_stats["health"] += 25
			inventory.remove(line)
		elif value["id"] == "4":
			player_stats["strength"] += 5
			player_stats["defence"] += 5
			player_stats["health"] += 50
			inventory.remove(line)


def execute_drop(item_id):
	for item in inventory:
		if item_id == item["id"]:
			inventory.remove(item)
			current_room["items"].append(item)
			print("you have dropped " + str(item["name"]))
			break
		else:
			print("You cannot drop that")

def execute_take(item_id):
	for item in current_room["items"]:
		if item_id == item["id"]:
			inventory.append(item)
			current_room["items"].remove(item)
			print("you have taken " + str(item["name"]))
			break
		else:
			print("You cannot take that.")

def execute_buy(user_input):
    if user_input == "1":
        if player_stats["credits"] >= item_1["cost"]:
            inventory.append(item_1)
            player_stats["credits"] = int(player_stats["credits"]) - int(item_1["cost"])
        else:
            print("You do not have enough credits")
    elif user_input == "2":
        if player_stats["credits"] >= item_2["cost"]:
            inventory.append(item_2)
            player_stats["credits"] = int(player_stats["credits"]) - int(item_2["cost"])
        else:
            print("You do not have enough credits")
    elif user_input == "3":
        if player_stats["credits"] >= item_3["cost"]:
            inventory.append(item_3)
            player_stats["credits"] = int(player_stats["credits"]) - int(item_3["cost"])
        else:
            print("You do not have enough credits")
    elif user_input == "4":
        if player_stats["credits"] >= item_4["cost"]:
            inventory.append(item_4)
            player_stats["credits"] = int(player_stats["credits"]) - int(item_4["cost"])
        else:
            print("You do not have enough credits")
    elif user_input == "retire":
    	retire()



#  prints the menu of actions using print_menu() function.
#It then prompts the player to type an action. (add actions)
def menu(exits, room_items, inventory, room_stall):
	if current_room["type"] == "loot":
		print("You received 50 credits\n")
		player_stats["credits"] += 50
		current_room["type"] = "empty"

	print_menu(exits, room_items, inventory, room_stall)
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
	elif command[0] == "take":
		if len(command) > 1:
			execute_take(command[1])
		else:
			print("Take what?")
	elif command[0] == "drop":
		if len(command) > 1:
			execute_drop(command[1])
		else:
			print("Drop what?")
	elif command[0] == "buy":
		if len(command) > 1:
			execute_buy(command[1])
		else:
			print("Buy what?")

def print_player():
	for x in player_stats:
		print(x, ": ", player_stats[x])

def main():
	# Main game loop
	print("""  
OUT IN THE DEPTHS OF SPACE. A STATION STRANDED. 
IT HAS BEEN ATTACKED BY CREATURES HELLBENT ON DESTROYING THE HUMAN RACE. 
THEY DONT BELIEVE IN OUR VALUES OR VIRTUES.
TO THEM WE ARE IMPURE, A CURSE APON THE MULTIVERSE. 
BUT YOU HAVE BEEN SENT BY SPACE COMMAND TO STOP THESE FORCES OF EVIL AND SEND THEM BACK TO THE DARKEST CORNERS OF DEEP SPACE
FROM WHICH THEY CAME.

YOUR MISSION, SHOULD YOU ACCEPT IT:

1) RESCUE REMAINING SURVIVERS OF THE ISS: INTERVENTION

2) INSPECT THE SHIP AND SEE WHAT YOU CAN SALVAGE

3) FINALLY DESTROY ANY CREATURES THAT CROSS YOUR PATH AND MAKE THEM PAY FOR THE LIVES THEY HAVE TAKEN FROM US! 

GOOD LUCK CAPTAIN.

FOR LIFE AND ETERNITY. \n
""")
	input("continue... \n")
	while True:
	# Display game status (room description, inventory etc.)
		print_room(current_room)
		input("continue...\n")
		if current_room["type"] == "enemy" or current_room["type"] == "boss":
			battle(current_room)
			if player_stats["health"] < 1:
				retire()
	# Show the menu with possible actions and ask the player
		command = menu(current_room["exits"], current_room["items"], inventory, current_room["stall"])
	# Execute the player's command
		execute_command(command)



def retire():
	#Ends the game. Depending wether the player died or chose to retire, prints a different message and calculates/shows the final score.
	#Add retire() to use. It will exit the program once done.

	if player_stats["health"] > 0:
		print("\nYou have escaped from the ship, barely holding on to your life and your sanity.\n")
	else:
		print("\nYou died fighting. While no one will remember you, you feel you have made a difference.\n")

	print_player()
	finalscore = player_stats["credits"] + player_stats["health"] + player_stats["strength"]*5 + player_stats["defence"]*5
	print("Your final score is: %d" % (finalscore))
	input("Please enter anything to end the game.")
	exit()

if __name__ == "__main__":
	main()
