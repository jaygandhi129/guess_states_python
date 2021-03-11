import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()


data = pandas.read_csv("50_states.csv")
states = data['state'].to_list()
score = 0
correct_guesses = []
is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's "
                                                                                              "name?").title()
    if answer_state == "Exit":
        to_learn_states = [state for state in states if state not in correct_guesses]
        df = pandas.DataFrame(to_learn_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        correct_guesses.append(answer_state)
        state_data = data[data.state == answer_state]
        pen.goto(int(state_data.x), int(state_data.y))
        pen.write(answer_state)
    if len(correct_guesses) == 50:
        is_game_on = False

