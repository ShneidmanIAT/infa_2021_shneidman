import math
import random
from random import choice
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.g = 1

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x + self.vx > screen.get_width() - 50 and self.vx > 0:
            self.vx = -self.vx
        if self.x + self.vx < 50 and self.vx < 0:
                self.vx = -self.vx
        if self.y + self.vy < 50 and self.vy > 0:
            self.vy = - self.vy
        if self.y + self.vy > screen.get_height() - 50 and self.vy < 0:
            self.vy = - self.vy
        self.x = self.x + self.vx
        self.y = self.y - self.vy
        self.vy = self.vy - self.g
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, tx, ty, tr):
        if ((self.x - tx) ** 2 + (self.y - ty) ** 2) < (tr+10)**2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 20
        self.y = 450
        self.points = 0

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        if event.pos[0]-new_ball.x == 0:
            self.an = 0.785
        else:
            self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] - 20== 0:
                self.an = 0.785
            else:
                self.an = math.atan2((event.pos[1] - 450), (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY
    def move(self, key_pressed):
        if key_pressed[pygame.K_LEFT]:
            self.x = self.x - 2
        if key_pressed[pygame.K_RIGHT]:
            self.x = self.x + 2
        if key_pressed[pygame.K_UP]:
            self.y = self.y - 2
        if key_pressed[pygame.K_DOWN]:
            self.y = self.y + 2



    def draw(self):
        pygame.draw.polygon(screen, BLACK, ((self.x, self.y), (self.x + math.sin(self.an)*7, self.y - math.cos(self.an)*7), (self.x + math.cos(self.an)*self.f2_power + math.sin(self.an)*7, self.y + math.sin(self.an)*self.f2_power- math.cos(self.an)*7),
                                            (self.x + math.cos(self.an)*self.f2_power, self.y + math.sin(self.an)*self.f2_power)))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target(Ball):
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = random.randint(300, screen.get_width() - 50)
        self.y = random.randint(50, screen.get_height() - 50)
        self.r = random.randint(20, 80)
        self.vx = random.randint(-5 , 5)
        self.vy = random.randint(-5 , 5)
        self.color = choice(GAME_COLORS)
        self.live = 1
        self.g = 0
    def new_target(self):
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.r = random.randint(2, 50)
        self.live = 1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
balls_am = 0

clock = pygame.time.Clock()
gun = Gun(screen)
targ = [Target(screen), Target(screen)]
finished = False
t = 0
all_died = False
while not finished:
    all_died = True
    screen.fill(WHITE)
    gun.draw()
    for target in targ:
        if target.live != 0:
            target.draw()
            target.move()
            all_died = False
    for b in balls:
        b.draw()
    if all_died:
        t = 100
        balls_am = len(balls)
        balls = []
        gun.points += 10
        for i in range(len(targ)):
            targ[i] = Target(screen)

    if(t > 0):
        MYFONT = pygame.font.SysFont('cmmi10', 30)
        textsurface = MYFONT.render('  Вы уничтожили все цели за ' + str(balls_am) + ' шаров, ваш счет ' + str(gun.points), False, GREEN)
        screen.blit(textsurface, (200, 200))
        t = t - 1
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        gun.move(pygame.key.get_pressed())

    for b in balls:
        b.move()
        for target in targ:
            if b.hittest(target.x, target.y, target.r) and target.live:
                target.live = 0
                balls_am = len(balls)
    gun.power_up()

pygame.quit()