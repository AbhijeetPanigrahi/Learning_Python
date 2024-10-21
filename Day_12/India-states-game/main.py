# inspiration: https://www.sporcle.com/games/g/indiastates

import turtle
import pandas 
screen = turtle.Screen()
screen.title = "Indaia_States"

image = r"D:\Learning_Python\Day_12\day-25-us-states-game-start\India_states.gif"
screen.addshape(image)
turtle.shape(image)

# This below 5 line code is for finding the coordinates of all  the states in india and write in the CSV file

# def get_mouse_click_coor(x,y):
#     print(f"{int(x)},{int(y)}")
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("28_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 28:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/28 States Correct" , prompt = "What's the another state's name?").title()
    print(answer_state)
# If the answer_state is one of the states in all the states of the 28_states.csv
    # If they got it right :
    #    create a turtle to write the name of the state at the state's x,y coordinates

    if answer_state == "exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item() , state_data.y.item())
        t.write(answer_state)
        # screen.exitonclick()


screen.exitonclick()