#from turtle import Turtle, Screen
import random
import turtle as t

colors = ['gainsboro','lime green','hot pink', 'indigo', 'orange', 'wheat', 'blue' , 'red', 'black']
directions = [0,90,180,270]
step_size = [30, 35, 45]

t.colormode(155)


def draw_line():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


def draw_polygon(num_sides):
    angle = 360 / num_sides
    timmy_the_turtle.color(random.choice(colors))
    for i in range(num_sides):
        timmy_the_turtle.right(angle)
        timmy_the_turtle.forward(100)


def randon_walk():
    timmy_the_turtle.speed('fastest')
    timmy_the_turtle.pensize(15)
    timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.forward(random.choice(step_size))
    timmy_the_turtle.setheading(random.choice(directions))


timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("circle")
timmy_the_turtle.color("blue")

current_exercise = 3
if current_exercise == 2:
    for shape_side_n in range(3, 8):
        draw_polygon(shape_side_n)
elif current_exercise == 3:
    for i in range (100):
        randon_walk()

screen = t.Screen()
screen.exitonclick()


