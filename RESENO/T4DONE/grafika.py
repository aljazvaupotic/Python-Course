#!/usr/bin/env python
# -*- coding: utf-8 -*-
#____________________________________________________________________
# TERMIN 4, 
# Grafika
#____________________________________________________________________

import turtle

# turtle je knjižnica, ki nam omogoča risanje
t = turtle.Turtle()
# https://i.redd.it/1zw2qzsy8p601.gif 

# premikanje: naprej, nazaj, levo, desno, goto, krog, hitrost
print(t.pos())
t.fd(100)
t.lt(90)
t.speed(1)
t.bk(50)
t.rt(35)
print(t.pos())
t.speed(10)
t.pu()
t.goto(-100,-20)
t.pd()
print(t.pos())
# barve: barva pisala, barva barvila, barva odzadja
t.setheading(90)
t.pen(fillcolor="black", pencolor="red", pensize=10)
t.begin_fill()
t.circle(25)
t.end_fill()
t.fd(200)
# lastnosti pisala: širina, stanje
print()

# 1. Nariši hišo (štirikotnik, vrata, okno, trikotna streha), sonce in drevo.
t.clear()
t.pen(fillcolor="brown", pencolor="black", pensize=0)
t.pu()
t.goto(0,0)
t.pd()
t.begin_fill()
n = 0
while n < 2:
	t.fd(50)
	t.lt(90)
	print(t.pos())
	t.fd(100)
	t.lt(90)
	n += 1
t.end_fill()
t.pen(fillcolor="blue", pencolor="white", pensize=0)
t.pu()
t.goto(-20,0)
t.pd()
t.begin_fill()
n = 0
while n < 2:
	t.fd(20)
	t.lt(90)
	t.fd(10)
	t.lt(90)
	n += 1
t.end_fill()
t.pen(fillcolor="blue", pencolor="white", pensize=0)
t.pu()
t.goto(-50,25)
t.pd()
t.begin_fill()
n = 0
while n < 2:
	t.fd(10)
	t.lt(90)
	t.fd(5)
	t.lt(90)
	n += 1
t.end_fill()

t.pen(fillcolor="red", pencolor="green", pensize=2)
t.pu()
t.goto(-0.00,50.00)
t.pd()
t.begin_fill()
t.goto(-50,80)
t.goto(-100,50)
t.goto(-0,50)
t.end_fill()

x = input("ENTER:")