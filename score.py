from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"{self.score_l}:{self.score_r}", align='center', font=('Arial', 24, 'normal'))

    def add_l_point(self):
        self.score_l += 1
        self.clear()
        self.write(f"{self.score_l}:{self.score_r}", align='center', font=('Arial', 24, 'normal'))

    def add_r_point(self):
        self.score_r += 1
        self.clear()
        self.write(f"{self.score_l}:{self.score_r}", align='center', font=('Arial', 24, 'normal'))
