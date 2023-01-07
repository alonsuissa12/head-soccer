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
        self.x_change = 4
        self.y_change = 0
        self.fliper = 0

    def ball_movement(self, x_change, y_change):
        self.x_change = x_change
        self.y_change = y_change

    def draw(self):
        self.y_change = self.gravity + self.y_change
        self.x_change = self.x_change * 0.995
        self.x += self.x_change
        self.y += self.y_change
        self.boundaries()
        if self.x_change >= 2 or self.x_change <= -2:
            self.fliper = (self.fliper + int(self.x_change * 2))
        elif (2 > self.x_change > 0.1) or (-2 < self.x_change < -0.1):
            self.fliper = self.fliper + 2
        elif 0.1 < self.x < 0.3 or -0.1 > self.x > -0.3:
            self.fliper = self.fliper + 1
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
        if self.x > 900:
            self.x = 900
            self.x_change = (-1 * self.x_change) / 1.5
        if self.x < 60:
            self.x = 60
            self.x_change = (-1 * self.x_change) / 1.5

        def collide_crossbar(collide: bool):
            if collide:
                self.x_change = (-1 * self.x_change) / 1.5
                self.y_change = (-1 * self.y_change) / 1.2
