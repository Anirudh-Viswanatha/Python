from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue", "yellow")

colors = ["green","blue","orange","purple","pink", "turquoise", "saddle brown", "hot pink", "red"]

for x in range(3, 11):
    color = random.choice(colors)
    tim.color(color)
    for i in range(x):
        tim.forward(100)
        tim.right(360/x)

screenclick = Screen()
screenclick.exitonclick()

