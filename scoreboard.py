from turtle import Turtle
FONT = ('Arial', 8, 'normal')
ALIGN = "right"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highest_score = file.read()
        self.goto(0, 280)
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", False, align=ALIGN, font=FONT)
        self.hideturtle()

    def reset(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", False, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over", True, align="center", font=('Arial', 20, 'normal'))
