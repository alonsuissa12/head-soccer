import pygame
from pygame import mixer

import goal_line
import soccer_player
import crossbar
import ball
import goal_line
# defines
floor = 440
gravity = 7

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

# goalposts
left_crossbar = crossbar.Crossbar('line(side).png', 0, 350, screen, 1.4)
right_crossbar = crossbar.Crossbar('line(side).png', 932, 350, screen, 1.4)

left_goal_line = goal_line.Goal_Line('goal_line2.jpg', 38, 580, screen, 0.9)
right_goal_line = goal_line.Goal_Line('goal_line2.jpg', 932, 580, screen, 0.9)

# ball
ball = ball.Ball('ball.png', 450, 100, screen,0.7)

# defines
up_was_pressed = False
w_was_pressed = False
is_left_plyer_collide = False
is_right_plyer_collide = False
objects = [left_crossbar, right_crossbar]

# plyers
right_player = soccer_player.SoccerPlayer('giraffe.png', 700, 440, screen, floor, gravity, 1)
left_player = soccer_player.SoccerPlayer('elephant.png', 200, 440, screen, floor, gravity, 1)
plyers = [left_player, right_player]

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
        # quit
        if event.type == pygame.QUIT:
            running = False
        # jump
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

    # collide check
    is_left_plyer_collide = left_crossbar.is_collide_crossbar(left_player.x, left_player.y) \
                            or right_crossbar.is_collide_crossbar(left_player.x + 80, left_player.y)
    is_right_plyer_collide = left_crossbar.is_collide_crossbar(right_player.x + 20, right_player.y) \
                             or right_crossbar.is_collide_crossbar(right_player.x + 80, right_player.y)
    ball.draw()
    left_goal_line.draw()
    right_goal_line.draw()
    left_crossbar.draw()
    right_crossbar.draw()
    plyers[0].draw(is_left_plyer_collide)
    plyers[1].draw(is_right_plyer_collide)
    pygame.time.delay(17)
    pygame.display.update()
