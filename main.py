import pygame
from pygame import mixer
import soccer_player
import crossbar

# initialize pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((1000, 600))

# background
field_img = pygame.image.load('backgroundIMG.jpg')
field_img = pygame.transform.scale(field_img, (1000, 600))

# background sound
mixer.music.load('background_Sound.mp3')
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("head soccer")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# defines
floor = 440
gravity = 7
up_was_pressed = False
w_was_pressed = False

# plyers
right_player = soccer_player.SoccerPlayer('giraffe.png', 700, 440, screen, floor, gravity, 1)
left_player = soccer_player.SoccerPlayer('elephant.png', 200, 440, screen, floor, gravity, 1)
plyers = [left_player, right_player]

# goalposts
left_crossbar = crossbar.Crossbar('line(side).png', 0, 350, screen, 1)


# game loop
running = True
while running:
    # screen
    screen.blit(field_img, (0, 0))
    # elephant side movement
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_LEFT]:
        right_player.side_movement(-5)
    if user_input[pygame.K_RIGHT]:
        right_player.side_movement(5)
        # giraffe side movement
    if user_input[pygame.K_a]:
        left_player.side_movement(-5)
    if user_input[pygame.K_d]:
        left_player.side_movement(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_was_pressed = True
            if event.key == pygame.K_w:
                w_was_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and up_was_pressed and not right_player.is_not_on_floor():
                right_player.jump(-48)
                up_was_pressed = False
            if event.key == pygame.K_w and w_was_pressed and not left_player.is_not_on_floor():
                left_player.jump(-48)
                w_was_pressed = False

    if left_crossbar.is_collide_crossbar(plyers[0].x, plyers[0].y):
        print("boom")

    left_crossbar.draw()
    plyers[0].draw()
    plyers[1].draw()
    pygame.time.delay(15)
    pygame.display.update()
