import turtle
from snake import Snake
from food import Food   
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#7517c2")
screen.title("Classic Snake Game")
screen.tracer(0)  # Turn off animation for instant updates

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")  



IS_GAME_ON = True

while IS_GAME_ON:
    screen.update()  # Show all movements at once
    time.sleep(0.1)  # Slow it down so you can see it
    snake.move()

    if snake.head.distance(food) < 15:  # Collision with food
        food.refresh()  # Move food to a new random location
        scoreboard.increase_score()
        snake.extend()  # Add a new segment to the snake
    
    #detect Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 270 or snake.head.ycor() < -290:
        IS_GAME_ON = False
        scoreboard.game_over()

    #detect Collision with tail
    for part in snake.body[1:]:  # Skip the head
        if snake.head.distance(part) < 10:
            IS_GAME_ON = False
            scoreboard.game_over()  

screen.exitonclick()