#Setup
inventory = []
room = 'The Lobby'
POTION = 1
KEY = 2

print("Welcome to chris the killer. Try and survive chris! type 'start' to start: ")

inventory = []
potion = 1
key = 2
#Main Loop
while True:
	print('You are in ' + room + '.')

	#Tell me what I can do in the room.
	if room == 'The Lobby':
		print ('Type start to start.')
	elif room == 'Living Room':
		print('a) go to the kitchen. b) go to the basement')
	elif room == 'The Kitchen':
		print("You can now go into the garden. a) go there. b) stay here: ")
	elif room == "The Garden":
		if (POTION not in inventory):
			print('You found a potion!')
			inventory += POTION
		print('a) to go back inside b) stay here')
	elif room == 'the basement':
		print("a) search, b) stay in here: ")	
	
	enter = input('Your choice: ')

	#Change my state based on my choice
	if room == 'The Lobby':
		if enter == 'start': room = 'Living Room'
	elif room == 'Living Room':
		if enter == 'a': room = 'The Kitchen'
		if enter == 'b': room = 'the basement'
	elif room == 'the basement':
		if enter == "a":
			print("You found something... YOU DIED IT WAS A MONSTER HIDING! ")
		elif enter == "b":
			print("Hmmm... What was that! ... ... ... AHHHHH! YOU DIE!")
	elif room == 'The Kitchen':
		if enter == "a": room = 'The Garden'
	elif room == 'The Garden':
		if enter == 'a': room = 'The Kitchen'
	
		


print('Arthurs previous game')


inventory = []
print("Welcome to chris the killer. Try and survive chris! type 'start' to start: ")
enter = input()
if enter == "start":
	while True:
		print("You spawn in the living room. a) go to the kitchen. b) go to the basement: ")
		enter = input()
		if enter == "a":
			print("Chris got you!!! YOU DIE")
			continue
		elif enter == "b":
			print("You are now in the basement. a) search . b) go out of the basement: ")
			enter = input()
			if enter == "a":
				inventory += [1]
				print("You got the potion! a) go outside. b) stay in the basement: ")
				enter = input()
				if enter == "a":
					print("You are now oustide. a) go to the garden b) go to the kitchen: ")
					enter = input()
					if enter == "a":
						print("Chris got you!")
						continue
					elif enter == "b":
						inventory += [2]
						print("You got the key! You now see a portal. a) go inside. b) go to the living room: ")
						print (inventory)
						enter = input()
						if enter == "a":
								if (1 in inventory) and (2 in inventory):
									print("You win!!!!")
									print("Made by Arthur Keller in less than 2 hours VirusRed.Inc")
									break
								else:
									print("YOU GOT KILLED BY CHRIS!!!!")
									continue	
						elif enter == "b":
								print("You die! CHRIS GOT YOU!!!")
								continue		
				elif enter == "b":
					print("YOU DIED!!! Chris got you!")
					continue
			elif enter == "b":
				print("YOU DIED! Chris got you!!!")
				continue
