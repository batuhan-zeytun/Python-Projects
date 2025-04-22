
from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []

    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.setx(car.xcor() - STARTING_MOVE_DISTANCE)
        
    def remove_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def reset(self):
        self.remove_cars()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()
