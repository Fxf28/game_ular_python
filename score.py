from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Times New Roman", 12, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../OneDrive/Documents/data.txt") as data_highscore:
            self.high_score = int(data_highscore.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=230)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} | HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../OneDrive/Documents/data.txt", mode="w") as data_highscore:
                data_highscore.write(f"{self.score}")
        self.score = 0
        self.update_score()