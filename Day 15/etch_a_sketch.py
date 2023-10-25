from turtle import Turtle , Screen

figo = Turtle()
screen = Screen()

def move_forward():
    figo.forward(10)
def move_backward():
    figo.backward(10)
def turn_right():
    figo.right(10)
def turn_left():
    figo.left(10)
def stop():
    figo.reset()
    

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=stop)
screen.exitonclick()