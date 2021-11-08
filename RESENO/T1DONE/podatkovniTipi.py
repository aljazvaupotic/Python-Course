#______________________________________________________________________________
# Termin 1
# Izpisovanje podatkov, tip podatkov
#______________________________________________________________________________

#Želimo izpisati "Zdravo"

print("Zdravo")

# "Zdravo" želimo shraniti kot pozdrav

pozdrav = "Zdravo"
Pozdrav = "Zdravo"
print(pozdrav)
print(Pozdrav)
print()
# pozdrav želimo spremeniti v "Dober dan" in ga izpišemo
pozdrav = "Dober Dan"
print(pozdrav)
print(Pozdrav)

# izpisati želimo pozdrav skupaj z imenom neke osebe ("Tilen") 
print()
print(pozdrav + " Tilen") # prva opcija
print(pozdrav + " " + "Tilen") # druga opcija
print(pozdrav, "Tilen") # tretja opcija

# shranimo ime te osebo pod spremenljivko ime in izpišemo
ime = "Tilen"
print()
print(pozdrav + " " + ime)
print(pozdrav, ime)


# v spremenljivko pozdravIme želimo združit pozdrav in ime in izpisati
pozdravIme = pozdrav + " " + ime
print()
print(pozdravIme)
# spremenljivko z imenom pozdrav želimo menjat v številko 5
pozdrav = 5
# pozdravIme želimo "updatat" in izpisati
#pozdravIme = pozdrav + " " + ime
#print()
#print(pozdravIme)
# pogledamo kakšnega tipa je katera spremenljivka 
print(type(ime), type(pozdrav))

# popravimo tipe tako da bo izpis deloval
pozdrav = str(pozdrav)
print(type(ime), type(pozdrav))
print()
pozdravIme = pozdrav + " " + ime
print()
print(pozdravIme)





# 1.
# Ustvari osebo s poljubnim imenom, priimkom in starostjo ter pripravi
# spremenljivko, ki jo bo predstavila ("Sem ta in ta, star sem toliko let").

ime = "Ema" 
priimek = "Premužič"
starost = 22

predstaviSe = ("Sem " + ime + " " + priimek + ", stara sem " + str(starost) + ".")
print(predstaviSe)













