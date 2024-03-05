from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from screen import SCREEN_HEIGHT, SCREEN_WIDTH
import time

# Initialize the screen
screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # Turn off the screen updates

# Initialize the game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up key listeners for snake movement
screen.listen()

# Arrows
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# w,s,a,d
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# Main game loop
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.01)  # Delay to control the game speed
    snake.move()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.generate()
        snake.grow()
        scoreboard.add_point()

        if scoreboard.score > 0 and scoreboard.score % 10 == 0:
            snake.speed_up()

    # Detect collisions with wall
    if snake.wall_hit():
        scoreboard.reset()
        snake.reset()

    # Detect body collisions
    if snake.body_hit():
        scoreboard.reset()
        snake.reset()

# Keep the screen open until the user clicks
screen.exitonclick()

