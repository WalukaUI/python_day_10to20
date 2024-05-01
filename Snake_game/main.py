from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collition with food
    if snake.head.distance(food) < 15:
        food.goto_newlocation()
        scoreboard.increase_score()
        snake.extend_tail()


    #detect collition with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_game()
        snake.reset_snake()


    #detect collition with tail
    for segmant in snake.obj[1:]:
        if snake.head.distance(segmant) < 10:
            scoreboard.reset_game()
            snake.reset_snake()


screen.exitonclick()

