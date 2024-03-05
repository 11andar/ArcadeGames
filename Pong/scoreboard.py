from turtle import Turtle

FONT = ("Arial", 60, "normal")  # Font style for the scoreboard display


class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the Scoreboard"""
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update()

    def update(self):
        """Update the scoreboard display"""
        self.clear()
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(200, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        """Increase left player's score by 1 and update the scoreboard"""
        self.l_score += 1
        self.update()

    def r_point(self):
        """Increase right player's score by 1 and update the scoreboard"""
        self.r_score += 1
        self.update()

    def announce_winner(self, side):
        """Display the winning message for the respective player"""
        # Set colors for winning and losing messages
        winning_color = "green"
        losing_color = "red"

        # Determine the positions for winning and losing messages
        winning_position = (200, 0) if side == "right" else (-200, 0)
        losing_position = (-winning_position[0], -winning_position[1])

        # Display winning message
        self.goto(winning_position)
        self.color(winning_color)
        self.write("You win!", align="center", font=FONT)

        # Display losing message
        self.goto(losing_position)
        self.color(losing_color)
        self.write("You lose!", align="center", font=FONT)
