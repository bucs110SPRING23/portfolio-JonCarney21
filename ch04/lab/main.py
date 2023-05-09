import pygame
import random
import math
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((500,400))
window.fill("white")
green = pygame.Rect(300, 150, 100, 100)
red = pygame.Rect(100, 150, 100, 100)
pygame.draw.rect(window, "green", green)
pygame.draw.rect(window, "red", red)
pygame.display.update()

guess = ""

while guess=="":
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if red.collidepoint(event.pos):
                    guess = "red"
                elif green.collidepoint(event.pos):
                    guess = "green"
            
window = pygame.display.set_mode((400,500))
window.fill('yellow')
pygame.draw.circle(window,'white',(200,200),200)
pygame.draw.line(window,'black',(200,0),(200,400))
pygame.draw.line(window,'black',(0,200),(400,200))

green_score = 0
red_score = 0
counter = 0

while counter < 10:
    #player green
    for i in range(1):
        xpos = random.randrange(1,400)
        ypos = random.randrange(1,400)
        distance_from_center = math.hypot(200-xpos, 200-ypos)
        is_in_circle = distance_from_center <= 200
        if is_in_circle:
            pygame.draw.circle(window, 'green', (xpos,ypos), 5) 
            green_score = green_score + 1
        else:
            pygame.draw.circle(window, 'blue', (xpos,ypos), 5)

    #player red
    for i in range(1):
        xpos = random.randrange(1,400)
        ypos = random.randrange(1,400)
        distance_from_center = math.hypot(200-xpos, 200-ypos)
        is_in_circle = distance_from_center <= 200
        if is_in_circle:
            pygame.draw.circle(window, 'red', (xpos,ypos), 5)
            red_score = red_score + 1
        else:
            pygame.draw.circle(window, 'orange', (xpos,ypos), 5)
    
    counter = counter + 1

if red_score > green_score:
    if guess == "green":
        font = pygame.font.Font(None, 48)
        text = font.render("guess incorrect" , True, "black")
        window.blit(text, (75, 450)) 
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("guess correct" , True, "black")
        window.blit(text, (75, 450))
    font = pygame.font.Font(None, 48)
    text = font.render("player red wins" , True, "black")
    window.blit(text, (75, 400)) 
elif green_score > red_score:
    if guess == "red":
        font = pygame.font.Font(None, 48)
        text = font.render("guess incorrect" , True, "black")
        window.blit(text, (75, 450)) 
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("guess correct" , True, "black")
        window.blit(text, (75, 450))
    font = pygame.font.Font(None, 48)
    text = font.render("player green wins" , True, "black")
    window.blit(text, (75, 400)) 
else:
    font = pygame.font.Font(None, 48)
    text = font.render("Tie" , True, "black")
    window.blit((text, 75, 400)) 

pygame.display.update()
pygame.time.wait(4000)
