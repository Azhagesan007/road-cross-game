from turtle import Turtle
import random
COLOR = ['red', 'green', 'blue', 'orange', 'turquoise', 'brown', 'yellow', 'black']


class Cars:
    """Controls all the car objects of the game"""
    def __init__(self):
        self.car = []
        for i in range(1, 500):
            t = Turtle()
            t.shape("square")
            t.color(random.choice(COLOR))
            t.shapesize(stretch_wid=1, stretch_len=3)
            t.penup()
            self.car.append(t)
        self.place()

    def place(self):
        for item in self.car:
            x = random.randint(-210, 28400)
            y = random.randint(-240, 260)
            item.goto(x, y)
            item.setheading(180)

    def move(self):
        for car in self.car:
            car.forward(10)
