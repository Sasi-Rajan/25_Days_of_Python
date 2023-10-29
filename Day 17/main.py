from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()

score=Scoreboard()

game_on=True

screen.listen()
screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key="Down",fun=r_paddle.down)
screen.onkey(key="w",fun=l_paddle.up)
screen.onkey(key="s",fun=l_paddle.down)



while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.y_bounce()
        
        
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() > -320):
        ball.x_bounce()
        
        
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        
        
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        
        
screen.exitonclick()