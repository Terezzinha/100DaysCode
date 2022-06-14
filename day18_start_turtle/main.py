from turtle import Turtle, Screen


def draw_line():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


def draw_polygon(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        timmy_the_turtle.right(angle)
        timmy_the_turtle.forward(100)


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("circle")
timmy_the_turtle.color("blue")

for i in range(3, 8):
    draw_polygon(i)


screen = Screen()
screen.exitonclick()


