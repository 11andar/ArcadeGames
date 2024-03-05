from turtle import Turtle

# Constants
ALIGNMENT = "center"  # Text alignment for the scoreboard display
FONT = ("Arial", 24, "normal")  # Font style for the scoreboard display


class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 270)
        self.set_highest_score()
        self.display()

    def display(self):
        """Display the current score."""
        self.clear()
        self.write(f"Score: {self.score} \t  Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        """Add a point to the score."""
        self.score += 1
        self.display()

    def reset(self):
        """Update the highest score and reset the score"""
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score_data.txt", mode="w") as file:
                file.write(f"Highest score: {self.highest_score}")

        self.score = 0
        self.display()

    def set_highest_score(self):
        """Get a highest score from a file and assign it to the highest score."""
        h_score = ""

        with open("highest_score_data.txt", mode="r") as file:
            data = file.read()
            for letter in data:
                if letter.isdigit():
                    h_score += letter

        self.highest_score = int(h_score)