import turtle as tu
import pandas as pd

# todo record de correct in a list
# todo keep track of the score

FONT = ("Courier", 12, "normal")

screen = tu.Screen()
screen.title("US STATES GAMES")
screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
all_states_lst = data.state.to_list()

guessed_state = []
count_answers = 0

while count_answers < 50:
    count_answers = len(guessed_state)

    answer_state = screen.textinput(f"{count_answers}/50 States Correct", "State:").capitalize()
    if answer_state == "Exit":
        break
    if answer_state in all_states_lst:
        guessed_state.append(answer_state)
        pos_x = int(data[data.state == answer_state].x)
        pos_y = int(data[data.state == answer_state].y)
        tu.penup()
        tu.goto(pos_x, pos_y)

        tu.write(answer_state, align="left", font=FONT)

with open("score.txt", mode="w") as score_file:
    score_file.write(str(count_answers))
