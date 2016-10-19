#	This module contains methods and functions for the combat system.
import math
import random
import time
from game import *
from enemy import *
from player import *
from normalise_input import remove_punct


xpPoints = 0

def battle():

	#Enemy stats set to enemy pirate for now to test the code. Needs to be randomised by dificulty instead
	global enemy_stats
	global current_room
	
	rand = random.randrange(1, 100)
	
	if rand >= 90:
		enemy_stats = enemy_pirate_armsman
		enemy_stats["health"] = 100
	elif rand >= 70 and rand < 90:
		enemy_stats = enemy_pirate_corsair
		enemy_stats["health"] = 100
	elif rand < 70:
		enemy_stats = enemy_pirate
		enemy_stats["health"] = 100
	elif current_room["type"] == "boss":
		enemy_stats = enemy_pirate_ravager
		enemy_stats["health"] = 100
	
	print(enemy_stats["name"].upper(), "\n" + enemy_stats["description"], "\n")

	""" The use of this function is to loop a battle encounter until one of 
		the parties involved is dead. It gives the player their options and 
		runs different functions depending on what they choose.

	"""
	escape = False
	while (player_stats["health"] > 0 and enemy_stats["health"] > 0) or escape == True:

		print("What would you like to do? You can:")
		print("1. Attack")
		print("2. Attack 5 times")
		print("3. Attack until dead")
		print("4. Escape")
		x = input("")
		x = remove_punct(x).lower().strip()
		if x == 'attack' or x == "1":
			compute_turn_damage()
		elif x == "attack 5 times" or x == "2":
			for _ in " " * 5:
				compute_turn_damage()
				time.sleep(0.5)
				if player_stats["health"] < 0 or enemy_stats["health"] < 0:
					break
		elif x == "attack until dead" or x == "3":
			while player_stats["health"] > 0 and enemy_stats["health"] > 0:
				compute_turn_damage()
				time.sleep(0.5)
		elif x == "escape" or x == "4":
			escapeChance = escape_dependent_on_health(player_stats)
			escape = escape_likelyhood(escapeChance)
			if escape == True:
				print("You escape the room successfully")
				break
			else:
				print("you must STAND and FIGHT!") # or print nothing and continue fighting
				compute_enemy_damage()

	if enemy_stats["health"] < 1:

		player_stats["credits"] + xpPoints
		current_room["type"] = "empty"
		return(False)
	else:
		return(True)

def compute_turn_damage():
	
	""" The use of this function is to calculate the events of a turn 
		where the player attacks the enemy. It calculates how much
		damage is dealt to the player and the enemy	that they are fighting,
		and awards experience to the player	accordingly. It then prints
		the events of that turn.
		
		Tests are not available for this function since it uses randomised
		variables in its operation. """

	player_incre = player_takes_damage(player_stats, enemy_stats)
	enemy_incre = enemy_takes_damage(player_stats, enemy_stats)
	
	player_stats["health"] -= player_incre
	enemy_stats["health"] -= enemy_incre
	print("The player deals %d damage to the enemy, leaving it at %d health!" % (enemy_incre, enemy_stats["health"]))
	print("The enemy deals %d damage to the player, leaving them at %d health!" % (player_incre, player_stats["health"]))
	
def compute_enemy_damage():
	
	""" The use of this function is to calculate the events of a turn 
		where the player attacks the enemy. It calculates how much
		damage is dealt to the player and the enemy	that they are fighting,
		and awards experience to the player	accordingly. It then prints
		the events of that turn.
		
		Tests are not available for this function since it uses randomised
		variables in its operation. """

	player_incre = player_takes_damage(player_stats, enemy_stats)
	
	player_stats["health"] -= player_incre
	print("The enemy deals %d damage to the player, leaving them at %d health!" % (player_incre, player_stats["health"]))

def compute_experience(damage):

	""" The use of this function is to calculate how much experience the player
		will gain for each hit that they successfully land on an enemy. It
		takes the argument 'damage', and generates a random amount
		of experience based on how much damage the player deals.
		
		Tests are not available for this function since it uses randomised
		variables in its operation.	"""

	xpPoints = random.randrange(0, (enemy_takes_damage*2))
	return(xpPoints)

def player_takes_damage(player, enemy):

	""" The use of this function is to calculate how much damage the player 
		will deal with each strike of their weapon. It takes the following 
		arguments: 'player', 'enemy', and 'damage'. It takes into account 
		the statistics of the player and enemy, and changes the health of
		the enemy depending on a calculation using a random variable with
		a minimum range of 1, and a maximum range that is equal to the 
		enemy's.

		Tests are not available for this function since it uses randomised
		variables in its operation.	"""

	damage = enemy["strength"] + random.randrange(1, enemy["strength"])
	return(damage)


def enemy_takes_damage(player, enemy):

	""" The use of this function is to calculate how much damage the enemy 
		will deal with each strike. It takes the following arguments:
		'player' and 'enemy'. It takes into account the statistics of the 
		player and enemy, and changes the health of the enemy depending on
		a calculation using a random variable with a minimum range of 1,
		and a maximum range that is equal to the player's strength.

		Tests are not available for this function since it uses randomised
		variables in its operation.	"""

	damage = player["strength"] + random.randrange(1, player["weapon"])
	return(damage)
	
def escape_dependent_on_health(player_stats):
	if player_stats["health"] >= 75:
		chance_of_escape = 60
	
	elif player_stats["health"] >= 50:
		chance_of_escape = 40
	
	else:
		chance_of_escape = 20
			
	return (chance_of_escape)

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
