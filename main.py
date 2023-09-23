import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

HEIGHT = 600
WIDTH = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Jokeward's Snake Game")

# Create a snake body
snake = Snake()

# Create Food
food = Food()

# Create a scoreboard
score_board = Scoreboard()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  # Collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    score_board.increase_score()
    snake.extend()

  # Collision with wall
  if abs(snake.head.xcor()) > (WIDTH / 2 - 10) or abs(
      snake.head.ycor()) > (WIDTH / 2 - 10):
    game_is_on = False
    score_board.game_over()

  # Collision with tail
  for body in snake.snake_body[1:]:
    if snake.head.distance(body) < 10:
      print(body)
      game_is_on = False
      score_board.game_over()

screen.exitonclick()
