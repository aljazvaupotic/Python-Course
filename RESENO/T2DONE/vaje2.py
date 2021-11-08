#______________________________________________________________________________
# Termin 2, 30.5.2019
# Vaje in DN
#______________________________________________________________________________

# 1. Preštej kolikokrat se pojavijo samoglasniki v besedah : 
niz = ["Dialektičnomaterialističen", "buržoaznonacionalističen", "starocerkvenoslovanščina","OnkrajSveta"]

# def sg(beseda):
	# beseda = beseda.lower()
	#A
	# a = beseda.count("a")
	#E
	# e = beseda.count("e")
	#I
	# i = beseda.count("i")
	#O
	# o = beseda.count("o")
	#U
	# u = beseda.count("u")
	# return a+e+i+o+u
# skupnaVsota = 0
# for b in niz:
	# skupnaVsota += sg(b)
	# print(sg(b))
	
# print(skupnaVsota)

# 2. Sestavite funkcijo `vsota_kvadratov_stevk(n)`, ki vrne vsoto kvadratov števk
# *tromestnega* števila `n`.
# 
#     >>> vsota_kvadratov_stevk(123)
#     14
# print()
# def vsota_kvadratov_stevk3(n):
	# e = n % 10
	# n //= 10
	# d = n % 10
	# s = n // 10
	# return e*e + d*d + s*s
# print(vsota_kvadratov_stevk3(123))
# print(vsota_kvadratov_stevk3(244))
# print(vsota_kvadratov_stevk3(25))
# print(vsota_kvadratov_stevk3(1234))
# print()
# def vsota_kvadratov_stevk(n):
	# vsota = 0
	# while n > 0 :
		# v = n% 10
		# vsota += v*v
		# n //= 10
		# print(vsota)
	# return vsota
# print(vsota_kvadratov_stevk(123))
# print(vsota_kvadratov_stevk(244))
# print(vsota_kvadratov_stevk(25))
# print()
# print(vsota_kvadratov_stevk(1234978974564))

# 3.
#	a) Sestavite funkcijo `obrat(n)`, ki vrne število, ki ga dobimo, če številu `n`
# zamenjamo števki na mestu enic in stotic.
 
#     >>> obrat(123)
#     321
# print()
# def obrat3(n):
	# e = n % 10
	# d = (n//10)%10
	# s = n//100
	# return e*100+d*10+s
# print(obrat3(123))
# print(obrat3(23))
# print(obrat3(123456))

#	b) Sestavi funkcijo še za poljubno dolgo število ali besedo.

# def obrat(n):
	# o = 0
	# while n > 9:
		# o += n % 10
		# n //= 10
		# o *= 10
	# return o+n
# print(obrat(123))
# print(obrat(23))
# print(obrat(123456))

# print(12315135)
# print(int(str(12315135)[::-1]))
	
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
count = 0

# Dodati želimo Hondo ki je dosegljiva v modri, zeleni in beli barvi
mZnamke.append("Honda")

while( count < 3):
	vnos = input("Vnesi željeno kombinacijo: ")
	#print(vnos) preveri branje podatkov
	vnosTabela = vnos.split(" ")
	if vnosTabela[1].title() in mZnamke:
		barva = vnosTabela[0][0:3].lower()
		znamka = vnosTabela[1].title()
	elif vnosTabela[0].title() in mZnamke:
		barva = vnosTabela[1][0:3].lower()
		znamka = vnosTabela[0].title()
	else: 
		print("Izbrali ste napačno znamko!")
		continue
	#print(znamka, barva)
	if barva not in mBarve:
		print("Izbrali ste napačno bravo!")
		continue
	# print(barva, znamka) preverimo če znamo razdeliti vnos na barve in znamke

	if znamka == mZnamke[0] : #FERRARI
		if(barva == mBarve[1] or barva == mBarve[3]):
			print("Dodaj v košarico!")
			count += 1
			#break
		else:
			print("Kombinacija ni mogoča! Izberi novo!")
	elif znamka == mZnamke[1] : #RENAULT
		if(barva == mBarve[0]) :
			print("Kombinacija ni mogoča! Izberi novo!")
		else:
			print("Dodaj v košarico!")
			count += 1
			#break
	elif znamka == mZnamke[2] : #AUDI
		if(barva == mBarve[0] or barva == mBarve[4] or barva == mBarve[5]):
			print("Dodaj v košarico!")
			count += 1
			#break
		else:
			print("Kombinacija ni mogoča! Izberi novo!")
	elif znamka == mZnamke[5] : #HONDA
		if(barva == mBarve[0] or barva == mBarve[4] or barva == mBarve[2]):
			print("Dodaj v košarico!")
			count += 1
			#break
		else:
			print("Kombinacija ni mogoča! Izberi novo!")
	else:
		print("Dodaj v košarico!")
		count += 1
		#break
		
print("Pošiljka v dostavi!")
