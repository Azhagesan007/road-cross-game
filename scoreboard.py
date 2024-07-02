from turtle import Turtle
FONT = ("Arial", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    """It deals with the score system of the game"""
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("black")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def score_increases(self):
        self.goto(0, 260)
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(arg=f"Game over, Your Score is: {self.score}", align=ALIGN, font=FONT)

    def you_won(self):
        self.goto(0, 0)
        self.clear()
        self.write(arg=f"You won, Your Score is: {self.score}", align=ALIGN, font=FONT)
