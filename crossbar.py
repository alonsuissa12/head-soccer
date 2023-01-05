import pygame


class Crossbar:
    def __init__(self, img, x, y, screen, scale=1):
        temp_img = pygame.image.load(img)
        self.img = pygame.transform.scale(temp_img, (temp_img.get_width() * scale, temp_img.get_height() * scale))
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))

    def is_collide_crossbar(self, x, y):
        endX = self.x + self.img.get_width()
        return self.x - 20 < x < endX and (self.y - 5) < y < (self.y + 5)
