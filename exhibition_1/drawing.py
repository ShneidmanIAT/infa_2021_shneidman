import random
import pygame
from pygame.draw import *

pygame.init()
sc = pygame.display.set_mode((800, 800))

blue = (0, 0, 150)
brown = (160, 82, 45)
dogBrown = (80, 62, 25)
green = (0, 200, 0)
black = (0, 0, 0)
white = (255, 255, 255)

rect(sc, blue, (0, 0, 800, 400))
rect(sc, green, (0, 400, 800, 400))


def draw_house(coordinate_x, coordinate_y, size):
    s1 = pygame.Surface((400 * size, 200 * size)).convert_alpha()
    s1.fill([0, 0, 0, 0])
    polygon(s1, brown, [[200 * size, 50 * size], [200 * size, 150 * size], [300 * size, 200 * size], [300 * size, 80 * size]])
    polygon(s1, brown, [[200 * size, 50 * size], [250 * size, 30 * size], [300 * size, 80 * size]])
    polygon(s1, brown, [[350 * size, 0 * size], [250 * size, 30 * size], [300 * size, 80 * size], [399 * size, 50 * size]])
    polygon(s1, brown, [[300 * size, 200 * size], [300 * size, 80 * size], [399 * size, 50 * size], [399 * size, 130 * size]])
    polygon(s1, black, [[200 * size, 50 * size], [200 * size, 150 * size], [300 * size, 200 * size], [300 * size, 80 * size]], 1)
    polygon(s1, black, [[200 * size, 50 * size], [250 * size, 30 * size], [300 * size, 80 * size]], 1 * size)
    polygon(s1, black, [[350 * size, 0 * size], [250 * size, 30 * size], [300 * size, 80 * size], [399 * size, 50 * size]], 1)
    polygon(s1, black, [[300 * size, 200 * size], [300 * size, 80 * size], [399 * size, 50 * size], [399 * size, 130 * size]], 1)
    circle(s1, black, (250 * size, 120 * size), 25 * size)
    ychain = 120 * size
    xchain = 208 * size
    for i in range(15):
        ellipse(s1, black, (xchain, ychain, 20 * size, random.randint(7, 13) * size), 1)
        xchain += -14 * size + random.randint(0, 4) * size
        ychain += 3 * size + random.randint(-3, 3) * size
    sc.blit(s1, (coordinate_x, coordinate_y))
    pygame.display.update()


def draw_fence(coordinate_x, coordinate_y, size, frequency):
    s2 = pygame.Surface((800*size, 300*size)).convert_alpha()
    s2.fill([0, 0, 0, 0])
    rect(s2, brown, (0, 0, 800*size, 300*size))
    line(s2, black, (0, 0), (800*size, 0), 2)
    line(s2, black, (0, 298*size), (800*size, 298*size), 2)
    pos = 10
    while pos < 800*size:
        line(s2, black, (pos, 0), (pos,  300*size), 2)
        pos += frequency
    sc.blit(s2, (coordinate_x, coordinate_y))
    pygame.display.update()


def draw_dog(coordinate_x, coordinate_y, size):
    s3 = pygame.Surface((210 * size, 200 * size)).convert_alpha()
    s3.fill([0, 0, 0, 0])
    ellipse(s3, dogBrown, (0, 160*size, 30*size, 15*size))
    ellipse(s3, dogBrown, (60 * size, 185*size, 30 * size, 15 * size))
    ellipse(s3, dogBrown, (180 * size, 150 * size, 20 * size, 10 * size))
    ellipse(s3, dogBrown, (130 * size, 125*size, 20 * size, 10 * size))
    ellipse(s3, dogBrown, (10 * size, 85 * size, 30 * size, 80 * size))
    ellipse(s3, dogBrown, (70 * size, 110 * size, 30 * size, 80 * size))
    ellipse(s3, dogBrown, (190 * size, 110 * size, 20 * size, 45 * size))
    ellipse(s3, dogBrown, (140 * size, 85 * size, 20 * size, 45 * size))
    circle(s3, dogBrown, (135 * size, 75 * size), 25*size)
    circle(s3, dogBrown, (185 * size, 100 * size), 25 * size)
    ellipse(s3, dogBrown, (10 * size, 70 * size, 150 * size, 70 * size))
    ellipse(s3, dogBrown, (110 * size, 50 * size, 90 * size, 60 * size))
    rect(s3, dogBrown, (16 * size, 1 * size, 85 * size, 85 * size))
    rect(s3, black, (16 * size, 1 * size, 85 * size, 85 * size), 1)
    ellipse(s3, dogBrown, (0, 0, 20 * size, 20 * size))
    ellipse(s3, black, (0, 0, 20 * size, 20 * size), 1)
    ellipse(s3, dogBrown, (97 * size, 0, 20 * size, 20 * size))
    ellipse(s3, black, (97 * size, 0, 20 * size, 20 * size), 1)
    ellipse(s3, white, (30 * size, 16 * size, 15 * size, 10 * size))
    ellipse(s3, black, (30 * size, 16 * size, 15 * size, 10 * size), 1)
    ellipse(s3, white, (30 * size, 16 * size, 15 * size, 10 * size))
    ellipse(s3, black, (30 * size, 16 * size, 15 * size, 10 * size), 1)
    ellipse(s3, white, (72 * size, 16 * size, 15 * size, 10 * size))
    ellipse(s3, black, (72 * size, 16 * size, 15 * size, 10 * size), 1)
    circle(s3, black, (79.5 * size, 21 * size), 4*size)
    circle(s3, black, (37.5 * size, 21 * size), 4*size)
    polygon(s3, white, ((50 * size, 45 * size), (55 * size, 55 * size), (45 * size, 55 * size)))
    polygon(s3, white, ((67 * size, 45 * size), (72 * size, 55 * size), (62 * size, 55 * size)))
    polygon(s3, black, ((50 * size, 45 * size), (55 * size, 55 * size), (45 * size, 55 * size)), 1)
    polygon(s3, black, ((67 * size, 45 * size), (72 * size, 55 * size), (62 * size, 55 * size)), 1)
    ellipse(s3, dogBrown, (26 * size, 53 * size, 65 * size, 30 * size))
    ellipse(s3, black, (26 * size, 53 * size, 65 * size, 30 * size), 1)
    rect(s3, dogBrown, (17 * size, 65 * size, 83 * size, 19 * size))
    sc.blit(s3, (coordinate_x, coordinate_y))
    pygame.display.update()

draw_fence(0, 200, 1, 20)
draw_house(350, 450, 1)
draw_dog(70, 501, 1.2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
