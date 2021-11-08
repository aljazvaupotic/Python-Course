#!/usr/bin/env python
# -*- coding: utf-8 -*-
#____________________________________________________________________
# TERMIN 4, 
# Moduli / Knjižice
#____________________________________________________________________

# https://docs.python.org/3/library/
# Python ima veliko že vgrajenih knjižnic, ki vključujejo uporabne funkcije in metode.

# MATH
import datetime as dt
casZacetek = dt.datetime.now()

import math
# poišči najmanjši in največji element v seznamu a.
a = [35,42,312,77,95,214,2,56]
print(min(a))
print(max(a))

# Koliko je kvadratni koren št x.
x = 1764
y = 2
i = 1
kvadarat = math.sqrt(y)
print(kvadarat)
# Izpiši v stopinjah kolikšen kot je k

k = math.pi * 1.7

print(math.degrees(k))
print(math.radians(180))

# Koliko je vsota vseh elementov seznama a.
vsota = 0
for el in a :
	vsota += el
print (vsota)
print(math.fsum(a))

# RANDOM
print()
print("KOCKA")
print()
# Napiši igrico ki bo metala kocko (1-6).
# Uporabnik naj na začetku izbere željeno končno število. Progam naj izpisuje mete, hkrati sešteva njihovo vsoto. 
# Ko je vsota večja ali enaka željenemu število. Izpiši statistiko.
# Koliko metov je bilo potrebnih, povprečno vrednost meta, 
# katero število smo vrgli največkrat, koliko več metov od optimalne kombinacije smo porabili? 
import random as rd
ponovitve = [0,0,0,0,0,0,0]
cilj = eval(input("Vnesi število med 1 in 1000: "))
vsota = 0
stMetov = 0
while vsota < cilj : 
	met = rd.randint(1,6)
	print(met)
	vsota += met
	stMetov += 1
	ponovitve[met] +=  1

print(vsota,stMetov,ponovitve[1:7])
print("Povp. vrednost",vsota / stMetov )
m = max(ponovitve)
izpis = "Najveckrat smo vrgli "
for i in range(1,7):
	if( ponovitve[i] == m):
		izpis += str(i) +  " " 
print(izpis.strip())
optimalna = math.ceil(cilj/6)
print("Porabili smo :", stMetov - optimalna, "preveč" )
print(stMetov == int(math.fsum(ponovitve)))

# DATETIME
casZdaj = dt.datetime.now()
print(casZdaj - casZacetek)
# Izpiši kako dolgo se izvaja program


# SYSTEM / PLATFORM
import platform
import sys 
import os
# v knjižnici poišči metodo ki nam izpiše verzijo operacijskega sistema
print(platform.platform())

# MojModul

# Sestavili bomo svoj modul, ki bo vseboval metode:
# - pozdrav
# - odzdrav
# - small talk: ki bo imel 4 različne opcije (a,b,c,d)


import mmodul 

mmodul.pozdrav()
mmodul.smalltalk("drr")
