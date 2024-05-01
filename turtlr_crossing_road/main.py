from turtle import Screen
from player import Tut
from cars import CarManager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.title("car race")
screen.tracer(0)
player1 = Tut()
car_manager = CarManager()
score_board = ScoreBoard()
is_game_on = True

screen.listen()
screen.onkey(player1.go_up, "Up")
sleep_time = 0.1

while is_game_on:
    time.sleep(sleep_time)
    screen.update()
    car_manager.create_car()
    car_manager.change_pos()
    player_y_position = player1.ycor()
    player_x_position = player1.xcor()
    if player_y_position > 270:
        score_board.increase_score()
        player1.goto(100, -275)
        sleep_time = sleep_time * 0.5

    #detect collition
    for car in car_manager.all_cars:
        if car.distance(player1) < 20:
            score_board.gameover()
            is_game_on = False



screen.exitonclick()

