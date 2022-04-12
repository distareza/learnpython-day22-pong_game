from turtle import Turtle

class ScoreBoard(Turtle):

    score = [0, 0]
    screen_height = 260

    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.penup()
        self.color("white")
        self.hideturtle()
        self.sety(self.screen_height)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score[0]} : {self.score[1]}", align="center", font=("Arial", 18, "normal"))

    def add_score_player_1(self):
        self.score[0] += 1
        self.clear()
        self.update_scoreboard()

    def add_score_player_2(self):
        self.score[1] += 1
        self.clear()
        self.update_scoreboard()
