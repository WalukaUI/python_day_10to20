from turtle import Turtle


class Tut(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(100, -275)
        self.setheading(90)

    def go_up(self):
        self.forward(10)



