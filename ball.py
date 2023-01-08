import math

import pygame


class Ball:
    def __init__(self, img, x, y, screen, scale=1, floor=460, gravity=2):
        self.x = x
        self.y = y
        self.screen = screen
        temp_img = pygame.image.load(img)
        self.img = pygame.transform.scale(temp_img, (temp_img.get_width() * scale, temp_img.get_height() * scale))
        self.gravity = gravity
        self.floor = floor
        self.x_change = 0
        self.y_change = 0
        self.fliper = 0

    def ball_movement(self, x_change, y_change):
        self.x_change = x_change
        self.y_change = y_change

    def draw(self):
        self.collide_crossbar()
        print(self.y_change, end=", ")
        self.y_change = self.gravity + self.y_change
        print(self.y_change)
        self.x_change = self.x_change * 0.995
        self.x += self.x_change
        self.y += self.y_change
        self.boundaries()

        if math.fabs(self.x_change) >= 2:
            self.fliper = (self.fliper + math.fabs(int(self.x_change * 2)))
        elif 2 > math.fabs(self.x_change) >= 0.3:
            self.fliper = self.fliper + 2
        elif 0.2 < math.fabs(self.x_change) < 0.3:
            self.fliper = self.fliper + 1
        if 0 < math.fabs(self.x_change) < 0.2:
            self.x_change = 0
        self.img = pygame.transform.flip(self.img, self.fliper >= 9, self.fliper >= 9)
        self.fliper %= 10
        self.screen.blit(self.img, (self.x, self.y))

    def boundaries(self):
        if self.y < 0:
            self.y = 0
            self.y_change = (-1 * self.y_change) / 1.2
        if self.y > self.floor:
            self.y = self.floor
            self.y_change = (-1 * self.y_change) / 1.2
        if self.x > 910:
            self.x = 910
            self.x_change = (-1 * self.x_change) / 1.5
        if self.x < 0:
            self.x = 0
            self.x_change = (-1 * self.x_change) / 1.5

    def collide_crossbar(self):
        crossbar_width = 50
        crossbar_hight = 350
        x_deflect = 2
        collide = ((crossbar_hight < self.y + 96 < crossbar_hight + 180) and (crossbar_width >= self.x >= 0))
        collide = collide or ((crossbar_hight < self.y + 96 < crossbar_hight + 180) and (910 >= self.x >= 910 - crossbar_width))
        if collide:
            if 0 <= self.y_change < 1:
                self.y_change = -self.gravity
            else:
                self.x_change = (-1 * self.x_change) / 1.5
                self.y_change = (-1 * self.y_change) / 1.2
                if crossbar_width >= self.x >= 35:
                    self.x_change += x_deflect
                if 850 + 35 >= self.x >= 850:
                    self.x_change += -1 * x_deflect

