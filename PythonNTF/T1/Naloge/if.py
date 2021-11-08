#______________________________________________________________________________
# Termin 1
# Pogojni stavek
#______________________________________________________________________________

# Ugotovili smo da primerjave nam za odgovor podajo tip boolean (True/False)
# To lahko uporabimo tako da programu naročimo da preveri če je nek pogoj pravilen
# potem izvede del kode drugače pa je ne




# Lahko imamo več kot en pogoj! Preverimo če je st2 večje, manjše ali enako 1,7,99

# V enem pogojnem stavko lahko preverimo več stvari
# Poglejmo če je število med 10 IN 15


# Preverimo če je s večji od 10 ALI manjši od 15 






# Vsi boksarji se morajo pred dvobojem stehtati. Ker nihče ne ve natanko
# v katero kategorijo kdo spada, so si organizatorji zaželeli novo
# supermoderno tehtnico, ki ob tehtanju izpiše ne le težo boksarja,
# temveč tudi v katero težnostno kategorijo sodi.  Napiši funkcijo
# `teznostna_kategorija(teza)` za pripadajoči program tehtnice, ki vrne podatek,
# v katero težnostno kategorijo sodi boksar. Boks je razdeljen na 11
# kategorij in sicer: lahka mušja (do 48 kg), mušja (do 51 kg), bantam
# (do 54 kg), peresna (do 57 kg), lahka (do 60 kg), lahka velterska
# (do 64 kg), velterska (do 69 kg), srednja (do 75 kg), poltežka
# (do 81 kg), težka (do 91 kg) ter super težka (nad 91 kg). Za argumente
# manjše ali enake 0 naj funkcija vrne niz »Napaka!«.
# 
#     >>> teznostna_kategorija(54)
#     "bantamska kategorija"
#     >>> teznostna_kategorija(48.000001)
#     "mušja kategorija"