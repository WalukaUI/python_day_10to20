from turtle import Turtle
LENTH = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.obj = []
        self.create_snake()
        self.head = self.obj[0]

    def create_snake(self):
        for position in LENTH:
            self.add_tail(position)

    def add_tail(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.obj.append(tim)

    def extend_tail(self):
        self.add_tail(self.obj[-1].position())

    def move(self):
        for obj_num in range(len(self.obj)-1, 0, -1):
            new_x = self.obj[obj_num-1].xcor()
            new_y = self.obj[obj_num-1].ycor()
            self.obj[obj_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.obj:
            seg.goto(1000,1000)
        self.obj.clear()
        self.create_snake()
        self.head = self.obj[0]

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



