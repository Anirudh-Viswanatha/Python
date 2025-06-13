from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue", "yellow")
tim.pensize(20)
tim.speed(100)

colors = ["green","blue","orange","purple","pink", "turquoise", "saddle brown", "hot pink", "red"]
direction = [90, 180, 270, 360]

for x in range(100):
    tim.color(random.choice(colors))
    tim.forward(50)
    # tim.right(random.choice(direction)) or 
    tim.setheading(random.choice(direction))


screenclick = Screen()
screenclick.exitonclick()


# -----------------------------------------------------------------------------
## Optimized ## Using random RGB colors rather than selecting from a list of limited colors

# import turtle
# from turtle import Turtle, Screen
# import random

# turtle.colormode(255)


# tim = Turtle()
# tim.shape("turtle")
# tim.color("blue", "yellow")
# tim.pensize(20)
# tim.speed(100)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple

# # colors = ["green","blue","orange","purple","pink", "turquoise", "saddle brown", "hot pink", "red"]
# direction = [90, 180, 270, 360]


# for x in range(100):
#     # tim.color(random.choice(colors))
#     tim.pencolor(random_color()) # or tim.color(random_color())
#     tim.forward(50)
#     # tim.right(random.choice(direction)) or
#     tim.setheading(random.choice(direction))


# screenclick = Screen()
# screenclick.exitonclick()





