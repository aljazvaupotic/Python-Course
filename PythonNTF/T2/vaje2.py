#______________________________________________________________________________
# Termin 2, 30.5.2019
# Vaje in DN
#______________________________________________________________________________

# 1. Preštej kolikokrat se pojavijo samoglasniki v besedah : 
niz = ["Dialektičnomaterialističen", "buržoaznonacionalističen", "starocerkvenoslovanščina","OnkrajSveta"]

def samoglasniki (beseda):
	vsota = 0
	for i in beseda:
		if(i == "a" or i == "A"):#A
			vsota += 1
		if(i == "e" or i == "E"):#E
			vsota += 1
		if(i == "i" or i == "I"):#I
			vsota += 1
		if(i == "o" or i == "O"):#O
			vsota += 1
		if(i == "u" or i == "U"):#U
			vsota += 1
	return vsota
def sg(beseda):
	vsota = 0
	vsota += beseda.count("a") + beseda.count("A") 
	vsota += beseda.count("e") + beseda.count("E") 
	vsota += beseda.count("i") + beseda.count("I")
	vsota += beseda.count("o") + beseda.count("O")
	vsota += beseda.count("u") + beseda.count("U")
	return vsota




skupnavsota = 0
for b in niz:
	skupnavsota += samoglasniki(b)
	#print(samoglasniki(b))
	print(sg(b))
print(skupnavsota)

print()

# 2. Sestavite funkcijo `vsota_kvadratov_stevk(n)`, ki vrne vsoto kvadratov števk
# *tromestnega* števila `n`.
# 
#     >>> vsota_kvadratov_stevk(123)
#     14
def vsk3 (x):
	#print (x)
	enica = x % 10 
	x = x // 10
	#print(x)
	desetica = x % 10
	x = x// 10
	stotica = x % 10 
	#print(x)
	vsota = enica**2 + desetica**2 + stotica**2
	return vsota


def vsk (x):
	vsota = 0
	while(x > 0):
		st = x % 10
		vsota += st**2
		x = x//10
	return vsota
print()
print(vsk3(123))
print(vsk(99999999999999999999))
print(vsk(712345423134504385093845094808123205498309466758735642534135676135))

print()
# 3.
#	a) Sestavite funkcijo `obrat(n)`, ki vrne število, ki ga dobimo, če številu `n`
# zamenjamo števki na mestu enic in stotic.
 
#     >>> obrat(123)
#     321

def obrat3(x):
		#print (x)
	enica = x % 10 
	x = x // 10
	#print(x)
	desetica = x % 10
	x = x// 10
	stotica = x % 10 
	x = enica * 100 + desetica * 10 + stotica
	return x
#	b) Sestavi funkcijo še za poljubno dolgo število ali besedo.
def obrat(n):
	n = str(n)
	m = n[::-1]
	m = int(m)
	return m

def obratlep(n):
	m = 0
	while n > 0:
		m += n % 10
		m = m * 10
		n = n // 10
		#print(n,m)
	m = m//10
	return m

print(obrat3(123456))
print(obrat(123456))
print(obratlep(123456))



# 4. Imaš paleto 6-ih barv (modra, rdeča, zelena, rumena, bela, črna)
#	 in imaš 5 znamk avtomobilov (Ferrari, Renault, Audi, Mazda, Seat).

# Ferrariji so lahko le rdeči in rumeni
# Renaulti so lahko vseh barv razen modri
# Audiji so lahko beli, črni ali modri
# Mazde in Seati so lahko vseh barv

# Naj oseba vnese kombinacijo barve in avta, če je le ta dovoljena izpiši "Dodaj v košarico", če ni izpiši
# "kombinacija ni mogoča" in naj si izbere novo kombinacijo.
mBarve = ["mod","rde","zel","rum","bel","črn"]
mZnamke = ["Ferrari","Renault","Audi","Mazda","Seat"]
#dodam v možne znamke Hondo katere lahko prodajm v modri in rdeči barvi
mZnamke.append("Honda")
count = 0
while(count < 3):
	vnos = input("Vnesi željeno kombinacijo: ")
	vnos = vnos.split(" ")
	if(vnos[0][0:3].lower() in mBarve):
		barva =  vnos[0][0:3].lower()
		znamka =vnos[1].title()

	elif(vnos[1][0:3].lower() in mBarve):
		barva =  vnos[1][0:3].lower()
		znamka =vnos[0].title()
	else:
		print("Kombinacija ni mogoča popravi BARVO. Izberi novo!")
		continue
	if znamka not in mZnamke:
		print("Kombinacija ni mogoča popravi ZNAMKO. Izberi novo!")
		continue
	if(znamka == mZnamke[0]): # FERRARI
		if(barva == mBarve[1] or barva == mBarve[3]):
			print("Dodaj v košarico")
			count += 1
				#break
		else:
			print("Kombinacija ni mogoča. Izberi novo!")
			continue
	elif(znamka == mZnamke[1]): #RENAULT
		if(barva != mBarve[0]):
			print("Dodaj v košarico")
			count += 1
				#break
		else:
			print("Kombinacija ni mogoča. Izberi novo!")
			continue
	elif(znamka == mZnamke[2]): #AUDI
		if(barva == mBarve[0] or barva == mBarve[4] or barva == mBarve[5]):
			print("Dodaj v košarico")
			count += 1
					#break
		else:
			print("Kombinacija ni mogoča. Izberi novo!")
			continue
	elif(znamka == mZnamke[5]): #HONDA
		if(barva == mBarve[0] or barva == mBarve[1]):
			print("Dodaj v košarico")
			count += 1
					#break
		else:
			print("Kombinacija ni mogoča. Izberi novo!")
			continue
	else: # SEAT in Mazda
		print("Dodaj v košarico")
		count += 1
				#break
		#print("Kombinacija ni mogoča. Izberi novo!")	
print("V dostavi!")	
