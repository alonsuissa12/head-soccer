import pygame
from pygame import mixer
import soccer_player

# initialize pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((1000, 600))

# background
field_img = pygame.image.load('background_img3.jpg')
field_img = pygame.transform.scale(field_img, (1000, 600))

# background sound
mixer.music.load('background_Sound.mp3')
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("head soccer")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# plyers
right_player = soccer_player.SoccerPlayer('right_head.png', 700, 450, screen, 2.5)
left_player = soccer_player.SoccerPlayer('left_head.png', 200, 450, screen, 2.5 )
plyers = [left_player, right_player]

#


# game loop
running = True
while running:
    screen.blit(field_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    plyers[0].draw()
    plyers[1].draw()
    pygame.display.update()
