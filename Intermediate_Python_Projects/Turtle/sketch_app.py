import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed("fastest")

screen = turtle.Screen()
screen.screensize(canvwidth=2500, canvheight=2500)
screen.bgcolor("cyan")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)    

def turn_left():    
    tim.left(10)    

def turn_right():   
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)




turtle.done()