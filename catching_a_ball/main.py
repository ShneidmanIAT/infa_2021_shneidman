import random

import pygame
from pygame.draw import *


FPS = 30
pygame.init()
screen = pygame.display.set_mode((400, 400))
numofelements = 2

def handle_events(x, y, finished):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
    return(finished, x, y)


def game_process(xcirc, ycirc, x, y, rad, score, ball_speed):
    for i in range(len(xcirc)):
        if (x - xcirc[i])**2 + (y-ycirc[i])**2 < rad[i]**2:
            score += 10
            print(score)
            xcirc[i], ycirc[i], rad[i], ball_speed[i] = new_ball(xcirc[i], ycirc[i], rad[i], ball_speed[i])
    for i in range(len(xcirc)):
        xcirc[i], ycirc[i], rad[i], ball_speed[i] = move_ball(xcirc[i], ycirc[i], rad[i], ball_speed[i])
    return (xcirc, ycirc, rad, score, ball_speed)


def move_ball(xcirc, ycirc, rad, ball_speed):
    circle(screen, (0, 0, 0), (xcirc, ycirc), rad)
    if xcirc + ball_speed[0] > 400 and xcirc > 0:
        ball_speed[0] = -ball_speed[0]
    elif xcirc + ball_speed[0] < 0 and xcirc < 0:
        ball_speed[0] = -ball_speed[0]
    if ycirc + ball_speed[1] > 400 and ycirc > 0:
        ball_speed[1] = -ball_speed[1]
    elif ycirc + ball_speed[1] < 0 and ycirc < 0:
        ball_speed[1] = -ball_speed[1]
    ycirc += ball_speed[1]
    xcirc += ball_speed[0]
    circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (xcirc, ycirc), rad)
    return (xcirc, ycirc, rad, ball_speed)


def new_ball(xcirc, ycirc, rad, ball_speed):
    circle(screen, (0, 0, 0), (xcirc, ycirc), rad)
    ycirc = random.randint(50, 350)
    xcirc = random.randint(50, 350)
    rad = random.randint(12, 50)
    ball_speed[0] = random.randint(-10, 15)
    ball_speed[1] = random.randint(-10, 10)
    circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (xcirc, ycirc), rad)
    return xcirc, ycirc, rad, ball_speed


ycirc = [None] * numofelements
xcirc = [None] * numofelements
rad = [None] * numofelements
ball_speed = []
for i in range(numofelements):
    ycirc[i] = random.randint(20, 380)
    xcirc[i] = random.randint(20, 380)
    rad[i] = random.randint(12, 50)
    ball_speed.append([random.randint(10,50), random.randint(10, 50)])

for i in range(len(xcirc)):
    xcirc[i], ycirc[i], rad[i], ball_speed[i] = new_ball(ycirc[i], xcirc[i], rad[i], ball_speed[i])

pygame.display.update()
clock = pygame.time.Clock()
finished = False
x = 0
y = 0
score = 0

while not finished:
    clock.tick(FPS)
    finished, x, y = handle_events(x, y, finished)
    xcirc, ycirc, rad, score, ball_speed = game_process(xcirc, ycirc, x, y, rad, score, ball_speed)
    x = 800
    y = 800
    pygame.display.update()


pygame.quit()