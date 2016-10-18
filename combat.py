#	This module contains methods and functions for the combat system.
import math
import random
from game import *
from enemy import *
from player import *

#Enemy stats set to enemy pirate for now to test the code. Needs to be randomised by dificulty instead
enemy_stats = enemy_pirate
xpPoints = 0

def battle():


	print(enemy_stats["name"].upper(), "\n" + enemy_stats["description"], "\n")

	""" The use of this function is to loop a battle encounter until one of 
		the parties involved is dead. It gives the player their options and 
		runs different functions depending on what they choose.

	"""
	global current_room
	while player_stats["health"] > 0 and enemy_stats["health"] > 0:

		print("What would you like to do? You can:")
		print("Attack")
		x = input("")
		if x == "attack" or "Attack":
			compute_turn_damage()

	if enemy_stats["health"] < 1:
		player_stats["gold"] + xpPoints
		current_room["enemy"] = False
		return

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
