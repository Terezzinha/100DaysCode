import turtle as tu
import pandas as pd

# todo keep track of the score

FONT = ("Courier", 12, "normal")

screen = tu.Screen()
screen.title("US STATES GAMES")
screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
all_states_lst = data.state.to_list()

guessed_state_lst = []
count_answers = 0
states_to_learn_lst = []

while count_answers < 50:
    count_answers = len(guessed_state_lst)

    answer_state = screen.textinput(f"{count_answers}/50 States Correct", "State:").capitalize()
    if answer_state == "Exit":
        missing_states_lst = []
        for state in all_states_lst:
            if state not in guessed_state_lst:
                missing_states_lst.append(state)
        states_missing_df = pd.DataFrame(missing_states_lst, columns=['state_missing'])
        states_missing_df.to_csv("missing_states_fl.csv")
        break
    if answer_state in all_states_lst:
        guessed_state_lst.append(answer_state)
        pos_x = int(data[data.state == answer_state].x)
        pos_y = int(data[data.state == answer_state].y)
        tu.penup()
        tu.goto(pos_x, pos_y)

        tu.write(answer_state, align="left", font=FONT)
    else:
        states_to_learn_lst.append(str(answer_state))

with open("score.txt", mode="w") as score_file:
    score_file.write(str(count_answers))

states_to_learn_df = pd.DataFrame(states_to_learn_lst, columns=['states_to_learn'])
states_to_learn_df.to_csv("states_to_learn_fl.csv")

