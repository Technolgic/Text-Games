import time
inventory = []
coins = 'coins'
sword = 'sword'
GoldenKey = 'GoldenKey'
location = ""
axe = 'axe'


print("------------      ")
print("------------      ")
print("       / /        ")
print("      / /         ")
print("     / /          ")
print("    / /        |--------|    -----|   |--| |--/  |-|   -|   |----    ")
print("   / /         |   __   |    |  | |   |  | | /   | |  | |   | ___\      ")
print("  / /          |  |__|  |    |  |_|   |   >^|    | |  | |   | |__      ")
print("------------   |        |    |  |     |  |>| \   | |__| |   ---| |   ")      
print("------------   |________|    |  |     |__| |__\  |______|  |____/ /    ")
print("Technologic® 2023. Game made by Arthur Keller Technologic CEO and head Programmer in 2023. Welcome to Zorkus 1! The Forgotten Land! Your commands are 'use', 'south', 'west', 'north', 'up', 'down' 'grab', 'fight'.")

inventory = []
coins = 'coins'
sword = 'sword'
GoldenKey = 'GoldenKey'
location = ""
axe = 'axe'


while True:
	print("Your inventory is:",inventory)
	print("Your location is: ",location)
	
	
	if location == "":
		print("Type 'start' to start")
	elif location == "Outside The Old Cottage":
		print("You are standing outside of an old cottage. Your possible exits are south and north.")
	elif location == "Fence":
		print("Your possible exits are north.")
	elif location == "Outside Of Deserted Mine":
		print("Your possible exits are down, south, and west.")
	elif location == "Deserted Mine":
		print("Your possible exits are up and north.")
	elif location == "Dark Woods":
		print("You must use an axe to chop down the trees to get through. If you have an axe, than type 'use' to use it. Your possible exits are east and south. Also the trees re-grow after you cut them so when you come back you must cut it down again as this is a curse Zorkus put on the land")
	elif location == "River":
		print("You can't swim across the River as it is too strong. Your possible exits are north.")
	elif location == "Treasure Chest 1":
		print("You can open it with 'grab'. Your possible exits are south.")
	elif location == "Open Treasure Chest 1":
		print("Your possible exits are south.")
	elif location == "Village":
		print("You have reached the Village. Your possible exits are north, east and west.")
	elif location == "Village Shop":
		print("If you have coins, then type 'use' to spend them. Your possible exits are east.")
	elif location == "Desert":
		print("You are in the Desert. Your possible exits are north, south, east and west.")
	elif location == "Ambush":
		print("You run into wolves! Type 'fight' to attack them. Your possible exits are south.")
	elif location == "Heavy Grass":
		print("You see that you need a sword to cut through the heavy grass, and so you can't go any further unless you have a sword! Type 'use' to use your sword. Your possible exits are east. Also the grass re-grows after you cut it so when you come back you must cut it down again as this is a curse Zorkus put on the land.")
	elif location == "Chest 2":
		print("You can open the chest with 'grab'. Your possible exits are west.")
	elif location == "Open chest 2":
		print("Your possible exits are west.")
	elif location == "Misty Woods":
		print("You find yourself near the emperors castle! But you must first get through the Misty Woods. Your possible exits are north and east.")
	elif location == "Outside Of Castle":
		print("You see a guard at the castle door! You can attack him with 'fight'. Your possible exits are south.")
	elif location == "Castle Doors":
		print("You can open the doors with 'use'. Your possible exits are south.")
	elif location == "Emperor's Throne":
		print("You see the Evil Emporer Zorkus! You can attack him with 'fight', as he is very weak!")
	
	enter=input(": ")
	
	
	if location == "":
		if enter == "start":
			print("Long, Long ago, there was a forgotten land, that was ruled a dark person. You are now the poor man who must save this land from the evil emperor Zorkus that had let the monsters such as wolves run freely...")
			time.sleep(8)
			location = 'Outside The Old Cottage'
		else:
			continue
	elif location == "Outside The Old Cottage":
		if enter == "north":
			print("You reach a deserted mine.")
			location = 'Outside Of Deserted Mine'
		elif enter == "south":
			print("You find a fence of a house and you can't go any further.")
			location = "Fence"
	elif location == "Fence":
		if enter == "north":
			print("You have reached Outside The Old Cottage.")
			location = "Outside The Old Cottage"
	elif location == "Outside Of Deserted Mine":
		if enter == "west":
			print("You have reached the Dark Woods.")
			location = "Dark Woods"
		elif enter == "down":
			print("You are inside the Deserted Mine.")
			location = "Deserted Mine"
		elif enter == "south":
			location = 'Outside The Old Cottage'
	elif location == "Deserted Mine":
		if enter == "north":
			print("You have reached a Treasure Chest!")
			location = "Treasure Chest 1"
		elif enter == "up":
			location = "Outside Of Deserted Mine"
	elif location == "Dark Woods":
		if enter == "use":
			if axe in inventory:
				print("You chop down the trees and get through!")
				location = "Village"
		elif enter == "east":
			location = "Outside Of Deserted Mine"
		elif enter == "south":
			print("You have reached the River.")
			location = "River"
	elif location == "River":
		if enter == "north":
			location = "Dark Woods"
	elif location == "Treasure Chest 1":
		if enter == "grab":
			if axe in inventory:
				print("The chest has nothing inside!")
				location = "Open Treasure Chest 1"
			else:
				print("You found an axe!")
				inventory += [axe]
				location = "Open Treasure Chest 1"
		elif enter == "south":
				location = "Deserted Mine"
	elif location == "Open Treasure Chest 1":
		if enter == "south":
			location = "Deserted Mine"
	elif location == "Village":
		if enter == "north":
			print("You have left the Village and are now in the Desert.")
			location = "Desert"
		elif enter == "west":
			print("You have reached the Village Shop!")
			location = "Village Shop"
		elif enter == 'east':
			location = "Outside Of Deserted Mine"
			print("You went through the dark forest (The cut down one) and went to the deserted mine.")
	elif location == "Village Shop":
		if enter == "use":
			if coins in inventory:
				if sword in inventory:
					print("The shop has nothing in stock")
				else:
					print("You bought a sword!")
					inventory += [sword]
			else:
				print("You have no coins.")
		elif enter == "east":
			location = "Village"
	elif location == "Desert":
		if enter == "north":
			print("You run into wolves!")
			location = "Ambush"
		elif enter == "south":
			location = "Village"
		elif enter == "west":
			print("You run into Heavy Grass!")
			location = "Heavy Grass"
		elif enter == "east":
			print("You find a chest!")
			location = "Chest 2"			
	elif location == "Ambush":
		if enter == "south":
			location = "Desert"
		elif enter == "fight":
			if sword in inventory:
				print("You kill the wolves! Sadly, there is a Mountain so you can't go any further and turn back!")
				location = "Desert"
			else:
				print("You don't have a sword and have to run away!")
				location = "Desert"
	elif location == "Heavy Grass":
		if enter == "east":
			location = "Desert"
		elif enter == "use":
			if sword in inventory:
				print("You cut throgh the grass!")
				location = "Misty Woods"
			else:
				print("You don't have the sword and turn back.")
				location = "Desert"
	elif location == "Chest 2":
		if enter == "west":
			location = "Desert"
		elif enter == "grab":
			if coins in inventory:
				print("The chest is empty!")
				location = "Open chest 2"
			else:
				print("You get some coins! You can spend them at the Village Shop!")
				inventory += [coins]
				location = "Open chest 2"	 
	elif location == "Open chest 2":
		if enter == "west":
			location = "Desert"
	elif location == "Misty Woods":
		if enter == "north":
			print("You make it to the castle!")
			location = "Outside Of Castle"
		elif enter == "west":
				print("You go back through the grass (What it used to be) and to the Desert.")
				location = "Desert"
	elif location == "Outside Of Castle":
		if enter == "south":
			print("You go back to the Misty Woods.")
			location = "Misty Woods"
		elif enter == "fight":
			print("You kill the Guard and get a key!")
			inventory += [GoldenKey]
			location = "Castle Doors"
	elif location == "Castle Doors":
		if enter == "use":
			if GoldenKey in inventory:
				print("You open the Doors!")
				location = "Emperor's Throne"
			else:
				print("You can't unlock the Door.")
		elif enter == "south":
			location = "Outside Of Castle"
	elif location == "Emperor's Throne":
		if enter == "fight":
			print("You attack him and banish him from this land! The land is now at peace, and you have been crowned king! Zorkus will never cause havoc again!")
			print("YOU WIN!!!!! ")
			break
