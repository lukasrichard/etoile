from turtle import *
from random import *
def Couleur() :
    C = randint(1,6)
    if C == 1 :
        return color("red")
    if C == 2 :
        return color("green")
    if C == 4 :
        return color("yellow")
    if C == 5 :
        return color("blue")

def Triangle(L) :
    j=randint(10,100)
    for m in range (8):
        forward(j)
        left(120)
        forward(j)
        left(120)
        forward(j)
        left(120)
        forward(j)
        right(45)

    return

bgcolor("black")
speed(10)
for b in range(100):
    up()
    x=randint(-500,500)
    y=randint(-500,500)
    l=randint(10,100)
    goto(x,y)
    down()
    Couleur()
    Triangle(l)
    mainloop



