from turtle import Turtle,Screen,colormode
import random
 
color_list = [(230, 238, 246), (235, 245, 240), (200, 157, 115), (43, 110, 146), (134, 172, 193), (226, 208, 113),
              (134, 84, 67), (148, 65, 85), (198, 140, 153), (193, 83, 102), (182, 159, 51), (150, 178, 164),
              (191, 98, 83), (68, 114, 94), (227, 170, 182), (36, 51, 68), (225, 177, 168), (45, 157, 186),
              (60, 47, 41), (155, 205, 218), (49, 56, 94), (22, 90, 76), (129, 38, 59), (58, 44, 52), (33, 60, 53),
              (97, 146, 125), (173, 203, 189), (178, 188, 212)]
 
tim = Turtle()
colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()
 
for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        tim.goto(x,y)
        tim.dot(20, random.choice(color_list))
 
screen = Screen()
screen.exitonclick()