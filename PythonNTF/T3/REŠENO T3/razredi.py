#______________________________________________________________________________
# TERMIN 3      11.6.2019
# MyClass
#______________________________________________________________________________

# Če nam tipi, katere smo do sedaj ne ustrezajo si lahko izmislimo svojega:

class Oseba:
	def __init__ (self,ime,priimek,spol,starost):
		self.ime = ime
		self.priimek = priimek
		self.spol = spol
		self.starost = starost
	rojstni_kraj = "Ljubljana"

# ustvarimo novo osebo:

p = Oseba("Janez","Novak","M",24)

print(p.ime,p.priimek,p.spol,p.rojstni_kraj)
p.priimek = "Grad"
print(p.ime,p.priimek,p.spol,p.rojstni_kraj)
p.zena = "Da"
print(p.ime,p.priimek,p.spol,p.rojstni_kraj,p.zena)
# Več oseb nam lahko ustvari seznam oseb. Izmisli si še 5 oseb. 
seznam = [p]
seznam.append(Oseba("Klemen","K","M",18))
seznam.append(Oseba("Sandra","S","Ž",19))
seznam.append(Oseba("Patrik","P","M",55))
seznam.append(Oseba("Julija","S","Ž",22))
seznam.append(Oseba("Tina","T","Ž",92))
print()
for o in seznam:
	print(o.ime,o.starost)
print()

# Vsem osebam prištej 5 let
for o in seznam:
	if o.starost > 90:
		seznam.remove(o)
	else:
		o.starost += 5
for o in seznam:
	print(o.ime,o.starost)
print()	


# Izpiši število žensk.
c = 0
for o in seznam:
	if(o.spol == "Ž"):
		c += 1
print(c)
# Razredi imajo lahko tudi vgrajene funkcije. Ustavri class hrana, ki naj vsebuje
# ime hrane, barvo, tip (meso,sadje,zelenjava). In napiši funkcijo v tem razredu,
# ki bo predstavilo izpisal ime te hrane.
class Hrana:
	def __init__ (self,ime,barva,tip,):
		self.ime = ime
		self.barva = barva
		self.tip = tip
	def predstaviSe(self):
		print("Sem " + self.ime + " in sem " + self.tip)

h = Hrana("Ribica","rdeča","meso")
print("Sem",h.ime,"in sem",h.tip)
h.predstaviSe()


# Dedovanje v pythonu

# Primer: Vsi študentje so ljudje, vsi ljudje niso študentje. 
# Torej vsak študent ima vse lastnosti, ki jih ima oseba. 
#Vse osebe nimajo "lastnosti", katere imajo študentje. 
# npr. letnik, kreditne točke

class Student(Oseba):
	def __init__(self,ime,priimek,spol,starost,letnik,kt):
		Oseba.__init__(self,ime,priimek,spol,starost)
		self.letnik = letnik
		self.kt = kt

s1 = Student("Aljaž","V","M",23,3,"Dovolj")
o = Oseba("Ema","D","Ž",19)
s2 = Student(o.ime,o.priimek,o.spol,o.starost,1,"Premalo")
print(s1)
print(o)	
print(s2)



PAVZA 16:45















