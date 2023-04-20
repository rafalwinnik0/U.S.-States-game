import pandas
import turtle

screen = turtle.Screen()
turtle.setup(725, 491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/50",
                                    prompt="What's another state name?")
    if answer_state in guessed_states:
        print(f"You repeated a state: {answer_state}")
    elif answer_state in data.state.unique():
        finded_state = data[data.state == answer_state]
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(finded_state.x.item(), finded_state.y.item())
        state.write(finded_state.state.item())
        guessed_states.append(answer_state)
    elif answer_state == "exit":
        break
    else:
        print(f"There is no state like {answer_state} in U.S.")


