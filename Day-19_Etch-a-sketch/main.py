from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# W- Forwards
# S- Backwards
# A- Counter-Clockwise
# D- Clockwise
# C- Clear Drawing

def move_forwards():
    tim.forward(10)
    tim.pensize(2)
    tim.pencolor("pink")
    

def move_backwards():
    tim.backward(10)
    tim.pensize(2)
    tim.pencolor("blue")

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    tim.pensize(2)
    tim.pencolor("red")

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    tim.pensize(2)
    tim.pencolor("yellow")

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
