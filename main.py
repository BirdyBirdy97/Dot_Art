import turtle
import functions
from turtle import Turtle, Screen

# colour_list = functions.get_rgb_pic_colours("cyberpunk_colours.jpg", 20)
# print(colour_list)

# Then I copied and pasted it so I could edit the colours/take out the ones I didn't like or were too dark
colour_list = [(26, 22, 55), (62, 88, 155), (52, 45, 110), (47, 18, 64), (120, 157, 172), (86, 37, 109), (74, 155, 167),
               (126, 65, 144), (169, 144, 172), (103, 111, 168), (133, 167, 165), (153, 104, 164), (168, 167, 164),
               (76, 163, 161), (21, 80, 99), (93, 131, 129)]

# Setup
franklin = Turtle()
screen = Screen()
turtle.colormode(255)
screen.bgcolor("#1c1c21")

# Variable for dot_art
num_of_dots = 100

# Calling the dot_art function
functions.dot_art(franklin, colour_list, num_of_dots)

screen.exitonclick()
