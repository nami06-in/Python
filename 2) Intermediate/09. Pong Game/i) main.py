from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from center_line import Center
import time

# Goal 1: Create the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

screen.tracer(0)

r_paddle = Paddle((350, 0))
# Goal 3: Create another Paddle
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
line = Center()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Goal 5: Detect Collision with wall and Bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Goal 6: Detect Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed()

    # Goal 7.a: Detect when right Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Goal 7.b: Detect when left Paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()