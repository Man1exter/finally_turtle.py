import turtle
import math
import random

monitor = turtle.Screen()
monitor.bgcolor('black')
Mariusz = turtle.Turtle()
Mariusz.speed(0)
Mariusz.color('white')
rotate=int(360)

def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4

def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)

drawSpecial(Mariusz,100,10)
Krystov = turtle.Turtle()
Krystov.speed(0)
Krystov.color('yellow')
rotate=int(90)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10

def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(Krystov,100,10)
Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('blue')
rotate=int(80)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5

def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(Barry,100,10)
Jons = turtle.Turtle()
Jons.speed(0)
Jons.color('orange')
rotate=int(90)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19

def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(Jons,100,10)
Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
rotate=int(90)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20

def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(Will,100,10)