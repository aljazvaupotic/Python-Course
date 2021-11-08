#______________________________________________________________________________
# Termin 1
# Vnos podatkov
#______________________________________________________________________________

x = 2
# Od uprabnika programov lahko tudi zahtevamo, da vnese podatke.
# Zato uporabljamo vgrajeno metodo input 
y = eval(input("Vnesi stevilko: "))
print(x, y)
#Želimo da uporabnik vnese svoje ime. Nato ga pa pozdravimo
ime = str(input("Vnesi ime: "))
print("Dober dan", ime)
# Sedaj od uporabnika še želimo, da nam poda svojo starost in domači kraj
starost = eval(input("Vnesi starost: "))
kraj = input("Vnesi domači kraj: ")

print(starost , kraj)
# preverimo tipe podatkov 
print(type(y),type(ime),type(starost),type(kraj))

# podatke lahko manipuluramo, da nam njihovi tipi vedno odgovarjajo


# Uporabnik naj vnese neko letnico v prihodnosti ti pa izračunaj koliko bo oseba
# stara tisto leto in to tudi izpiši.




# Preberemo letnico kot številko
letnicaPrihodnosti = eval(input("Vnesi letnico v prihodnosti: ")) 
# Izračunamo razliko med letošnjim letom in prihodnostjo
kolikoLet = letnicaPrihodnosti - 2019
# Starost danes prištejom razliko let da dobimo starostVPrihodnosti
starostVPrihodnosti = starost + kolikoLet
#To izpišemo
print("Leta " + str(letnicaPrihodnosti) + " bo oseba starta "+ str(starostVPrihodnosti))






