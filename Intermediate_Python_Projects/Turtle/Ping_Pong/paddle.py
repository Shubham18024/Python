import turtle

PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
PADDLE_MOVE_DISTANCE = 20

class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.construct_paddle(position)


    def construct_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.fd(PADDLE_MOVE_DISTANCE)

    def move_down(self):
        self.bk(PADDLE_MOVE_DISTANCE)
        
