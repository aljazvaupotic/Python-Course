#______________________________________________________________________________
# TERMIN 3      11.6.2019
# MyClass
#______________________________________________________________________________

# Če nam tipi, katere smo do sedaj ne ustrezajo si lahko izmislimo svojega:

class Oseba:
	def __init__ (self,ime,priimek,spol):
		self.ime = ime
		self.priimek = priimek
		self.spol = spol

# ustvarimo novo osebo:

p = Oseba("Janez","Novak","M")

print(p)

# Več oseb nam lahko ustvari seznam oseb. Izmisli si še 5 oseb. 


# Vsem osebam prištej 5 let

# Izpiši število žensk.




# Razredi imajo lahko tudi vgrajene funkcije. Ustavri class hrana, ki naj vsebuje
# ime zelenjave, barvo, tip (meso,sadje,zelenjava). In napiši funkcijo v tem razredu,
# ki bo predstavilo izpisal ime te hrane.







# Dedovanje v pythonu

# Primer: Vsi študentje so ljudje, vsi ljudje niso študentje. 
# Torej vsak študent ima vse lastnosti, ki jih ima oseba. Vse osebe nimajo "lastnosti", katere imajo študentje. npr. letnik, kreditne točke

class Student(Oseba):
	def __init__(self,ime,priimek,spol,letnik,kt):
		Oseba.__init__(self,ime,priimek,spol)
		self.letnik = letnik
		self.kt = kt