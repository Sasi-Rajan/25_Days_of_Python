from turtle import Turtle
SPEED=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.all_turtles=[]
        self.create_snake()
        
    def create_snake(self):
        for x in range(0,60,20):
            turtle=Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=x,y=0)
            self.all_turtles.append(turtle)
            
    def move(self):
        for segment in range(len(self.all_turtles)-1,0,-1):
            new_x=self.all_turtles[segment-1].xcor()
            new_y=self.all_turtles[segment-1].ycor()
            self.all_turtles[segment].goto(new_x,new_y)
        self.all_turtles[0].forward(SPEED)
        
    def up(self):
        if self.all_turtles[0].heading() != DOWN:
            self.all_turtles[0].setheading(UP)
        
    def down(self):
        if self.all_turtles[0].heading() != UP:
            self.all_turtles[0].setheading(DOWN)
        
    def left(self):
        if self.all_turtles[0].heading() != RIGHT:
            self.all_turtles[0].setheading(LEFT)
        
    def right(self):
        if self.all_turtles[0].heading() != LEFT:
            self.all_turtles[0].setheading(RIGHT)
    