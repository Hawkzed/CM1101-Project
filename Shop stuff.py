room_shop = {
    "name": "Shop",
    "description": "A small robot stands behind a counter",
    "stall": [item_1, item_2, item_3]

}

    
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
            credit = credit + int((0.5*int(item["cost"])))
            current_room["stall"].append(item)
            print("you have sold " + str(item["name"]) + " you have gained, " + str(int(0.5*item["cost"])) + " credits.")
            print("you have " + str(credit) + " credits")
            # same thing as buy but the other way around, but only gives you half of the credits back
            break
        else: 
            print("You cannot sell that")
