import turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = turtle.Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

def dashed_line():
    dashed = turtle.Turtle()
    dashed.color("white")
    dashed.penup()
    dashed.goto(0, 300)
    dashed.setheading(270)
    dashed.hideturtle()
    for _ in range(15):
        dashed.pendown()
        dashed.fd(20)
        dashed.penup()
        dashed.fd(20)

dashed_line()

screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_up, "W")
screen.onkey(paddle2.move_down, "s")
screen.onkey(paddle2.move_down, "S")


IS_GAME_ON = True

while IS_GAME_ON:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() 

    #Detect collision with paddle
    if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.bounce_x() 

    #Detect when paddle misses the ball
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.increase_score2()    

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.increase_score1()    

screen.exitonclick()