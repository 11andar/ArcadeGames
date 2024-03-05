from turtle import Turtle
from screen import SCREEN_HEIGHT, SCREEN_WIDTH
import random


class Food(Turtle):
    def __init__(self):
        """Initialize the food."""
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.generate()

    def generate(self):
        """Generate food in a random position within the screen boundaries."""
        random_x = random.randint(-SCREEN_WIDTH//2 + 20, SCREEN_WIDTH//2 - 20)
        random_y = random.randint(-SCREEN_HEIGHT//2 + 20, SCREEN_HEIGHT//2 - 20)
        self.setheading(random.randint(0, 360))
        self.goto(random_x, random_y)  # Move food to generated random position
