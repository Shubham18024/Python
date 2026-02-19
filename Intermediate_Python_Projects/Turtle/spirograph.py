import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.width(2)
for _ in range(100):
    tim.color(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )
    tim.circle(100)
    tim.left(5)


screen = t.Screen()
screen.exitonclick()