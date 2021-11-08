#______________________________________________________________________________
# Termin 2, 30.5.2019
# Smrečica
#______________________________________________________________________________

# 1. podnaloga
# Petvrstično smrečico lahko v Pythonu izpišemo z naslednjim programom:
# 
print("       *")
print("      * *")
print("     * * *")
print("    * * * *")
print("   * * * * *")
print("  * * * * * *")
print(" * * * * * * *")
print("* * * * * * * *")
# 
# Sestavite program, ki izpiše osemvrstično smrečico.




# 2. podnaloga
# Program za izpis osemvrstične smrečice popravite tako, da namesto niza
# z $n$ zvezdicami `'**...*'` uporabite izraz `n * '*'`, na primer namesto
# niza `'*****'` uporabite izraz `5 * '*'`.

print(1*"*")
print(2*"*")
print(3*"*")
print(4*"*")
print(5*"*")
print(6*"*")
print(7*"*")
print(8*"*")



# 3. podnaloga
# Osemvrstično smrečico izpišite z enim samim klicem funkcije `print`.
# 
# *Namig*: znak za prelom vrstice je `"\n"`.

print(1*"*"+"\n"+2*"*"+"\n"+3*"*"+"\n"+4*"*"+"\n"+5*"*"+"\n"+6*"*"+"\n"+7*"*"+"\n"+8*"*"+"\n")
i = 1
while i <= 8:
	print(i*"*")
	i += 1

# 4. podnaloga
# Osemvrstično smrečico izpišite še desno poravnano. Petvrstična desno
# poravnana smrečica izgleda takole:
# 
#         *
#        **
#       ***
#      ****
#     *****
# 
# *Namig*: na začetku vsake vrstice izpišite ustrezno število presledkov.

dolzina = 8
zvezdice = 1
while zvezdice <= 8:
	print((dolzina-zvezdice)*" "+zvezdice*"*")
	zvezdice += 1

# 5. podnaloga
# Osemvrstično smrečico izpišite še sredinsko poravnano in z razmaki.
# Petvrstična sredinsko poravnana smrečica z razmaki izgleda takole:
# 
#         *
#        * *
#       * * *
#      * * * *
#     * * * * *
# 
# *Namig*: levi rob je enak kot pri desno poravnani smrečici, za vsakim
# osnovnim znakom pa je presledek.
dolzina = 8
znak = "* "
i = 1
while i <= 8:
	print((dolzina - i) * " " + i * znak)
	i += 1










