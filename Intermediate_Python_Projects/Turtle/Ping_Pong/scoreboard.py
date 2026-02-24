import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(f"{self.score2}", align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(f"{self.score1}", align="center", font=("Courier", 80, "normal"))

    def increase_score1(self):
        self.score1 += 1
        self.update_scoreboard()

    def increase_score2(self):
        self.score2 += 1
        self.update_scoreboard()