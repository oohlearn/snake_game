from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = Scoreboard()


game_is_on = True
screen.listen()


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.make_new_food()
        score.add_score()
        snake.create_seg()
    if snake.head.xcor() == 280 or snake.head.xcor() == -280 or snake.head.ycor() == 280\
            or snake.head.ycor() == -280:
        score.game_over()
        game_is_on = False
    elif snake.check_touch():
        score.game_over()
        game_is_on = False


screen.exitonclick()
