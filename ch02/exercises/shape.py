import pygame
pygame.init()
screen = pygame.display.set_mode()

pygame.draw.circle(screen, "light blue", [600, 250], 75)
pygame.draw.circle(screen, "light blue", [600, 150], 50)
pygame.draw.circle(screen, "light blue", [600, 75], 30)
pygame.display.flip()
pygame.time.wait(5000)