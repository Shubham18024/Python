import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.width(7)
directions = [0, 90, 180, 270]
for _ in range(1000):
    tim.color(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )
    tim.forward(30)
    tim.setheading(random.choice(directions))    


screen = t.Screen()
screen.exitonclick()