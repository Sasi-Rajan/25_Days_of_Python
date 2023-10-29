from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(pos)



    def up(self):
        y_pos=self.ycor()+30
        self.goto(self.xcor(),y_pos)

    def down(self):
        y_pos=self.ycor()-30
        self.goto(self.xcor(),y_pos)
