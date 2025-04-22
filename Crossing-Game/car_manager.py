# car_manager.py

import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
MAX_CARS = 50  

class CarManager:
    def __init__(self, spawn_chance=0.1):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawn_chance = spawn_chance

    def _create_single_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(300, random.randint(-240, 240))
        self.cars.append(new_car)

    def move_cars(self):
        if random.random() < self.spawn_chance and len(self.cars) < MAX_CARS:
            self._create_single_car()

        for car in self.cars:
            car.setx(car.xcor() - self.car_speed)

        self.cars = [car for car in self.cars if car.xcor() > -320]

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def reset(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
