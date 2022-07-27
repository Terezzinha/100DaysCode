#my_screen.exitonclick()
#from turtle import Turtle, Screen

#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("coral")

#timmy.goto(20,20)
#timmy.forward(50)

#timmy.towards(10, 10)
#my_screen = Screen()



from prettytable import PrettyTable
table = PrettyTable()
print("petty table")
table.add_column("Pokemom",["pikachu", "squirtle"])
table.add_column("Tipo", ["t1", "t2"])
table.align = "l"
print(table)
