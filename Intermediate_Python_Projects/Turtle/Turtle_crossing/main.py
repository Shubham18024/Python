import turtle
from player import Player
from car_manager import CarManager
from levelboard import Levelboard
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Crossing")
screen.bgcolor("#B292FC")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
level = Levelboard()

def finish_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.penup()
    line.color("#531616")
    line.pensize(3)
    line.goto(-350, 260)
    for _ in range(18):
        line.penup()
        line.fd(20)
        line.pendown()
        line.fd(20)    

finish_line()

screen.listen()
screen.onkey(player.move_up, "Up")

IS_GAME_ON = True
PLAYER_CAR_DISTANCE = 22

while IS_GAME_ON:
    time.sleep(0.05)
    screen.update()

    cars.maybe_create_car()
    cars.cars_movement()


    if player.ycor() > 260:
        level.increase_score()
        cars.increase_speed()
        player.reset_position()

    #collision detection with car
    for car in cars.all_cars :
        if car.distance(player) < PLAYER_CAR_DISTANCE :
            level.game_over()
            IS_GAME_ON = False

screen.exitonclick()