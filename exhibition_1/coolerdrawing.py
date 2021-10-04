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


def house(posx, posy, s):
    s1 = pygame.Surface((400 * s, 200 * s)).convert_alpha()
    s1.fill([0, 0, 0, 0])
    polygon(s1, brown, [[200 * s, 50 * s], [200 * s, 150 * s], [300 * s, 200 * s], [300 * s, 80 * s]])
    polygon(s1, brown, [[200 * s, 50 * s], [250 * s, 30 * s], [300 * s, 80 * s]])
    polygon(s1, brown, [[350 * s, 0 * s], [250 * s, 30 * s], [300 * s, 80 * s], [399 * s, 50 * s]])
    polygon(s1, brown, [[300 * s, 200 * s], [300 * s, 80 * s], [399 * s, 50 * s], [399 * s, 130 * s]])
    polygon(s1, black, [[200 * s, 50 * s], [200 * s, 150 * s], [300 * s, 200 * s], [300 * s, 80 * s]], 1)
    polygon(s1, black, [[200 * s, 50 * s], [250 * s, 30 * s], [300 * s, 80 * s]], 1 * s)
    polygon(s1, black, [[350 * s, 0 * s], [250 * s, 30 * s], [300 * s, 80 * s], [399 * s, 50 * s]], 1)
    polygon(s1, black, [[300 * s, 200 * s], [300 * s, 80 * s], [399 * s, 50 * s], [399 * s, 130 * s]], 1)
    circle(s1, black, (250 * s, 120 * s), 25 * s)
    ychain = 120 * s
    xchain = 208 * s
    for i in range(15):
        ellipse(s1, black, (xchain, ychain, 20 * s, random.randint(7, 13) * s), 1)
        xchain += -14 * s + random.randint(0, 4) * s
        ychain += 3 * s + random.randint(-3, 3) * s
    sc.blit(s1, (posx, posy))
    pygame.display.update()


def fence(posx, posy, s, frequency):
    s2 = pygame.Surface((800*s, 300*s)).convert_alpha()
    s2.fill([0, 0, 0, 0])
    rect(s2, brown, (0, 0, 800*s, 300*s))
    line(s2, black, (0, 0), (800*s, 0), 2)
    line(s2, black, (0, 298*s), (800*s, 298*s), 2)
    pos = 10
    while pos < 800*s:
        line(s2, black, (pos, 0), (pos,  300*s), 2)
        pos += frequency
    sc.blit(s2, (posx, posy))
    pygame.display.update()


def dog(posx, posy, s, a):
    s3 = pygame.Surface((210 * s, 200 * s)).convert_alpha()
    s3.fill([0, 0, 0, 0])
    ellipse(s3, dogBrown, (0, 160*s, 30*s, 15*s))
    ellipse(s3, dogBrown, (60 * s, 185*s, 30 * s, 15 * s))
    ellipse(s3, dogBrown, (180 * s, 150 * s, 20 * s, 10 * s))
    ellipse(s3, dogBrown, (130 * s, 125*s, 20 * s, 10 * s))
    ellipse(s3, dogBrown, (10 * s, 85 * s, 30 * s, 80 * s))
    ellipse(s3, dogBrown, (70 * s, 110 * s, 30 * s, 80 * s))
    ellipse(s3, dogBrown, (190 * s, 110 * s, 20 * s, 45 * s))
    ellipse(s3, dogBrown, (140 * s, 85 * s, 20 * s, 45 * s))
    circle(s3, dogBrown, (135 * s, 75 * s), 25*s)
    circle(s3, dogBrown, (185 * s, 100 * s), 25 * s)
    ellipse(s3, dogBrown, (10 * s, 70 * s, 150 * s, 70 * s))
    ellipse(s3, dogBrown, (110 * s, 50 * s, 90 * s, 60 * s))
    rect(s3, dogBrown, (16 * s, 1 * s, 85 * s, 85 * s))
    rect(s3, black, (16 * s, 1 * s, 85 * s, 85 * s), 1)
    ellipse(s3, dogBrown, (0, 0, 20 * s, 20 * s))
    ellipse(s3, black, (0, 0, 20 * s, 20 * s), 1)
    ellipse(s3, dogBrown, (97 * s, 0, 20 * s, 20 * s))
    ellipse(s3, black, (97 * s, 0, 20 * s, 20 * s), 1)
    ellipse(s3, white, (30 * s, 16 * s, 15 * s, 10 * s))
    ellipse(s3, black, (30 * s, 16 * s, 15 * s, 10 * s), 1)
    ellipse(s3, white, (30 * s, 16 * s, 15 * s, 10 * s))
    ellipse(s3, black, (30 * s, 16 * s, 15 * s, 10 * s), 1)
    ellipse(s3, white, (72 * s, 16 * s, 15 * s, 10 * s))
    ellipse(s3, black, (72 * s, 16 * s, 15 * s, 10 * s), 1)
    circle(s3, black, (79.5 * s, 21 * s), 4*s)
    circle(s3, black, (37.5 * s, 21 * s), 4*s)
    polygon(s3, white, ((50 * s, 45 * s), (55 * s, 55 * s), (45 * s, 55 * s)))
    polygon(s3, white, ((67 * s, 45 * s), (72 * s, 55 * s), (62 * s, 55 * s)))
    polygon(s3, black, ((50 * s, 45 * s), (55 * s, 55 * s), (45 * s, 55 * s)), 1)
    polygon(s3, black, ((67 * s, 45 * s), (72 * s, 55 * s), (62 * s, 55 * s)), 1)
    ellipse(s3, dogBrown, (26 * s, 53 * s, 65 * s, 30 * s))
    ellipse(s3, black, (26 * s, 53 * s, 65 * s, 30 * s), 1)
    rect(s3, dogBrown, (17 * s, 65 * s, 83 * s, 19 * s))
    s3 = pygame.transform.flip(s3, a, False)
    sc.blit(s3, (posx, posy))
    pygame.display.update()


fence(0, 200, 0.5, 20)
house(350, 450, 1)
dog(70, 501, 1.2, False)
fence(400, 100, 0.7, 10)
fence(200, 300, 0.5, 10)
fence(0, 400, 0.3, 10)
dog(400, 450, 1, True)
dog(550, 550, 3, False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()