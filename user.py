from turtle import Turtle


class User(Turtle):
    """Control the turtle"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def up(self):
        self.setheading(90)
        self.move()

    def down(self):
        self.setheading(270)
        self.move()
