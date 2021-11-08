#!/usr/bin/env python
# -*- coding: utf-8 -*-

#______________________________________________________________________________
# TERMIN 3      
# MyClass
#______________________________________________________________________________

# Če nam tipi, katere smo do sedaj ne ustrezajo si lahko izmislimo svojega:
class Oseba:
	def __init__(self,ime,priimek,spol,starost):
		self.ime = ime
		self.priimek = priimek
		self.spol = spol
		self.starost = starost
	kraj = "LJ"
	def izpis(self):
		print(self.ime,self.priimek,self.spol,self.starost,self.kraj)

# ustvarimo novo osebo:
p = Oseba("Janez","Novak","M",24)
print(p.ime,p.spol,p.kraj)
p.starost += 1
p.ime = "Luka"
print(p.ime, p.starost)
p.rojstnikraj = "Celje"
print(p.rojstnikraj)
# Več oseb nam lahko ustvari seznam oseb. Izmisli si še 5 oseb. 
sez = [p]
# VSI PODATKI BREZ LOOPA - NA KRATKO
print(sez)
sez.append(Oseba("Klemen","K","M",87))
sez.append(Oseba("Tina","V","Ž",44))
sez.append(Oseba("Sandra","F","R",23))
sez.append(Oseba("Klemen","K","M",18))
sez.append(Oseba("Franci","T","Ž",27))
print(sez[0].ime)
for o in sez:
	o.rojstnikraj = "Kranj"
	print(o.ime, o.starost, o.rojstnikraj)

print()
# Vsem osebam prištej 5 let
d = len(sez)
i = 0
while i < d:
	sez[i].starost += 5
	print(sez[i].ime, sez[i].starost)
	if sez[i].starost > 90:
		sez.pop(i)
		d -= 1
		continue
	i += 1

for o in sez:
	print(o.ime)
# Izpiši število žensk.

c = 0
for o in sez:
	if o.spol == "Ž":
		c += 1
print(c)


# Razredi imajo lahko tudi vgrajene funkcije. Ustavri class hrana, ki naj vsebuje
# ime zelenjave, barvo, tip (meso,sadje,zelenjava). In napiši funkcijo v tem razredu,
# ki bo predstavilo izpisal ime te hrane.

class Hrana:
	def __init__ (self,ime,barve,tip):
		self.ime = ime
		self.barve = barve
		self.tip = tip
	def predstavi(self):
		print("Sem " + self.ime + " in sem " + self.tip)
		
h1 = Hrana("Riba","modra","meso")
h2 = Hrana("Brokoli","zelen","zelenjava")

h1.predstavi()
x = 5
p.izpis()





# Dedovanje v pythonu

# Primer: Vsi študentje so ljudje, vsi ljudje niso študentje. 
# Torej vsak študent ima vse lastnosti, ki jih ima oseba. Vse osebe nimajo "lastnosti", katere imajo študentje. npr. letnik, kreditne točke


class Student(Oseba):
	def __init__(self,ime,priimek,spol,starost,letnik,kt):
		Oseba.__init__(self,ime,priimek,spol,starost)
		self.letnik = letnik
		self.kt = kt
		
s1 = Student("Aljaž","V","M",23,3,"premalo")
s1.izpis()

sezSt = [s1]
for o in sez:
	if o.starost <= 30:
		sezSt.append(Student(o.ime,o.priimek,o.spol,o.starost,2,"DOVOLJ"))
for st in sezSt:
	print(st.ime,st.letnik)
















