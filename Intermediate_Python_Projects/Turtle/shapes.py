import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

screen = Screen()
screen.screensize(canvwidth=2500, canvheight=2500)
screen.bgcolor("whitesmoke")

tim = Turtle()
tim.speed("fast")
tim.width(5)
for i in range(3, 31):
    for j in range(i):
        tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.fd(100)
        tim.right(360 / i)


turtle.done()