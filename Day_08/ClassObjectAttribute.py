# Constructing Object --------------------------------

from turtle import Turtle, Screen       # Turtle library

timmy = Turtle()    # timmy is object and Turtle is class
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
# Object Attributes --------------------------------

my_screen = Screen()

print(my_screen.canvheight) # my_screen is object and canvheight is attribute

# Object Methods --------------------------------

my_screen.exitonclick()
# timmy.shape("turtle") You can't use this here


