## draw spirograph by manually mentioning how many circles in range

import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


tim = Turtle()
tim.shape("turtle")
tim.color("blue", "yellow")
tim.speed(100)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


for x in range(72):
    tim.pencolor(random_color()) # or tim.color(random_color())
    tim.circle(100)
    tim.right(5) # or tim.setheading(tim.heading()+5) 



screenclick = Screen()
screenclick.exitonclick()


## ----------------------------------------------------------------------------

# Optimized and designed to draw with equal gaps without manually mentioning how many circles in range  

# import turtle
# from turtle import Turtle, Screen
# import random

# turtle.colormode(255)

# tim = Turtle()
# tim.shape("turtle")
# tim.color("blue", "yellow")
# tim.speed(100)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple


# def gap(size_of_gap):
#     for x in range(int(360/size_of_gap)):
#         tim.pencolor(random_color()) # or tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading()+size_of_gap)
# gap(20)

# screenclick = Screen()
# screenclick.exitonclick()

