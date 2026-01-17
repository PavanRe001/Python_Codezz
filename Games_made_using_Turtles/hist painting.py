import colorgram,random
from turtle import Turtle,colormode,Screen
# colors=colorgram.extract('hirst_paintings.jpg',13 )
timmy=Turtle()
#My code
# list_of_colors = []
# rgb = first_color.rgb
# for i in range(0,len(colors)):
#     list_of_colors.append(colors[i].rgb)
# print(list(tuple(list_of_colors)))


#angela code
# rgb_color=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
colormode(255)
color_list=[ (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253),
 (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17)]
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)


for i in range(101):
    if i==10 or i==30 or i==50 or i==70 or i==90:

        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        continue
    elif i==20 or i==40 or i==60 or i==80:

        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)
        continue
    else:
        if i==0:
            timmy.dot(20,"white")
            timmy.forward(50)
            continue

    timmy.dot(20,random.choice(color_list))
    timmy.forward(50)





screen = Screen()
screen.exitonclick()


