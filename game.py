#This is the main game engine#This is the main game engine
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
    for item in inventory:
        print("DROP " + str(item["id"]).upper() + " to drop " + str(item["name"]) + ".")
    if len(current_room["stall"]) > 0:
        for item in room_stall:
            print("BUY " + str(item["id"].upper()) + " for " + str(item["cost"]) + " credits.")
        for item in inventory:
            print("SELL " + str(item["id"]).upper() + " to receive " + str(0.5*int(item["cost"])) + " credits.")
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

        i = random.randrange(1,3)
        current_room["description"] = descriptions[1]
    else:
        print("You cannot go there.")

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

def execute_buy(item_id):
    global credit
    # credit is made global as the value is being changed
    for item in current_room["stall"]:
        # searches the room for a stall dictionary
        if item_id == item["id"]:
            if credit > item["cost"]:
                # checks you have enough money
                inventory.append(item)
                current_room["stall"].remove(item)
                credit = credit - item["cost"]
                # adds the item to your inv and then changes your credits
                print("you have bought " + str(item["name"]))
                print("you have " + str(credit) + " credits")
                break
            else:
                print("You do not have enough credits")

def execute_sell(item_id):
    global credit

    for item in inventory:
        if item_id == item["id"]:
            inventory.remove(item)
            credit = credit + int((0.5 * int(item["cost"])))
            current_room["stall"].append(item)
            print("you have sold " + str(item["name"]) + " you've gained, " + str(int(0.5*item["cost"])) + " credits.")
            print("you have " + str(credit) + " credits")
            # same thing as buy but the other way around, but only gives you half of the credits back
            break
        else:
            print("You cannot sell that")


#  prints the menu of actions using print_menu() function.
#It then prompts the player to type an action. (add actions)
def menu(exits, room_items, inventory, room_stall):
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
    elif command[0] == "sell":
        if len(command) > 1:
            execute_sell(command[1])
        else:
            print("Sell what?")

    

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
