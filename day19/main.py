import turtle as t
import random

tutu = t.Turtle()
screen = t.Screen()


def move_forwards():
    tutu.forward(10)


def move_backwards():
    tutu.backwards(10)


def turn_left():
    new_heading = tutu.heading() + 10
    tutu.setheading(new_heading)


def turn_right():
    new_heading = tutu.heading() - 10
    tutu.setheading(new_heading)


def clear():
    tutu.clear()
    tutu.penup()
    tutu.home()
    tutu.pendown()
    

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
