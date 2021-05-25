import turtle
import random
import sys

# initialization elements..
tur = turtle.Turtle()
tur.shape('turtle')

# settings turtle..
turtle.bgcolor('black')
tur.speed(10)

# drawing loop code mode..
for it in range(50,500):
  tur.color(random.choice(["blue","red","yellow","brown","purple"]))
  tur.forward(it)
  tur.right(92)

# exit from the window with turtle
tur.exitonclick()