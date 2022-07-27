import random
import turtle as t

colors = ['gainsboro', 'lime green', 'hot pink', 'indigo', 'orange', 'wheat', 'blue', 'red', 'black']
directions = [0, 90, 180, 270]
step_size = [30, 35, 45]

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color


def draw_line():
    tutu.forward(100)
    tutu.left(90)


def draw_polygon(num_sides):
    angle = 360 / num_sides
    tutu.color(random.choice(colors))
    for i in range(num_sides):
        tutu.right(angle)
        tutu.forward(100)


def randon_walk():
    tutu.speed('fastest')
    tutu.pensize(15)
    tutu.color(random_color())
    tutu.forward(random.choice(step_size))
    tutu.setheading(random.choice(directions))


def draw_spirolog(size_gap):  #4
    tutu.speed('fastest')
    for _ in range(int(360 / size_gap)):
        tutu.color(random_color())
        tutu.circle(100)
        tutu.setheading(tutu.heading() + size_gap)


tutu = t.Turtle()
tutu.shape("circle")
tutu.color("blue")

current_exercise = 4
if current_exercise == 2:
    for shape_side_n in range(3, 8):
        draw_polygon(shape_side_n)
elif current_exercise == 3:
    for i in range(100):
        randon_walk()
elif current_exercise == 4:
    draw_spirolog(int(5))


screen = t.Screen()
screen.exitonclick()
