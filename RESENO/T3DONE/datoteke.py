#!/usr/bin/env python
# -*- coding: utf-8 -*-

#______________________________________________________________________________
# TERMIN 3      
# Datoteke
#______________________________________________________________________________


# odpremo lahko že obstoječo ali pa novo datoteko
# pazimo da sta že obstoječa datoteka in naš program v isti mapi! če nista moramo dodati pravilno pot (path)

# Datoteko lahko :
#		- beremo (prevzeta vrednost, odpre datoteko za branje, error če ta ne obstaja)
#		- dodajamo (odpre datoteko z možnostjo dodajanja, če ne obstaja jo ustvari)
#		- pišemo (odpre datoteko za pisanje, prav tako jo ustvari če ne obstaja)
#		- ustvarimo (ustvari datoteko, error če ta obstaja)


#lahko še dodamo tip datoteke (text ali binary)

datoteka = open("demo.txt","r")

# Branje datoteke
# vsebina = datoteka.read()
# print(vsebina)
vsebina1 = datoteka.readline()
print(vsebina1)
vsebina2 = datoteka.readline()
print(vsebina2)
# Zapiranje datoteke
datoteka.close()

#1. Odpri datoteko tekst1.txt in izpiši vsako drugo vrstico.
branaDatoteka = open("tekst1.txt","r")
pisanaDatoteka = open("naloga.txt","w")

for index,vrstico in enumerate(branaDatoteka):
	if index % 2 == 1:
		print(vrstico.strip())
		pisanaDatoteka.write(vrstico.strip()+"\n")
branaDatoteka.close()
pisanaDatoteka.close()

fp = open("C:/Users/predavalnica25/Documents/faraway.txt","r")
print(fp.read())
fp.close()
#2. Odpri datoteko dict.txt in preštej koliko krat se pojavi katera beseda. 
#  (Ločuj med velikimi začetnicami in malimi)

fp = open("dict.txt","r")
poved = fp.read()
print(poved)
sb = poved.split(" ")
print(sb)
d = {}  
print(type(d))
d = dict()
print(type(d))
for b in sb:
	dodaj = True
	for kljuc, vrednost in d.items():
		if b.lower() == kljuc :
			dodaj = False
	if dodaj == False:
		d[b.lower()] += 1
	else:
		d[b.lower()] = 1
print()
for kljuc, vrednost in d.items():
	print(kljuc,vrednost)

o = {}	
	
for b in sb:
	dodaj = True
	for kljuc, vrednost in o.items():
		if b.lower() == kljuc :
			dodaj = False
	if dodaj :
		o[b.lower()] = 1
	else:
		o[b.lower()] += 1
print()
for kljuc, vrednost in o.items():
	print(kljuc,vrednost)
