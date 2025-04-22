# main.py

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

class TurtleCrossingGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

        choice = self.screen.textinput(
            "Zorluk Seviyesi",
            "Kolay, Orta veya Zor? "
        )
        choice = choice.lower() if choice else "kolay"
        spawn_map = {"kolay": 0.1, "orta": 0.2, "zor": 0.4}
        spawn_chance = spawn_map.get(choice, 0.1)

        self.player = Player()
        self.car_manager = CarManager(spawn_chance=spawn_chance)
        self.scoreboard = Scoreboard()

        self.screen.listen()
        self.screen.onkey(self.player.move, "Up")
        self.game_is_on = True

    def run(self):
        while self.game_is_on:
            time.sleep(0.1)
            self.screen.update()
            self.car_manager.move_cars()

            self._check_finish_line()
            self._check_collisions()

        self.scoreboard.game_over()
        self.screen.exitonclick()

    def _check_finish_line(self):
        if self.player.is_at_finish_line():
            self.scoreboard.increase_score()
            self.player.reset_position()
            self.car_manager.reset()

    def _check_collisions(self):
        for car in self.car_manager.cars:
            if self.player.distance(car) < 20:
                self.game_is_on = False
                break

if __name__ == "__main__":
    game = TurtleCrossingGame()
    game.run()
