from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(location)


    def go_up(self):
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
            new_yy = new_y = self.ycor() - 20
            self.goto(self.xcor(), new_yy)