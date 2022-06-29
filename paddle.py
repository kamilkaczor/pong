from turtle import Turtle, Screen



class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.fillcolor("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.x_posiotion = x_pos
        self.y_position = y_pos
        self.goto(x_pos, y_pos)


    def paddle_move_up(self):
        self.y_position = self.ycor()
        if self.y_position > 240:
            pass
        else:
            self.goto(self.x_posiotion, self.y_position+20)


    def paddle_move_down(self):
        self.y_position = self.ycor()
        if self.y_position < -220:
            pass
        else:
            self.goto(self.x_posiotion, self.y_position-20)


