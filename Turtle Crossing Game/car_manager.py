from turtle import *
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car=Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            self.all_cars.append(new_car)
            y_position=(random.randint(-250, 250))
            x_position=300
            new_car.goto(x_position, y_position)
            new_car.setheading(0)



    def move(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    
    
    