import turtle
import random
COLORS = ["red", "black", "yellow", "darkgreen", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
SPEED_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def maybe_create_car(self):
        # Spawn a car only sometimes to reduce crowding/lag.
        if random.randint(1, 6) != 1:
            return
        car = turtle.Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        random_y = random.randint(-250, 246)
        car.goto(300, random_y)
        self.all_cars.append(car)

    def cars_movement(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        # Remove cars that are off-screen to keep the list small.
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def increase_speed(self):
        self.car_speed += SPEED_INCREMENT



        




