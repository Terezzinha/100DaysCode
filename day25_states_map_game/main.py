import turtle as tu
import pandas as pd
import timeit as ti


FONT = ("Courier", 12, "normal")

screen = tu.Screen()
screen.title("US STATES GAMES")
screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
answer_state = screen.textinput("Where", "State:").capitalize()
print(data.[data.state == answer_state].values)


game_is_on = False
while game_is_on:

    if not (data[data.state == answer_state]):
        pos_x = int(data[data.state == answer_state].x)
        pos_y = int(data[data.state == answer_state].y)
        tu.penup()
        tu.goto(pos_x, pos_y)

        tu.write(answer_state, align="left", font=FONT)
    else:
        game_is_on = False
screen.exitonclick()


