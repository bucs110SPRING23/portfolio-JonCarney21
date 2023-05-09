import turtle
import random

def is_in_screen(w, t):

wn = turtle.Screen()
wn.bgcolor("yellow")
wn.setup(400,400)
t1 = turtle.Turtle()
t1.speed(0)

# 1 = heads
# 2 = tails
is_in_screen = True
angle = 90 
distance = 50

while is_in_screen (wn, t1):
    random_number = random.randint(1,2)
    print(random_number)

    if random_number == 1:
        t1.right(angle)
    else:
        t1.left(angle)
    t1.forward(distance)

turtlex = t1.xcor()
turtley = t1.ycor()

