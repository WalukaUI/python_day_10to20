from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)
colors = ["red", "blue", "green", "orange", "purple"]
user_bet = screen.textinput(title="make your bet", prompt="Which will win the race")
height = [-100, -50, 0, 50, 100]

obj = []
for x in range(0, 5):
    newname = colors[x]
    newname = Turtle(shape="turtle")
    obj.append({"name": colors[x], "obj": newname})
    newname.color(colors[x])
    newname.penup()
    newname.goto(-230, height[x])

if user_bet:
    is_on = True
winner = ""
while is_on:
    for x in range(0, 5):
        if obj[x]["obj"].xcor() >= 190:
            is_on = False
            winner = obj[x]["name"]
        distance = random.randrange(5, 50)
        obj[x]["obj"].forward(distance)
        obj[x]["obj"].xcor()

if winner == user_bet:
    print(f"you are the winner.***** color is {winner}")
else:
    print(f"you are the losttttttttt.%%%%%%%% color is {winner}")
screen.exitonclick()


