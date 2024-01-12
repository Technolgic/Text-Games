import time
inventory = []
knife = 'knife'
key = "key"
room = ""
clue = 'clue'

print("Welcome to Chris The Killer 3 - The Apprentice! ")

import time
inventory = []
knife = 'knife'
key = "key"
room = ""
clue = 'clue'


while True:
	print("Your inventory is: ")
	print(inventory)
	print("Your room is: ")
	print(room)
	
	
	if room == "":
		print("Type 'start' to start: ")
	elif room == "Torture room":
		print("Huh! You remember the prisoner escaping and Chris getting furious at you! This led him to hitting you on the head, and you think he is going to kill you know, even though you're his apprentice. You can now A) Try and get out of the room, or B) Hide as you think Chris is coming: '")
	elif room == "Dungeon Corridor":
		print("You must find a way to take revenge on Chris! You think as a sudden rush of anger hits you. But you must do it without him getting you you think. You can now A), look around for a clue to find a weapon, or B) Stay where you are: ")
	elif room == "Locked door":
		print("You can now A) Try and find the clue for a weapon, or the B) key to the door: ")
	elif room == "Mystery room":
		print("You are now in a room with tons of notes covering the walls. You think that one of those notes might have a clue how to find the weapon! A) look for the clue, B) Hide as you think Chris is coming:  ")
	elif room == "Mystery Room":
		print("You can now A) Search for the clue, or B) stay where you are: ")
	elif room == "mystery room":
		print("You can now A) Leave the mystery room: ")
	elif room == "dungeon Corridor":
		print("You can now A) try and search for the key, or B) Hide as you think Chris is coming: ")
	elif room == "Dungeon corridor":
		print("You can now A) Try and get the key: ")
	elif room == "Pile of boxes":
		print("Now that you have the key, all you have to do is get to the door! For some reason, you already think you know where the door is! You can now A) Go to the place where you think the door is, or B) stay where you are: ")
	elif room == "locked Door":
		print("You can now A) Unlock the door, or B) Enter the corridor again: ")
	elif room == "Weapon Room":
		print("You can now A) Hide as you think Chris is coming, or B) Search for the weapon ")
	elif room == "Weapon room":
		print("You can now A) as you have a weapon, hunt down Chris. YOUR NOT THE ONE HIDING ANYMORE! YOUR THE KILLER! or B) Stay where you are: ")
	elif room == "Corner":
		print("You can now A) Attack Chris and have revenge, or B) apologize to Chris for trying to kill him: ")
			
	enter = input()
	
	
	if room == "":
		if enter == "start":
			print("You fall unconscious to the floor...")
			time.sleep(6)
			room = "Torture room"
	elif room == "Torture room":
		if enter == "A":
			print("You make it out of the Torture room, and find yourself in a old Dungeon!")
			room = 'Dungeon Corridor'
		elif enter == "B":
			print("Chris enters the room and realises that you are gone! He searches everywhere and finds you! YOU DIE!!!!!!")
			continue
	elif room == "Dungeon Corridor":
		if enter == "A":
			print("You don't find a clue for a weapon, but instead find a locked door!")
			room = "Locked door"
		elif enter == "B":
			print("Chris got you! YOU DIE!!!!")
	elif room == "Locked door":
		if enter == "A":
			print("You found a mysterious room while looking around, and so you went inside it!")
			room = 'Mystery room'
		elif enter == "B":
			print("Chris find you looking around! YOU DIE!!!!!!!")
			continue
	elif room == "Mystery room":
		if enter == "A":
			print("Chris got you! YOU DIE!!!!")
			continue
		elif enter == "B":
			print("You successfully hide from Chris!")
			room = "Mystery Room"
	elif room == "Mystery Room":
		if enter == "A":
			print("You find a clue! The clue says 'Find the key to get closer to the weapon and unlock the door with the key'!")
			inventory += [clue]
			room = 'mystery room'
		elif enter == "B":
			print("Chris got you! YOU DIE!!!!!")
			continue
	elif room == "mystery room":
		if enter == "A":			
			print("You successfully leave the mystery room without Chris getting you!")
			room = "dungeon Corridor"
	elif room == "dungeon Corridor":
		if enter == "A":
			print("Chris gets you! YOU DIE!!!!")
			continue
		elif enter == "B":
			print("You hide from Chris and don't die!")
			room = "Dungeon corridor"
	elif room == "Dungeon corridor":
		if enter == "A":
			print("You get the key!")
			inventory += [key]
			room = 'Pile of boxes'
	elif room == "Pile of boxes":
		if enter == "A":
			print("You reach the door without being caught by Chris!")
			room = "locked Door"
		elif enter == "B":
			print("Chris found you! YOU DIE!!!!!")
			continue
	elif room == "locked Door":
		if enter == "A":
			print("You unlock the door!")
			room = 'Weapon Room'
		elif enter == "B":
			print("Chris found you in the Corridor! YOU DIE!!!!!")
			continue
	elif room == "Weapon Room":
		if enter == "A":
			print("You ran intoc Chris when trying to hide! YOU DIE!!!!!")
			continue
		elif enter == "B":
			print("You find a kife!!!!")
			inventory += [knife]
			room = "Weapon room"		
	elif room == "Weapon room":
		if enter == "A":
			print("You find Chris and he's cowering in a corner as he sees you with a knife!")
			room = 'Corner'
		elif enter == "B":
			print("Ahh! Chris stabs you in the back! YOU DIE!!!!")
			continue
	elif room == "Corner":
		if enter == "A":
			print("You attack Chris and later you chain him up! You have gotten your revenge and Chris will never kill anyone again! You will also not become a killer, as you realise the pain that you cause as Chris almost killed you!")
			print("YOU WIN!!!!!")
			break
		elif enter == "B":
			print("Chris tricked you after accepting your apology and attacks you! YOU DIE!!!!")
			continue
