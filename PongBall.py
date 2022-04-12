import time
from turtle import Turtle, Screen


class Ball(Turtle):
    my_screen: Screen() = {}

    window_top = 290
    window_bottom = -290
    window_right = 390
    window_left = -390

    def __init__(self, screen):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.my_screen = screen
        self.setheading(45)
        self.my_screen.update()

    def move(self):
        self.penup()
        if self.detect_wall():
            self.bounce()
        self.forward(5)
        self.pendown()
        self.my_screen.update()

    def detect_wall(self):
        if self.ycor() >= self.window_top or self.ycor() <= self.window_bottom:
            return True
        # if self.xcor() > self.window_right or self.xcor() < self.window_left:
        #     return True
        return False

    def bounce(self):
        self.setheading(self.heading() - 90)

    def is_out_of_range(self):
        return self.is_ball_on_right() or self.is_ball_on_left()

    def is_ball_on_right(self):
        return self.xcor() > self.window_right

    def is_ball_on_left(self):
        return self.xcor() < self.window_left

    def reset_position(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.my_screen.update()