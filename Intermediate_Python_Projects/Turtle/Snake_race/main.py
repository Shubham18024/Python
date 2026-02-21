import turtle
from snake import Snake
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#473CAC")
screen.title("Classic Snake Game")
screen.tracer(0)  # Turn off animation for instant updates

snake = Snake()

IS_GAME_ON = True

while IS_GAME_ON:
    screen.update()  # Show all movements at once
    time.sleep(0.1)  # Slow it down so you can see it

    snake.move()


screen.exitonclick()