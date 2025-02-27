"""
   the 'Get Cordinates of US States' folder has the code for getting coordinates by clicking the screen.

   turtle can only works with .gif format. You can set turtle shape as an image by loading it, using screen object.
   addscreen() method is used.

   CHALLANGE: 1. Convert the guess to Title case
              2. Check if the guess is among the 50 states
              3. Write correct guesses onto the map
              4. Use a loop to allow the user to keep guessing
              5. Record the correct guesses in a list
              6. Keep track of the score

   The item() looks into the underlying data and it basically just grabs the first element.
               
   CHALLANGE: generate a states_to_learn.csv file which is going to contain the names of states which have not been 
              guessed by the user when they exit the game.

"""

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?\nOR\nEnter 'exit' to close").title()

    if answer_state == "Exit":
        missing_states = []

        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())  # item() will take the exact value, otherwise
        # index will also be included
        t.write(arg=answer_state, font=("Arial", 8, "bold"))

screen.exitonclick()
