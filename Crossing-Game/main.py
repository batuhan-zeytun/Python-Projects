import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")


#screen.listen()
#screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if player.is_at_finish_line():
        car_manager.remove_cars()
        scoreboard.increase_score()
        player.reset_position()
        car_manager.reset()
        continue

    for car in car_manager.cars:
        if player.distance(car) < 20:  # 20 limiti deneyebilirsin
            # çarpışma oldu, game over yazdır
            scoreboard.game_over()       # veya direkt Turtle ile yazdır
            game_is_on = False



screen.exitonclick()
