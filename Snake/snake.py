from turtle import Turtle
from screen import SCREEN_HEIGHT, SCREEN_WIDTH

# Constants
STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))  # Initial positions of the snake segments
MOVE_DISTANCE = 4  # Distance to move the snake in each step
COLOR = "green"  # Color of the snake segments
SHAPE = "square"  # Shape of the snake segments
LENGTH = 3  # Initial length of the snake
UP = 90  # Heading direction for moving up
DOWN = 270  # Heading direction for moving down
LEFT = 180  # Heading direction for moving left
RIGHT = 0  # Heading direction for moving right


class Snake:
    def __init__(self):
        """Initialize the snake."""
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.speed = MOVE_DISTANCE

    def create_snake(self):
        """Create the initial snake with starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add new body segment."""
        new_segment = Turtle(SHAPE)
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def grow(self):
        """Grow the snake."""
        for _ in range(2):
            self.add_segment(self.body[-1].position())

    def move(self):
        """Move the snake forward."""
        # Move each segment of the snake except the head to the position of the previous segment
        for seg_num in range(len(self.body)-1, 0, -1):
            new_x = self.body[seg_num-1].xcor()
            new_y = self.body[seg_num-1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        # Move the head of the snake forward
        self.head.forward(self.speed)

    def up(self):
        """Change the snake's direction to up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Change the snake's direction to right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Change the snake's direction to left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def speed_up(self):
        """Increase snake's moving speed"""
        self.speed += 0.3

    def wall_hit(self):
        """Check if the snake hits the wall."""
        # Check if the snake's head hits any of the screen boundaries
        if self.head.xcor() > SCREEN_WIDTH//2 - 10 or self.head.xcor() < -SCREEN_WIDTH//2 + 10:
            return True
        elif self.head.ycor() > SCREEN_HEIGHT//2 - 10 or self.head.ycor() < -SCREEN_HEIGHT//2 + 10:
            return True

        return False  # Return False if the snake does not hit the wall

    def body_hit(self):
        """Check if the snake hits the body."""
        for segment in self.body[1:]:
            if self.head.distance(segment) < 1:
                return True
        return False

    def reset(self):
        """Reset the snake"""
        for segment in self.body:
            segment.goto(SCREEN_HEIGHT+400, SCREEN_WIDTH+400)
        self.body.clear()
        self.create_snake()  # Create the initial snake
        self.head = self.body[0]
