import pygame
pygame.init()

def main():
   graph_coordinates(threenp1range(10))

window = pygame.display.set_mode()

def threenp1(n):
    count = 0
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
        count = count + 1
       else:
        n = int(3 * n + 1)
        count = count + 1
    return count
def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2,upper_limit + 1):
        objs_in_sequence[i] = threenp1(i)
    return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict):
    new_display = pygame.transform.flip(window, False, True)
    coords = list(threenplus1_iters_dict.items())
    pygame.draw.lines(new_display, "red", False, coords)
    max = 0
    for i in threenplus1_iters_dict:
      a = threenplus1_iters_dict[i]
      if max < a:
         max = a
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 10, height * 10))
    window.blit(new_display, (0,0))
    font = pygame.font.SysFont("None", 100)
    msg = font.render("max so far is:" + str(max), True, "red")
    window.blit(msg, (200,100))

    pygame.display.update()
    pygame.time.wait(6000)
       
main()