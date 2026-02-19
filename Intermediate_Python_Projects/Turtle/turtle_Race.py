import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
screen.bgcolor("#2ecc71")
screen.title("Turtle Racing Championship")

colors = ["red", "yellow", "green", "blue", "orange", "purple"]

user_bet = screen.textinput(
    title="Make your bet",
    prompt=f"Which turtle will win the race?\nChoices: {', '.join(colors)}"
)

if user_bet:
    user_bet = user_bet.lower()

bet_writer = turtle.Turtle()
bet_writer.hideturtle()
bet_writer.penup()
bet_writer.color("white")
bet_writer.goto(0, 160)

if user_bet:
    bet_writer.write(
        f"You bet on: {user_bet.upper()}",
        align="center",
        font=("Arial", 16, "bold")
    )

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(6):
    racer = turtle.Turtle(shape="turtle")
    racer.color(colors[index])
    racer.penup()
    racer.goto(x=-230, y=y_positions[index])
    all_turtles.append(racer)

def display_result(winning_color, user_bet):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(0, 0)

    if user_bet == winning_color:
        writer.color("gold")
        message = f"🎉 YOU WON! {winning_color.upper()} turtle wins! 🎉"
    else:
        writer.color("black")
        message = f"You lost 😢 {winning_color.upper()} turtle wins."

    writer.write(
        message,
        align="center",
        font=("Arial", 16, "bold")
    )

is_race_on = bool(user_bet)

while is_race_on:
    for racer in all_turtles:
        racer.forward(random.randint(0, 10))

        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            display_result(winning_color, user_bet)
            break

screen.exitonclick()
