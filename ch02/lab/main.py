
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)


#Part B
import random

x = random.randrange(1,10)
print(x)

import turtle

def main():
    # Create two turtle objects
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    
    # Place the turtles at their starting positions
    t1.penup()
    t1.goto(-100, 20)
    t1.pendown()
    
    t2.penup()
    t2.goto(-100, -20)
    t2.pendown()
    
    # Move the turtles forward a random distance
    for _ in range(10):
        distance1 = random.randint(1, 100)
        distance2 = random.randint(1, 100)
        t1.forward(distance1)
        t2.forward(distance2)
    
    # Reset the turtles to their starting position
    t1.penup()
    t1.goto(-100, 20)
    t1.pendown()
    
    t2.penup()
    t2.goto(-100, -20)
    t2.pendown()


