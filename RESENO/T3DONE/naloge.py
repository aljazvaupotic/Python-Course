#!/usr/bin/env python
# -*- coding: utf-8 -*-

#______________________________________________________________________________
# TERMIN 3      
# Naloge
#______________________________________________________________________________




# 1. Ustvari seznam Sadje, katerega elementi so sadezi.
# Sadez naj vsebuje ime in informacijo o tem ali ima koščice ali ne (jagoda nima, jabolko ima =D )
class Sadez:
	def __init__ (self,ime,k):
		self.ime = ime
		self.k = k
sadje = []
	
# 2. Ustvari funkcijo, ki bo dodajala elemente v seznam. Izmisli si tudi 5 
def neobstoj(ime):
	global sadje
	for s in sadje:
		if ime.capitalize() == s.ime:
			return False
	return True

def dodaj(ime,k):
	global sadje 
	s = Sadez(ime.capitalize(),k.upper())
	if s.k != "DA" and s.k != "NE" :
		s.k = input("Vnes ali ima sadež " + s.ime + " koščice! V obliki DA/NE: ")
		s.k = s.k.upper()
	if neobstoj(s.ime):
		sadje.append(s)

dodaj("Lubenica","da")
dodaj("Hruška","Da")
dodaj("Banana","NE")
dodaj("Jagoda","NIMAJO")
dodaj("Kokos","ne")

for x in sadje:
	print(x.ime,x.k)
		
# 3. V seznamu preštej, koliko sadežev nima koščic.
stBrez = 0
for p in sadje:
	if p.k == "NE":
		stBrez += 1
print(stBrez)


# 4. Uporabnik naj doda še en sadež 
def vnos(niz):
	u = niz.split(" ")
	imeS = ""
	for b in range(len(u) - 1):
		imeS += u[b] + " "
	koscice = u[len(u) - 1]

	imeS = imeS.capitalize().strip()
	koscice = koscice.upper()
	dodaj(imeS,koscice)

u = input("Vnesi ime sadeža in ali ima koščice (DA/NE)")
vnos(u)

for x in sadje:
	print(x.ime,x.k)
print()
# 5. Iz datoteke sadje.txt preberi sadeže, preveri če sadež še ne obstaja ga dodaj drugače preskoči.

fp = open("sadje.txt","r")

for line in fp:
	vnos(line.strip())


for x in sadje:
	print(x.ime,x.k)




# 6 Izpiši imena sadežev.
