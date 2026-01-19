import random
from turtle import Turtle,Screen

screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle would you bet on?")
colors=["red","blue","green","yellow","violet","orange"]
y_coordinates=[-100,-50,0,50,100]
all_turtles=[]

for turtle_index in range(0,5):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230,y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color=turtles.pencolor()
            if winning_color == user_bet:
                print(f"Your {winning_color} turtle wins!")
            else:
                print(f"Your {user_bet} turtle loses. The {winning_color} turtle wins!")

        random_distance=random.randint(0,10)
        turtles.forward(random_distance)












screen.exitonclick()
