import turtle 
import os 

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0 

# Paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle b 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

# Might have to mess with these numbers a bit, the lower the number the slower the ball
ball.dx = 1   
ball.dy = -1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = "center", font =("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

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
    y-= 20
    paddle_b.sety(y)

# Keyboard Bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Code to move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking

    # Top and Bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    # Left and Right
    if ball.xcor() > 390:
        scoreA += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font = ("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1

    elif ball.xcor() < -390:
        scoreB += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1

    # Paddle and ball collisions  
    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1  

    elif (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
    
    