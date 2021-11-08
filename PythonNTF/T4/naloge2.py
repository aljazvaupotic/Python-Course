#____________________________________________________________________
# TERMIN 4, 12.6.2019
# naloge2
#____________________________________________________________________

# Kuhamo in pečemo
#
# Sestavine, ki jih potrebujemo za nek recept, opišemo s slovarjem, v
# katerem so ključi sestavine, vrednosti pa količine, ki jih potrebujemo.



# 1. podnaloga
# Sestavite funkcijo `pomnozi(recept, faktor)`, ki sestavi in vrne nov
# recept. Ta naj vsebuje iste sestavine kot recept `recept`, le da so vse
# količine v njem pomnožene z danim faktorjem.
# 
#     >>> pomnozi({'jajca': 4, 'moka': 500}, 2)
#     {'jajca': 8, 'moka': 1000}


# 2. podnaloga
# Sestavite funkcijo `imamo_sestavine(recept, shramba)`, ki preveri, ali
# imamo v shrambi dovolj sestavin za dani recept. Sestavine, ki jih imamo
# v shrambi, so predstavljene s slovarjem na enak način kot sestavine v
# receptu.
# 
#     >>> imamo_sestavine({'jajca': 3, 'moka': 500}, {'moka': 600})
#     False

# 3. podnaloga
# Sestavite funkcijo `potrebno_kupiti(recept, shramba)`, ki vrne slovar
# sestavin s pripadajočimi količinami, ki jih moramo še dokupiti, da bomo
# lahko skuhali jed po danem receptu.
# 
#     >>> potrebno_kupiti({'jajca': 3, 'moka': 500}, {'moka': 1000, 'sladkor': 1000})
#     {'jajca': 3}


