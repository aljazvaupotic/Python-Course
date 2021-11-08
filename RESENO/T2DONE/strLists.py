#!/usr/bin/env python
# -*- coding: utf-8 -*-



#______________________________________________________________________________
# Termin 2, 
# Nizi in seznami
#______________________________________________________________________________


# cmd /K python "$(FULL_CURRENT_PATH)" 




# Naslednja koda vsebuje, kar se zamikov tiče, cel kup napak.
# 
#x = int(input('x: '))
#y = int(input('y: '))
# if x == 3 and y == 4:
	# print("x je 3")
# print("y je morda 4, vem pa ne")

# if x > 2 and y < 5:
	# print("x > 2")
	# print("y < 5")
	
# if x < 4 and y > 3 :
	# print("x < 4")
	# print("y > 3")

# Skopiraj jo in jo popravi! Stavkov samih ne spreminjaj, le njihove zamike!
# Popravki morajo biti taki, da so izpisi smiselni!



# 1. V povedi: "VčeRaj jE bIL SonČEn dAn". 
niz = "VčeRaj jE bIL SonČEn dAn"

#	a) Poišči in izpiši črko na 5-tem mestu
print(niz)
print(niz[4])
print(niz[0])

#	b) Izpiši dolžino niza (stringa)

print(len(niz))

#	c) Izpiši niz med 3-jim in 9-im mestom (vkjučno z 3 in 9).
print(niz[2], niz[8])
print(niz[2:9])
print(niz[10:len(niz)])
# 	c) Vse prve črke besede spremeni v velike, vse ostale v majhne.

print(niz.title())
print(niz.upper())
print(niz.lower())
print(niz.swapcase())
print(niz.capitalize())

niz = niz.capitalize()
print(niz)
#	d) Če poved vsebuje besedo "sončen" izpiši "Res je bil."
# print("King" in "Kings Landing")
# print("Jon Snow" in "Kings Landing")
print()

if "sončen" in niz : 
	print("Res je bil.")
else:
	print("Padal je dež.")


#	e) Zamenjaj vse e-je v u-je


# NAPAČNO ZAPOREDJE print(niz.replace("e","u").lower())
# PRAVILNO ZAPOREDJE print(niz.lower().replace("e","u"))
print(niz.replace("e","u"))


print()
# 2. 
#	a) Sestavi seznam s tremi števili.
s = [42,84,456,84]
#	b) Izpiši ta seznam.
print(s)
print(type(s))
#	c) Dodaj števili 11 in 24 na konec seznama, 
#a = [11,312,3215436,6758]
s += [11]
print(s)
s.append(24)
print(s)
#	dodaj število 5 na 2-go mesto.
s.insert(1,5)
print(s)
print(s[2])
#s[2] = "lagj"
#print(s[2],type(s[2]))

#	d) Ponovno izpiši ta seznam.
print(s)
print("Dolzina je ",len(s))
#	e) Poišči najmanjšo in največjo številko v seznamu.
print(min(s))
print(max(s))
# pop remove
s.remove(84)
print(s)
s.pop()
print(s)
s.pop(0)
print(s)

# 	f) Izpiši seznam v nasportnem vrstnem redu.
s.reverse()
print(s)
print(s[::-1])
print(s[0:len(s):2])
print()
sadje = ["banana","jagoda","avokado","črešja","lubenica","Jagoda"]
#iskanje v seznamu 
print(sadje)
if "Jagoda" in sadje:
	print("Imamo Jagode")
if "jagoda" in sadje:
	print("Imamo jagode")
else:
	print("Ni ni.")
print()
# poved v seznam
poved = "Učilnica je bila velika, nato so jo zmanjšali."
print(poved)
povedVSeznam = poved.split(" ")
print(povedVSeznam)
povedVSeznam[3] = "majhna"
povedVSeznam[len(povedVSeznam)-1] = "povečali."
print(povedVSeznam)
poved = (" ").join(povedVSeznam)
print(poved)
print()
# 3. 
s1 = [12,23,34,14,154,48,85,96,77,123,27,90]
# Ustvari kopijo seznam in vsakemu členu prištej 1.
s2 = s1.copy()
d =  len(s2)
#s2[0] += 1
#s2[1] += 1
print(s2)
for index in range(d) :
	
	s2[index] += 1
	print(index, s2)
print(s2)

# Ustvari seznam, katerega vrednosti so kvadarati osnovnega seznama.
s3 = s1.copy()
for i in range(d):
	s3[i] = s3[i] * s3[i]
print(s3)

