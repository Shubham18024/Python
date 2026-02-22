from turtle import Turtle
ALIGNMENT = "center"
FONT_SCORE = ("Courier", 24, "normal")
FONT_GAME_OVER = ("Courier", 36, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("Gold")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_SCORE)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("Red")
        self.write("GAME OVER 🥺", align=ALIGNMENT, font=FONT_GAME_OVER)


