#____________________________________________________________________
# TERMIN 4, 12.6.2019
# naloge2
#____________________________________________________________________

# Kuhamo in pečemo
#
# Sestavine, ki jih potrebujemo za nek recept, opišemo s slovarjem, v
# katerem so ključi sestavine, vrednosti pa količine, ki jih potrebujemo.
recept = {"mleko": 500,"moka":240,"jajca":2,"sol":1,"olje" : 2,"ginger": 1}
shramba = dict()
fp = open("shramba.txt","r")
for line in fp:
	if(line == "\n"):
		break
	l = line.split(":")
	sestavina = l[0].strip()
	kolicina = int(l[1].strip())
	shramba[sestavina] = kolicina

fp.close()
print("shramba")
for x,y in shramba.items():
	print(x,y)
print()
print("recept")
for x,y in recept.items():
	print(x,y)

# 1. podnaloga
# Sestavite funkcijo `pomnozi(recept, faktor)`, ki sestavi in vrne nov
# recept. Ta naj vsebuje iste sestavine kot recept `recept`, le da so vse
# količine v njem pomnožene z danim faktorjem.
# 
#     >>> pomnozi({'jajca': 4, 'moka': 500}, 2)
#     {'jajca': 8, 'moka': 1000}

def pomnozi(r, faktor):
	for x in r:
		r[x] *= faktor
	return r
#print()
#print("recept after")
# recept2 = pomnozi(recept,2.3)
# for x,y in recept2.items():
# 	print(x,y)
# print()


# 2. podnaloga
# Sestavite funkcijo `imamo_sestavine(recept, shramba)`, ki preveri, ali
# imamo v shrambi dovolj sestavin za dani recept. Sestavine, ki jih imamo
# v shrambi, so predstavljene s slovarjem na enak način kot sestavine v
# receptu.
# 
#     >>> imamo_sestavine({'jajca': 3, 'moka': 500}, {'moka': 600})
#     False
print()
def imamo(r,s):
	jeStvar = 0
	for kuha, kolikoKuha in r.items() :
		for doma, kolikoDoma in s.items():
			#print(doma,kuha)

			if(doma == kuha):
				#print("Našel v shrambi")
				if(kolikoDoma >= kolikoKuha):
					jeStvar += 1
					break

	#print(jeStvar)
	#print(len(recept))
	vse = jeStvar == len(recept)


	return vse

print(imamo(recept,shramba))






# 3. podnaloga
# Sestavite funkcijo `potrebno_kupiti(recept, shramba)`, ki vrne slovar
# sestavin s pripadajočimi količinami, ki jih moramo še dokupiti, da bomo
# lahko skuhali jed po danem receptu.
# 
#     >>> potrebno_kupiti({'jajca': 3, 'moka': 500}, {'moka': 1000, 'sladkor': 1000})
#     {'jajca': 3}


def potrebno_kupiti(s,r):
	#print("SMO TUKAJ")
	listek = dict()
	for kuha, kolikoKuha in r.items() :
		flag = 0
		for doma, kolikoDoma in s.items():
			#print(doma,kuha)

			if(doma == kuha):
				flag = 1
				if(kolikoDoma < kolikoKuha):
					listek[kuha] = kolikoKuha - kolikoDoma
					break

		#print(kuha,flag)
		if(flag == 0):
			listek[kuha] = kolikoKuha


	return listek

nakup = potrebno_kupiti(shramba,recept)
for x,y in nakup.items():
	print(x,y)




