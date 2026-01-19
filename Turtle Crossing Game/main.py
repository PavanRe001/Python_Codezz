import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
scoreboard=Scoreboard()
car=CarManager()
screen.listen()
screen.onkeypress(player.go_up, "Up")

#detect collision

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    screen.update()
    car.create_car()
    car.move()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        player.go_to_start()
        scoreboard.increase_level()
        car.increase_speed()


screen.exitonclick()
