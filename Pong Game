import turtle
import winsound

window = turtle.Screen()
window.title("Pong by Mehyeddin")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


score_a = 0
score_b = 0


recA = turtle.Turtle()
recA.speed(0)
recA.shape("square")
recA.color("white")
recA.shapesize(stretch_len=1, stretch_wid=5)
recA.penup()
recA.goto(-350,0)

recB = turtle.Turtle()
recB.speed(0)
recB.shape("square")
recB.color("white")
recB.shapesize(stretch_len=1, stretch_wid=5)
recB.penup()
recB.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.penup()
ball.goto(0,0)
ball.dx = 0.14
ball.dy = 0.14

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))


def recA_Up():
    y = recA.ycor()
    y = y + 20
    recA.sety(y)

window.listen()
window.onkeypress(recA_Up,"w")

def recA_Down():
    y = recA.ycor()
    y = y - 20
    recA.sety(y)

window.listen()
window.onkeypress(recA_Down,"s")

def recB_Up():
    y = recB.ycor()
    y = y + 20
    recB.sety(y)

window.listen()
window.onkeypress(recB_Up,"Up")

def recB_Down():
    y = recB.ycor()
    y = y - 20
    recB.sety(y)

window.listen()
window.onkeypress(recB_Down,"Down")


while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * (-1)
        winsound.PlaySound("SPRTField_Balloon against wall 1 (ID 1825)_BSB.wav", winsound.SND_ASYNC)

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy = ball.dy * (-1)
        winsound.PlaySound("SPRTField_Balloon against wall 1 (ID 1825)_BSB.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * (-1)
        score_a = score_a + 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * (-1)
        score_b = score_b + 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and  ball.ycor() < recB.ycor() + 40 and ball.ycor() > recB.ycor() - 40:
        ball.setx(340)
        ball.dx = ball.dx * (-1)

    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < recA.ycor() + 40 and ball.ycor() > recA.ycor() - 40:
        ball.setx(-340)
        ball.dx = ball.dx * (-1)
