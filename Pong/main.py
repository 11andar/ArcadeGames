from paddle import Paddle
from ball import Ball
from turtle import Screen
from scoreboard import Scoreboard
from screen import SCREEN_HEIGHT, SCREEN_WIDTH
import time

# Initialize screen
screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Initialize game objects
l_paddle = Paddle((-360, 0))
r_paddle = Paddle((360, 0))
ball = Ball()
scoreboard = Scoreboard()

# Game controls
screen.listen()

# Paddle on the left
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Paddle on the right
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Game loop
game_over = False

while not game_over:
    screen.update()
    ball.move()
    time.sleep(0.01)

    # Detect collisions with upper and lower walls
    if ball.ycor() > SCREEN_HEIGHT//2 - 20 or ball.ycor() <= -SCREEN_HEIGHT//2 + 20:
        ball.bounce_vertical()

    # Detect collisions with a paddle
    if (ball.xcor() > SCREEN_WIDTH//2 - 65 and ball.distance(r_paddle) <= r_paddle.height//2 + 5 or
            ball.xcor() < -SCREEN_WIDTH//2 + 65 and ball.distance(l_paddle) <= l_paddle.height//2 + 5):
        ball.bounce_horizontal()

    # Detect collisions with right and left walls
    # Right wall
    if ball.xcor() > SCREEN_WIDTH//2 - 35:
        scoreboard.l_point()
        ball.reset()

    # Left wall
    if ball.xcor() < -SCREEN_WIDTH//2 + 35:
        scoreboard.r_point()
        ball.reset()

    # Determine who wins
    if scoreboard.l_score == 11:
        game_over = True
        scoreboard.announce_winner("left")
    elif scoreboard.r_score == 11:
        game_over = True
        scoreboard.announce_winner("right")

screen.exitonclick()
