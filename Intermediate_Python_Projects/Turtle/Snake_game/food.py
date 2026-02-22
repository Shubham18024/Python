from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#5a2016")  # Tomato red
        self.penup()
        self.turtlesize(stretch_len=0.75, stretch_wid=0.75, outline=2)  # Make it smaller
        self.blink()  # Start blinking immediately
        self.speed("fastest")  # No animation delay
        self.refresh()  # Place it at a random position when created

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)

    def blink(self):
        if self.isvisible():
            self.hideturtle()
        else:
            self.showturtle()
        # Schedule the next blink after 500 milliseconds
        self.getscreen().ontimer(self.blink, 250)

    
    