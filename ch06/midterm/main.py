import turtle
import random
def main():
    screen = turtle.Screen()
    screen.setup(800,800)
    turtle1 = turtle.Turtle()
    turtle1.speed(0)
    screen.bgcolor("skyblue")

    #Grass
    turtle1.penup()
    turtle1.goto(-400,-100)
    turtle1.pendown()
    turtle1.color("limegreen")
    turtle1.begin_fill()
    for i in range(2):
        turtle1.forward(800)
        turtle1.right(90)
        turtle1.forward(400)
        turtle1.right(90)
    turtle1.end_fill()
        
    make_mountain(turtle1, -400, -100, "dimgray")
    make_mountain(turtle1, 100, -100, "dimgray")

    #Middle Mountain
    turtle1.penup()
    turtle1.goto(-160,-100)
    turtle1.pendown()
    turtle1.color("gray")
    turtle1.begin_fill()
    for i in range(3):
        turtle1.forward(400)
        turtle1.left(120)
    turtle1.end_fill()

    #Middle Mountain Ice Cap
    turtle1.penup()
    turtle1.goto(-35, 120)
    turtle1.pendown()
    turtle1.color("white")
    turtle1.begin_fill()
    turtle1.left(35)
    turtle1.forward(60)
    turtle1.right(90)
    turtle1.forward(30)
    turtle1.left(100)
    turtle1.forward(45)
    turtle1.right(85)
    turtle1.forward(65)
    turtle1.left(160)
    turtle1.forward(150)
    turtle1.end_fill()

    #Left Mountain Ice Cap
    turtle1.penup()
    turtle1.goto(-215, 100)
    turtle1.pendown()
    turtle1.color("snow")
    turtle1.begin_fill()
    turtle1.forward(70)
    turtle1.left(120)
    turtle1.forward(75)
    turtle1.left(150)
    turtle1.forward(45)
    turtle1.right(90)
    turtle1.forward(45)
    turtle1.left(120)
    turtle1.end_fill()

    #Right Mountain Ice Cap
    turtle1.penup()
    turtle1.goto(203, 80)
    turtle1.pendown()
    turtle1.begin_fill()
    turtle1.forward(95)
    turtle1.right(120)
    turtle1.forward(80)
    turtle1.right(150)
    turtle1.forward(50)
    turtle1.left(70)
    turtle1.end_fill()

    turtle1.left(50)

    # Sun
    turtle1.penup()
    turtle1.goto(-500, 350)
    turtle1.pendown()
    turtle1.color("yellow")
    turtle1.begin_fill()
    turtle1.circle(125)
    turtle1.end_fill()

    screen.exitonclick()


# Mountains
def make_mountain(turtle, xpos, ypos, color):
    turtle.penup()
    turtle.goto(xpos,ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.fd(300)
        turtle.left(120)
    turtle.end_fill()
main()