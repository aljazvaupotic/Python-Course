#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Gnezdenje oklepajev
#
# Oklepaji so pravilno gnezdeni, če predklepaji in zaklepaji nastopajo v
# parih in število zaklepajev nikoli ne preseže števila predklepajev, ko
# jih štejemo od leve proti desni.
# =====================================================================@014990=
# 1. podnaloga
# Sestavite funkcijo `oklepaji(niz)`, ki bo preverila, ali so v danem
# nizu oklepaji pravilno gnezdeni. Na ostale znake naj se funkcija ne
# ozira. Zgled:
# 
#     >>> oklepaji('(a + b)^2 = (((a^2) + 2ab) + b^2)')
#     True
#     >>> oklepaji('())(()')
#     False
# =============================================================================

def narediSeznam (niz):
	sez = []
	for znak in niz:
		if znak == "(" or znak == ")" :
			sez.append(znak)
	return sez

def oklepaji(niz):
	seznamOklepajev = narediSeznam(niz)
	print(seznamOklepajev) #preveri delovanje funkcije narediSeznam
	stOk = 0
	stZa = 0
	x = 0
	for oklepaj in seznamOklepajev :
		if oklepaj == "(" :
			stOk += 1
			x += 1
		else :
			stZa += 1
			x -= 1
		if stOk < stZa or x < 0:
			return False
	#return stOk == stZa
	return x == 0
print(oklepaji('(a + b)^2 = (((a^2) + 2ab) + b^2)'))
print(oklepaji(")("))
print(oklepaji("()()()()()()("))