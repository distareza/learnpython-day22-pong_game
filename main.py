"""
Challenge Create Pong Game
1. Create the screen
2. Create and move the paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with wall and bounce
6. Detect Collision with paddle
7. Detect when paddle misses
8. Keep Score
"""
import time
from turtle import Turtle, Screen
from ScoreBoard import ScoreBoard

# 1. Setup Screen
screen = Screen()
screen_width = 800
screen_height = 600
screen.bgcolor("black")
screen.setup(screen_width, screen_height)
screen.title("Pong")
screen.tracer(0)

# 2. Create and move the paddle
from MyPaddle import MyPaddle
r_paddle = MyPaddle(screen, "right")
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

# 3. Create another Paddle
l_paddle = MyPaddle(screen, "left")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# create wall
import Wall
Wall.create_separator()
Wall.create_wall()
screen.update()

# 4. create ball
from PongBall import Ball
ball = Ball(screen)

# 8. Keep Score
score_board = ScoreBoard()

while True:
    ball.reset_position()

    #7. Detect when paddle misses
    while not ball.is_out_of_range():
        time.sleep(0.01)

        # 6. Detect Collision with paddle
        if ball.distance(r_paddle) < 20 or ball.distance(l_paddle) < 20:
            ball.bounce()

        # 5. Detect collision with wall and bounce
        ball.move()

    if ball.is_ball_on_right():
        score_board.add_score_player_2()
    else:
        score_board.add_score_player_1()

screen.exitonclick()
