import os
from dotenv import load_dotenv

load_dotenv()

"""
      The data.txt file is going to contain a single number, zero. And we're going to use the data 
      that's in this data.txt file to keep track of the high score.

      The file path is stored in .env file which was explained in the preveous project.

"""

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(os.getenv("SNAKE_GAME_HIGH_SCORE_FILE_PATH")) as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(os.getenv("SNAKE_GAME_HIGH_SCORE_FILE_PATH"), mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
