import random

import pygame
from pygame.draw import *


FPS = 70
pygame.init()
screen = pygame.display.set_mode((700, 700))
Amount_of_balls = 100


def handle_events(gameon, save, show_results):
    """
    gets the tap on screen or on the cross
    """
    ch = ''
    finish_clicked = False
    x = screen.get_width() + 100
    y = screen.get_height() + 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish_clicked = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
        if event.type == pygame.KEYDOWN:
            ch = event.unicode
            print(ch)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameon = True
            if event.key == pygame.K_LALT:
                save = True
            if event.key == pygame.K_RALT:
                show_results = not show_results
    return(finish_clicked, x, y, ch, gameon, save, show_results)


def game_process(xcirc, ycirc, xclick, yclick, rad, score, ball_speed, colour, rare):
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
        screen.fill((0, 0, 0))
        if (xclick - xcirc[i])**2 + (yclick - ycirc[i])**2 < rad[i]**2:
            if rare[i] == 1:
                score += 10
            else:
                score += 1
            xcirc[i], ycirc[i], rad[i], ball_speed[i], colour[i], rare[i] = new_ball(
                xcirc[i], ycirc[i], rad[i], ball_speed[i], rare[i])
    for i in range(len(xcirc)):
        xcirc[i], ycirc[i], rad[i], ball_speed[i] = move_ball(
            xcirc[i], ycirc[i], rad[i], ball_speed[i])
        circle(screen, colour[i], (xcirc[i], ycirc[i]), rad[i])
        if rare[i] == 1:
            for j in range(int(rad[i]/4 - 1)):
                circle(screen, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], (xcirc[i], ycirc[i]), rad[i] - 4*j)

    return (xcirc, ycirc, rad, score, ball_speed, colour, rare)


def move_ball(xcirc, ycirc, rad, ball_speed):
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
    return (xcirc, ycirc, rad, ball_speed)


def new_ball(xcirc, ycirc, rad, ball_speed, rare):
    """
    replaces clicked ball on screen with new with random parametres
    :param xcirc: x coord of replaced ball
    :param ycirc: y coord of replaced ball
    :param rad: rad coord of replaced ball
    :param ball_speed: ball speed array of replaced ball
    """
    ycirc = random.randint(50, screen.get_height())
    xcirc = random.randint(50, screen.get_width())
    rad = random.randint(12, 50)
    ball_speed[0] = random.randint(-10, 15)
    ball_speed[1] = random.randint(-10, 10)
    rare = random.randint(1, 10)
    colour = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return xcirc, ycirc, rad, ball_speed, colour, rare


def score_to_screen(score, name):
    """
    draws score on screen
    :param score: score of player
    """
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(score) + "  " + str(name), False, (0, 180, 0))
    screen.blit(textsurface, (10, 10))


def get_name(name):
    screen.fill((0, 0, 0))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    namesurface = myfont.render(str(name), False, (0, 180, 0))
    textsurface1 = myfont.render("Enter Your name", False, (0, 180, 0))
    textsurface2 = myfont.render("Escape to continue", False, (0, 180, 0))
    textsurface3 = myfont.render("LALT to save result", False, (0, 180, 0))
    textsurface4 = myfont.render("RALT to show results table", False, (0, 180, 0))
    screen.blit(namesurface, (10, screen.get_height()/2))
    screen.blit(textsurface1, (10, screen.get_height() / 2 - 60))
    screen.blit(textsurface2, (10, screen.get_height() / 2 - 30))
    screen.blit(textsurface3, (10, 60))
    screen.blit(textsurface4, (10,screen.get_height() - 100))


def show_result():
    f = open('results.txt', 'r')
    screen.fill((0, 0, 0))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    yline = 10
    for line in f:
        if len(line) != 1:
            namesurface = myfont.render(line[:-1], False, (0, 180, 0))
            screen.blit(namesurface, (10, yline))
            yline += 30
    f.close()


ycirc = [None] * Amount_of_balls
xcirc = [None] * Amount_of_balls
rad = [None] * Amount_of_balls
ball_speed = []
colour = []
rare = [None] * Amount_of_balls
for i in range(Amount_of_balls):
    ycirc[i] = random.randint(20, screen.get_height())
    xcirc[i] = random.randint(20, screen.get_width())
    rad[i] = random.randint(12, 50)
    ball_speed.append([random.randint(10, 50), random.randint(10, 50)])
    colour.append([0, 0, 0])
    rare[i] = random.randint(0, 20)

for i in range(len(xcirc)):
    xcirc[i], ycirc[i], rad[i], ball_speed[i], colour[i], rare[i]  = new_ball(ycirc[i], xcirc[i], rad[i], ball_speed[i], rare[i])

pygame.display.update()
clock = pygame.time.Clock()
finished = False
pygame.font.init()
xclick = 0
yclick = 0
score = 0
name = ""
ch = ''
gameon = False
save = False
show_results = False
while not finished:
    clock.tick(FPS)
    finished, xclick, yclick, ch, gameon, save, show_results = handle_events(gameon, save, show_results)
    if gameon:
        xcirc, ycirc, rad, score, ball_speed, colour, rare = game_process(
            xcirc, ycirc, xclick, yclick, rad, score, ball_speed, colour, rare)
        score_to_screen(score, name)
    elif not show_results:
        name = name + ch
        ch = 0
        get_name(name)
    else:
        show_result()
    if save and finished and score != 0:
        f = open('results.txt', 'a')
        f.write(str(name) + "  " + str(score) + "\n")
        f.close()
    pygame.display.update()
pygame.quit()