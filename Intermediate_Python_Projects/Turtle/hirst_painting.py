import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.width(10)
for i in range(10):
    tim.penup()
    tim.goto(0, 30*i)
    tim.pendown()
    for j in range(10):
        tim.color(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        tim.dot()
        tim.penup()
        tim.fd(30)
        tim.pendown()

screen = t.Screen()
screen.exitonclick()