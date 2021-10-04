import pygame
from pygame.draw import *
pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill([100, 100, 100])
circle(screen, (255, 255, 0), (400, 400), 100)
circle(screen, (0, 0, 0), (400, 400), 103, 3)
circle(screen, (255, 0, 0), (360, 370), 20)
circle(screen, (255, 0, 0), (440, 370), 15)
circle(screen, (0, 0, 0), (360, 370), 7)
circle(screen, (0, 0, 0), (440, 370), 5)
line(screen, (0, 0, 0), (382, 368), (357, 326), 4)
line(screen, (0, 0, 0), (420, 371), (435, 346), 5)
line(screen, (0, 0, 0), (350, 450), (450, 450), 15)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
