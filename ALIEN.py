#Setup
inventory = []
room = '1'
key1 = 'blue key'
key2 = 'red key'
extra = 'laser gun'

print("Welcome to ALIEN. You are a human soldier fighting the aliens. You have been captured and you must escape the alienship.")

inventory = []
room = '1'


#Main loop: 	
while True:
#tell me what room I am in
		print("You are in " +room+ " right now.")
			
#tell me what is in my inventory
		print("Your inventory: ")
		print(inventory) 
		
#tell me what I can do
		if room == '1':
			print("Type 'start' to start")
		elif room == 'storage room':
			print("A) go to the door inside " + room + " or , B) Search the " + room)		
		elif room == 'GF':
			print("A) Look around, B) check on the crates that are in the far end of " +room)
		elif room == "hall":
			print("There is a door but it is locked. A) Try the door anyway, B) Search for the key: ")
		elif room == 'drains':
			print("You see a door but it is guarded by aliens. A) go and sneak past the aliens, B) look for another option: ")
		elif room == 'Door':
				print("A) You can open the door with the key or B) You can look for another entrance: ")
		elif room == 'captain room':
			print("You see another locked door! A) Go and sneak to the door. B) Go and try and steal the keys that you see on the alien: ")
		elif room == 'door 2':
			print("A) Unlock the door. B) Search around the captain room.")
		elif room == 'Final door (door 2)':
			print("You can now unlock the door with A: ")
			
#ask me, what I want to do
		enter=input("Your next move: ")
						
#effect
		if room == '1':
			if enter == "start" : room = 'storage room'
		elif room == 'storage room':
			if enter == "A":
				print("AN ALIEN FOUND YOU! YOU DIE!")
			elif enter == "B":
				room = 'GF'
				print("You found nothing... wait! You find a trapdoor and enter it!") 
		elif room == 'GF':
			if enter == 'A':
				room = 'hall'
				print("Great! You found the other trapdoor and now made it to the hall!")
			elif enter == "B":
				print("OH NO! AN ALIEN SEES YOU AND YOU DIE!")
		elif room == 'hall':
			if enter == "A":
				print("All the noise made an Alien spot you!!! YOU DIE!")
			elif enter == "B":
				inventory += [key1]
				room = 'drains'
				print (inventory)
				print("You got the key! CRRRRRCK! What was that! The floor breaks and you end up in the drains!")
		elif room == 'drains':
			if enter == "A":
				room = 'Door'
				print("You make it! You are now where the locked door is!")
			elif enter == "B":
				print("It's a dead end! The aliens spot you and you die!'")
		elif room == 'Door':
			if enter == "A":
				if key1 in inventory:
					room = 'captain room'
					print("YES! You made it and are now in the captains room, a step closer to escaping the alienship!!!")
				elif enter == "B":
					print("OH NO! YOU DIE FROM AN ALIEN!!!")
			elif enter == "B":
				print("AN ALIEN SAW YOU LOOKING AROUND AND KILLS YOU!!!")
		elif room == 'captain room':
			if enter == "A":
				print("AAAH! AN ALIEN SAW YOU, KILLING YOU!")
			elif enter == "B":
				room = 'door 2'
				inventory += [key2]
				print("AMAZING JOB! You got the key and sneak to the door!")
		elif room == 'door 2':
			if enter == "A":
				if (key1 in inventory) and (key2 in inventory):
					print("YESSSSS! YOU ESCAPE THE ALIENSHIP! YOU FINISHED WITHOUT EXTRA POINTS THOUGH...")
					break
			elif enter == "B":
				inventory += [extra]
				room = 'Final door (door 2)'
				print("Great job! You found extra points!")
		elif room == 'Final door (door 2)':
			if enter == "A":
				if (key1 in inventory) and (key2 in inventory) and (extra in inventory):
					print("YOU MADE IT! YOU HAVE ESCAPED THE ALIENSHIP WITH EXTRA POINTS!!!")
					break
