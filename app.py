#import modules
import turtle
#initialisation screen
wind=turtle.Screen()
wind.title("ping pong")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)
#3sa1
a3sa1=turtle.Turtle()
a3sa1.speed(0)
a3sa1.shape("square")
a3sa1.shapesize(stretch_wid=5,stretch_len=1)
a3sa1.color("blue")
a3sa1.penup()
a3sa1.goto(-350,0)
#3ssa2
a3sa2=turtle.Turtle()
a3sa2.speed(0)
a3sa2.shape("square")
a3sa2.shapesize(stretch_wid=5,stretch_len=1)
a3sa2.color("red")
a3sa2.penup()
a3sa2.goto(350,0)
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=-0.5
#fuction
def a3sa1_up():
    y=a3sa1.ycor()
    y+=20
    a3sa1.sety(y)
def a3sa1_down():
    y=a3sa1.ycor()
    y-=20
    a3sa1.sety(y)
def a3sa2_up():
    y=a3sa2.ycor()
    y+=20
    a3sa2.sety(y)
def a3sa2_down():
    y=a3sa2.ycor()
    y-=20
    a3sa2.sety(y)
#keybord binding
wind.listen()
wind.onkeypress(a3sa1_up,"w")
wind.onkeypress(a3sa1_down,"x")
wind.onkeypress(a3sa2_up,"Up")
wind.onkeypress(a3sa2_down,"Down")
#main game loup
while True:
    wind.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
#border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*=-1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*=-1
    #tasadom a3sa m3a ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < a3sa2.ycor()+40 and ball.ycor() > a3sa2.ycor() -40):
        ball.sety(340)
        ball.dx*=-1      
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < a3sa1.ycor()+40 and ball.ycor() > a3sa1.ycor() -40):
        ball.sety(-340)
        ball.dx*=-1  
