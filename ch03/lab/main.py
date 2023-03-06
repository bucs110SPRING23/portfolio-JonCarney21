import pygame
import random
import math
pygame.init()
window = pygame.display.set_mode((400,400))
window.fill('blue')
pygame.draw.circle(window,'red',(200,200),200)
pygame.draw.line(window,'black',(200,0),(200,400))
pygame.draw.line(window,'black',(0,200),(400,200))
for i in range(10):
    xpos = random.randrange(1,400)
    ypos = random.randrange(1,400)
    distance_from_center = math.hypot(200-xpos, 200-ypos)
    is_in_circle = distance_from_center <= 200
    if is_in_circle:
        pygame.draw.circle(window, 'black', (xpos,ypos), 5)
    else:
        pygame.draw.circle(window, 'green', (xpos,ypos), 5)
pygame.display.update()
pygame.time.wait(5000)
