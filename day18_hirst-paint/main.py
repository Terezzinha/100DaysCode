import colorgram
import turtle as t
import random


def get_color_from_image ():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)

t.colormode(255)
tutu = t.Turtle()
tutu.speed('fastest')
tutu.penup()
tutu.hideturtle()
color_list = [ (203, 165, 108), (152, 75, 48), (53, 93, 124), (223, 202, 135), (171, 153, 42), (137, 32, 20), (132, 163, 184), (47, 121, 86), (200, 90, 72), (72, 45, 36), (15, 98, 73), (97, 73, 75), (147, 180, 147), (164, 142, 157), (234, 175, 164), (55, 47, 50), (182, 205, 171), (155, 18, 23), (37, 61, 73), (22, 83, 89), (80, 147, 128), (187, 86, 89), (39, 66, 91), (16, 72, 62), (106, 128, 153), (175, 192, 211)]

tutu.setheading(225)
tutu.forward(300)
tutu.setheading(0)
number_dots = 100

for dot_count in range(1, number_dots + 1):
    tutu.dot(20, random.choice(color_list))
    tutu.forward(50)

    if dot_count % 10 == 0:
        tutu.setheading(90)
        tutu.forward(50)
        tutu.setheading(180)
        tutu.forward(500)
        tutu.setheading(0)
    

screen = t.Screen()
screen.exitonclick()