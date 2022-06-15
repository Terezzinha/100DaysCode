import random
import turtle as t

screen = t.Screen()


def create_snake_body():
    starting_position = [(0, 0), (-20,0), (-40, 0)]
    for position in starting_position:
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.goto(position)


create_snake_body()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.exitonclick()