import pandas
import turtle

screen = turtle.Screen()
turtle.setup(725, 491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

while True:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?")
    answer_state in data.state.unique()

    finded_state = data[data.state == answer_state]
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(finded_state.x.item(), finded_state.y.item())
    state.write(finded_state.state.item())

#

turtle.exitonclick()


