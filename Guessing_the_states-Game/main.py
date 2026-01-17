import turtle,pandas

screen = turtle.Screen()
new_turtle= turtle.Turtle()
screen.title("U.S. States Game Start")
image="blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
i=0
states=pandas.read_csv("50_states.csv")
x_cor=states["x"]
y_cor=states["y"]
states_names=states["state"]

#return output of x and y of the given state
#How does iloc[0] work or use item()
#{The Solution - .iloc[0]:
#.iloc[0] means: "Get the element at index position 0"}

def output_x(input_state):
    xcor = states[states.state == input_state]
    return int(xcor.x.iloc[0]) #can use item() instead of iloc[0]
def output_y(input_state):
    ycor = states[states.state == input_state]
    return int(ycor.y.iloc[0]) #can use item() instead of iloc[0]

states1=states_names.tolist()

is_game_on = True
Guessed_list=[]
while is_game_on:

    #screen.goto(-257,193)
    answer_state = screen.textinput(title=f"{i}/50 Guess the state name", prompt="What's another state name?").title()
    #screen.hideturtle()

    if answer_state == "Exit":
        missing_states=[]
        for state2 in states1:
            if state2 not in Guessed_list:
                missing_states.append(state2)
        data_frame = pandas.DataFrame(missing_states)
        data_frame.to_csv("states_to_learn.csv")
    if answer_state in states1:
        if answer_state in Guessed_list:
            continue
        x=(output_x(answer_state))
        y=(output_y(answer_state))
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(x,y)
        new_turtle.write(f"{answer_state}",align="center", font=("Arial", 8 , "bold"))
        Guessed_list.append(answer_state)
        i+=1
    if i==50:
        is_game_on=False
        new_turtle.write("You win!", align="center", font=("Arial", 30, "bold"))


screen.mainloop()