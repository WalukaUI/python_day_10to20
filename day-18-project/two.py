from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()








def move_fw():
    tim.forward(50)

def move_bk():
    tim.backward(50)

def move_lft():
    tim.right(90)

def move_rgt():
    tim.right(90)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_fw, "w")
screen.onkey(move_bk, "s")
screen.onkey(move_lft, "a")
screen.onkey(move_rgt, "d")
screen.onkey(clear, "c")

screen.exitonclick()