# 1. Preštej koliko krat se pojavijo samoglasniki v besedah : Dialéktičnomaterialístičen, buržoaznonacionalističen, starocerkvenoslovanščina



# 2.
# Sestavite funkcijo `vsota_kvadratov_stevk(n)`, ki vrne vsoto kvadratov števk
# *tromestnega* števila `n`.
# 
#     >>> vsota_kvadratov_stevk(123)
#     14



# 3.
#	a) Sestavite funkcijo `obrat(n)`, ki vrne število, ki ga dobimo, če številu `n`
# zamenjamo števki na mestu enic in stotic.
 
#     >>> obrat(123)
#     321


#	b) Sestavi funkcijo še za poljubno dolgo število ali besedo.



# 4. Imaš paleto 6ih barv (modra, rdeča, zelena, rumena, bela, črna)
#	a in imaš 5 znamk avtomobilov (Ferrari, Renault, Audi, Mazda, Seat)

# Ferrariji so lahko le rdeči in rumeni
# Renaulti so lahko vseh barv razen modri
# Audiji so lahko beli, črni ali modri
# Mazde in Seati so lahko vseh barv

# Naj si oseba vnese kombinacijo barve in avta, če je le ta dovoljena izpiši "Dodaj v košarico", če ni odpiši da takšna kombinacija ni mogoča.

def barva (str) : 
	return {
		"mod" : 1,
		"rde" : 2,
		"zel" : 3,
		"rum" : 4,
		"bel" : 5,
		"črn" : 6,
	}[str]

def avtomobilov(str) : 
	return {
		"Ferrari"	: 1,
		"Renault"	: 2,
		"Audi"		: 3,
		"Mazda"		: 4,
		"Seat"		: 5,
	}[str]


barve = ["modra","rdeča","zelena","rumena","bela","črna"]
znamke =["Ferrari","Renault","Audi","Mazda","Seat"]

while(True):
	kombinacija = input("Vnesi željeno kombinacijo barve in avtomobila: ")
	kombinacija = kombinacija.split(" ")
	kombinacija[0] = kombinacija[0].lower() 
	kombinacija[1] = kombinacija[1].title()
	#print(barva(kombinacija[0][0:3]))
	x = int(barva(kombinacija[0][0:3]))
	y = int(avtomobilov(kombinacija[1]))

#Ferarri
	if y == 1:
		if x == 2 or x == 4 :
			print("Dodano v košarico")
			break
		else :
			print("Ta barvna kombinacija ni mogoča")
			continue

#Renault
	if y == 2:
		if x == 1:
			print("Ta barvna kombinacija ni mogoča")
			continue
		else:
			print("Dodano v košarico")
			break
#Audi
	if y == 3:
		if x == 2 or x == 3 or x == 4:
			print("Ta barvna kombinacija ni mogoča")
			continue
		else:
			print("Dodano v košarico")
			break


#Mazda Seat
	else:
		print("Dodano v košarico")
		break


# Dodaj svojo znamko in dopiši pravila za njo :D
