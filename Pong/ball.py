from turtle import Turtle


# Constants
COLOR = "white"
POSITION = (0, 0)
MOVE_DISTANCE = 5


class Ball(Turtle):
    def __init__(self):
        """Initialize the Ball"""
        super().__init__()
        self.shape("circle")
        self.color(COLOR)
        self.penup()
        self.goto(POSITION)
        self.speed("fastest")
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE

    def move(self):
        """Move the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        """Change the vertical direction of the ball"""
        self.y_move *= -1

    def bounce_horizontal(self):
        """Change the horizontal direction of the ball"""
        self.x_move *= -1

    def reset(self):
        """Reset the ball position and horizontal direction"""
        self.goto(0, 0)
        self.bounce_horizontal()
