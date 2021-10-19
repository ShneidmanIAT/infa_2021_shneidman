import random

import pygame
from pygame.draw import *


FPS = 30
pygame.init()
screen = pygame.display.set_mode((700, 700))
Amount_of_balls = 4


def handle_events():
    """
    gets the tap on screen or on the cross
    """
    finish_clicked = False
    x = screen.get_width() + 100
    y = screen.get_height() + 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish_clicked = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
    return(finish_clicked, x, y)


def game_process(xcirc, ycirc, xclick, yclick, rad, score, ball_speed, colour):
    """
    matches clikced coords with coords of every ball and moves/replaces them
    :param xcirc: array of x coordinates of balls
    :param ycirc: array of y coordinates of balls
    :param xclick: x of click
    :param yclick: y of click
    :param rad: array of rads of balls
    :param score: score of playa
    :param ball_speed: array of x and y speeds  of balls
    :param colour: array of colours of balls
    :return:
    """
    for i in range(len(xcirc)):
        circle(screen, (0, 0, 0), (xcirc[i], ycirc[i]), rad[i])
        if (xclick - xcirc[i])**2 + (yclick - ycirc[i])**2 < rad[i]**2:
            score += 10
            xcirc[i], ycirc[i], rad[i], ball_speed[i], colour[i] = new_ball(xcirc[i], ycirc[i], rad[i], ball_speed[i])
    for i in range(len(xcirc)):
        xcirc[i], ycirc[i], rad[i], ball_speed[i], colour[i] = move_ball(xcirc[i], ycirc[i], rad[i], ball_speed[i], colour[i])
    return (xcirc, ycirc, rad, score, ball_speed, colour)


def move_ball(xcirc, ycirc, rad, ball_speed, colour):
    """
    moves a ball on parameters tied with speed
    :param xcirc: x coord of moved ball
    :param ycirc: y coord of moved ball
    :param rad: rad coord of moved ball
    :param ball_speed: ball speed array of moved ball
    :param colour: colour array of moved ball
    """
    if xcirc + ball_speed[0] > screen.get_width() and xcirc > 0:
        ball_speed[0] = -ball_speed[0]
    elif xcirc + ball_speed[0] < 0 and xcirc < 0:
        ball_speed[0] = -ball_speed[0]
    if ycirc + ball_speed[1] > screen.get_height() and ycirc > 0:
        ball_speed[1] = -ball_speed[1]
    elif ycirc + ball_speed[1] < 0 and ycirc < 0:
        ball_speed[1] = -ball_speed[1]
    ycirc += ball_speed[1]
    xcirc += ball_speed[0]
    circle(screen, colour, (xcirc, ycirc), rad)
    return (xcirc, ycirc, rad, ball_speed, colour)


def new_ball(xcirc, ycirc, rad, ball_speed):
    """
    replaces clicked ball on screen with new with random parametres
    :param xcirc: x coord of replaced ball
    :param ycirc: y coord of replaced ball
    :param rad: rad coord of replaced ball
    :param ball_speed: ball speed array of replaced ball
    """
    circle(screen, (0, 0, 0), (xcirc, ycirc), rad)
    ycirc = random.randint(50, screen.get_height())
    xcirc = random.randint(50, screen.get_width())
    rad = random.randint(12, 50)
    ball_speed[0] = random.randint(-10, 15)
    ball_speed[1] = random.randint(-10, 10)
    colour = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return xcirc, ycirc, rad, ball_speed, colour


def score_to_screen(score):
    """
    draws score on screen
    :param score: score of player
    """
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(score), False, (0, 180, 0))
    rect(screen, (0, 0, 0), (0, 0, 200, 200))
    screen.blit(textsurface, (10, 10))


ycirc = [None] * Amount_of_balls
xcirc = [None] * Amount_of_balls
rad = [None] * Amount_of_balls
ball_speed = []
colour = []
for i in range(Amount_of_balls):
    ycirc[i] = random.randint(20, screen.get_height())
    xcirc[i] = random.randint(20, screen.get_width())
    rad[i] = random.randint(12, 50)
    ball_speed.append([random.randint(10, 50), random.randint(10, 50)])
    colour.append([0, 0, 0])

for i in range(len(xcirc)):
    xcirc[i], ycirc[i], rad[i], ball_speed[i], colour[i] = new_ball(ycirc[i], xcirc[i], rad[i], ball_speed[i])

pygame.display.update()
clock = pygame.time.Clock()
finished = False
pygame.font.init()
xclick = 0
yclick = 0
score = 0
while not finished:
    clock.tick(FPS)
    score_to_screen(score)
    finished, xclick, yclick = handle_events()
    xcirc, ycirc, rad, score, ball_speed, colour = game_process(xcirc, ycirc, xclick, yclick, rad, score, ball_speed, colour)
    xclick = screen.get_width() + 100
    yclick = screen.get_height() + 100
    pygame.display.update()
pygame.quit()