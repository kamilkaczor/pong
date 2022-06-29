import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen = Screen()
screen.tracer(0)
r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)
screen.listen()
ball = Ball()
game_is_on = True
scoreboard = Score()
screen.onkey(r_paddle.paddle_move_up, "Up")
screen.onkey(r_paddle.paddle_move_down, "Down")

screen.onkey(l_paddle.paddle_move_up, "w")
screen.onkey(l_paddle.paddle_move_down, "s")
while game_is_on:
    time.sleep(ball.move_speed)
    screen.tracer(1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(r_paddle) < 50 and ball.xcor()) > 320 or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.add_l_point()
        ball.move()
    if ball.xcor() < -370:
        scoreboard.add_r_point()
        ball.reset_position()
        ball.move()



screen.exitonclick()