# player escape
# assuming player health is out of 100 otherwise change accordingly

import random

# chance of escape is dependent on players current health and is lower the lower the health so that game is not too easy.

def escape_dependent_on_health(player_stats,chance_of_escape)
for i in player_stats["health"]:
		if i >= 75:
			chance_of_escape = 40
		
		elif i >= 50:
			chance_of_escape = 30
		
		else:
			chance_of_escape = 20
pass

# statement for returning player_escape function which will then move Player to other room (maybe safe, maybe not?) 
# range in brackets can be changed when range of players health is known

def escape_likelyhood(chance_of_escape):
	
	random_chance = random.uniform(1,100)
	
	if (random_chance < chance_of_escape):
		return True
	else:
		return False

# function that will move player to another room if the chance is in their favor otherwise they dont move room and a motivational message 
# tells them to stand and fight



def player_escape(room,escape_likelyhood):
	# if user types in escape
	if user_input == "escape":
		
		if escape_likelyhood == True:
			print("code to move room")/ current_room = move(exits, direction) # if it stays the same as that in the template
		
		elif escape_likelyhood == False:
			print("you must STAND and FIGHT!") # or print nothing and continue fighting
	
	else: return
# move room function(same as one in game template) or different if their is random generation
 









