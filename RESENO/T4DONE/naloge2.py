#!/usr/bin/env python
# -*- coding: utf-8 -*-
#____________________________________________________________________
# TERMIN 4, 
# naloge2
#____________________________________________________________________

# Kuhamo in pečemo
#
# Sestavine, ki jih potrebujemo za nek recept, opišemo s slovarjem, v
# katerem so ključi sestavine, vrednosti pa količine, ki jih potrebujemo.
recept = {"mleko": 500, "moka": 240,"jajca" : 2, "sol" : 1, "olje" : 2, "ginger" : 2}
shramba = dict() # shramba = {}
fp = open("shramba.txt","r")
for line in fp:
	if( line ==  "\n"):
		continue
	l = line.split(":")
	sestavina = l[0].strip()
	kolicina = int(l[1].strip())
	shramba[sestavina] = kolicina
fp.close()
print(shramba)

# 1. podnaloga
# Sestavite funkcijo `pomnozi(recept, faktor)`, ki sestavi in vrne nov
# recept. Ta naj vsebuje iste sestavine kot recept `recept`, le da so vse
# količine v njem pomnožene z danim faktorjem.
# 
#     >>> pomnozi({'jajca': 4, 'moka': 500}, 2)
#     {'jajca': 8, 'moka': 1000}

def pomnozi(recept, f ) :
	for x in recept:
		recept[x] *= f
	return recept
			
#print(recept)
recept = pomnozi(recept,1.5)		
print(recept)

# 2. podnaloga
# Sestavite funkcijo `imamo_sestavine(recept, shramba)`, ki preveri, ali
# imamo v shrambi dovolj sestavin za dani recept. Sestavine, ki jih imamo
# v shrambi, so predstavljene s slovarjem na enak način kot sestavine v
# receptu.
# 
#     >>> imamo_sestavine({'jajca': 3, 'moka': 500}, {'moka': 600})
#     False
def imam(r,s) :
	jeStvar = 0
	for kr, vr in r.items():
		for ks,vs in s.items():
			if(kr == ks):
				if(vr <= vs):
					jeStvar += 1
					break
	return jeStvar == len(r)

print(imam(recept,shramba))

# 3. podnaloga
# Sestavite funkcijo `potrebno_kupiti(recept, shramba)`, ki vrne slovar
# sestavin s pripadajočimi količinami, ki jih moramo še dokupiti, da bomo
# lahko skuhali jed po danem receptu.
# 
#     >>> potrebno_kupiti({'jajca': 3, 'moka': 500}, {'moka': 1000, 'sladkor': 1000})
#     {'jajca': 3}

def kupi(r,s):
	listek = dict()
	for kr, vr in r.items():
		flag = False
		for ks,vs in s.items():
			if(kr == ks):
				flag = True
				if(vr > vs):
					listek[kr] = vr - vs
					break
		if flag == 0:
			listek[kr] = vr
	return listek

nakup = kupi(recept,shramba)

for x, y in nakup.items():
	print(x,y)
		