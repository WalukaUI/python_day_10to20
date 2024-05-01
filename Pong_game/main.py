from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

l_bar = Paddle((-370, 0))
r_bar = Paddle((370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_bar.go_up, "Up")
screen.onkey(r_bar.go_down, "Down")
screen.onkey(l_bar.go_up, "w")
screen.onkey(l_bar.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    #detect collition with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect colltion with r_bar
    if ball.distance(r_bar) < 50 and ball.xcor() > 320 or ball.distance(l_bar) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #detect r_bar pass the ball
    if ball.xcor() > 380:
        ball.reset_ball_position()
        scoreboard.increaase_lscore()
    # detect l_bar pass the ball
    if ball.xcor() < -380:
        ball.reset_ball_position()
        scoreboard.increaase_rscore()






screen.exitonclick()
