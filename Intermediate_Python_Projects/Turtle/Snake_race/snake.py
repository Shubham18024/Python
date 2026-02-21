import turtle
SNAKE_PARTS_POSITION = 20
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.move()

    def create_snake(self):
        for i in range(3):
            part = turtle.Turtle()
            part.shape("square")
            part.color("white")
            part.penup()
            part.goto(-(SNAKE_PARTS_POSITION * i), 0)
            self.body.append(part)

    def move(self):
        for parts in range(len(self.body) - 1, 0, -1):
            new_x = self.body[parts - 1].xcor()
            new_y = self.body[parts - 1].ycor()
            self.body[parts].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

