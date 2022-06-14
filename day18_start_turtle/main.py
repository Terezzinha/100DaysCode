from turtle import Turtle, Screen
import heroes

#timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("circle")
#timmy_the_turtle.color("red", "green")

def draw_line():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("circle")
timmy_the_turtle.color("blue")

for _ in range(4):
    draw_line()


screen = Screen()
screen.exitonclick()
