from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Times New Roman", 12, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=230)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER.", align=ALIGNMENT, font=FONT)