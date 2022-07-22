import turtle as tu
import pandas as pd

FONT = ("Courier", 12, "normal")

screen = tu.Screen()
screen.title = "U.S States Games"
screen.bgpic("blank_states_img.gif")

ask_state = screen.textinput("Where", "State:").capitalize()

data = pd.read_csv("50_states.csv")
pos_x = int(data[data.state == ask_state].x)
pos_y = int(data[data.state == ask_state].y)
tu.penup()
tu.goto(pos_x, pos_y)

tu.write(ask_state, align="left", font=FONT)
#
# def aks_the_state():
#
# ask_state = input("Estado: ").capitalize()
#
# print(data[data.state == ask_state])
#pos_x
#pos_y = data[data.state == ask_state].y
# print(f"pos_y {int(pos_x)} e {int(pos_y)}")



screen.exitonclick()


