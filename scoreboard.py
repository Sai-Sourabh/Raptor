from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt", "r") as file:
            self.contents = int(file.read())
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE:{self.score} HighScore: {self.contents}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.contents:
            self.contents = self.score
            with open("data.txt", mode="w")as file:
                file.write(f"{self.contents}")

        self.score = 0
        self.update_scoreboard()

