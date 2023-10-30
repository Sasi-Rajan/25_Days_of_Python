import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle=Player()
screen.listen()
screen.onkey(key="Up",fun=turtle.up)


cars=CarManager()
cars.hideturtle()

score=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            game_is_on=False
            score.game_over()
    
    if turtle.finish_line():
        turtle.start()
        cars.level_up()
        score.increase()
    
    
    
screen.exitonclick()
