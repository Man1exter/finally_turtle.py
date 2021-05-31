import random
import time
import turtle

# settings

user = turtle.Turtle()
user.shape("turtle")
user.color("green")
user.pensize(5)
turtle.bgcolor("black")
user.hideturtle()
turtle.title("who's first at the finish line?")

# players

# 1
user_one_pink = turtle.Turtle()
user_one_pink.color("pink")
user_one_pink.shape("turtle")
user_one_pink.pensize(3)
user_one_pink.penup()
user_one_pink.goto(-200,100)
user_one_pink.pendown()

# 2
user_two_yellow = turtle.Turtle()
user_two_yellow.color("yellow")
user_two_yellow.shape("turtle")
user_two_yellow.pensize(3)
user_two_yellow.penup()
user_two_yellow.goto(-200,-10)
user_two_yellow.pendown()

# start-line

# finish-line

finish_line = turtle.Turtle()
finish_line.color("lightblue")
finish_line.penup()
finish_line.goto(250,250)
finish_line.write("FINISH",font=("helvetic",20,"bold"))

finish_line.penup()
finish_line.pensize(5)
finish_line.color("white")
finish_line.goto(290,250)
finish_line.pendown()
finish_line.goto(290,-200)

finish_line.hideturtle()

# options with name of users / turtles

# events + loop


# close / exit
turtle.exitonclick()