inventory = []
key1 = 'key1'
key2 = 'key2'
potion = 'potion'
room = ''
note = 'note'

print("Welcome to Chris The Killer 2! - The Return")

inventory = []
key1 = 'key1'
key2 = 'key2'
potion = 'potion'
room = ''

while True:
	print("Your Inventory is: ")
	print(inventory)
	print("Your room is: ")
	print(room)
	
	#Tell me what I can do
	if room == '':
		print("Type 'start' to start: ")
	elif room == 'road':
		print("You are walking down the road, when you see Chris The Killer running at you! Impossible! You think. You can now A) Start running away: ")
	elif room == "Dead end":
		print("Quick! You must escape! You can A) Try and hide, or B) Try and run out of the dead end hopefully before Chris comes: ")
	elif room == "Lab":
		print("You find yourself chained to a wall! OH NO! You have been captured by Chris! Luckily, you see the keys right next to you! You can now A) Try and reach the keys, or B) Stay still and act unconscious: ")
	elif room == "lab":
		print("You can now A) get the keys, or B) try and break the chains: ")
	elif room == "Labratory":
		print("You can now A) Look around, or B) Try and leave the room: ")
	elif room == "Hallway":
		print("You find yourself in a hallway! It looks like you have been captured in an abandoned forttress! You can now A) Go to the Prison, or B) Go to the Dungeon: ")
	elif room == "Prison":
		print("You can now A) Look around, or B) Go outside of the Prison: ")
	elif room == "Secret room":
		print("Wow! You can now A) look around, or B) Hide, as you think Chris is coming: ")
	elif room == "Pile of Boxes":
		print("You can now A) Leave the secret room, or B) Stay in the Pile Of Boxes: ")
	elif room == "prison":
		print("You can now A) Leave the prison or B) Search around: ")
	elif room == "corner":
		print("You can now, A) Leave the prison (out of the corner and into the hallway) or B) stay in the corner: ")
	elif room == "hallway":
		print("You can now A) go to the dungeon, or B) Stay in the hallway: ")
	elif room == "Dungeon":
		print("You can now A) Search for the second key, or B) Hide as you think Chris is coming: ")
	elif room == "Corner":
		print("You can now A) Search for the Hidden room, or B) Hide as you think Chris is near: ")
	elif room == "Box":
		print("You can now A) Search for the hidden room: ")
	elif room == "Hidden Room":
		print("You can now A) Search for the potion or B) Leave the secret room: ")
	elif room == "Storage Section of Hidden Room":
		print("You can now A) Drink the potion, or B) Leave the secret room: ")
	elif room == "storage section of the hidden room":
		print("You can now A) Search for the Chamber Door (Leaving the Secret Room): ")
	elif room == "Chamber Door":
		print("In the distance, you see Chris beating up someone and shouting,'HOW COULD YOU LET HIM ESCAPE!'. You wonder who the person is as they fall on the ground. You can now A) Open the door, or B) Try and help the person:  ")
		
		
		
	enter = input()
		
		
	#Respond to my request
	if room == '':
		if enter == "start":
			room = 'road'
	elif room == 'road':
		if enter == "A":
			print("OH NO! YOU RUN INTO A DEAD END AND CHRIS IS COMING!")
			room = "Dead end"
	elif room == "Dead end":
		if enter == "A":
			print("Chris sees you! He has a large bat and hits you on the head...")
			room = 'Lab'
		elif enter == "B":
			print("You run straight into Chris! He hits you with a large bat...")
			room = 'Lab'
	elif room == "Lab":
		if enter == "A":
			print("Chris comes and sees you trying to get the keys! YOU DIE!!!")
		elif enter == "B":
			print("Chris comes in and sees you 'unconscious' and walks away.")
			room = 'lab'
	elif room == "lab":
		if enter == "A":
			print("You get the keys and you are free!!!!!!")
			room = 'Labratory'
		elif enter == "B":
			print("The chains start making a tremendous noise because of your shaking, and Chris comes! YOU DIE!!!!!")
	elif room == "Labratory":
		if enter == "A":
			print("Chris finds you! YOU DIE!!!!")
		elif enter == "B":
			print("You succesfully make it out of the Lab! ")
			room = 'Hallway'
	elif room == "Hallway":
		if enter == "A":
			print("You make it to the Prison!")
			room = "Prison"
		elif enter == "B":
			print("Chris was in the Dungeon! YOU DIE!!!!!!!")
	elif room == "Prison":
		if enter == "A":
			print("You found a secret room!")
			room = "Secret room"
		elif enter == "B":
			print("CHRIS WAS IN THE HALLWAY! YOU DIE!!!!!")			
	elif room == "Secret room":
		if enter == "A":
			print("You find a key!")
			inventory += [key1]
			room = "Pile of Boxes"
		elif enter == "B":
			print("You could not hide in time! Chris comes and kills you! YOU DIE!!!!")
	elif room == "Pile of Boxes":
		if enter == "A":
			print("You are now in the prison")
			room = 'prison'
		elif enter == "B":
			print("Chris found you! YOU DIE!!!!!")
	elif room == "prison":
		if enter == "A":
			print("Chris was in the Hallway! YOU DIE!!!!!")
		elif enter == "B":
			print("You find a note saying ' The second key is in the dungeon '!")
			inventory += [note]
			room = 'corner'
	elif room == "corner":
		if enter == "A":
			print("You make it to the hallway!")
			room = "hallway"
		elif enter == "B":
			print("Chris gets you! YOU DIE!!!!")
	elif room == "hallway":
		if enter == "A":
			print("You make it to the dungeon!")
			room = "Dungeon"
		elif enter == "B":
			print("Chris got you! YOU DIE!!!!")
	elif room == "Dungeon":
		if enter == "A":
			print("You found the second key! It also has a note on it saying 'The potion is in the hidden room in the dungeon'")
			inventory += [key2]
			room = "Corner"
		elif enter == "B":
			print("Chris actually did not come to your old location, but he went where you hid! YOU DIE!!! ")
	elif room == "Corner":
		if enter == "A":
			print("Chris found you looking around! YOU DIE!!!!")
		elif enter == "B":
			print("You successfully don't get caught by Chris!")
			room = "Box"
	elif room == "Box":
		if enter == "A":
			print("You find the hidden room!")
			room = "Hidden Room"
	elif room == "Hidden Room":
		if enter == "A":
			print("You find the potion! Coming with the potion, theres a message! The message says 'Put Both keys into the Chamber Door and drink the potion to find the location of the Chamber Door'! ")
			inventory += [potion]
			room = "Storage Section of Hidden Room"
		elif enter == "B":
			print("Chris was in the Dungeon! YOU DIE!!!!!")
	elif room == "Storage Section of Hidden Room":
		if enter == "A":
			print("You now know that the Chamber Door is in the Dungeon!")
			room = "storage section of the hidden room"
		elif enter == "B":
			print("Chris finds you in the Dungeon! YOU DIE!!!!")
	elif room == "storage section of the hidden room":
		if enter == "A":
			print("You find the Chamber Door!")
			room = "Chamber Door"
	elif room == "Chamber Door":
		if enter == "A":
			print("YOU ESCAPE!!!! YOU WIN!!!!!!!")
			break
		elif enter == "B":
			print("Chris catches you! YOU DIE!!!!")
