#____________________________________________________________________
# TERMIN 4, 12.6.2019
# Moduli / Knjižice
#____________________________________________________________________

# https://docs.python.org/3/library/
# Python ima veliko že vgrajenih knjižnic, ki vključujejo uporabne funkcije in metode.
import datetime as dt

casNaZacetku = dt.datetime.now()
print(casNaZacetku)


# MATH
import math

# poišči najmanjši in največji element v seznamu a.
a = [35,42,312,77,-95,-214,2,-56, 1242415,535]
print(min(a),max(a))
for i,x in enumerate(a) :
	#print(math.fabs(x))
	a[i] = int(math.fabs(x))
print(min(a),max(a))
# Koliko je kvadratni koren št x.
x = 1764
print(math.sqrt(x))
print(42*42*42*42*42 , int(math.pow(42,5)))

# Izpiši v stopinjah kolikšen kot je k

k = math.pi * 1.7
e = math.e
print(math.degrees(k+1))
print(math.radians(21413254))
print(math.degrees(1))



# Koliko je vsota vseh elementov seznama a.
vsota = 0
for s in a:
	vsota += s

print(vsota)

print(int(math.fsum(a)))

# RANDOM

# Napiši igrico ki bo metala kocko (1-6).
#Uporabnik naj na začetku izbere željeno končno število. 
#Progam naj izpisuje mete, hkrati sešteva njihovo vsoto. 
# Ko je vsota večja ali enaka željenemu število. Izpiši statistiko.
# Koliko metov je bilo potrebnih, povprečno vrednost meta,
# katero število smo vrgli največkrat, koliko več metov od optimalne kombinacije smo porabili? 
import random

ponovitve = [0,0,0,0,0,0,0] # [št metov 0,št metov 1,št metov 2, št metov 3......]

cilj = int(eval(input("Vnesi število med 1 in 1000:")))
vsota = 0
koliko = 0
while vsota < cilj :
	met = random.randint(1,6)
	print(met)
	vsota += met
	koliko += 1
	ponovitve[met] += 1


def optimal(x):
	return (math.ceil(x/6))
index = ""
najveckrat = max(ponovitve)

for i in range(1,7):
	if(ponovitve[i] == najveckrat) :
		index += str(i) + " "

print("Potrebovali smo", koliko, "metov.")
print("povprečna vrednost je bila", round(vsota/koliko,4))
print(index +"smo vrgli največkrat")
print("Potrebovali smo", koliko - optimal(cilj), "več od optimalne št metov")

print(koliko == int(math.fsum(ponovitve)))
# DATETIME

# Izpiši kako dolgo se izvaja program
casNaKoncu = dt.datetime.now()

print(casNaKoncu - casNaZacetku)

# SYSTEM / PLATFORM
 
# v knjižnici poišči metodo ki nam izpiše verzijo operacijskega sistema
import platform

print(platform.platform())




# MojModul

# Sestavili bomo svoj modul, ki bo vseboval metode:
# - pozdrav
# - odzdrav
# - small talk: ki bo imel 4 različne opcije (a,b,c,d)

import mojmodul 

mojmodul.pozdrav("Aljaž")
mojmodul.smallTalk("d")
