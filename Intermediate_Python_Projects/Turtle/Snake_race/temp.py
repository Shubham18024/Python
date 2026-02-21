import turtle
import time

# 1. Setup
screen = turtle.Screen()
screen.tracer(0)  # Turns off animation for instant updates
segments = []

# 2. Create Body (3 segments)
for i in range(3):
    new_segment = turtle.Turtle("square")
    new_segment.penup()
    new_segment.goto(x=-i * 20, y=0) # Space them out by 20 pixels
    segments.append(new_segment)

# 3. Collective Movement Loop
while True:
    screen.update() # Show all movements at once
    time.sleep(0.1) # Slow it down so you can see it

    # Move segments from back to front
    for i in range(len(segments) - 1, 0, -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)

    # Move the head last
    segments[0].forward(MOVE)
