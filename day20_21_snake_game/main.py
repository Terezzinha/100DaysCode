import turtle as t
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboar


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

sucuri = Snake()
food = Food()
scoreboard = Scoreboar()

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

    #Detect Collision with food
    if sucuri.head.distance(food) < 15:
        food.refresh()
        sucuri.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if sucuri.head.xcor() > 280 or sucuri.head.xcor() < -280 or sucuri.head.ycor() > 280 or sucuri.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tall
    for segment in sucuri.segments[1:]:
        if sucuri.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()