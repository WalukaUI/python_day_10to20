from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "blue", "black"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def change_pos(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def create_car(self):
        rand_int = random.randint(1, 6)
        if rand_int == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randrange(-250, 250)
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)
