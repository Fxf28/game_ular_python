from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Times New Roman", 12, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
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
        self.score = 0
        self.update_score()