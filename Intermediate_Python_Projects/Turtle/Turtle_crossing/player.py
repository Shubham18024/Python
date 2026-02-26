import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#531616")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.speed("fastest")

    def move_up(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)