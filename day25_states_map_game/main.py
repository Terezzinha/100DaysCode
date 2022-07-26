import turtle as tu
import pandas as pd
import timeit as ti
#todo record de correct in a list
#todo keep track of the score

FONT = ("Courier", 12, "normal")

screen = tu.Screen()
screen.title("US STATES GAMES")
screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")

guessed_state = []
count_answers = 0

while count_answers < 4:
    count_answers = len(guessed_state)

    answer_state = screen.textinput(f"{count_answers}/50 States Correct", "State:").capitalize()
    guessed_state.append(answer_state)

    pos_x = int(data[data.state == answer_state].x)
    pos_y = int(data[data.state == answer_state].y)
    tu.penup()
    tu.goto(pos_x, pos_y)

    tu.write(answer_state, align="left", font=FONT)

with open("score.txt", mode="w") as score_file:
    score_file.write(str(count_answers))

#
#
# game_is_on = True
# while game_is_on:
#
#     if not (data[data.state == answer_state]):
#         pos_x = int(data[data.state == answer_state].x)
#         pos_y = int(data[data.state == answer_state].y)
#         tu.penup()
#         tu.goto(pos_x, pos_y)
#
#         tu.write(answer_state, align="left", font=FONT)
#     else:
#         game_is_on = False
screen.exitonclick()


