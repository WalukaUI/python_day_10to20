import colorgram as co
from turtle import Turtle, Screen
import turtle as t
import random
timmy = Turtle()
t.colormode(255)
timmy.shape("circle")
timmy.speed("fastest")

count = 3
angele = 360

# def rand_color():
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#
#     color_tuple = (r, b, g)
#     return color_tuple

# for y in range(10):
#     for x in range(count):
#         timmy.color(rand_color())
#         timmy.forward(100)
#         timmy.left(360/count)
#     count += 1

# heading = timmy.heading()
# count = 0
#
# for y in range(75):
#     timmy.color(rand_color())
#     timmy.circle(100)
#     timmy.setheading(count)
#     count += 5
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.hideturtle()
colors = co.extract('img.jpg', 30)
rgb_colors = []
for x in colors:
    r = x.rgb.r
    b = x.rgb.b
    g = x.rgb.g
    color = (r, b, g)
    rgb_colors.append(color)
count = 0
for _ in range(10):
    count += 1
    for _ in range(9):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.forward(50)
        timmy.dot(20, random.choice(rgb_colors))
    if count != 10:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(450)
        timmy.setheading(360)








screen = Screen()
screen.exitonclick()