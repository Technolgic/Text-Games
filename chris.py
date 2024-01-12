


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
