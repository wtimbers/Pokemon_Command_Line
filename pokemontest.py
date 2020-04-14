import time
import random

# Force a user to switch away from a fainted pokemon
# weird spaces when repeating turn


def main():
	'''	print("\nWelcome to your first amateur Pokemon match!")
	time.sleep(2)

	print("\nYou can 'attack', 'use potion', 'use revive', 'switch pokemon', or 'see pokemon'.\nType 'help' for a reminder.\n")
	time.sleep(4)

	print("Let the battle begin!")
	time.sleep(2)
	print("\n")'''

	# pokemon list, name, potions, revives, current pokemon index
	#ash = Trainer([ash_charmander, ash_squirtle, ash_bulbasaur], "Ash", 4, 2, 0)
	#gary = Trainer([gary_charmander, gary_squirtle, gary_bulbasaur], "Gary", 4, 2, 2)

	ash = Trainer([ash_charmander], "Ash", 4, 2, 0)
	gary = Trainer([gary_bulbasaur], "Gary", 4, 2, 0)

	def check_status():
		if ash.pokemon_remaining & gary.pokemon_remaining > 0:
			return True
		else:
			return False

	while check_status() == True:
		ash_turn_complete = False
		gary_turn_complete = False
		ash_battle_list = [str(i) for i in ash.pokemon_list]
		gary_battle_list = [str(i) for i in gary.pokemon_list]
		
		# Ash's turn
		#print(f"\nAsh's {ash.pokemon_list[ash.current_pokemon].name} vs Gary's {gary.pokemon_list[gary.current_pokemon].name}\n")
		print()
		while ash_turn_complete == False:
			for pokemon in ash.pokemon_list:
				if pokemon.health == 0 or pokemon.ko == True:
					ash_battle_list[ash.pokemon_list.index(pokemon)] = strike(ash_battle_list[ash.pokemon_list.index(pokemon)])
				else:
					ash_battle_list[ash.pokemon_list.index(pokemon)] = pokemon

			time.sleep(1)
			ash_attack = False
			ash_turn = input("What do you want to do, Ash?\n").lower()
			
			if ash_turn == "help":
				print("You can 'attack', 'use potion', 'revive', 'switch pokemon', or 'see pokemon'.\nType 'help' for a reminder.")

			elif ash_turn == "see pokemon":
				print(ash_battle_list)

			elif ash_turn == "attack":
				ash_attack = True
				ash_turn_complete = True
			
			elif ash_turn == "use potion":
				if ash.use_potion():
					ash_turn_complete = True
			
			elif ash_turn == "use revive":
				if ash.use_revive():
					ash_turn_complete = True

			elif ash_turn == "switch pokemon":
				if ash.switch_pokemon():
					ash_turn_complete = True
			else:
				print("You can 'attack', 'use potion', 'revive', 'switch pokemon', or 'see pokemon'.\nType 'help' for a reminder.")


		# Gary's turn
		#print(f"\nGary's {gary.pokemon_list[gary.current_pokemon].name} vs Ash's {ash.pokemon_list[ash.current_pokemon].name}\n")
		print()
		while gary_turn_complete == False:
			for pokemon in gary.pokemon_list:
				if pokemon.health == 0 or pokemon.ko == True:
					gary_battle_list[gary.pokemon_list.index(pokemon)] = strike(gary_battle_list[gary.pokemon_list.index(pokemon)])
				else:
					gary_battle_list[gary.pokemon_list.index(pokemon)] = str(pokemon)
			
			time.sleep(1)
			gary_attack = False
			gary_turn = input("What do you want to do, Gary?\n").lower()
			
			if gary_turn == "help":
				print("You can 'attack', 'use potion', 'revive', 'switch pokemon', or 'see pokemon'.\nType 'help' for a reminder.")
			
			elif gary_turn == "see pokemon":
				print(gary_battle_list)

			elif gary_turn == "attack":
				gary_attack = True
				gary_turn_complete = True
			
			elif gary_turn == "use potion":
				if gary.use_potion():
					gary_turn_complete = True
			
			elif gary_turn == "use revive":
				if gary.use_revive():
					gary_turn_complete = True

			elif gary_turn == "switch pokemon":
				if gary.switch_pokemon():
					gary_turn_complete = True
						
			else:
				print("You can 'attack', 'use potion', 'revive', 'switch pokemon', or 'see pokemon'.\nType 'help' for a reminder.")

		time.sleep(1)
		print()

		if ash_attack & gary_attack == True:
			if ash.pokemon_list[ash.current_pokemon].speed > gary.pokemon_list[gary.current_pokemon].speed:
				ash.attack(gary)
				if check_status() == False: continue
				time.sleep(1)
				print()
				gary.attack(ash)
			elif ash.pokemon_list[ash.current_pokemon].speed < gary.pokemon_list[gary.current_pokemon].speed:
				gary.attack(ash)
				if check_status() == False: continue
				time.sleep(1)
				print()
				ash.attack(gary)
			else:
				coin_toss = random.choice(["heads", "tails"])
				if coin_toss == "heads":
					gary.attack(ash)
					if check_status() == False: continue
					time.sleep(1)
					print()
					ash.attack(gary)
				else:
					ash.attack(gary)
					if check_status() == False: continue
					time.sleep(1)
					print()
					gary.attack(ash)
		elif ash_attack == True:
			ash.attack(gary)
		elif gary_attack == True:
			gary.attack(ash)

		time.sleep(1)

	if gary.pokemon_remaining == 0:
		time.sleep(1)
		print("\nGary is all out of pokemon!")
		time.sleep(2)
		print("\nAsh wins!\n")
	elif ash.pokemon_remaining == 0:
		time.sleep(1)
		print("\nAsh is all out of pokemon!")
		time.sleep(2)
		print("\nGary wins!\n")

def strike(name):
	result = ""
	for char in name:
		result = result + char + '\u0336'
	return result

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
		time.sleep(1)
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

# Pokemon
# name, level (for attacks), type, max_health, health, ko, speed
ash_charmander = Pokemon("Charmander", 10, "Fire", 50, 50, False, 6)
ash_squirtle = Pokemon("Squirtle", 10, "Water", 60, 60, False, 3)
ash_bulbasaur = Pokemon("Bulbasaur", 10, "Grass", 60, 60, False, 4)

gary_charmander = Pokemon("Charmander", 10, "Fire", 50, 50, False, 6)
gary_squirtle = Pokemon("Squirtle", 10, "Water", 60, 60, False, 3)
gary_bulbasaur = Pokemon("Bulbasaur", 10, "Grass", 60, 60, False, 4)

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

	'''def use_super_potion(self):
					print(f"{self.name} used a super potion on {self.pokemon_list[self.current_pokemon]}")
					self.pokemon_list[self.current_pokemon].gain_health(50)
			
				def use_hyper_potion(self):
					print(f"{self.name} used a hyper potion on {self.pokemon_list[self.current_pokemon]}")
					self.pokemon_list[self.current_pokemon].gain_health(200)
			
				def use_max_potion(self):
					print(f"{self.name} used a max potion on {self.pokemon_list[self.current_pokemon]}")
					self.pokemon_list[self.current_pokemon].gain_health(float('inf'))'''

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


