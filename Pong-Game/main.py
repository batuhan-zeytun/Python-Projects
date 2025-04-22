from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

coordinates = [(-625, 0), (625, 0)]
screen = Screen()
screen.tracer(0)
screen.setup(width=1300, height=700) # Bu pencere boyutunu ayarlıyor
screen.bgcolor("black")  # opsiyonel, zemin rengi falan istersen
screen.title("Pong Oyunu")  # opsiyonel, pencere başlığı

paddle1 = Paddle(coordinates[0])
paddle2 = Paddle(coordinates[1])
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    if ball.ycor() > 337 or ball.ycor() < -337:
        ball.bounce()

    if ball.xcor() > 500 or ball.xcor() < -500:
        ball.check_collusion(paddle1)
        ball.check_collusion(paddle2)

    if ball.xcor() > 800:
        ball.reset()
        scoreboard.l_point()
        
        
    if ball.xcor() < -800:
        ball.reset()
        scoreboard.r_point()
        
    if scoreboard.r_score > 9 or scoreboard.l_score > 9:
        game_is_on = False


screen.exitonclick()
