XP = []
inventory = []
rusty = 'rusty sword'
area = '0'
sticks = 'sticks'


print("Welcome to Adventure Island! 2023 Technologic © .")

XP = []
inventory = []
area = '0'

while True:
	print("You are in this area right now: " + area)
	print("Your inventory is: ")
	print(inventory)
	print("Your XP is: ")
	print(XP)
	
	#Tell me what I can do
	if area == '0':
		print("Type 'start' to start: ")
	elif area == 'shore':
		print("You wake up the shore of an uncharted island. A) Go into the woods near you, B) look for supplies near your broken raft: ")
	elif area == 'raft':
		print("You can now go to the forest. A) OK B) Explore the raft more: ")
	elif area == "BATTLE 1":
		print("The wolves are about to attack you! There are 2 wolves. A) Attack the wolves, B) Run away: ")
	elif area == 'Cave 1 entrance':
		print("You have found a cave entrance! A) go onside the cave, B) Go back to the forest: ")
	elif area == 'Forest':
		print("You can now go further into the forest (A) or B) Try and find shelter as night is coming soon: ")
	elif area == 'Cave 2 entrance':
		print("You can A) enter the cave or B) Look for supplies in the forest before you enter (such as sticks): ")
	elif area == 'Woods':
		print("Now that you have sticks you can A) Go back to the cave, B) Stay here and look for more supplies: ")
	elif area == 'Cave 2':
		print("You can now make a fire! A) OK: ")
	
	enter = input()
	
	
	if area == '0':
		if enter == "start":
			area = 'shore'
	elif area == 'shore':
		if enter == "A":
			print("ARRRGH! A PACK OF WOLVES FIND YOU! YOU DIE ")
			continue
		elif enter == "B":
			area = 'raft'
			inventory += [rusty]
			print("WOW! YOU FOUND YOUR RUSTY SWORD!")
	elif area == 'raft':
		if enter == "A":
			area = 'BATTLE 1'
			print("You encounter wolves!")
		elif enter == "B":
			print("A pack of Ogres sneak up upon you, killing you! YOU DIE! ")
			continue
	elif area == 'BATTLE 1':
		if enter == "A":
			area = 'Forest'
			XP += [50]
			print("SLISH! SLASH! You kill both wolves! You have gained 50 XP! At the end of the game, add up all of your XP! ")
		elif enter =="B":
			area = 'Cave 1 entrance'
			print("Phew! You ran way succesfully and found a cave!")
	elif area == 'Cave 1 entrance':
		if enter == "A":
			print("OH NO! IT WAS THE OGRES CAVE! YOU DIE!!!")
			break
		elif enter == "B":
			print("THE WOLVES KILL YOU! YOU DIE!!!")
			break
	elif area == 'Forest':
		if enter == "A":
			print("OH NO! It's an Oger! YOU DIE!!!")
			break
		elif enter == "B":
			area = 'Cave 2 entrance'
			print("You find a cave entrance!")
	elif area == 'Cave 2 entrance':
		if enter == "B":
			area = 'Woods'
			inventory += [sticks]
			print("You found some sticks! You can use these to make a fire!")
		elif enter == "A":
			print("OH NO! YOU DONT HAVE STICKS TO MAKE A FIRE, AND YOU DIE AS YOU TURN TO COLD WITH YOUR TORN CLOTHES!")
			continue
	elif area == 'Woods':
		if enter == "A":
			area = 'Cave 2'
			print("You are now in the cave.")
		elif enter == "B":
			print("AHHHH! A MASSIVE SPIDER EATS YOU! YOU DIE!!!!")
			continue
	elif area == 'Cave 2':
		if enter == "A":
			if sticks in inventory: 
				print("YOU MAKE A FIRE AND SURVIVE THE NIGHT! YOU WIN!")
				break
		else:
			print("ERROR")
				
		



