import turtle as tu
import pandas as pd
import csv

# todo keep track of the score

FONT = ("Courier", 12, "normal")

screen = tu.Screen()
screen.title("US STATES GAMES")
screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
all_states_lst = data.state.to_list()

guessed_state = []
count_answers = 0
states_to_learn_lst = []

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
    else:
        states_to_learn_lst.append(str(answer_state))

with open("score.txt", mode="w") as score_file:
    score_file.write(str(count_answers))

states_to_learn_df = pd.DataFrame (states_to_learn_lst, columns = ['states_to_learn'])
states_to_learn_df.to_csv("states_to_learn_fl.csv")
# with open("states_to_learn.csv", mode="w", newline='') as states_to_learn_fl:
#     states_to_learn_fl.writerow(states_to_learn_lst)
