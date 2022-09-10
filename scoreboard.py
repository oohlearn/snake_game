from turtle import Turtle
FONT = ('Arial', 8, 'normal')
ALIGN = "right"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0, 260)
        self.write(f"Score: {self.score}", True, align=ALIGN, font=FONT)
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", True, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", True, align="center", font=('Arial', 20, 'normal'))
