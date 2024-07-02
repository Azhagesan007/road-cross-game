from turtle import Screen
from user import User
from cars import Cars
import time
from scoreboard import Scoreboard

score = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
timmy = User()
screen.listen()
screen.onkeypress(key="Up", fun=timmy.up)
screen.onkeypress(key="Down", fun=timmy.down)
screen.title("Cross to the other end")
car = Cars()
start = True
a = 0.1
while start:
    # print(a)
    time.sleep(a)
    screen.update()
    car.move()
    for item in car.car:
        x = timmy.ycor()
        if item.distance(timmy.xcor(), timmy.ycor()) < 30 and x - 20 < item.ycor() < x + 20:
            # print(item.ycor())
            # print(timmy.ycor())
            screen.update()
            score.game_over()
            start = False
    if timmy.ycor() > 300:
        score.score_increases()
        timmy.goto(0, -280)
        if a == 0:
            score.you_won()
            start = False
        a = a / 3


screen.exitonclick()
