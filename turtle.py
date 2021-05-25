import turtle
import random

# initialization elements..
tur = turtle.Turtle()
tur.shape('turtle')

# settings turtle..
turtle.bgcolor('lightblue')
tur.speed(5)

# drawing loop code mode..
for it in range(50,500):
  tur.color(random.choice(["white","black"]))
  tur.forward(it)
  tur.right(92)

# exit from the window with turtle
tur.exitonclick()