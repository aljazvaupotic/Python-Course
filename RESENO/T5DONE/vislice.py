#!/usr/bin/env python
# -*- coding: utf-8 -*-
#______________________________________________________________________________
#Termin 5
# vaje
#______________________________________________________________________________

import random as rd
# 1. Vislice
# Oseba 1 vnese besedo / računalnik zbere naključno besedo iz datoteke besede.txt
# Oseba 2 vnaša črke.
# Izpis naj bo takšen beseda je (continent) :  
# c _ _ _ _ _ _ _ _
# input(Vnesi črko) : t 
# c _ _ t _ _ _ _ t 
# življenja : 10
# do sedaj smo poizkusili : t
# input(Vnesi črko) : f
# c _ _ t _ _ _ _ t 
# življenja : 9
# do sedaj smo poizkusili : t, f

# BRANJE
fp = open("besede.txt","r")
opt = []
life = 10
zadete = 1
for line in fp:
	opt.append(line.strip())
#print(opt) preveri izpis opcij iz datoteke
# IZBIRA
beseda = opt[rd.randint(0,len(opt)-1)]
#print(beseda) # izpis random besede
d = len(beseda)
p = beseda[0]+ " "
#print(p) preverimo ce deluje izpis prve crke
kombinacija = "_ "
p += (d-1) * kombinacija
# IZPIS
def izpis(b,p,t,d):
	#print(b,p,t,d)
	p = p.split(" ")
	#print(p)
	for i in range(d):
		p[i] += " "
		if(b[i] == t):
			p[i] = t+" " 
	p = "".join(p)
	#print(p)
	return p
#izpis(beseda,d)
# VPRASAJ
probane = []
print(p)
while zadete != d and life > 0:
	t = input("Vnesi crko: ")
	
	# SEZNAM PROBANIH

	while t in probane:
		print("Ze probane:", probane)
		t = input("Vnesi crko, ki se je nisi probal: ")
	probane.append(t)		
	
		
	#print("Probane,",probane)

	# PREVERI CE JE V BESEDI

	if (t in beseda):#(t not in "".join(probane)):
		zadete += beseda.count(t)
		p = izpis(beseda,p,t,d)
	else :
		life -= 1
	
	print(p)
	print("Preostala življenja:", life)
	print("Že izpisane:", probane)
if life == 0:
	print("Več sreče prihodnjič, beseda ki si jo iskal je:", beseda)
else:
	print("Čestitam ugotovil si besedo:", beseda)

















