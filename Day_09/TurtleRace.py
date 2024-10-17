from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 800, height = 600)
user_bet = screen.textinput(title='Make your bet', prompt='Which Tutle will win the race? Enter a color: ')
# print(user_bet)


colors = ['MediumBlue', 'LawnGreen', 'DarkTurquoise', 'Peru', 'Gold', 'RoyalBlue']

# y_positions = [-240, -200, -160, -120, -80, -40]
y_positions = [-150, -90, -30, 30, 90, 150]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")    # you can use shape here also
    new_turtle.turtlesize(2)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -380, y= y_positions[turtle_index])  # if we do x= exactly 400 which is 800/2 then it will go beyond the screen
    # goto is for taking the turtle to the leaft of the screen
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:

        # turtle stopping algo
        if turtle.xcor() > 380:
            # print(turtle.colot())
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
                is_race_on = False
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
                is_race_on = False

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()