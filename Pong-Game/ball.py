from turtle import Turtle
import random
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 700


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(self.make_direction())
    
    def move(self):
        self.forward(15)
    
    def bounce(self):
        head = self.heading()
        self.setheading(-head)

    def check_collusion(self, paddle):
        if self.distance(paddle) < 50 and (self.xcor() > 610 or self.xcor() < -610):
            self.setheading(180 - self.heading())

    def make_direction(self):
        while True:
            direction = random.randint(0, 360)
            if (direction < 120 and direction > 60) or (direction < 310 and direction > 230):
                direction = random.randint(0, 360)
            else:
                return direction
            
    def reset(self):
        self.setheading(self.make_direction())
        self.goto(0, 0)

    