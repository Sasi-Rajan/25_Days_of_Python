from turtle import Turtle , Screen
import random
colors=["red","orange","yellow","green","blue","purple"]
y_pos=[-70,-40,-10,20,50,80]
race=False
total_turtle=[]


screen=Screen()
screen.setup(width=500,height=400)
user_input=screen.textinput(title="Make your bet", prompt="Which color turtle wins the race? ")


if user_input:
    race=True

for turtle_index in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_pos[turtle_index])
    total_turtle.append(new_turtle)

while race:
    for turtle in total_turtle:
        if turtle.xcor() > 230:
            race=False
            win_color=turtle.pencolor()
            if win_color == user_input:
                print(f"Yahh you win the game with {win_color}")
            else:
                print(f"{win_color} came first. You lost :(")
        distance=random.randint(0,10)
        turtle.forward(distance=distance)



screen.exitonclick()