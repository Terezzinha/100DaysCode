from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")

timmy.towards(10, 10)
timmy.goto(20,20)
timmy.forward(50)
my_screen = Screen()

my_screen.exitonclick()