# width 20, heigh 100, x 350, y 0
from turtle import Turtle
WIDTH = 20
HEIGHT = 100

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_position = x_pos
        self.y_position = y_pos
# 
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        # self.new_paddle.hideturtle()
        self.goto(x=self.x_position, y=self.y_position)
        # self.new_paddle.showturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=HEIGHT/20, stretch_len=WIDTH/20)
 
    def up(self):
        self.y_position += 20
        self.goto(x=self.x_position, y=self.y_position)

    def down(self):
        self.y_position -= 20
        self.goto(x=self.x_position, y=self.y_position)