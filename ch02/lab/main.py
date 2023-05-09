import pygame
import random
import turtle
import math
# Race 1
sc = turtle.Screen()
sc.setup(400,400)
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
write = turtle.Turtle()
write.penup()
write.goto(-100,40)
write.pendown()
write.write('Race 1')
write.penup()
turtle1.color('red')
turtle2.color('blue')
turtle1.penup()
turtle2.penup()
turtle1.goto(-100, 20)
turtle2.goto(-100, 10)
turtle1.pendown()
turtle2.pendown()
ran1 = random.randrange(1,100)
ran2 = random.randrange(1,100)
turtle1.fd(ran1)
turtle2.fd(ran2)

# Race 2
racer1 = turtle.Turtle()
racer2 = turtle.Turtle()
racer1.color('green')
racer2.color('orange')
racer1.penup()
racer2.penup()
racer1.goto(-100,-30)
racer2.goto(-100,-40)
racer1.pendown()
racer2.pendown()
write.goto(-100,-20)
write.write("Race 2")
write.penup()
for i in range(10):
    ran3 = random.randrange(1,10)
    ran4 = random.randrange(1,10)
    racer1.fd(ran3)
    racer2.fd(ran4)
racer1.penup()
racer2.penup()
racer1.goto(-100,-30)
racer2.goto(-100,-40)
racer1.pendown()
racer2.pendown()
sc.exitonclick()

# part 2
pygame.init()
window = pygame.display.set_mode()
window.fill('white')
# traingle
num_sides = 3
side_length = 150
xpos = 200
ypos = 200
points = []
for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    tuple = (x,y)
    points.append(tuple)
pygame.draw.polygon(window, 'red', points)
pygame.display.update()
pygame.time.wait(2500)
window.fill('white')
pygame.display.update()
pygame.time.wait(1000)

# square
num_sides = 4
side_length = 150
xpos = 200
ypos = 200
points = []
for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    tuple = (x,y)
    points.append(tuple)
pygame.draw.polygon(window, 'red', points)
pygame.display.update()
pygame.time.wait(2500)
window.fill('white')
pygame.display.update()
pygame.time.wait(1000)

# hexagon
num_sides = 6
side_length = 150
xpos = 200
ypos = 200
points = []
for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    tuple = (x,y)
    points.append(tuple)
pygame.draw.polygon(window, 'red', points)
pygame.display.update()
pygame.time.wait(2500)
window.fill('white')
pygame.display.update()
pygame.time.wait(1000)

# icosagon
num_sides = 20
side_length = 150
xpos = 200
ypos = 200
points = []
for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    tuple = (x,y)
    points.append(tuple)
pygame.draw.polygon(window, 'red', points)
pygame.display.update()
pygame.time.wait(2500)
window.fill('white')
pygame.display.update()
pygame.time.wait(1000)

# hectagon
num_sides = 100
side_length = 150
xpos = 200
ypos = 200
points = []
for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    tuple = (x,y)
    points.append(tuple)
pygame.draw.polygon(window, 'red', points)
pygame.display.update()
pygame.time.wait(2500)
window.fill('white')
pygame.display.update()
pygame.time.wait(1000)

# circle-ish
num_sides = 360
side_length = 150
xpos = 200
ypos = 200
points = []
for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    tuple = (x,y)
    points.append(tuple)
pygame.draw.polygon(window, 'red', points)
pygame.display.update()
pygame.time.wait(2500)
window.fill('white')
pygame.display.update()
pygame.time.wait(1000)