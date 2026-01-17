import turtle
from turtle import Turtle,Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
# for _ in range(80):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()



#
timmy.pendown()
# timmy.width(5)
# directions=[90,180,270,360,45]
#
turtle.colormode(255)
def colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color= (r,g,b)
    return random_color
#
# colours=["orange red","royal blue","yellow","green yellow","gold"]
# for i in range(200):

#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#     timmy.speed(5)
#
timmy.pensize(2)

for angle in range (0,371):
    timmy.color((colors()))
    timmy.circle(100)
    cu=timmy.heading()
    timmy.setheading(cu + 10)

    timmy.speed("fastest")





screen = Screen()
screen.exitonclick()