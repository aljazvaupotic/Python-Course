#____________________________________________________________________
# TERMIN 4, 12.6.2019
# naloge1
#____________________________________________________________________

# Gnezdenje oklepajev
#
# Oklepaji so pravilno gnezdeni, če predklepaji in zaklepaji nastopajo v
# parih in število zaklepajev nikoli ne preseže števila predklepajev, ko
# jih štejemo od leve proti desni.

# 1
# Sestavite funkcijo `oklepaji(niz)`, ki bo preverila, ali so v danem
# nizu oklepaji pravilno gnezdeni. Na ostale znake naj se funkcija ne
# ozira. Zgled:
# 
#     >>> oklepaji('(a + b)^2 = (((a^2) + 2ab) + b^2)')
#     True
#     >>> oklepaji('())(()')
#     False

def oklepaji(s):
	stOklepajev = 0
	stZaklepajev = 0
	for znak in s:
		if(stZaklepajev > stOklepajev): 
			return False
		if(znak == "(") : 
			stOklepajev += 1 
		if(znak == ")") : 
			stZaklepajev += 1
	if(stOklepajev == stZaklepajev):
		return True
	return False

print(oklepaji("(a+b(*232(fsadg)))()"))


# 2
# Sestavi funkcijo `imena_na_B(imena)`, ki sprejme seznam
# imen in vrne seznam imen, ki se začnejo z črko `'B'`.
# 
# Primer:
# 
#     >>> imena_na_B(["Mojca", "Janez", "Bojana", "Bine", "Ana", "Blaž"])
#     ['Bojana', 'Bine', 'Blaž']
#     >>> imena_na_B(["Borut", "miza", "balon"])
#     ['Borut']

def imena_na_B(seznamImen):
	novSeznam = []
	for ime in seznamImen:
		if ime[0] == "B":
			novSeznam.append(ime)
	return novSeznam
s = ["Mojca", "Janez", "Bojana", "Bine", "Ana", "Blaž","banana","MBranko"]
print(imena_na_B(s))



# 3
# Sestavi funkcijo `odstrani_predolge(besede)`,
# ki sprejme seznam besed in vrne seznam
# tistih besed, ki so krajse od $7$.
# 
# Primer:
# 
#     >>> odstrani_predolge(["svetilnik", "sok"])
#     ['sok']

def odstrani_predolge(seznam):
	nS = []
	for b in seznam :
		if(len(b) < 7):
			nS.append(b)

	return nS


s = ["količnik","vsota","integrabilnost","mavrica","pes","križ"]

m = odstrani_predolge(s)

print(m)
# 4
# Sestavi funkcijo `prestej_predolge(besede)`,
# ki sprejme seznam besed in vrne stevilo besed, ki so daljše od $6$.
# 
# Primer:
# 
#     >>> prestej_predolge(["avtobus", "sirena", "kolesar", "pes", "moka"])
#     2
def prestej_predolge(s,dolzina):
	counter = 0
	for beseda in s:
			if len(beseda) > dolzina :
				counter += 1
	return counter

print(prestej_predolge(s,11))




# 5 
# Sestavi funkcijo  `precisti_seznam(seznam)`,
# ki iz seznama umakne vse elemente kateri niso števila
def precisti(s) :
	nS = []
	for el in s :
		if isinstance(el,(int,float)):
			nS.append(el)
		elif isinstance(el,list):
			nS += (precisti(el))
	return nS

print()

stevila = [1,["fasdagasd","#"],324,5657.655, 2141,"fdsjad",[1,[232,213, "#",4],23,456,54],3,"#!"]
print(stevila)
print(precisti(stevila))


