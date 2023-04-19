import pandas
import turtle

# screen = turtle.Screen()
# turtle.setup(725, 491)
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
states = []
data = pandas.read_csv("50_states.csv")

while True:
    # answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?")
    answer_state = input("What's another state name? ")
    states.append(data.state.to_list())
    # if answer_state == data.state.item()
    # answer_state class 'str'

    if data.state == 'Alabama':
        print("There is")
    else:
        print("There is not")


    # if data.state == answer_state:
    #     pass
    # else:
    #     pass

#     finded_state = data[data.state == answer_state]
#     state = turtle.Turtle()
#     states.append(state)
#     state.hideturtle()
#     state.penup()
#     state.goto(finded_state.x.item(), finded_state.y.item())
#     state.write(finded_state.state.item())
#     print(len(states))
#
#
# turtle.exitonclick()


