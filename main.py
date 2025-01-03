import time
from turtle import Screen
from score import ScoreBoard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(2)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="space", fun=snake.move)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.growth()
        score.add_score()

    # wall collision
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        score.reset()
        snake.reset()

    # tail collision
    for segments in snake.snake[1:]:
        if snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()

screen.mainloop()
