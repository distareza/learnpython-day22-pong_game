from turtle import Turtle


class MyPaddle(Turtle):
    width = 20
    height = 100
    x_pos = 350
    y_pos = 0
    my_screen = {}

    def __init__(self, screen, side):
        super().__init__(shape="square")

        if side == "right":
            self.x_pos = 360
        elif side == "left":
            self.x_pos = -360

        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x=self.x_pos, y=self.y_pos)
        self.pendown()
        self.my_screen = screen
        self.my_screen.update()

    def up(self):
        new_y = int(self.ycor()) + 20
        if new_y > ((self.my_screen.window_height() / 2) - (self.height / 2)):
            return
        self.penup()
        self.goto(self.x_pos, new_y)
        self.pendown()
        self.my_screen.update()

    def down(self):
        new_y = int(self.ycor()) - 20
        if new_y < ((-self.my_screen.window_height() / 2) + (self.height / 2)):
            return
        self.penup()
        self.goto(self.x_pos, new_y)
        self.pendown()
        self.my_screen.update()

