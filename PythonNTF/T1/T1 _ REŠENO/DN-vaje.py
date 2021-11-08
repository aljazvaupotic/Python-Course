#______________________________________________________________________________
# Termin 1, 16.5.2019
# Vaje
#______________________________________________________________________________


# Uporabnik naj vnese 2 stevilki, ti si izmisli eno in nato napisi program ki bo izpisal 
# najvecjo med njimi in njen izvor (USER/COMP)
m = 124840
u1 = input("Prva: ")
u2 = input("Druga: ")
u1 = int(u1)
u2 = int(u2)
if m > u1 and m > u2:
	print(m,"je najvecja, vnesel sem jo COMP")
elif u1 > u2:
	print(u1,"je najvecja, vnesel jo je USER")
else:
	print(u2,"je najvecja, vnesel jo je USER")
najvecja = max(m,u1)
najvecja = max(najvecja,u2)
print(najvecja)
# Preberi cas v vojaskem nacinu (1230 -> 12h in 30min),
# ter izpisi a je popoldan ali dopoldan in dodaj izpis casa v obliki HH:mm


