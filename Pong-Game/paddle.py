from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.shapesize(6, 1, 1)
        self.color("white")
        self.penup()
        self.setpos(coordinate)


    def up(self):
        if self.ycor() < 300:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -300:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
