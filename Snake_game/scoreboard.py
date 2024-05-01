from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("highscore.txt", mode="r") as file:
            textscore = file.read()
            start_idx = textscore.index("=") + 1
            end_idx = len(textscore)
            self.highscore = int(textscore[start_idx:end_idx])
        self.write(f"score is {self.score}, High score: {self.highscore}",  align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"\n new_highscore = {self.highscore}")
        self.score = 0

