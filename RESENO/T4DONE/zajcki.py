#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Zajčki
# n nam pove število mesecev
# m nam pove število novih parov
# Vedno začnemo z enim zajčjim parom

n = 5
m = 5

#Zanima nas koliko zajčkov bo živelo na koncu obdobja če domnevamo da so zajčki nesmrtni
stParov = 1
stZajcev = 2*stParov

while n > 0:
	stParov = stParov + m*stParov
	stZajcev = 2 * stParov
	n -= 1
	print(stZajcev, stParov)
	
print(stZajcev)
print()

#Koliko jih bo živeli če imajo življensko dobo 3 mesece
n = 5
stParov = 1
stNovoRojenih = 2
st1 = 0
st2 = 0
st3 = 0
stZajcev = st1 + st2 + stNovoRojenih
print(stZajcev, stParov)
while n > 0 :
	st3 = st2
	st2 = st1
	st1 = stNovoRojenih
	stNovoRojenih =  stParov * m * 2
	stZajcev = stNovoRojenih + st1 + st2
	stParov = stZajcev // 2
	print(stZajcev, stParov)
	n -= 1
print(stZajcev)


#Kaj moramo dodati če imajo moški zajčki dobo 2 meseca ženske pa 3
print()
n = 5
stParov = 1
stNovoRojenih = 2
st1 = 0
st2 = 0
st3 = 0
stZajcev = stNovoRojenih
print(stZajcev, stParov)
while n > 0:
	st3 = st2 // 2
	st2 = st1
	st1 = stNovoRojenih
	stNovoRojenih = (st1+st2) * m
	stZajcev = stNovoRojenih + st1 + (st2 // 2)
	stParov = (stNovoRojenih + st1) //2 
	print(stZajcev, stParov)
	n -= 1
print(stZajcev)