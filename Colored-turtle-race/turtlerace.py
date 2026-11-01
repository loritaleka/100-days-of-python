import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20 ,50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                winning_message = (f"You've won! The {winning_color} turtle is the winner!")
                turtle.goto(0, 0)
                turtle.write(winning_message, align="center", font=("Calibri",15,"bold"))
                
            else:
                losing_message = (f"You've lost! The {winning_color} turtle is the winner!")
                turtle.goto(0, 0)
                turtle.write(losing_message, align="center", font=("Calibri", 15, "bold"))
                # print(f"You've lost! The {winning_color} turtle is the winner!")
              


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()