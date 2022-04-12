from turtle import Turtle

screen_width = 800
screen_height = 600
def create_separator():
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color("white")
    turtle.pencolor("white")
    turtle.penup()
    turtle.goto(0, 300)
    turtle.setheading(270)

    for i in range(60):
        if i % 2 == 0:
            turtle.penup()
        else:
            turtle.pendown()
        turtle.forward(10)

def create_wall():
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color("white")
    turtle.pencolor("white")
    turtle.penup()
    turtle.goto(-screen_width/2, screen_height/2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(screen_width)
    turtle.penup()
    turtle.goto(-screen_width/2, -screen_height/2)
    turtle.pendown()
    turtle.forward(screen_width)

