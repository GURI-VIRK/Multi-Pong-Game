import turtle
import os
import time

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("green")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 3
ball1.dy = -3

# Ball
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("blue")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -3
ball2.dy = -3

balls = [ball1, ball2]

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    if paddle_a.ycor() > 265:
        paddle_a.sety(265)
    else:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() < -265:
        paddle_a.sety(-265)
    else:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    if paddle_b.ycor() > 265:
        paddle_b.sety(265)
    else:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() < -265:
        paddle_b.sety(-265)
    else:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    for ball in balls:
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        time.sleep(0.01)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            # os.system("afplay bounce.wav&")

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            # os.system("afplay bounce.wav&")

        if ball.xcor() > 400:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            if score_a==1:
                paddle_b.shapesize(stretch_wid=5, stretch_len=1)
            elif score_a==3:
                paddle_b.shapesize(stretch_wid=4, stretch_len=1)
            elif score_a==5:
                paddle_b.shapesize(stretch_wid=3, stretch_len=1)
            elif score_a==7:
                paddle_b.shapesize(stretch_wid=2, stretch_len=1)
            elif score_a==9:
                paddle_b.shapesize(stretch_wid=1, stretch_len=1)
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -400:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            if score_b==1:
                paddle_a.shapesize(stretch_wid=5, stretch_len=1)
            elif score_b==3:
                paddle_a.shapesize(stretch_wid=4, stretch_len=1)
            elif score_b==5:
                paddle_a.shapesize(stretch_wid=3, stretch_len=1)
            elif score_b==7:
                paddle_a.shapesize(stretch_wid=2, stretch_len=1)
            elif score_b==9:
                paddle_a.shapesize(stretch_wid=1, stretch_len=1)
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1
            # os.system("afplay bounce.wav&")

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
            # os.system("afplay bounce.wav&")

    # AI Player - play with computer
    closest_ball = balls[0]
    # for ball in balls:
    #     if ball.xcor() > closest_ball.xcor():
    #         closest_ball = ball
    #
    # if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10:
    #     paddle_b_up()
    #
    # elif paddle_b.ycor() > closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10:
    #    paddle_b_down()