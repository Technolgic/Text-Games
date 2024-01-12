inventory = []
key1 = 'key1'
key2 = 'key2'
torch = 'torch'
room = 'START'
CD = 'CD'

print("Welc0Me T0 OrcrY0sS. TyPE YoUr NAmE: ")
name = input()
print("WeLComE " + name + ". YoU ArE A MisSing ChIlD wHo HAs BEeN KIdNapPeD. YoU MuSt LeaVe ThE hoUse To SuRVIVe.")

inventory = []
key1 = 'key1'
key2 = 'key2'
torch = 'torch'
room = 'START'
CD = 'CD'


while True:
	print("YoUR InVeNtOry Is: ")
	print(inventory)
	print("YoU ArE iN ThIS roOm sO FaR: " + room)
	
	
	#Tell me what to do
	if room == 'START':
		print("TyPE 'start' T0 StArT: ")
	elif room == 'BASEMENT':
		print("YoU SpAWn iN ThE BaSeMEnT. A) Lo0K ArOund, B) G0 ToWArDS THe D00r ThaT YoU SEe: ")
	elif room == 'BOX PILE':
		print("YoU CaN noW (A) G0 To ThE D0oR oR (B) LoOk ArOunD ThE BoXeS: ")
	elif room == 'HALLWAY':
		print("YoU CAn N0w A) G0 T0 ThE LaUnDrY oR B) G0 T0 ThE CoNTrOL RoOm: ")
	elif room == 'CONTROL ROOM':
		print("YoU CaN NoW A) TakE ThE KEyS AnD LoOK At ThE CD or B) HiDE IN ThE BOxES STaTionED, As YoU hERe OrCRyosS: ")
	elif room == 'CONTROL PANNEL':
		print("YoU CaN NOw A) G0 ANd LoOk FoR tHe 2 LocKEd dOorS oR B) StAy ArOunD AnD HidE In HerE, DuE T0 SoUnDS Of OrcRyOsS: ")
	elif room == "HALL":
		print("YoU CaN NOw A) G0 AnD SEArcH FoR ThE fIrsT L0CkEd Do0r oR B) StAy At ThE ContrOL PanNel: ")
	elif room == "ENTRANCE TO THE FIRST LOCKED ROOM":
		print("YoU cAn NoW A) OpEN ThE Do0R: ")
	elif room == "LOCKED ROOM 1":
		print("Y0u SeE a TV! A) G0 AnD ViEw It 0R B) StaY nEar ThE Do0r: ")	
	elif room == 'TV':
		print('YoU CaN NOw A) PuT ThE CD In: ')
	elif room == "CORRIDOR":
		print("YoU CoUlD NoW A) Lo0K FoR ThE lAsT r0Om Or B) STaY IN thE CorrIDor: ")
	elif room == "THE FINAL DOOR ENTRANCE (LOCKED DOOR 2)":
		print("YoU CaN NoW UnlOCk ThE D0oR wiTh (A): ")
		
		
	enter = input()
	
	if room == 'START':
		if enter == 'start':
			room = 'BASEMENT'
	elif room == 'BASEMENT':
		if enter == 'A':
			inventory += [torch]
			room = 'BOX PILE'
			print("Y0u FoUnd A torCH!")
		elif enter == 'B':
			print('ThE MaN iN YeLLoW GoT YOu! YoU DiE!')
			continue
	elif room == 'BOX PILE':
		if enter == 'A':
			print("YoU MaKE It T0 ThE DOor AnD OpEn iT!")
			room = 'HALLWAY'
		elif enter == 'B':
			print("ThE MAn iN YelLoW fOuNd YoU! YoU DiE!!!")
	elif room == "HALLWAY":
		if enter == "A":
			print("OrCRyOSS FoUNd YoU IN ThE LAuNDRy!!! YoU DiE!")
		elif enter == "B":
			room = 'CONTROL ROOM'
			print("YoU EntER THe ConTrOL ROom")
	elif room == 'CONTROL ROOM':
		if enter == "A":
			inventory += [key1]
			inventory += [key2]
			inventory += [CD]
			room = 'CONTROL PANNEL'
			print("YoU GEt ThE KEys To ThE 2 LoCkeD RoOmS! YoU ALsO GEt A CD! YOu CAn FInD A Tv To ViEw It!")
		elif enter == "B": 
			print("OrCRyOsS DiD NoT CoME BuT waIt! The SoUnD Of ThE BoXeS AttRacTED ThE mAn In YeLLoW! YoU DiE!!!")
	elif room == 'CONTROL PANNEL':
		if enter == "A":
			room ="HALL"
			print("YoU ENtEr ThE HaLl")
		elif enter == "B":
			print("OcRyOSs FouNd YoU EvEN WiTh YouR HiDiNG! YOu DiE!!!")
	elif room == 'HALL':
		if enter == "A":
			room = "ENTRANCE TO THE FIRST LOCKED ROOM"
			print("YoU FoUNd ThE ENtRAnCE T0 ThE FirST L0CKeD D00r!")
		elif enter == "B":
			print("ThE MAn In YelLOw GoT Y0u! YOu DIe!!!")
	elif room == "ENTRANCE TO THE FIRST LOCKED ROOM":
		if enter == "A":
			if key1 in inventory:
				room = "LOCKED ROOM 1"
				print("YoU MaDe It InTO ThE LOcKed ro0M 1!")
	elif room == "LOCKED ROOM 1":
		if enter == "A":
			room = "TV"
			print("YoU WenT T0 ThE TV")
		elif enter == "B":
			print("N0ThIng HAppEneD OnCe YoU wenT To ThE Do0r So YoU WenT bAcK To ThE rOOm")
	elif room == 'TV':
		if enter == "A":
			if CD in inventory:
				room = "CORRIDOR"
				print("ThE TV SHoWs YoU WHerE ThE LAsT Ro0M Is!")
	elif room == "CORRIDOR":
		if enter == "A":
			room = "THE FINAL DOOR ENTRANCE (LOCKED DOOR 2)"
			print("YoU FOuND ThE FinAL DOoR ENtRAnCE!")
		elif enter == "B":
			print("OrCrYoSs FouND YoU! YoU DiE!")
	elif room == "THE FINAL DOOR ENTRANCE (LOCKED DOOR 2)":
		if enter == "A":
			print("YoU OpEn ThE DOoR AnD EsCaPe ThE HouSE! YoU WiN!!!")
			break
			
