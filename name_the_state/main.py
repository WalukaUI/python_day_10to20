import turtle
import pandas
from turtle import Turtle, Screen

screen = turtle.Screen()
screen.title("States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
is_game_on = True
datas = pandas.read_csv("./50_states.csv")
states = datas["state"]
correct_answers = []

while is_game_on:
    answer_box = screen.textinput("State name", "Enter a state")
    for state in states:
        if state == answer_box:
            correct_answers.append(state)
        else:
            is_game_on = False

print(correct_answers)






turtle.mainloop()
# screen.exitonclick()



