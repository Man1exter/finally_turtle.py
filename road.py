import random
import time
import turtle

# settings

user = turtle.Turtle()
user.shape("turtle")
user.color("green")
user.pensize(5)
turtle.bgcolor("black")
turtle.title("who's first at the finish line?")

# players

# start-line

# finish-line

finish_line = turtle.Turtle()
finish_line.color("white")
finish_line.penup()
finish_line.goto(250,250)
finish_line.write("FINISH",font=("helvetic",20,"bold"))

finish_line.penup()
finish_line.pensize(5)
finish_line.goto(290,250)
finish_line.pendown()
finish_line.goto(290,-200)

finish_line.hideturtle()

# close / exit
turtle.exitonclick()