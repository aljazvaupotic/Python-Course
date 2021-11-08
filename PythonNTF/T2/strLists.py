#______________________________________________________________________________
# Termin 2, 30.5.2019
# Nizi in seznami
#______________________________________________________________________________

# Naslednja koda vsebuje, kar se zamikov tiče, cel kup napak.
# 
x = int(input('x: '))
y = int(input('y: '))
if x == 3 and y == 4:
    print("x je 3")
print("y je morda 4, vem pa ne")
if x > 2 and y < 5:
	print("x > 2")
	print("y < 5")
if x < 4 and y > 3 :
		print("x < 4")
		print("y > 3")

# Skopiraj jo in jo popravi! Stavkov samih ne spreminjaj, le njihove zamike!
# Popravki morajo biti taki, da so izpisi smiselni!



# 1. V povedi: "VčeRaj jE bIL SonČEn dAn". 
niz = "VčeRaj jE bIL SonČEn dAn"

#	a) Poišči in izpiši črko na 5-tem mestu
peta = niz[4]
print(peta)
#	b) Izpiši dolžino niza (stringa)
dol = len(niz)
print(niz)
print(dol)
#	c) Izpiši niz med 3-jim in 9-im mestom (vkjučno z 3 in 9).
print(niz[2:10])
# 	c) Vse prve črke besede spremeni v velike, vse ostale v majhne.
print()
print(niz)
print(niz.upper())
print(niz.lower())
niz = niz.title()
print(niz)


#	d) Če poved vsebuje besedo "sončen" izpiši "Res je bil."
if("sončen" in niz.lower()):
	print("Res je bil")
#	e) Zamenjaj vse e-je v u-je
print()
niz = niz.replace("e","u")
print(niz)


niz2 = "             fopsdgsf dsakjflksd.        "
print(niz2)
print(niz2.strip())


# 2. 
#	a) Sestavi seznam s tremi števili.
stevila = [23,30,8]
#	b) Izpiši ta seznam.
print(type(stevila))
print(type(stevila[1]))
print(type(stevila[2]))
print(stevila)
print(stevila[1]+stevila[0])
#	c) Dodaj števili 11 in 24 na konec seznama, 
#	dodaj število 5 na 2-go mesto.
stevila.append(11)
stevila.append(24)
stevila.insert(1,5)




#	d) Ponovno izpiši ta seznam.
print(stevila)


#	e) Poišči najmanjšo in največjo številko v seznamu.
print(max(stevila))
print(min(stevila))


# 	f) Izpiši seznam v nasportnem vrstnem redu.
print(stevila[::-1])
print()
print(stevila)
stevila.remove(5)
stevila.pop()
print(stevila)
stevila.pop(0)
print(stevila)
#poglej pavaza


sadje = ["banana","jagoda","avokado","črešja","lubenica"]
print(sadje)
if("banana" in sadje):
	print("Lahko dobiš banano, opica!")
sadje[2] = "hruška"
print(sadje)


poved = "Janezek vozi kolo."
povedVSeznam = poved.split(" ")
print(povedVSeznam)
povedVSeznam = list(poved)
print(poved)
print(povedVSeznam)

# 3. 
s1 = [12,23,34,14,154,48,85,96,77,123,27,90]
print(s1)
# Ustvari kopijo seznam in vsakemu členu prištej 1.
s2 = s1.copy()
for i in range(0,len(s2)):
	s2[i] += 1
print(s2)
# Ustvari seznam, katerega vrednosti so kvadarati osnovnega seznama.
s3 = s1.copy()
for i in range(0,len(s3)):
	s3[i] = s3[i]**2
print(s3)

