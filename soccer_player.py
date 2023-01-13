import pygame


class SoccerPlayer:
    def __init__(self, img, x, y, screen, floor, gravity, scale=1, shoe_angle=30, flip_shoe=False,
                 shoeImg='soccer-shoe.png', shoe_scale=0.7):
        temp_img = pygame.image.load(img)
        self.img = pygame.transform.scale(temp_img, (temp_img.get_width() * scale, temp_img.get_height() * scale))
        self.x = x
        self.y = y
        self.screen = screen
        self.floor = floor
        self.gravity = gravity
        self.Ychange = 0
        self.Xchange = 0
        self.jump_timer = 10
        temp_shoe = pygame.image.load(shoeImg)
        temp_shoe = pygame.transform.rotate(temp_shoe, shoe_angle)
        if not flip_shoe:
            temp_shoe = pygame.transform.flip(temp_shoe, True, False)
        self.shoe_img = pygame.transform.scale(temp_shoe, (
            temp_shoe.get_width() * shoe_scale, temp_shoe.get_height() * shoe_scale))
        self.isRight = flip_shoe

    def draw(self, is_collide):
        if self.is_not_on_floor():
            if self.jump_timer > 0:
                self.jump_timer -= 1
                self.Ychange -= self.gravity * 0.2
            self.plyer_up_movement(is_collide)
        else:
            self.jump_timer = 10

        self.x = self.x + self.Xchange
        self.y = self.y + self.Ychange
        self.boundaries()
        self.screen.blit(self.img, (self.x, self.y))
        self.Xchange = 0

    def jump(self, hieght):
        self.Ychange = hieght

    # how the plyer will move when he is in the air
    def plyer_up_movement(self, is_collide):
        # plyer is in the air
        if self.y < self.floor:
            self.Ychange += self.gravity
            self.collide(is_collide)

        # plyer go under floor
        if self.y >= self.floor:
            self.Ychange = 0
            self.y = self.floor

    def is_not_on_floor(self):
        if self.y != self.floor:
            return True
        return False

    def side_movement(self, speed):
        self.Xchange = speed

    def boundaries(self):
        if self.x < 0:
            self.x = 0
        if self.x > 870:
            self.x = 870

    def collide(self, is_collide):
        if is_collide:
            self.Ychange = self.gravity
            self.Xchange = 0

    def kick(self):
        if self.isRight:
            kick_x = self.x + 70

        else:
            kick_x = self.x - 100
        self.screen.blit(self.shoe_img, (kick_x, self.y))
