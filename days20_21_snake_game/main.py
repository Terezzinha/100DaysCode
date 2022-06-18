import random
import turtle as t
from snake import Snake
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

sucuri = Snake()

screen.listen()
screen.onkey(sucuri.up, "Up")
screen.onkey(sucuri.down, "Down")
screen.onkey(sucuri.left, "Left")
screen.onkey(sucuri.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    sucuri.move()


screen.exitonclick()