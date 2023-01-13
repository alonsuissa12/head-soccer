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
        self.y_change = self.gravity + self.y_change
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
        if self.x > 950:
            self.x = 950
            self.x_change = (-1 * self.x_change) / 1.5
        if self.x < 0:
            self.x = 0
            self.x_change = (-1 * self.x_change) / 1.5

    def collide_crossbar(self):
        crossbar_width = 50
        crossbar_hight = 360
        x_deflect = 2
        collide = ((crossbar_hight - 50 < self.y + 30 < crossbar_hight + 50) and (crossbar_width >= self.x >= 0))
        collide = collide or (
                (crossbar_hight - 50 < self.y + 30 < crossbar_hight + 50) and (950 >= self.x >= 950 - crossbar_width))
        if collide:
            if 0 <= self.x_change < 2:
                self.x_change *= 2
            if self.y_change > 0:
                self.y_change = self.gravity * 5
                if self.x > 450:
                    self.x_change += 2
                else:
                    self.x_change -= 2

            self.x_change = (-1 * self.x_change) / 1.5
            self.y_change = (-1 * self.y_change) / 1.1
            if crossbar_width >= self.x >= 35:
                self.x_change += x_deflect
            if 850 + 35 >= self.x >= 850:
                self.x_change += -1 * x_deflect

    def collide_player(self, p_x, p_y, p_x_change, p_y_change, is_left_player):
        if is_left_player:
            if (p_x + 100 > self.x > p_x - 30) and (p_y + 50 > self.y > p_y - 50):
                self.x_change = (-1 * self.x_change) / 1.5
                self.y_change = (-1 * self.y_change) / 1.2
                self.x_change += p_x_change * 5
                self.y_change += p_y_change * 2
                self.x_change += 1
        #         if self.x < p_x -30:
        #             self.x_change = -1 * math.fabs(p_x_change * 2) - 1 * self.x_change
        #             self.y_change = p_y_change * 1.3 + 0.7 * self.y_change
        #         else:
        #             self.x_change = math.fabs(p_x_change * 2) - 1 * self.x_change
        #             self.y_change = p_y_change * 1.3 + 0.7 * self.x_change
        # # left player
        elif (p_x + 100 > self.x > p_x - 30) and (p_y + 50 > self.y > p_y - 50):
            self.x_change = (-1 * self.x_change) / 1.5
            self.y_change = (-1 * self.y_change) / 1.2
            self.x_change += p_x_change * 2
            self.y_change += p_y_change * 2
            # if self.x > p_x + 100:
            #     self.x_change = -1 * math.fabs(p_x_change * 2) - 1 * self.x_change
            #     self.y_change = p_y_change * 1.3 + 0.7 * self.y_change
            # else:
            #     self.x_change = math.fabs(p_x_change * 2) - 1 * self.x_change
            #     self.y_change = p_y_change * 1.3 + 0.7 * self.x_change
