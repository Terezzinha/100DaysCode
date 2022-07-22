import turtle as tu
FONT = ("Courier", 24, "normal")

screen = tu.Screen()
screen.title = "U.S States Games"
screen.bgpic("blank_states_img.gif")


def aks_the_state():
    new_state = screen.textinput("NIM", "Name of first player:")
    tu.write(new_state, align="left", font=FONT)



# TODO criar uma classe screen_map

screen.exitonclick()


