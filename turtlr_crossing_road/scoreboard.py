from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.player_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_score, align="center", font=("Courier", 40, "normal"))

    def gameover(self):
        self.clear()
        self.write(f"Game Over, your score is {self.player_score}", align="center", font=("Courier", 20, "normal"))

