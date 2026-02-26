import turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "bold")


class Levelboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.update_levelboard()

    def update_levelboard(self):
        self.clear()
        self.color("Gold")
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_levelboard()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.home()
        self.color("darkred")
        self.write(f"GAME OVER", align="center", font=FONT)


        