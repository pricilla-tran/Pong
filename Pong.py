# Simple Pong in Python 3 for Beginners

import turtle
import os
import winsound

wn = turtle.Screen()
wn.title("Pong by Pricilla Tran")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # stops window from updating so we have to manually update, speed up games

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Paddle A
paddle_a = turtle.Turtle() # Turtle object
paddle_a.speed(0) # Speed of animation
paddle_a.shape("square") # define shape
paddle_a.color("white") # define colour
paddle_a.shapesize(stretch_wid=5,stretch_len=1) # stretch shape
paddle_a.penup() # no drawing when moving
paddle_a.goto(-350, 0) # starting point

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Functions
def paddle_a_up(): # defined function
    y = paddle_a.ycor() # find current y coordinate
    y += 20 # increases the pixels in the y coordinate
    paddle_a.sety(y) # set y to the new y

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
wn.listen() # Observer
wn.onkeypress(paddle_a_up, "w") # when press w, the paddle will go up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update() # when the loop runs, the screen is updated
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    # Top
    if ball.ycor() > 290:
        ball.sety(290) # set it back to 290
        ball.dy *= -1 # changes the direction
        #os.system("afplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # this is for windows
        # the last part is so it doesn't buffer/stop the game


    # Bottom
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #os.system("aplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # this is for windows
        # the last part is so it doesn't buffer/stop the game

    # Left
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Right
    elif ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        #os.system("aplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # this is for windows
        # the last part makes sure it doesn't buffer/stop the game


    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        #os.system("aplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # this is for windows
        # the last part is so it doesn't buffer/stop the game
