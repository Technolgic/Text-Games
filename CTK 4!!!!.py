import time
inventory = []
room = ""
dagger = "dagger"
key1 = "key1"
map = "map"
key2 = "key2"

print("|---------  ___________              ")
print("|---------  |---- ----|   |-|   /-/")
print("||              | |       | |  / /        ")
print("||              | |       | | / /   ") 
print("||              | |       | |/ |    ")
print("||              | |       | |\ \      ")
print("||_________     | |       | | \ \      ")
print("|_________|     | |       |_|  \_\            ") 

print("Welcome To Chris The Killer 4! - The Final Challenge! ")

import time
inventory = []
room = ""
dagger = "dagger"
key1 = "key1"
map = "map"
key2 = "key2"

while True:
	print("Your inventory is: ",inventory)
	print("Your room is: ",room)
	
	if room == "":
		print("Type 'start' to start the final game! NOTE: PLEASE TYPE IN CAPITALS EXCEPT 'start'.")
	elif room == "Old Corridor":
		print("You find yourself in an Old Corridor! You can now A) Look around or B) Hide as you think Chris is coming.")
	elif room == "Shelf":
		print("You can now A) Stay in the shelf or B) Go outside of it.")
	elif room == "Old corridor":
		print("You realise that you have to find a escape quickly or Chris will eventually end you. Your possible options are A) Go to a door you see in the distance, B) Look around or C) Stay where you are.")
	elif room == "Outside Of Door":
		print("You can now A) Open the door.")
	elif room == "Old Chamber":
		print("You can now A) Hide, B) Look around or C) Scan for dangers.")
	elif room == "Old chamber":
		print("The map says 'You must find both keys to leave'. You can now A) Search for the keys or B) hide.")
	elif room == "Box":
		print("You can now A) Leave the box or B) Stay in it.")
	elif room == "old chamber":
		print("You can now A) Search for the keys or B) Stay where you are.")
	elif room == "Dusty Room":
		print("You found the first key! You had to leave the chamber though to find it. You can now A) Search for the second key, B) Hide, or C) Stand where you are.")
	elif room == "Dusty room":
		print("You can now A) Search for the second key.")
	elif room == "Pile of boxes":
		print("You now have the second key! You also realise that you will have to kill Chris as well. You can now A) Hide, B) Look for a exit as the pile of boxes collapsed or C) Stay where you are. ")
	elif room == "dusty room":
		print("You're now back in the dusty room! You can now A) Look for a weapon, B) Scan for dangers or C) Hide.")
	elif room == "Corner":
		print("You found a dagger! You can now A) Search for Chris.")
	elif room == "Old Kitchen":
		print("You confront Chris and he tries to run away from you. You can now A) End his horrible ways for good or B) Apolagize.")
	elif room == "Old kitchen":
		print("Now that you've killed Chris you can A) Look for the exit to the mansion.")

	
	enter = input("Enter: ")
	
	if room == "":
		if enter == "start":
			print("Ten years ago after Chris died, a group of teens revived Chris in an old mansion. Chris turned on them though, and killed all of them except one who could escape Chris's clutches. You are now this teen who must escape this mansion and end Chris once and for all.... ")
			time.sleep(10)
			room = "Old Corridor"
		elif enter == "hacks":
			print("D0 yUo WaNt t0 uSe hAcKS? TYpE 'yes' 0r 'no'.")
			enter = input(":")
			if enter == "yes":
				inventory += [dagger]
				inventory + [key1]
				inventory += [key2]
				inventory += [map]
				room = "Old Corridor"
			elif enter == "no":
				print("You don't use hacks but skip prolog.")
				room = "Old Corridor"
	elif room == "Old Corridor":
		if enter == "A":
			print("Chris got you...")
			time.sleep(2)
			print("YOU DIE!!!!")
			room = "Old Corridor"
			inventory = []
		elif enter == "B":
			print("You hide in a shelf!")
			room = "Shelf"
	elif room == "Shelf":
		if enter == "A":
			print("Chris gets you...")
			time.sleep(2)
			print("YOU DIE!!!")
			room = "Old Corridor"
			inventory = []
		elif enter == "B":
			print("You find yourself back in the Old Corridor!")
			room = "Old corridor"
	elif room == "Old corridor":
		if enter == "A":
			print("You go to the door!")
			room = "Outside Of Door"
		elif enter == "B":
			print("Chris gets you...")
			time.sleep(2)
			print("YOU DIE!!!!")
			room = "Old Corridor"
			inventory = []
		elif enter == "C":
			print("Chris gets you...")
			time.sleep(2)
			print("YOU DIE!!!!")
			room = "Old Corridor"
			inventory = []
	elif room == "Outside Of Door":
		if enter == "A":
			print("You find yourself in an old chamber!")
			room = "Old Chamber"
	elif room == "Old Chamber":
		if enter == "A":
			print("Chris finds you in your hiding spot...")
			time.sleep(2)
			print("YOU DIE!!!!")
			room = "Old Corridor"
			inventory = []
		elif enter == "B":
			print("You find a map!")
			inventory += [map]
			room = "Old chamber"
		elif enter == "C":
			print("Chris opens the door behind you....")
			time.sleep(2)
			print("YOU DIE!!!!")
			inventory = []
			room = "Old Corridor"
	elif room == "Old chamber":
		if enter == "A":
			print("Chris gets you....")
			time.sleep(2)
			print("YOU DIE!!!!")
			inventory = []
			room = "Old Corridor"	
		elif enter == "B":
			print("You hide!")
			room = "Box"	
	elif room == "Box":
		if enter == "A":
			print("You leave the Box!")
			room = "old chamber"
		elif enter == "B":
			print("Chris gets you....")
			time.sleep(2)
			print("YOU DIE!!!")
			room = "Old Corridor"
			inventory = []
	elif room == "old chamber":
		if enter == "A":
			print("You find a key!")
			inventory += [key1]
			room = "Dusty Room"
		elif enter == "B":
			print("Chris gets you....")
			time.sleep(2)
			print("YOU DIE!!!!!")
			inventory = []
			room = "Old Corridor"
	elif room == "Dusty Room":
		if enter == "A":
			print("Chris gets you...")
			time.sleep(2)
			print("YOU DIE!!!!")
			inventory = []
			room = "Old Corridor"
		elif enter == "B":
			print("Chris got you...")
			time.sleep(2)
			print("YOU DIE!!!!")
			inventory = []
			room = "Old Corridor"
		elif enter == "C":
			print("You stay where you are and Chris doesnt get you!")
			room = "Dusty room"
	elif room == "Dusty room":
		if enter == "A":
			print("You find the second key!")
			inventory += [key2]
			room = "Pile of boxes"
	elif room == "Pile of boxes":
		if enter == "A":
			print("Chris gets you...")
			time.sleep(2)
			print("YOU DIE!!!")
			room = "Old Corridor"
			inventory = []
		elif enter == "B":
			print("You find an exit!")
			room = "dusty room"
		elif enter == "C":
			print("Chris gets you...")
			time.sleep(2)
			print("YOU DIE!!!!")
			inventory = []
			room = "Old Corridor"			
	elif room == "dusty room":
		if enter == "A":
			print("Chris gets you...")
			time.sleep(2)
			print("YOU DIE!!!")
			inventory = []
			room = "Old Corridor"
		elif enter == "B":
			print("You see no dangers and start searching for a weapon...")
			time.sleep(2)
			print("Searching...")
			time.sleep(2)
			print("You find a dagger!")
			inventory += [dagger]
			room = "Corner"
		elif enter == "C":
			print("Chris gets you....")
			time.sleep(2)
			print("YOU DIE!!!!")
			room = "Old Corridor"
			inventory = []
	elif room == "Corner":
		if enter == "A":
			print("You find Chris!")
			room = "Old Kitchen"
	elif room == "Old Kitchen":
		if enter == "A":
			print("You kill Chris!!!!!!!!!!")
			room = "Old kitchen"
		elif enter == "B":
			print("Chris gets you...")
			time.sleep(2)
			print("YOU DIE!!!!")
			inventory = []
			room = "Old Corridor"
	elif room == "Old kitchen":
		if enter == "A":
			if key1 and key2 in inventory:
				print("YOU ESCAPE!!!!")
				print("YOU WIN!!!!!!!!")
				time.sleep(2)
				print("Game made by Arthur Keller Technologic CEO in 2023. Great job CTK gamer!")
				break
		
		
