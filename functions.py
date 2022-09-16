import random
import colorgram


def get_rgb_pic_colours(jpg_image, num_of_colours):
    rgb = []
    colours = colorgram.extract(jpg_image, num_of_colours)
    for colour in colours:
        r = colour.rgb.r
        g = colour.rgb.g
        b = colour.rgb.b
        rgb_format = (r, g, b)
        rgb.append(rgb_format)
    return rgb


def dot_art(turtle, colour_list, num_dots):
    turtle.penup()
    turtle.goto(-235, -220)
    turtle.setheading(360)
    x = turtle.position()[0]
    y = turtle.position()[1]

    for dots in range(1, num_dots + 1):
        turtle.dot(20, random.choice(colour_list))
        turtle.forward(50)
        if dots % 10 == 0:
            y += 50
            turtle.goto(x, y)
    turtle.hideturtle()

