import pygame


class Goal_Line:
    def __init__(self, img, x, y, screen, scale=1):
        self.x = x
        self.y = y
        temp_img = pygame.image.load(img)
        self.img = pygame.transform.scale(temp_img, (temp_img.get_width() * scale, temp_img.get_height() * scale))

        self.screen = screen

    def is_goal(self, ball_x, ball_y):
        return (self.x - 5 < ball_x < self.x + 5) and (self.y - 170 < ball_y, self.y + 5)

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))
