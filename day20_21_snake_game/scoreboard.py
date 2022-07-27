from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboar(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as score_file:
            self.high_score = int(score_file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboar()

    def update_scoreboar(self):
        self.clear()
        self.write(f"Score {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as score_file:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboar()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        new_score = int(self.high_score) + 1
        with open("data.txt", mode="w") as score_file:
            score_file.write(str(new_score))

        self.clear()
        self.update_scoreboar()




