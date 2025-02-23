"""
   Create a turtle that will allow you to press the Up key to go forwards, the Down key to go backwards,
   the Left key to go counterclockwise or leftwards and the Right key to go right or clockwise.
   When you press the C key, it should clear all your drawings and put your turtle back in the center.

"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    # OR
    # tim.left(10)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    # OR
    # tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    # OR
    # tim.reset()


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
#                 OR
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=anti_clockwise)
# screen.onkey(key="c", fun=clear)

screen.exitonclick()
