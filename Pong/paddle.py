from turtle import Turtle

# Constants
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        """Initialize the Paddle"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.width = 20*1
        self.height = 20*5
        self.penup()
        self.goto(position)

    def up(self):
        """Move the paddle up"""
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def down(self):
        """Move the paddle down"""
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
