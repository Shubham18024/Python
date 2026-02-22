import turtle
INITIAL_SNAKE_PARTS = 3
SNAKE_PARTS_POSITION = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake_initial()
        self.head = self.body[0]

    def create_snake_initial(self):
        for i in range(INITIAL_SNAKE_PARTS):
            part = turtle.Turtle()
            part.shape("square")
            part.color("white")
            part.penup()
            part.speed("fastest")  # No animation delay
            part.goto(-(SNAKE_PARTS_POSITION * i), 0)
            self.body.append(part)

    def extend(self):
        new_part = turtle.Turtle()
        new_part.shape("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(self.body[-1].position())
        self.body.append(new_part)

    def move(self):
        for parts in range(len(self.body) - 1, 0, -1):
            new_x = self.body[parts - 1].xcor()
            new_y = self.body[parts - 1].ycor()
            self.body[parts].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)    

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  


