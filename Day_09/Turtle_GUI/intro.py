# --------------------- Always refer documentation and StackOverFlow ----------------------

import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

# Draw a square
tim.forward(100)
tim.left(90)   # 90 is angle 
tim.forward(100)
tim.left(90) 
tim.forward(100)
tim.left(90) 
tim.forward(100)

# Or use for loop

for _ in range(4):
    tim.forward(100)
    tim.right(90)

# Draw a dashed line

tim.left(45)

for _ in range(6):
    tim.forward(10)
    tim.penup() # you can write - tim.pu()
    tim.forward(10)
    tim.pendown() # you can write - tim.pd()

# Draw different shapes (triangle, square, pentagon, hexagon, heptagon, nonagon, etc...)

colors = ['MediumBlue', 'LawnGreen', 'DarkTurquoise', 'Peru	', 'Gold', 'RoyalBlue', 'MediumSlateBlue']
# Choosing colors from : https://trinket.io/docs/colors
tim.left(45)

def draw_shape(num_slides):
    angle = 360/ num_slides
    for _ in range(num_slides):
        tim.forward(100)
        tim.right(angle)
for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()


