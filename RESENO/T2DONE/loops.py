#!/usr/bin/env python
# -*- coding: utf-8 -*-


#______________________________________________________________________________
# Termin 2, 30.5.2019
# While and For
#______________________________________________________________________________

# Izpiši števila od 1 do 10:
print(1,2,3,4,5,6,7,8,9,10)
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
print()
# Izpiši števila od 1 do 10 z uporabo zanke while:

i = 1

while i <= 10:
	print(i)
	i+= 1
print()
# Izpiši števila od 1 do 10 z uporabo zanke for:

for stevilo in range(1,11):
	print(stevilo)

print()


# 	Kakšna je razlika med while in for?
# While uporabljamo, ko ne vemo kolikokrat bomo dostopali v zanko.
# For uporabljamo, ko poznamo dolžino svojega "sprehoda"

niz = "Meza je velika jed. Sladoled je zelo sladek. Potica omara je mogoče super nekoč bila vedno je."

# Dokler nebos prestel 2eh Ojev izpisuj nisem še
stO = 0
niz = niz.lower()
dolzina = len(niz)
i = 0
while stO < 2 and i != dolzina  :
	if(niz[i] == "o"):
		stO += 1
	#print(niz[:i+1])
	i += 1
print("Na i-tem mestu se pojavi drugi o :",i)

stO = 0
i = 0
for c in niz:
	if c == "o":
		stO += 1
	
	#print(niz[:i+1])
#	i += 1
	if stO == 2:
		break
print("Na i-tem mestu se pojavi drugi o :",i)
# Izberi si eno število med 1 in 100. 
x = 71
# a) Izpiši vsa števila CELA POZITVNA manjša od izbranega, uporabi obe zanki!
i = 1
while i < x :
	print(i)
	i += 1 # i = i + 1 

for st in range(1,x):
	print(st)


# b) Izpiši le to število in njegove večkratnike, manjše od števila 500. 
# Ponovno uporabi obe zanki!
i = 1
print()
while x*i < 500:
	print(x*i)
	i += 1
y = 71
x = 71
print()
while y < 500:
	print(y)
	y += x
print()
for i in range(1,501):
	if(i % x == 0):
		print(i)

