from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.STARTING_MOVE_DISTANCE = 5
    
    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance == 1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(x=260,y=random_y)
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.backward(self.STARTING_MOVE_DISTANCE)
            
    def level_up(self):
        self.STARTING_MOVE_DISTANCE+=MOVE_INCREMENT