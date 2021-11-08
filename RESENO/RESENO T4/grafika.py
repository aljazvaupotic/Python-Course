#____________________________________________________________________
# TERMIN 4, 12.6.2019
# Grafika
#____________________________________________________________________

import turtle

# turtle je knjižnica, ki nam omogoča risanje
t = turtle.Turtle()
sc = turtle.Screen()
# https://i.redd.it/1zw2qzsy8p601.gif 
print(t.pos())
# premikanje: naprej, nazaj, levo, desno, goto, krog, hitrost
t.fd(100)
t.lt(45)
t.bk(100)
t.rt(10)


print(t.pos())
# barve: barva pisala, barva barvila, barva odzadja
t.color("#ffff2a","red")
t.begin_fill()
t.fd(-50)
t.circle(-25)
t.end_fill()

# lastnosti pisala: širina, stanje
t.pu()
t.goto(-100,130)
t.pd()
t.width(10)
t.circle(100)
t.clear()
t.pu()
t.goto(-50,-100)
t.pd()
# 1. Nariši hišo (štirikotnik, vrata, okno, trikotna streha), sonce in drevo.
t.setheading(0)
t.pen( pencolor = "black",pensize = 10, speed = 9)

x = 4
while x != 0:
	t.fd(150)
	t.lt(90)
	x -= 1
t.pen(pencolor = "#60472b",pensize = 6, fillcolor = "#b28552")
t.pu()
t.fd(50)
t.pd()
t.begin_fill()
t.lt(90)
t.fd(33*2)
t.lt(90)
t.fd(20*2)
t.lt(90)
t.fd(33*2)
t.end_fill()
t.pen(pencolor = "#ffffff",pensize = 6, fillcolor = "#8ee4ff")
t.pu()
t.goto(40,0)
t.pd()
x = 4
t.begin_fill()
while x != 0:
	t.fd(30)
	t.lt(90)
	x -= 1
t.end_fill()

t.pu()
t.goto(-50,50)
t.pd()
t.color("red")
t.fillcolor("#ff8e8e")
t.begin_fill()
t.goto(25,75)
t.goto(100,50)
t.goto(-50,50)
t.end_fill()


x = input("ENTER:")
