import time
import random

def main():
	print("\nWelcome to your first amateur Pokemon match!\n")
	time.sleep(2)

	def options():
		print("You can 'attack', 'use potion', 'use revive', 'switch pokemon', or 'see pokemon'.\nType 'help' for a reminder.")
	options()
	time.sleep(3)

	print("\nLet the battle begin!")
	time.sleep(2)
	print()

	# pokemon list, name, potions, revives, current pokemon index
	ash = Trainer([ash_charmander, ash_squirtle, ash_bulbasaur], "Ash", 4, 2, 0)
	gary = Trainer([gary_bulbasaur, gary_charmander, gary_squirtle], "Gary", 4, 2, 0)
	#ash = Trainer([ash_charmander, ash_squirtle], "Ash", 4, 2, 0)
	#gary = Trainer([gary_bulbasaur, gary_squirtle], "Gary", 4, 2, 0)

	ash_battle_list = [i.name for i in ash.pokemon_list]
	gary_battle_list = [i.name for i in gary.pokemon_list]

	def check_status():
		if ash.pokemon_remaining > 0 and gary.pokemon_remaining > 0:
			battle_list()
			check_current_pokemon()
			return True
		else:
			return False
	def battle_list():
		for pokemon in ash.pokemon_list:
			if pokemon.health == 0 or pokemon.ko == True:
				ash_battle_list[ash.pokemon_list.index(pokemon)] = strike(ash_battle_list[ash.pokemon_list.index(pokemon)])
			else:
				ash_battle_list[ash.pokemon_list.index(pokemon)] = pokemon.name
		for pokemon in gary.pokemon_list:
			if pokemon.health == 0 or pokemon.ko == True:
				gary_battle_list[gary.pokemon_list.index(pokemon)] = strike(gary_battle_list[gary.pokemon_list.index(pokemon)])
			else:
				gary_battle_list[gary.pokemon_list.index(pokemon)] = pokemon.name
	def check_current_pokemon():
		time.sleep(1)
		if ash.pokemon_list[ash.current_pokemon].ko == True:
			print(ash_battle_list)
			ash.forced_switch()
		elif gary.pokemon_list[gary.current_pokemon].ko == True:
			print(gary_battle_list)
			gary.forced_switch()
	def strike(name):
		result = ""
		for char in name:
			result = result + char + '\u0336'
		return result
	def attack_order():
		if ash.pokemon_list[ash.current_pokemon].speed > gary.pokemon_list[gary.current_pokemon].speed:
			ash.attack(gary)
			if gary.pokemon_list[gary.current_pokemon].ko == True:	
				check_status()
			else:
				time.sleep(1)
				print()
				gary.attack(ash)
		elif ash.pokemon_list[ash.current_pokemon].speed < gary.pokemon_list[gary.current_pokemon].speed:
			gary.attack(ash)
			if ash.pokemon_list[ash.current_pokemon].ko == True:
				check_status()
			else:
				time.sleep(1)
				print()
				ash.attack(gary)
		else:
			coin_toss = random.choice(["heads", "tails"])
			if coin_toss == "heads":
				gary.attack(ash)
				if ash.pokemon_list[ash.current_pokemon].ko == True:
					check_status()
				else:
					time.sleep(1)
					print()
					ash.attack(gary)
			else:
				ash.attack(gary)
				if gary.pokemon_list[gary.current_pokemon].ko == True:	
					check_status()
				else:
					time.sleep(1)
					print()
					gary.attack(ash)
	
	# Battle
	while check_status() == True:
		ash_turn_complete = False
		gary_turn_complete = False
		
		# Ash's turn
		print(f"\n\n|| Ash's {ash.pokemon_list[ash.current_pokemon].name} vs Gary's {gary.pokemon_list[gary.current_pokemon].name} ||\n\n")
		time.sleep(1)
		while ash_turn_complete == False:
			time.sleep(1)
			ash_attack = False
			ash_turn = input("What do you want to do, Ash?\n").lower()
			
			if ash_turn == "help":
				options()

			elif ash_turn == "see pokemon":
				print(ash_battle_list)

			elif ash_turn == "attack":
				ash_attack = True
				ash_turn_complete = True
			
			elif ash_turn == "use potion":
				print(ash_battle_list)
				if ash.use_potion():
					ash_turn_complete = True
			
			elif ash_turn == "use revive":
				print(ash_battle_list)
				if ash.use_revive():
					check_status()
					ash_turn_complete = True

			elif ash_turn == "switch pokemon":
				print(ash_battle_list)
				if ash.switch_pokemon():
					ash_turn_complete = True
			else:
				options()

		# Gary's turn
		print()
		while gary_turn_complete == False:
			time.sleep(1)
			gary_attack = False
			gary_turn = input("What do you want to do, Gary?\n").lower()
			
			if gary_turn == "help":
				options()

			elif gary_turn == "see pokemon":
				print(gary_battle_list)

			elif gary_turn == "attack":
				gary_attack = True
				gary_turn_complete = True
			
			elif gary_turn == "use potion":
				print(gary_battle_list)
				if gary.use_potion():
					gary_turn_complete = True
			
			elif gary_turn == "use revive":
				print(gary_battle_list)
				if gary.use_revive():
					check_status()
					gary_turn_complete = True

			elif gary_turn == "switch pokemon":
				print(gary_battle_list)
				if gary.switch_pokemon():
					gary_turn_complete = True
						
			else:
				options()

		time.sleep(1)
		print()

		# Attacks - order based on pokemon's speed
		if ash_attack and gary_attack == True:
			attack_order()
		elif ash_attack == True:
			ash.attack(gary)
		elif gary_attack == True:
			gary.attack(ash)

		time.sleep(1)

	# Winner announcement
	if gary.pokemon_remaining == 0:
		time.sleep(1)
		print("\nGary is all out of pokemon!")
		time.sleep(2)
		print("\nAsh wins!\n")
		time.sleep(2)
	elif ash.pokemon_remaining == 0:
		time.sleep(1)
		print("\nAsh is all out of pokemon!")
		time.sleep(2)
		print("\nGary wins!\n")
		time.sleep(2)

class Pokemon:
	def __init__(self, name, level, type, max_health, health, ko, speed):
		self.name = name
		self.level = level
		self.type = type
		self.max_health = max_health
		self.health = health
		self.ko = ko
		self.speed = speed

	def __repr__(self):
		return self.name

	def knock_out(self, trainer):
		self.ko = True
		trainer.pokemon_remaining -= 1
		print(f"{self.name} fainted!")

	def lose_health(self, hp_lost, trainer, other_trainer):
		self.health = max(self.health - hp_lost, 0)
		if self.health == 0:
			self.knock_out(other_trainer)
		else:
			print(f"{other_trainer}'s {self.name} now has {self.health} health")

	def gain_health(self, hp_gained):
		self.health = min(self.health + hp_gained, self.max_health)
		if self.health == self.max_health:
			print(f"{self.name} is fully healed!")
		else:
			print(f"{self.name} now has {self.health} health")

	def revive(self, trainer):
		self.health = self.max_health // 2
		self.ko = False
		trainer.pokemon_remaining += 1
		print(f"{self.name} has been revived! {self.name} has {self.health} health")

	def attack(self, trainer, other_trainer, other_pokemon):
		attack_multiplier = attack_multipliers.get(f"{self.type} vs {other_pokemon.type}")
		damage = int(self.level * attack_multiplier)
		if attack_multiplier == 2:
			extra_text = "It's super effective!"
		elif attack_multiplier == .5:
			extra_text = "It's not very effective..."
		else:
			extra_text = None
		print(f"{trainer}'s {self.name} attacked {other_trainer}'s {other_pokemon.name}!")
		time.sleep(2)
		if extra_text != None:
			print(extra_text)
			time.sleep(1)
		print(f"It did {damage} damage")
		time.sleep(1)
		other_pokemon.lose_health(damage, trainer, other_trainer)

attack_multipliers = {
	"Fire vs Water": .5, "Fire vs Grass": 2, "Fire vs Fire": 1,
	"Water vs Grass": .5, "Water vs Fire": 2, "Water vs Water": 1,
	"Grass vs Fire": .5, "Grass vs Water": 2, "Grass vs Grass": 1
	}

# name, level (for attacks), type, max_health, health, ko, speed
ash_charmander = Pokemon("Charmander", 20, "Fire", 50, 50, False, 6)
ash_squirtle = Pokemon("Squirtle", 20, "Water", 60, 60, False, 3)
ash_bulbasaur = Pokemon("Bulbasaur", 20, "Grass", 60, 60, False, 4)

gary_charmander = Pokemon("Charmander", 20, "Fire", 50, 50, False, 6)
gary_squirtle = Pokemon("Squirtle", 20, "Water", 60, 60, False, 3)
gary_bulbasaur = Pokemon("Bulbasaur", 20, "Grass", 60, 60, False, 4)

# Trainer has up to 6 pokemon in a list, number of potions, and current pokemon as a num
class Trainer:
	def __init__(self, pokemon_list, name, potions, revives, current_pokemon):
		self.pokemon_list = pokemon_list
		self.name = name
		self.potions = potions
		self.revives = revives
		self.current_pokemon = current_pokemon
		self.pokemon_remaining = len(pokemon_list)
		print(f"{self.name} sent out {self.pokemon_list[self.current_pokemon]}")
		time.sleep(1)

	def __repr__(self):
		return self.name

	def attack(self, other_trainer):
		if self.pokemon_list[self.current_pokemon].ko == True:
			print(f"{self.pokemon_list[self.current_pokemon]} has fainted. It can't attack!")
		else:
			self.pokemon_list[self.current_pokemon].attack(self, other_trainer, other_trainer.pokemon_list[other_trainer.current_pokemon])

	def use_potion(self):	
		if self.potions == 0:
				print("You don't have any potions left!")
		else:
			which_pokemon = input("Which pokemon do you want to heal?\n").lower().capitalize()
			in_list = False
			for pokemon in self.pokemon_list:
				if which_pokemon == pokemon.name:
					in_list = True
					if pokemon.health == pokemon.max_health:
						print(f"{pokemon} is already fully healed!")
						break
					elif pokemon.health == 0:
						print(f"{pokemon} must be revived first!")
					else:
						print(f"{self.name} used a potion on {pokemon.name}")
						time.sleep(1)
						pokemon.gain_health(20)
						self.potions -= 1
						if self.potions == 1:
							word = "potion"
						else:
							word = "potions"
						time.sleep(1)
						print(f"{self.name} has {self.potions} {word} left")
						return True
						break
			if in_list == False:
				print("You can't heal a pokemon you don't have!")

	def use_revive(self):
		if self.revives == 0:
			print("You don't have any revives left!")
		else:
			which_pokemon = input("Which pokemon do you want to revive?\n").lower().capitalize()
			in_list = False
			for pokemon in self.pokemon_list:
				if which_pokemon == pokemon.name:
					in_list = True
					if pokemon.health != 0:
						print(f"{pokemon} hasn't fainted!")
						break
					else:
						print(f"{self.name} used a revive on {pokemon.name}")
						time.sleep(1)
						pokemon.revive(self)
						self.revives -= 1
						if self.revives == 1:
							word = "revive"
						else:
							word = "revives"
						time.sleep(1)
						print(f"{self.name} has {self.revives} {word} left")
						return True
						break
			if in_list == False:
				print("You can't revive a pokemon you don't have!")

	def switch_pokemon(self):
		not_ko_count = 0
		for i in range(len(self.pokemon_list)):
			if self.pokemon_list[i].ko == False:
				not_ko_count += 1
		if not_ko_count <= 1:
			print("Your other pokemon have fainted!")
		else:
			which_pokemon = input("Who do you want to send out?\n" ).lower().capitalize()
			if which_pokemon == self.pokemon_list[self.current_pokemon].name:
				print(f"{which_pokemon} is already out!")
			elif which_pokemon != self.pokemon_list[self.current_pokemon].name:
				in_list = False
				for pokemon in self.pokemon_list:
					if which_pokemon == pokemon.name:
						in_list = True
						if pokemon.ko == True:
							print("Choose a pokemon that hasn't fainted!")
							break
						else:
							self.old_pokemon = self.current_pokemon
							self.current_pokemon = self.pokemon_list.index(pokemon)
							print(f"{self.name} switched out {self.pokemon_list[self.old_pokemon].name} for {self.pokemon_list[self.current_pokemon].name}")
							return True
							break
				if in_list == False:
					print("Nice try. Next time choose a pokemon you actually have!")

	'''def forced_switch(self):
					current_pokemon_fainted = True
					while current_pokemon_fainted == True:
						which_pokemon = input(f"Who do you want to send out, {self.name}?\n").lower().capitalize()
						if which_pokemon == self.pokemon_list[self.current_pokemon].name:
							print(f"{which_pokemon} fainted!")
							time.sleep(1)
						elif which_pokemon != self.pokemon_list[self.current_pokemon].name:
							in_list = False
							for pokemon in self.pokemon_list:
								if which_pokemon == pokemon.name:
									in_list = True
									if pokemon.ko == True:
										print("Choose a pokemon that hasn't fainted!")
										time.sleep(1)
										break
									else:
										self.old_pokemon = self.current_pokemon
										self.current_pokemon = self.pokemon_list.index(pokemon)
										print(f"{self.name} switched out {self.pokemon_list[self.old_pokemon].name} for {self.pokemon_list[self.current_pokemon].name}")
										return True
										break
							if in_list == False:
								print("Nice try. Next time choose a pokemon you actually have!")
								time.sleep(1)
			'''
	def forced_switch(self):
		while True:
			which_pokemon = input(f"Who do you want to send out, {self.name}?\n").lower().capitalize()
			if which_pokemon == self.pokemon_list[self.current_pokemon].name:
				print(f"{which_pokemon} fainted!")
				time.sleep(1)
			elif which_pokemon != self.pokemon_list[self.current_pokemon].name:
				pokemon_list = [pokemon.name for pokemon in self.pokemon_list]
				if which_pokemon in pokemon_list:
					pokemon_index = pokemon_list.index(which_pokemon)
					actual_pokemon_object = self.pokemon_list[pokemon_index]
					if actual_pokemon_object.ko == True:
						print("Choose a pokemon that hasn't fainted!")
						time.sleep(1)
						break
					else:
						self.old_pokemon = self.current_pokemon
						self.current_pokemon = pokemon_index
						print(f"{self.name} switched out {self.pokemon_list[self.old_pokemon].name} for {self.pokemon_list[self.current_pokemon].name}")
						return True
						break
				else:
					print("Nice try. Next time choose a pokemon you actually have!")
					time.sleep(1)
			

main()

'''def main():
	time.sleep(2)
	print()
	
	ash.attack(gary)
	time.sleep(2)
	print()
	
	gary.attack(ash)
	time.sleep(2)
	print()

	gary.switch_pokemon(2)
	time.sleep(2)
	print()

	ash.attack(gary)
	time.sleep(2)
	print()
	
	ash.attack(gary)
	time.sleep(2)
	print()
	
	gary.attack(ash)
	time.sleep(2)
	print()

	ash.use_potion()
	time.sleep(2)
	print()

	gary.attack(ash)
	time.sleep(2)
	print()

	ash.switch_pokemon(2)
	time.sleep(2)
	print()

	gary.attack(ash)
	time.sleep(2)
	print()

	gary.attack(ash)
	time.sleep(2)
	print()

	ash.attack(gary)
	time.sleep(2)
	print()

	gary.attack(ash)
	time.sleep(2)
	print()

	ash.attack(gary)
	time.sleep(2)
	print()

	gary.attack(ash)
	time.sleep(2)
	print()

	ash.attack(gary)
	time.sleep(2)
	print()
'''


