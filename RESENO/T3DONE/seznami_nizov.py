#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =====================================================================@015002=
# 1. podnaloga
# Sestavi funkcijo `imena_na_B(imena)`, ki sprejme seznam
# imen in vrne seznam imen, ki se začnejo z črko `'B'`.
# 
# Primer:
# 
#     >>> imena_na_B(["Mojca", "Janez", "Bojana", "Bine", "Ana", "Blaž"])
#     ['Bojana', 'Bine', 'Blaž']
#     >>> imena_na_B(["Borut", "miza", "balon"])
#     ['Borut']
# =============================================================================
def imenaNaB(seznamImen):
	s = []
	for ime in seznamImen :
		if( ime[0] == "B" ):
			s.append(ime)
	return s
	
seznamImen = ["Mojca", "Janez", "Bojana", "Bine", "Ana", "Blaž"]

print(imenaNaB(seznamImen))
print(imenaNaB(["miza","stol","Borut","Miha","Bojana","balon"]))
print(imenaNaB("Aljaž, Bine"))



        
# =====================================================================@015003=
# 2. podnaloga
# Sestavi funkcijo `odstrani_predolge(besede)`,
# ki sprejme seznam besed in vrne seznam
# tistih besed, ki so krajse od $7$.
# 
# Primer:
# 
#     >>> odstrani_predolge(["svetilnik", "sok"])
#     ['sok']
# =============================================================================

def odstraniPredolge(seznam):
	seznamKratkih = []
	for beseda in seznam:
		if len(beseda) < 7 :
			seznamKratkih.append(beseda)
	
	return seznamKratkih
	
s = ["avtobus", "sirena", "kolesar", "pes", "moka","svetilnik", "sok"]
print()
print(s)
print(odstraniPredolge(s))
ns = odstraniPredolge(s)
print(ns)
print(s)
s = odstraniPredolge(s)
print(s)


# =====================================================================@015005=
# 3. podnaloga
# Sestavi funkcijo `prestej_predolge(besede)`,
# ki sprejme seznam besed in vrne stevilo besed, ki so daljše od $6$.
# 
# Primer:
# 
#     >>> prestej_predolge(["avtobus", "sirena", "kolesar", "pes", "moka"])
#     2
# =============================================================================
print()

def prestejPredolge(seznam):
	c = 0
	for beseda in seznam:
		if len(beseda) >= 6 :
			c += 1
	return c
	
print(prestejPredolge(["avtobus", "sirena", "kolesar", "pes", "moka"]))






# =====================================================================@015006=
# 4. podnaloga
# Napiši funkcijo `cenzura(besede)`, ki sprejme seznam besed
# in vrne seznam, v katerem so vse besede prvotnega seznama,
# ki vsebujejo več kot eno črko x zamenjane za tri zvezdice `'***'`
# 
# Namig: Nalogo lahko rešiš z zanko skozi seznam.
# 
# Na primer:
# 
#     >>> cenzura(["a", "ax", "axx", "axxx", "axxxx"])
#     ['a', 'ax', '***', '***', '***']
#     >>> cenzura(["mix", "prefix", "mixfix", "park", "moto"])
#     ['mix', 'prefix', '***', 'park', 'moto']
# =============================================================================


def cenzura (seznam) :
	s = []
	for beseda in seznam :
		if beseda.lower().count("x") > 1 :
			s.append("***")
		else:
			s.append(beseda)
			
	return s
	
sez = ["a", "ax", "axx", "axxx", "axxxx"]
print()
print(sez)
print(cenzura(sez))

print(cenzura(["mix", "prefix", "mixfix", "park", "moto"]))




def cenzuraX (seznam):

	s = []
	s = []
	for beseda in seznam :
		if beseda.lower().count("x") > 1 :
			nb = ""
			for crka in beseda:
				if(crka.lower() == "x"):
					nb += "*"
				else:
					nb += crka
			s.append(nb)
		else:
			s.append(beseda)
			
	return s
print()
print(cenzuraX(["mix", "prefix", "mixfix", "XpArkX", "mXto"]))
